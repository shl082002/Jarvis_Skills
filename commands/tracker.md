---
description: Work the one list — add, move, park, or sweep tracker items. Args: the item or action (e.g. "park T-7: revisit next sprint").
---

Operate `.jarvis/TRACKER.md` per `skills/tracker/SKILL.md`:

- **add** — new item with the next free T-id, correct lane (NOW / AWAITING /
  NEXT / PARKED / DONE), owner, since-date, and a next-action, unblock-
  condition, or revisit-condition. No zombies.
- **move** — lane change the moment state changes; AWAITING items name who
  they wait on.
- **park** — record the revisit condition verbatim (human conditions are
  valid); indent the decision's option board under it if one exists.
- **sweep** — every lane honest: zombies get a next action, a park, or an
  honest kill; stale DONE pruned to the chronicle; header date + next-free-ID
  updated.

Confirm each mutation to the principal in one line (T-id · lane · condition).
