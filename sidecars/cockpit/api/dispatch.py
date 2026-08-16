"""Principal-owned run verbs. Inbox for the open Cursor chat — not a CLI watcher."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from mode import read_mode
from store import get_task, list_runs, now_iso, upsert_run

FLEET = {
    "dum-e": ("scout", "scout"),
    "u": ("librarian", "scout"),
    "jocasta": ("researcher", "scout"),
    "friday": ("builder", "build"),
    "edith": ("verifier", "verify"),
    "pepper": ("product", "scout"),
    "happy": ("ops", "scout"),
}

MUTATE_AGENTS = frozenset({"friday"})


def write_principal_reply(
    workroom: Path,
    *,
    task_id: str,
    text: str,
    parked: bool = False,
) -> dict[str, Any]:
    """Gym loop: principal ruling for the open Cursor chat (stop-hook wake)."""
    clipped = (text or "").strip()[:2000]
    inbox = {
        "at": now_iso(),
        "action": "reply",
        "task_id": task_id,
        "text": clipped,
        "parked": parked,
        "hands": "open Cursor chat — honor the Telegram/board ruling; do not wait in Cursor",
    }
    write_dispatch(workroom, inbox)
    return inbox


def write_dispatch(workroom: Path, payload: dict[str, Any]) -> Path:
    path = workroom / "dispatch.json"
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def read_dispatch(workroom: Path) -> Optional[dict[str, Any]]:
    path = workroom / "dispatch.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def _run_id(agent_id: str, task_id: str) -> str:
    slug_task = task_id.strip().lower().replace("_", "-")
    stamp = now_iso().replace(":", "").replace("-", "")[:15].lower()
    return f"{agent_id}-{slug_task}-{stamp}"[:64]


def deploy_run(
    workroom: Path,
    *,
    task_id: str,
    agent_id: str,
    mission: str = "",
) -> dict[str, Any]:
    gear = read_mode(workroom)
    agent = agent_id.strip().lower()
    if agent not in FLEET:
        raise ValueError(f"unknown agent — use one of {sorted(FLEET)}")
    if gear in {"discuss", "plan"} and agent in MUTATE_AGENTS:
        raise ValueError("discuss/plan refuse Deploy of FRIDAY — switch to build")
    task = get_task(workroom, task_id)
    if not task:
        raise ValueError("unknown task")
    role, phase = FLEET[agent]
    text = (mission.strip() or f"{role} on {task_id}: {task.get('title') or ''}")[:240]
    run_id = _run_id(agent, task_id)
    run = upsert_run(
        workroom,
        run_id=run_id,
        agent_id=agent,
        task_id=task_id,
        role=role,
        mission=text,
        phase=phase,
        status="queued",
    )
    inbox = {
        "at": now_iso(),
        "action": "deploy",
        "run_id": run["id"],
        "task_id": task_id,
        "agent_id": agent,
        "role": role,
        "mission": text,
        "hands": "open Cursor chat — Jarvis launches this agent; no CLI watcher",
    }
    write_dispatch(workroom, inbox)
    return {"run": run, "dispatch": inbox}


def stop_run(workroom: Path, run_id: str) -> dict[str, Any]:
    runs = {r["id"]: r for r in list_runs(workroom)}
    existing = runs.get(run_id)
    if not existing:
        raise ValueError("unknown run")
    run = upsert_run(
        workroom,
        run_id=run_id,
        agent_id=existing["agent_id"],
        task_id=existing.get("task_id"),
        role=existing.get("role") or "",
        mission=existing.get("mission") or "",
        phase=existing.get("phase") or "idle",
        status="stopped",
        report_path=existing.get("report_path") or "",
    )
    inbox = {
        "at": now_iso(),
        "action": "stop",
        "run_id": run["id"],
        "task_id": existing.get("task_id"),
        "agent_id": existing["agent_id"],
        "hands": "open Cursor chat — Jarvis interrupts this agent",
    }
    write_dispatch(workroom, inbox)
    return {"run": run, "dispatch": inbox}


def explain_run(workroom: Path, run_id: str) -> dict[str, Any]:
    runs = {r["id"]: r for r in list_runs(workroom)}
    run = runs.get(run_id)
    if not run:
        raise ValueError("unknown run")
    task = get_task(workroom, run["task_id"]) if run.get("task_id") else None
    live_path = workroom / "live" / f"{run['agent_id']}.json"
    live: Optional[dict[str, Any]] = None
    if live_path.is_file():
        try:
            loaded = json.loads(live_path.read_text(encoding="utf-8"))
            live = loaded if isinstance(loaded, dict) else None
        except (OSError, json.JSONDecodeError):
            live = None
    lines = [
        f"{run.get('agent_id')} is {run.get('status')} on {run.get('task_id') or 'no task'}.",
        f"Mission: {run.get('mission') or '—'}",
        f"Phase {run.get('phase') or '—'} · last beat {run.get('last_beat_at') or '—'}.",
    ]
    if run.get("report_path"):
        lines.append(f"Report: {run['report_path']}")
    else:
        lines.append("No report yet — Deploy queues work; Jarvis in chat is the hands.")
    return {
        "run": run,
        "task": task,
        "live": live,
        "summary": " ".join(lines),
    }
