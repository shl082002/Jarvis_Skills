---
description: Session-close ritual — commit, true up ledger/memory/chronicle/handover, leave cold-start-ready, ask about pushing.
---

Execute the day-close ritual defined in `skills/day-close/SKILL.md`:

1. Commit everything (or explicitly disposition uncommitted work).
2. True up `.jarvis/LEDGER.md` — verified against git, not memory.
3. Sweep memory: milestone updates for every initiative touched today.
4. Sweep `.jarvis/TRACKER.md`: lanes honest, zombies resolved, stale DONE
   pruned into the close doc.
5. Write the session-close doc in `.jarvis/chronicle/<today>/`.
6. Refresh `.jarvis/HANDOVER.md` (all six sections, fresh stamp).
7. Leave the world runnable; flag anything non-default.
8. If unpushed work exists: ASK about pushing (feature branches only — the
   ceiling). Never push without a fresh confirmation.

Close message: outcome first, verified-vs-built distinction explicit, pointers
to the close doc and handover, then the push question if applicable.
