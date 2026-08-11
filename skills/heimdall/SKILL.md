---
name: heimdall
description: Spectator over the workroom — files and optional heartbeats, never a second tracker. Use for dashboard, status board, who's working, or kit health.
---

# Heimdall — the spectator

Projects situational awareness from files that already exist. Does not hold
stones, branches, or authority. UI and chat use the **same contract**.

## Sources

| Panel | File |
|-------|------|
| Mission / next task | `WORKROOM/HANDOVER.md` |
| Lanes | `WORKROOM/TRACKER.md` |
| Branches | `WORKROOM/LEDGER.md` |
| Services | `bin/svc status` if present |
| Reports | `WORKROOM/reports/` mtime |
| Live | `WORKROOM/live/*.json` or **unknown** |

TRACKER wins if the glance disagrees. Missing heartbeat = idle / unknown —
never “working.” `last_beat` older than 15 minutes → unknown.

## Kit health

STALE when handover is older than one working day **and** NOW is non-empty
(or handover still says NEVER while NOW has items).

## Text glance (chat)

1. Mission · 2. NOW / AWAITING · 3. Live (or “no heartbeats”) ·
4. Services if any · 5. Next first task · 6. Kit health only if STALE.

## Board

`bin/heimdall serve` / `bin/cockpit open` → `http://127.0.0.1:3847/`
(React cockpit when present). Do not invent agents to fill the Live panel.
A check-in is `POST /api/live/beat` or a file in `live/<id>.json`.
Older than 90s → unknown.

Cockpit face: **Watching** = open browser sockets (you), not workers.
Mode switch writes `MODE.md`. HAPPY panel calls `bin/svc` for registered
names only. Empty registry is honest greenfield, not fake services.
