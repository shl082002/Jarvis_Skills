"""Gauntlet declare flag — same file the gauntlet CLI uses."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

STONE_NAMES = ("reality", "time", "mind")


def flag_path(workroom: Path) -> Path:
    return workroom / "run" / "GAUNTLET_ACTIVE"


def read_gauntlet(workroom: Path) -> dict:
    path = flag_path(workroom)
    if not path.is_file():
        return {"on": False, "reason": ""}
    text = path.read_text(encoding="utf-8", errors="replace").strip()
    reason = text.split(" — opened", 1)[0].strip() if text else "declared"
    return {"on": True, "reason": reason}


def _clear_dir(folder: Path) -> None:
    if not folder.is_dir():
        return
    for child in folder.iterdir():
        if child.is_file():
            child.unlink()


def set_gauntlet(workroom: Path, on: bool, reason: str = "") -> dict:
    run = workroom / "run"
    stones = run / "stones"
    claims = run / "claims"
    sessions = run / "sessions"
    for folder in (run, stones, claims, sessions, workroom / "gauntlet"):
        folder.mkdir(parents=True, exist_ok=True)
    path = flag_path(workroom)
    if on:
        why = (reason or "declared from Mission Control").strip()[:240]
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        path.write_text(f"{why} — opened {stamp}\n", encoding="utf-8")
        for name in STONE_NAMES:
            (stones / name).write_text("", encoding="utf-8")
        _clear_dir(claims)
        _clear_dir(sessions)
    else:
        path.unlink(missing_ok=True)
        for name in STONE_NAMES:
            target = stones / name
            if target.is_file():
                target.write_text("", encoding="utf-8")
        _clear_dir(claims)
        _clear_dir(sessions)
    return read_gauntlet(workroom)
