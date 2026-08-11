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
from project import project

WORKROOM = Path(os.environ.get("JARVIS_WORKROOM", "")).expanduser()
WEB_DIST = Path(__file__).resolve().parent.parent / "web" / "dist"

app = FastAPI(title="Jarvis cockpit", docs_url=None, redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3847", "http://localhost:3847", "http://127.0.0.1:5173"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


def _workroom() -> Path:
    if not WORKROOM or not WORKROOM.is_dir():
        raise HTTPException(503, "JARVIS_WORKROOM is not a directory")
    return WORKROOM


@app.get("/api/health")
def health() -> dict:
    return {"ok": True, "workroom": str(WORKROOM) if WORKROOM else ""}


@app.get("/api/state")
def state() -> dict:
    return project(_workroom())


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


@app.websocket("/api/stream")
async def stream(ws: WebSocket) -> None:
    await ws.accept()
    room = WORKROOM
    if not room.is_dir():
        await ws.close(code=1011)
        return
    await ws.send_json(project(room))
    try:
        async for _ in awatch(room, recursive=True):
            await ws.send_json(project(room))
    except WebSocketDisconnect:
        return


if WEB_DIST.is_dir():
    app.mount("/", StaticFiles(directory=str(WEB_DIST), html=True), name="ui")
