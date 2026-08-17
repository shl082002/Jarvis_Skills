#!/usr/bin/env python3
"""Wake the open Cursor agent when Mission Control needs a follow-up turn.

Portable: walk up to .jarvis. Install copies this to .cursor/hooks/.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def find_workroom() -> Path:
    for parent in Path(__file__).resolve().parents:
        wr = parent / ".jarvis"
        if wr.is_dir() and (
            (wr / "HANDOVER.md").is_file()
            or (wr / "LEDGER.md").is_file()
            or (wr / "dispatch.json").is_file()
        ):
            return wr
    return Path(__file__).resolve().parents[2] / ".jarvis"


def _empty() -> None:
    sys.stdout.write("{}\n")


def main() -> None:
    payload = {}
    raw = sys.stdin.read()
    if raw.strip():
        try:
            loaded = json.loads(raw)
            if isinstance(loaded, dict):
                payload = loaded
        except json.JSONDecodeError:
            payload = {}

    if payload.get("status") == "aborted":
        _empty()
        return
    if int(payload.get("loop_count") or 0) >= 3:
        _empty()
        return

    workroom = find_workroom()
    dispatch = workroom / "dispatch.json"
    claim_dir = workroom / "run"

    if not dispatch.is_file():
        _empty()
        return
    try:
        data = json.loads(dispatch.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        _empty()
        return
    if not isinstance(data, dict):
        _empty()
        return

    action = str(data.get("action") or "")
    claim_dir.mkdir(parents=True, exist_ok=True)

    if action == "reply":
        task = str(data.get("task_id") or "?")
        stamp = str(data.get("at") or "").replace(":", "")[:18]
        claimed = claim_dir / f"wake-reply-{task}-{stamp}"
        if claimed.is_file():
            _empty()
            return
        claimed.write_text("woken\n", encoding="utf-8")
        ruling = str(data.get("text") or "").strip() or "(empty)"
        if data.get("parked"):
            msg = (
                f"Principal from Telegram/board on {task}: not now. "
                f"Park that slice. Do not continue it. Ruling: {ruling}"
            )
        else:
            msg = (
                f"Jarvis: principal ruling on {task} from Telegram: {ruling} "
                "You are the commander — acknowledge it in this chat and dispatch the fleet. "
                "Do not wait for another beat. Do not use Cursor CLI agent -p."
            )
        sys.stdout.write(json.dumps({"followup_message": msg}) + "\n")
        return

    run_id = str(data.get("run_id") or "")
    if action not in {"deploy", "stop"} or not run_id:
        _empty()
        return

    claimed = claim_dir / f"wake-{run_id}"
    if claimed.is_file():
        _empty()
        return
    claimed.write_text("woken\n", encoding="utf-8")

    agent = data.get("agent_id") or "?"
    task = data.get("task_id") or "?"
    mission = data.get("mission") or ""
    msg = (
        f"Mission Control {action}: {agent} on {task} (run {run_id}). "
        f"{mission} "
        "Honor it in this chat now — launch or interrupt that fleet hat, beat the run, "
        "write a report if deploy. Do not use Cursor CLI agent -p. "
        "Read .jarvis/dispatch.json."
    )
    sys.stdout.write(json.dumps({"followup_message": msg}) + "\n")


if __name__ == "__main__":
    main()
