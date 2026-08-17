"""Write a heartbeat file. The file is truth; this is only a helper."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ALLOWED_PHASE = {"scout", "build", "verify", "blocked", "idle"}
ALLOWED_STATUS = {"running", "idle", "done", "failed"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{0,63}$")


def write_beat(
    workroom: Path,
    *,
    agent_id: str,
    role: str = "",
    mission: str = "",
    phase: str = "build",
    status: str = "running",
) -> Path:
    slug = agent_id.strip().lower()
    if not ID_RE.match(slug):
        raise ValueError("id must be a short slug (letters, digits, ._-)")
    phase = phase if phase in ALLOWED_PHASE else "idle"
    status = status if status in ALLOWED_STATUS else "running"
    live = workroom / "live"
    live.mkdir(parents=True, exist_ok=True)
    path = live / f"{slug}.json"
    now = datetime.now(timezone.utc).isoformat()
    existing: dict = {}
    if path.is_file():
        try:
            loaded = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                existing = loaded
        except (OSError, json.JSONDecodeError):
            existing = {}
    payload = {
        "id": slug,
        "role": (role or existing.get("role") or slug)[:80],
        "mission": (mission or existing.get("mission") or "")[:240],
        "phase": phase,
        "status": status,
        "started_at": existing.get("started_at") or now,
        "last_beat": now,
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path
