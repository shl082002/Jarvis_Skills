"""Morning OPEN clock — principal grant via Mission Control. Portable kit."""
from __future__ import annotations

import hashlib
import json
import os
import plistlib
import subprocess
import sys
from pathlib import Path
from typing import Any

CONFIG_NAME = "MORNING_OPEN.json"


def config_path(workroom: Path) -> Path:
    return workroom / "run" / CONFIG_NAME


def read_morning(workroom: Path) -> dict[str, Any]:
    path = config_path(workroom)
    defaults = {
        "on": False,
        "hour": 6,
        "minute": 0,
        "note": "Mac local clock. Off until you arm it on the face.",
        "backend": "none",
        "last_error": "",
    }
    if not path.is_file():
        return defaults
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return defaults
    if not isinstance(data, dict):
        return defaults
    out = {**defaults, **data}
    out["on"] = bool(out.get("on"))
    try:
        out["hour"] = max(0, min(23, int(out.get("hour", 6))))
        out["minute"] = max(0, min(59, int(out.get("minute", 0))))
    except (TypeError, ValueError):
        out["hour"], out["minute"] = 6, 0
    return out


def _script(workroom: Path) -> Path:
    for cand in (
        workroom / "bin" / "morning-open",
        workroom / "kit" / "bin" / "morning-open",
    ):
        if cand.is_file():
            return cand
    raise FileNotFoundError("morning-open binary missing — re-run kit install")


def _label(workroom: Path) -> str:
    digest = hashlib.sha256(str(workroom.resolve()).encode()).hexdigest()[:12]
    return f"com.jarvis.morning-open.{digest}"


def _plist_path(workroom: Path) -> Path:
    home = Path.home() / "Library" / "LaunchAgents"
    return home / f"{_label(workroom)}.plist"


def _unload_darwin(label: str, plist: Path) -> None:
    uid = os.getuid()
    domain = f"gui/{uid}/{label}"
    subprocess.run(
        ["launchctl", "bootout", domain],
        check=False,
        capture_output=True,
        text=True,
    )
    if plist.is_file():
        plist.unlink()


def _load_darwin(workroom: Path, hour: int, minute: int) -> str:
    script = _script(workroom).resolve()
    label = _label(workroom)
    agents = Path.home() / "Library" / "LaunchAgents"
    agents.mkdir(parents=True, exist_ok=True)
    plist = _plist_path(workroom)
    payload = {
        "Label": label,
        "ProgramArguments": [sys.executable, str(script)],
        "EnvironmentVariables": {
            "JARVIS_WORKROOM": str(workroom.resolve()),
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        },
        "StartCalendarInterval": {"Hour": hour, "Minute": minute},
        "StandardOutPath": str(workroom / "logs" / "morning-open.launchd.out.log"),
        "StandardErrorPath": str(workroom / "logs" / "morning-open.launchd.err.log"),
        "RunAtLoad": False,
    }
    (workroom / "logs").mkdir(parents=True, exist_ok=True)
    with plist.open("wb") as fh:
        plistlib.dump(payload, fh)
    uid = os.getuid()
    subprocess.run(
        ["launchctl", "bootstrap", f"gui/{uid}", str(plist)],
        check=True,
        capture_output=True,
        text=True,
    )
    return "launchd"


def set_morning(workroom: Path, on: bool, hour: int = 6, minute: int = 0) -> dict[str, Any]:
    run = workroom / "run"
    run.mkdir(parents=True, exist_ok=True)
    hour = max(0, min(23, int(hour)))
    minute = max(0, min(59, int(minute)))
    err = ""
    backend = "none"
    label = _label(workroom)
    plist = _plist_path(workroom)
    if sys.platform == "darwin":
        try:
            _unload_darwin(label, plist)
            if on:
                backend = _load_darwin(workroom, hour, minute)
        except (OSError, subprocess.CalledProcessError, FileNotFoundError) as exc:
            detail = getattr(exc, "stderr", None) or getattr(exc, "stdout", None) or str(exc)
            err = str(detail)[:400]
            on = False
            backend = "none"
    elif on:
        err = "Morning OPEN timer is launchd (macOS). Arm the face on a Mac, or run bin/morning-open from cron yourself."
        on = False
    data = {
        "on": on,
        "hour": hour,
        "minute": minute,
        "note": "Fires on this Mac's local clock. Does not open Cursor/Claude.",
        "backend": backend,
        "last_error": err,
        "label": label if on else "",
    }
    config_path(workroom).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return read_morning(workroom)
