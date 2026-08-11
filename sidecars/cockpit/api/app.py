"""Cockpit API — projector over the workroom. Bind 127.0.0.1 only."""
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

WORKROOM = Path(os.environ.get("JARVIS_WORKROOM", "")).expanduser()
WEB_DIST = Path(__file__).resolve().parent.parent / "web" / "dist"

app = FastAPI(title="Jarvis cockpit", docs_url=None, redoc_url=None)
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


def compose() -> dict:
    room_state = project(_workroom()) if WORKROOM.is_dir() else {}
    room_state["watching"] = room.watching
    room_state["service_board"] = (
        list_services(_workroom()) if WORKROOM.is_dir() else {"items": []}
    )
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


@app.post("/api/live/beat")
def live_beat(body: BeatIn) -> dict:
    try:
        path = write_beat(
            _workroom(),
            agent_id=body.id,
            role=body.role,
            mission=body.mission,
            phase=body.phase,
            status=body.status,
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"ok": True, "path": str(path)}


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
    return list_services(_workroom())


class ServiceIn(BaseModel):
    action: str


@app.post("/api/services/{name}")
def service_control(name: str, body: ServiceIn) -> dict:
    try:
        return control(_workroom(), name, body.action)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


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
