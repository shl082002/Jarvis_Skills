"""SQLite control plane. Workroom file is portable truth for Task/Run/Event/Approval."""
from __future__ import annotations

import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

LANES = ("now", "awaiting", "next", "parked", "done")
TASK_STATUSES = (
    "queued",
    "running",
    "waiting_for_user",
    "verifying",
    "completed",
    "failed",
    "parked",
)
RUN_STATUSES = ("queued", "running", "idle", "done", "failed", "waiting_for_user", "stopped")
TASK_ID_RE = re.compile(r"^T-\d+$")

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS tasks (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  lane TEXT NOT NULL,
  status TEXT NOT NULL,
  owner TEXT NOT NULL DEFAULT 'assistant',
  next_action TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS agent_runs (
  id TEXT PRIMARY KEY,
  task_id TEXT,
  agent_id TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT '',
  mission TEXT NOT NULL DEFAULT '',
  phase TEXT NOT NULL DEFAULT 'build',
  status TEXT NOT NULL DEFAULT 'running',
  report_path TEXT NOT NULL DEFAULT '',
  started_at TEXT NOT NULL,
  last_beat_at TEXT NOT NULL,
  ended_at TEXT
);
CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  type TEXT NOT NULL,
  payload TEXT NOT NULL DEFAULT '{}',
  task_id TEXT,
  run_id TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS approvals (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL,
  status TEXT NOT NULL,
  reason TEXT NOT NULL DEFAULT '',
  task_id TEXT,
  opened_at TEXT NOT NULL,
  expires_at TEXT,
  consumed_at TEXT
);
"""


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def db_path(workroom: Path) -> Path:
    return workroom / "control.db"


def connect(workroom: Path) -> sqlite3.Connection:
    workroom.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path(workroom)))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    conn.commit()
    return conn


def _next_task_n(conn: sqlite3.Connection) -> int:
    row = conn.execute("SELECT value FROM meta WHERE key = 'next_task_n'").fetchone()
    if row:
        return int(row["value"])
    n = 1
    for (tid,) in conn.execute("SELECT id FROM tasks"):
        m = re.match(r"^T-(\d+)$", tid)
        if m:
            n = max(n, int(m.group(1)) + 1)
    conn.execute(
        "INSERT OR REPLACE INTO meta(key, value) VALUES ('next_task_n', ?)",
        (str(n),),
    )
    return n


def emit(conn: sqlite3.Connection, typ: str, payload: dict, task_id: str | None = None, run_id: str | None = None) -> None:
    conn.execute(
        "INSERT INTO events(type, payload, task_id, run_id, created_at) VALUES (?,?,?,?,?)",
        (typ, json.dumps(payload), task_id, run_id, now_iso()),
    )


def task_row(row: sqlite3.Row) -> dict:
    return dict(row)


def list_tasks(workroom: Path) -> list[dict]:
    conn = connect(workroom)
    try:
        rows = conn.execute(
            "SELECT * FROM tasks ORDER BY updated_at DESC"
        ).fetchall()
        return [task_row(r) for r in rows]
    finally:
        conn.close()


def get_task(workroom: Path, task_id: str) -> dict | None:
    conn = connect(workroom)
    try:
        row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        return task_row(row) if row else None
    finally:
        conn.close()


def create_task(
    workroom: Path,
    *,
    title: str,
    lane: str = "now",
    status: str = "queued",
    owner: str = "assistant",
    next_action: str = "",
    task_id: str | None = None,
) -> dict:
    title = title.strip()
    if not title:
        raise ValueError("title required")
    lane = lane.strip().lower()
    status = status.strip().lower()
    if lane not in LANES:
        raise ValueError(f"lane must be one of {LANES}")
    if status not in TASK_STATUSES:
        raise ValueError(f"status must be one of {TASK_STATUSES}")
    conn = connect(workroom)
    try:
        if task_id:
            if not TASK_ID_RE.match(task_id):
                raise ValueError("id must look like T-12")
        else:
            n = _next_task_n(conn)
            task_id = f"T-{n}"
            conn.execute(
                "INSERT OR REPLACE INTO meta(key, value) VALUES ('next_task_n', ?)",
                (str(n + 1),),
            )
        ts = now_iso()
        conn.execute(
            """INSERT INTO tasks(id, title, lane, status, owner, next_action, created_at, updated_at)
               VALUES (?,?,?,?,?,?,?,?)""",
            (task_id, title[:240], lane, status, owner[:80], next_action[:240], ts, ts),
        )
        emit(conn, "TASK_UPSERT", {"id": task_id, "title": title, "lane": lane, "status": status}, task_id)
        conn.commit()
        row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        return task_row(row)
    finally:
        conn.close()


def update_task(workroom: Path, task_id: str, **fields: str) -> dict:
    allowed = {"title", "lane", "status", "owner", "next_action"}
    patch = {k: v for k, v in fields.items() if k in allowed and v is not None}
    if "lane" in patch and patch["lane"] not in LANES:
        raise ValueError(f"lane must be one of {LANES}")
    if "status" in patch and patch["status"] not in TASK_STATUSES:
        raise ValueError(f"status must be one of {TASK_STATUSES}")
    conn = connect(workroom)
    try:
        row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        if not row:
            raise ValueError("unknown task")
        if not patch:
            return task_row(row)
        sets = ", ".join(f"{k} = ?" for k in patch)
        vals = list(patch.values()) + [now_iso(), task_id]
        conn.execute(f"UPDATE tasks SET {sets}, updated_at = ? WHERE id = ?", vals)
        emit(conn, "TASK_UPSERT", {"id": task_id, **patch}, task_id)
        conn.commit()
        row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        return task_row(row)
    finally:
        conn.close()


def list_runs(workroom: Path, task_id: str | None = None) -> list[dict]:
    conn = connect(workroom)
    try:
        if task_id:
            rows = conn.execute(
                "SELECT * FROM agent_runs WHERE task_id = ? ORDER BY last_beat_at DESC",
                (task_id,),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM agent_runs ORDER BY last_beat_at DESC"
            ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def upsert_run(
    workroom: Path,
    *,
    run_id: str,
    agent_id: str,
    task_id: str | None = None,
    role: str = "",
    mission: str = "",
    phase: str = "build",
    status: str = "running",
    report_path: str = "",
) -> dict:
    slug = run_id.strip().lower()
    if not slug:
        raise ValueError("run id required")
    status = status if status in RUN_STATUSES else "running"
    ts = now_iso()
    conn = connect(workroom)
    try:
        existing = conn.execute("SELECT * FROM agent_runs WHERE id = ?", (slug,)).fetchone()
        if existing:
            ended = ts if status in {"stopped", "done", "failed"} else None
            conn.execute(
                """UPDATE agent_runs SET task_id=COALESCE(?, task_id), role=COALESCE(NULLIF(?,''), role),
                   mission=COALESCE(NULLIF(?,''), mission), phase=?, status=?,
                   report_path=COALESCE(NULLIF(?,''), report_path), last_beat_at=?,
                   ended_at=COALESCE(?, ended_at)
                   WHERE id=?""",
                (task_id, role, mission, phase, status, report_path, ts, ended, slug),
            )
        else:
            conn.execute(
                """INSERT INTO agent_runs(id, task_id, agent_id, role, mission, phase, status, report_path, started_at, last_beat_at)
                   VALUES (?,?,?,?,?,?,?,?,?,?)""",
                (slug, task_id, agent_id.strip()[:64], role[:80], mission[:240], phase[:40], status, report_path[:400], ts, ts),
            )
        emit(conn, "RUN_BEAT", {"id": slug, "status": status, "agent_id": agent_id}, task_id, slug)
        conn.commit()
        row = conn.execute("SELECT * FROM agent_runs WHERE id = ?", (slug,)).fetchone()
        return dict(row)
    finally:
        conn.close()


def recent_events(workroom: Path, limit: int = 40) -> list[dict]:
    conn = connect(workroom)
    try:
        rows = conn.execute(
            "SELECT * FROM events ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
        out = []
        for r in rows:
            item = dict(r)
            try:
                item["payload"] = json.loads(item["payload"])
            except json.JSONDecodeError:
                pass
            out.append(item)
        return out
    finally:
        conn.close()


def derive_occasion(tasks: list[dict], runs: list[dict]) -> str:
    """Locked mix: crisis if waiting, deep if a run is live, else away. Showcase is not auto."""
    if any(t.get("status") == "waiting_for_user" for t in tasks):
        return "crisis"
    if any(r.get("status") in {"running", "queued"} for r in runs):
        return "deep"
    return "away"
