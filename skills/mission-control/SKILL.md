---
name: mission-control
description: Living board + house lights — wake/sleep including the board, Deploy is a dispatch, TCP-only health. Use for lights on/off, Mission Control, cockpit, HAPPY turn-on/turn-off, or when tempted to Down the board from its own face.
---

# Mission Control — the living board and the lights

The workroom has a face (cockpit on loopback) and a butler (`bin/svc` + HAPPY).
They are not the same lever.

## Lights

Principal “turn on” / “turn off” / “lights on” / “lights off” means the
**whole registry**, including **Mission Control** (`cockpit`, typically :3847).

| Ask | Muscle |
|-----|--------|
| Lights on | `bin/svc lights on` (or `svc up all`) |
| Lights off | `bin/svc lights off` (or `svc down all`) |
| Board only | `svc up cockpit` / `svc down cockpit` |

HAPPY must not skip the board on a house sleep. Status before action
(`svc status`). Bind 127.0.0.1 only.

## Face vs butler

- The **face** mutates workroom state (mode, tasks, Deploy/Stop/Explain).
- The face **must not Down itself** — that suicides the page. Cockpit Down
  from the UI is refused on purpose.
- **HAPPY / svc** stops the board. That is the legal off switch.

## Gauntlet switch

The header **Gauntlet Off / On** is the principal's declare. It writes
`.jarvis/run/GAUNTLET_ACTIVE` — same file as `gauntlet open` / `close`.
The assistant never flips it. Off is the default.

## Health (T-10 class)

Never HTTP-health the board from the same worker that serves it (deadlock).
Registry: **TCP-only** for cockpit. No `health:` URL on that entry.

## Deploy is a dispatch

When the principal or the board **Deploys** a named fleet agent, the assistant
**launches that agent** with a mission brief, then commands (spot-check,
records, brief the principal). The assistant does not wear the hat and type
the slice. See `agents/friday.md` / `skills/council/` and charter amendment
on Deploy.

Discuss/plan mode still **blocks FRIDAY** until build.

## After lights on

Confirm with `svc status` (observed, not assumed). Offer the loopback URL.
Do not claim the UI is current without a live check.
