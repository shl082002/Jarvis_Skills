#!/usr/bin/env python3
"""Project workroom files into state.json. Read-only. No second tracker."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

STALE_SECONDS = 24 * 60 * 60
BEAT_STALE_SECONDS = 15 * 60


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
    items = []
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


def parse_live(live_dir: Path) -> list[dict]:
    if not live_dir.is_dir():
        return []
    out = []
    for p in sorted(live_dir.glob("*.json")):
        if p.name == "heimdall-state.json":
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(data, dict):
            continue
        beat = data.get("last_beat") or ""
        status = "unknown"
        try:
            beat_dt = datetime.fromisoformat(str(beat).replace("Z", "+00:00"))
            if beat_dt.tzinfo is None:
                beat_dt = beat_dt.replace(tzinfo=timezone.utc)
            delta = (now_utc() - beat_dt).total_seconds()
            if delta <= BEAT_STALE_SECONDS:
                status = str(data.get("status") or "unknown")
            else:
                status = "unknown"
        except (TypeError, ValueError):
            status = "unknown"
        out.append(
            {
                "id": data.get("id") or p.stem,
                "role": data.get("role") or "",
                "mission": data.get("mission") or "",
                "phase": data.get("phase") or "",
                "status": status,
                "last_beat": beat,
            }
        )
    return out


def svc_status(workroom: Path) -> str:
    svc = workroom / "bin" / "svc"
    if not svc.is_file():
        return "unknown"
    try:
        r = subprocess.run(
            [str(svc), "status"],
            capture_output=True,
            text=True,
            timeout=8,
        )
        text = (r.stdout or r.stderr or "").strip()
        return text[:2000] if text else "unknown"
    except (OSError, subprocess.TimeoutExpired):
        return "unknown"


def project(workroom: Path) -> dict:
    handover = workroom / "HANDOVER.md"
    tracker = workroom / "TRACKER.md"
    ledger = workroom / "LEDGER.md"
    reports = workroom / "reports"
    live = workroom / "live"

    ho = read_text(handover)
    tr = read_text(tracker)
    le = read_text(ledger)

    now_items = bullet_items(section(tr, "NOW"))
    awaiting = bullet_items(section(tr, "AWAITING"))
    ho_age = age_seconds(handover)
    stale = bool(
        now_items
        and ho_age is not None
        and ho_age > STALE_SECONDS
    )
    if "NEVER" in (first_line(section(ho, "1. Mission")) + read_text(handover)[:80]):
        if now_items:
            stale = True

    report_rows = []
    if reports.is_dir():
        files = [p for p in reports.iterdir() if p.is_file()]
        files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        for p in files[:12]:
            report_rows.append({"name": p.name, "mtime": iso_mtime(p)})

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
        "reports": report_rows,
        "live": parse_live(live),
        "kit_health": {
            "handover_mtime": iso_mtime(handover),
            "handover_age_seconds": int(ho_age) if ho_age is not None else None,
            "stale": stale,
            "status": "STALE" if stale else "ok",
        },
    }


def write_state(workroom: Path, kit_root: Path | None = None) -> Path:
    state = project(workroom)
    dests = []
    if kit_root:
        dist = kit_root / "sidecars" / "heimdall" / "dist"
        dist.mkdir(parents=True, exist_ok=True)
        dests.append(dist / "state.json")
    live = workroom / "live"
    live.mkdir(parents=True, exist_ok=True)
    dests.append(live / "heimdall-state.json")
    payload = json.dumps(state, indent=2) + "\n"
    for d in dests:
        d.write_text(payload, encoding="utf-8")
    return dests[0]


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: project.py <workroom> [kit-root]", file=sys.stderr)
        return 2
    workroom = Path(argv[1]).resolve()
    kit = Path(argv[2]).resolve() if len(argv) > 2 else None
    path = write_state(workroom, kit)
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
