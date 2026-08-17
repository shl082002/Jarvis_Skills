---
name: morning-open
description: Portable 6am house OPEN — lights, recollect, discuss, Telegram. Face switch is the grant. No Deploy.
---

# Morning OPEN

Principal grant (HAPPY never invents cron). Arm from Mission Control **Morning** Off/On.

At the chosen hour on **this Mac’s local clock**: `bin/morning-open` runs.

1. `svc lights on`
2. Write `.jarvis/inbox/morning.md` (handover, tracker, ledger, git)
3. Mode **discuss**
4. Telegram ping if workroom `.env` has the bot (same secrets as the sidecar)

Does **not** Deploy, BUILD, open Cursor/Claude, or start a gauntlet.

Install (`adapters/install.sh`) copies `bin/morning-open` into `.jarvis/bin` and `.jarvis/kit/bin`. Re-arm the face after install so launchd points at the new binary.

Linux: the face will refuse the timer; run `morning-open` from your own user cron if you must.
