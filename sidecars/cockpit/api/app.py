"""Cockpit API — Mission Control. Files for doctrine; SQLite for Task/Run."""
from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from watchfiles import awatch

from beat import write_beat
from mode import write_mode
from project import project
from room import room
from services import control, list_services
from store import (
    create_task,
    derive_occasion,
    get_task,
    list_runs,
    list_tasks,
    recent_events,
    update_task,
    upsert_run,
)
from tracker_sync import export_tracker, import_tracker_if_empty

WORKROOM = Path(os.environ.get("JARVIS_WORKROOM", "")).expanduser()
WEB_DIST = Path(__file__).resolve().parent.parent / "web" / "dist"

app = FastAPI(title="Jarvis Mission Control", docs_url=None, redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:3847",
        "http://localhost:3847",
        "http://127.0.0.1:5173",
    ],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


def _workroom() -> Path:
    if not WORKROOM or not WORKROOM.is_dir():
        raise HTTPException(503, "JARVIS_WORKROOM is not a directory")
    return WORKROOM


def _ensure_store(workroom: Path) -> None:
    import_tracker_if_empty(workroom)


def compose() -> dict:
    wr = _workroom() if WORKROOM.is_dir() else None
    room_state = project(wr) if wr else {}
    if wr:
        _ensure_store(wr)
        tasks = list_tasks(wr)
        runs = list_runs(wr)
        room_state["tasks"] = tasks
        room_state["runs"] = runs
        room_state["events"] = recent_events(wr, 24)
        room_state["occasion"] = derive_occasion(tasks, runs)
        waiting = next((t for t in tasks if t.get("status") == "waiting_for_user"), None)
        room_state["waiting"] = waiting
        room_state["service_board"] = list_services(wr, tcp_only=True)
    else:
        room_state["tasks"] = []
        room_state["runs"] = []
        room_state["events"] = []
        room_state["occasion"] = "away"
        room_state["waiting"] = None
        room_state["service_board"] = {"items": []}
    room_state["watching"] = room.watching
    return room_state


@app.get("/api/health")
def health() -> dict:
    return {"ok": True, "workroom": str(WORKROOM) if WORKROOM else ""}


@app.get("/api/state")
def state() -> dict:
    return compose()


class BeatIn(BaseModel):
    id: str = Field(min_length=1, max_length=64)
    role: str = ""
    mission: str = ""
    phase: str = "build"
    status: str = "running"
    task_id: str | None = None


@app.post("/api/live/beat")
def live_beat(body: BeatIn) -> dict:
    wr = _workroom()
    try:
        path = write_beat(
            wr,
            agent_id=body.id,
            role=body.role,
            mission=body.mission,
            phase=body.phase,
            status=body.status if body.status != "waiting_for_user" else "running",
        )
        run = upsert_run(
            wr,
            run_id=body.id,
            agent_id=body.id,
            task_id=body.task_id,
            role=body.role,
            mission=body.mission,
            phase=body.phase,
            status=body.status,
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"ok": True, "path": str(path), "run": run}


class ModeIn(BaseModel):
    mode: str


@app.post("/api/mode")
def set_mode(body: ModeIn) -> dict:
    try:
        path = write_mode(_workroom(), body.mode)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"ok": True, "path": str(path), "mode": body.mode.strip().lower()}


@app.get("/api/services")
def services() -> dict:
    return list_services(_workroom(), tcp_only=True)


class ServiceIn(BaseModel):
    action: str


@app.post("/api/services/{name}")
def service_control(name: str, body: ServiceIn) -> dict:
    try:
        return control(_workroom(), name, body.action)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


class TaskIn(BaseModel):
    title: str = Field(min_length=1, max_length=240)
    lane: str = "now"
    status: str = "queued"
    owner: str = "assistant"
    next_action: str = ""


class TaskPatch(BaseModel):
    title: str | None = None
    lane: str | None = None
    status: str | None = None
    owner: str | None = None
    next_action: str | None = None


@app.get("/api/tasks")
def tasks() -> dict:
    wr = _workroom()
    _ensure_store(wr)
    return {"items": list_tasks(wr)}


@app.post("/api/tasks")
def task_create(body: TaskIn) -> dict:
    wr = _workroom()
    _ensure_store(wr)
    try:
        task = create_task(
            wr,
            title=body.title,
            lane=body.lane,
            status=body.status,
            owner=body.owner,
            next_action=body.next_action,
        )
        export_tracker(wr)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"ok": True, "task": task}


@app.post("/api/tasks/{task_id}")
def task_patch(task_id: str, body: TaskPatch) -> dict:
    wr = _workroom()
    try:
        task = update_task(
            wr,
            task_id,
            title=body.title or None,
            lane=body.lane or None,
            status=body.status or None,
            owner=body.owner or None,
            next_action=body.next_action or None,
        )
        export_tracker(wr)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"ok": True, "task": task}


@app.post("/api/tasks/{task_id}/wait")
def task_wait(task_id: str) -> dict:
    wr = _workroom()
    if not get_task(wr, task_id):
        raise HTTPException(404, "unknown task")
    try:
        task = update_task(
            wr,
            task_id,
            status="waiting_for_user",
            lane="awaiting",
            next_action="principal decision",
        )
        export_tracker(wr)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"ok": True, "task": task}


@app.post("/api/tasks/{task_id}/not-now")
def task_not_now(task_id: str) -> dict:
    wr = _workroom()
    if not get_task(wr, task_id):
        raise HTTPException(404, "unknown task")
    try:
        task = update_task(
            wr,
            task_id,
            status="parked",
            lane="parked",
            next_action="revisit: principal said not now",
        )
        export_tracker(wr)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"ok": True, "task": task}


@app.post("/api/tasks/{task_id}/resume")
def task_resume(task_id: str) -> dict:
    wr = _workroom()
    if not get_task(wr, task_id):
        raise HTTPException(404, "unknown task")
    try:
        task = update_task(
            wr,
            task_id,
            status="running",
            lane="now",
            next_action="resumed",
        )
        export_tracker(wr)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"ok": True, "task": task}


@app.websocket("/api/stream")
async def stream(ws: WebSocket) -> None:
    await ws.accept()
    if not WORKROOM.is_dir():
        await ws.close(code=1011)
        return
    await room.join(ws)
    await room.broadcast(compose())
    try:
        async for _ in awatch(WORKROOM, recursive=True):
            await room.broadcast(compose())
    except WebSocketDisconnect:
        pass
    finally:
        await room.leave(ws)
        await room.broadcast(compose())


if WEB_DIST.is_dir():
    app.mount("/", StaticFiles(directory=str(WEB_DIST), html=True), name="ui")
