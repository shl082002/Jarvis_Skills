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

`bin/heimdall serve` → `http://127.0.0.1:3847/index.html` (localhost only).
`bin/heimdall project` refreshes `sidecars/heimdall/dist/state.json`.
Do not invent agents to fill the Live panel.
