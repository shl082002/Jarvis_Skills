"""Project workroom files into a state dict. Read-only. No second tracker."""
from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from mode import read_mode

STALE_HANDOVER_SECONDS = 24 * 60 * 60
BEAT_FRESH_SECONDS = 90
SKIP_LIVE = {"heimdall-state.json"}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def section(md: str, heading: str) -> str:
    pat = re.compile(
        r"^##[^\n]*" + re.escape(heading) + r"[^\n]*\n(.*?)(?=^## |\Z)",
        re.I | re.M | re.S,
    )
    m = pat.search(md)
    return (m.group(1).strip() if m else "").strip()


def first_line(text: str) -> str:
    for line in text.splitlines():
        s = line.strip()
        if s and not s.startswith("#") and s != "*(none)*":
            return s[:240]
    return ""


def bullet_items(text: str) -> list[str]:
    items: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("- ") or s.startswith("* "):
            body = s[2:].strip()
            if body and not body.lower().startswith("*(none)"):
                items.append(body[:240])
    return items


def iso_mtime(path: Path) -> str | None:
    if not path.exists():
        return None
    ts = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    return ts.isoformat()


def age_seconds(path: Path) -> float | None:
    if not path.exists():
        return None
    return now_utc().timestamp() - path.stat().st_mtime


def _parse_beat(beat: str) -> float | None:
    try:
        beat_dt = datetime.fromisoformat(str(beat).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    if beat_dt.tzinfo is None:
        beat_dt = beat_dt.replace(tzinfo=timezone.utc)
    return (now_utc() - beat_dt).total_seconds()


def parse_live(live_dir: Path) -> list[dict]:
    if not live_dir.is_dir():
        return []
    out: list[dict] = []
    for path in sorted(live_dir.glob("*.json")):
        if path.name in SKIP_LIVE:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(data, dict):
            continue
        delta = _parse_beat(str(data.get("last_beat") or ""))
        if delta is None:
            freshness, status = "unknown", "unknown"
        elif delta <= BEAT_FRESH_SECONDS:
            freshness = "fresh"
            status = str(data.get("status") or "unknown")
        else:
            freshness, status = "stale", "unknown"
        out.append(
            {
                "id": data.get("id") or path.stem,
                "role": data.get("role") or "",
                "mission": data.get("mission") or "",
                "phase": data.get("phase") or "",
                "status": status,
                "freshness": freshness,
                "last_beat": data.get("last_beat") or "",
            }
        )
    return out


def svc_status(workroom: Path) -> str:
    svc = workroom / "bin" / "svc"
    if not svc.is_file():
        return "unknown"
    try:
        result = subprocess.run(
            [str(svc), "status"],
            capture_output=True,
            text=True,
            timeout=8,
        )
        text = (result.stdout or result.stderr or "").strip()
        return text[:2000] if text else "unknown"
    except (OSError, subprocess.TimeoutExpired):
        return "unknown"


def project(workroom: Path) -> dict:
    handover = workroom / "HANDOVER.md"
    tracker = workroom / "TRACKER.md"
    ho = read_text(handover)
    tr = read_text(tracker)
    now_items = bullet_items(section(tr, "NOW"))
    awaiting = bullet_items(section(tr, "AWAITING"))
    ho_age = age_seconds(handover)
    stale = bool(now_items and ho_age is not None and ho_age > STALE_HANDOVER_SECONDS)
    if now_items and "NEVER" in (ho[:80] + first_line(section(ho, "1. Mission"))):
        stale = True
    reports: list[dict] = []
    reports_dir = workroom / "reports"
    if reports_dir.is_dir():
        files = [p for p in reports_dir.iterdir() if p.is_file()]
        files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        reports = [{"name": p.name, "mtime": iso_mtime(p)} for p in files[:12]]
    le = read_text(workroom / "LEDGER.md")
    return {
        "generated_at": now_utc().isoformat(),
        "workroom": str(workroom),
        "mission": first_line(section(ho, "1. Mission")) or first_line(section(ho, "Mission")),
        "next_task": first_line(section(ho, "3. Next first task"))
        or first_line(section(ho, "Next first task")),
        "lanes": {
            "now": now_items,
            "awaiting": awaiting,
            "awaiting_count": len(awaiting),
        },
        "branches": [ln.rstrip() for ln in le.splitlines() if ln.strip()][:24],
        "services": svc_status(workroom),
        "reports": reports,
        "live": parse_live(workroom / "live"),
        "mode": read_mode(workroom),
        "kit_health": {
            "handover_mtime": iso_mtime(handover),
            "handover_age_seconds": int(ho_age) if ho_age is not None else None,
            "stale": stale,
            "status": "STALE" if stale else "ok",
            "beat_fresh_seconds": BEAT_FRESH_SECONDS,
        },
    }


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) < 2:
        print("usage: project.py <workroom>", file=sys.stderr)
        raise SystemExit(2)
    print(json.dumps(project(Path(sys.argv[1]).resolve()), indent=2))
