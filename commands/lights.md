---
description: House lights — wake or sleep the whole registry, including Mission Control.
---

Apply `skills/mission-control/SKILL.md`.

1. `svc status` first (observed state).
2. On / off = `bin/svc lights on` or `bin/svc lights off` — **includes cockpit**.
3. Do not Down the board from its own face. Do not HTTP-health cockpit.
4. After the command, `svc status` again and report what is actually UP/DOWN.
5. Bind remains 127.0.0.1 only.
