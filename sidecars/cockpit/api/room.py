"""In-memory spectators. Not a second tracker."""
from __future__ import annotations

import asyncio
from typing import Any

from fastapi import WebSocket


class Room:
    def __init__(self) -> None:
        self._clients: set[WebSocket] = set()
        self._lock = asyncio.Lock()

    @property
    def watching(self) -> int:
        return len(self._clients)

    async def join(self, ws: WebSocket) -> None:
        async with self._lock:
            self._clients.add(ws)

    async def leave(self, ws: WebSocket) -> None:
        async with self._lock:
            self._clients.discard(ws)

    async def broadcast(self, payload: dict[str, Any]) -> None:
        dead: list[WebSocket] = []
        async with self._lock:
            clients = list(self._clients)
        for ws in clients:
            try:
                await ws.send_json(payload)
            except Exception:
                dead.append(ws)
        for ws in dead:
            await self.leave(ws)


room = Room()
