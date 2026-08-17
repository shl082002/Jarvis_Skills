"""Import TRACKER.md once; export after every Task write. Store is write authority."""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

from store import LANES, connect, create_task, list_tasks, _next_task_n

ITEM_RE = re.compile(
    r"^- \*\*(T-\d+)\*\*\s*·\s*(.+)$",
)
LANE_HEAD = {
    "now": "## NOW",
    "awaiting": "## AWAITING",
    "next": "## NEXT",
    "parked": "## PARKED",
    "done": "## DONE",
}


def _section(md: str, heading_prefix: str) -> str:
    pat = re.compile(
        r"^" + re.escape(heading_prefix) + r"[^\n]*\n(.*?)(?=^## |\Z)",
        re.M | re.S,
    )
    m = pat.search(md)
    return m.group(1) if m else ""


def import_tracker_if_empty(workroom: Path) -> int:
    """Seed SQLite from TRACKER.md when the task table is empty. Returns imported count."""
    conn = connect(workroom)
    try:
        n = conn.execute("SELECT COUNT(*) AS c FROM tasks").fetchone()["c"]
        if n:
            return 0
        max_n = _next_task_n(conn) - 1
    finally:
        conn.close()

    path = workroom / "TRACKER.md"
    if not path.is_file():
        return 0
    md = path.read_text(encoding="utf-8", errors="replace")
    imported = 0
    for lane in LANES:
        body = _section(md, LANE_HEAD[lane])
        for line in body.splitlines():
            m = ITEM_RE.match(line.strip())
            if not m:
                continue
            tid, rest = m.group(1), m.group(2).strip()
            title = rest.split(" · ")[0].strip()
            status = "queued"
            if lane == "awaiting":
                status = "waiting_for_user"
            elif lane == "parked":
                status = "parked"
            elif lane == "done":
                status = "completed"
            elif lane == "now":
                status = "running"
            try:
                create_task(
                    workroom,
                    title=title or tid,
                    lane=lane,
                    status=status,
                    task_id=tid,
                    next_action=rest[:240],
                )
                imported += 1
                num = int(tid.split("-", 1)[1])
                max_n = max(max_n, num)
            except ValueError:
                continue
    conn = connect(workroom)
    try:
        conn.execute(
            "INSERT OR REPLACE INTO meta(key, value) VALUES ('next_task_n', ?)",
            (str(max_n + 1),),
        )
        conn.commit()
    finally:
        conn.close()
    return imported


def export_tracker(workroom: Path) -> None:
    tasks = list_tasks(workroom)
    conn = connect(workroom)
    try:
        n = _next_task_n(conn)
    finally:
        conn.close()
    by: dict[str, list[dict]] = {lane: [] for lane in LANES}
    for t in tasks:
        by.setdefault(t["lane"], []).append(t)

    def bullets(lane: str) -> str:
        items = by.get(lane) or []
        if not items:
            return "*(none)*\n"
        lines = []
        for t in items:
            extra = t.get("next_action") or ""
            owner = t.get("owner") or "assistant"
            status = t.get("status") or ""
            bit = f"- **{t['id']}** · {t['title']} · owner: {owner} · status: {status}"
            if extra:
                bit += f" · {extra}"
            lines.append(bit)
        return "\n".join(lines) + "\n"

    today = date.today().isoformat()
    md = (
        f"# TRACKER — the one list · updated: {today} · next free ID: T-{n}\n\n"
        f"## NOW — being worked\n{bullets('now')}\n"
        f"## AWAITING — blocked on the principal or external\n{bullets('awaiting')}\n"
        f"## NEXT — open, queued\n{bullets('next')}\n"
        f"## PARKED — deliberately deferred (each with a revisit condition)\n{bullets('parked')}\n"
        f"## DONE — recent (pruned at day-close)\n{bullets('done')}"
    )
    (workroom / "TRACKER.md").write_text(md, encoding="utf-8")
