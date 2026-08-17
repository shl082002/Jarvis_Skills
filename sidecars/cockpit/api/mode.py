"""Standing gear. Chat words still win over this file."""
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ALLOWED = ("discuss", "plan", "build")
MODE_RE = re.compile(r"^mode:\s*(discuss|plan|build)\b", re.I | re.M)


def read_mode(workroom: Path) -> str:
    text = ""
    path = workroom / "MODE.md"
    if path.is_file():
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            return "unknown"
    match = MODE_RE.search(text)
    if not match:
        return "unknown"
    return match.group(1).lower()


def write_mode(workroom: Path, mode: str) -> Path:
    gear = mode.strip().lower()
    if gear not in ALLOWED:
        raise ValueError("mode must be discuss, plan, or build")
    path = workroom / "MODE.md"
    now = datetime.now(timezone.utc).isoformat()
    path.write_text(
        f"# MODE — standing gear. Chat words still override.\n"
        f"mode: {gear}\n"
        f"updated_at: {now}\n",
        encoding="utf-8",
    )
    return path
