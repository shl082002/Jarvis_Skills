---
name: tracker
description: The one list — a five-lane commitment tracker (NOW / AWAITING / NEXT / PARKED / DONE) so what's open, what needs focus, and what's deliberately deferred never gets messy. Use when work is promised, blocked, parked, or finished, and at every boot and day-close.
---

# Tracker — the one list

The records each own a domain: the ledger owns branches, memory owns facts, the
chronicle owns decisions, the handover owns the baton. Nothing owns
**commitments and their state** — so open items scatter across chat, memory
footnotes, and heads, and "what's actually open?" becomes archaeology. The
tracker is the single answer: `.jarvis/TRACKER.md`, one file, five lanes.

## The five lanes

| Lane | Meaning | Every item must carry |
|------|---------|----------------------|
| **NOW** | Being actively worked this session/day | the next concrete action |
| **AWAITING** | Blocked on the principal or an external party | WHO it waits on + what unblocks it |
| **NEXT** | Open and queued — will be worked without further discussion | the next concrete action |
| **PARKED** | Deliberately deferred — a decision, not neglect | a **revisit condition** |
| **DONE** | Recently finished | the completion date |

**AWAITING is the load-bearing lane.** Most "messy" trackers die because
blocked-on-a-human items masquerade as open tasks. If it's waiting on the
principal's ruling, creds, or manual pass — it lives in AWAITING with their
name on it, and the assistant stops feeling guilty about it.

**Parking is a first-class outcome.** A parked item is a completed decision
("not now"), not a failure. Revisit conditions may be event-based ("when
deploys become routine"), date-based, or entirely human ("some weekend
evening, drink in hand") — the tracker's job is to reproduce the item
faithfully when the condition arrives, not to nag.

## Item anatomy

One line per item, details indented under it only when genuinely needed:

```markdown
- **T-7** · Short imperative title · owner: principal|assistant|<agent> ·
  since <date> · next: <concrete action> | revisit: <condition> ·
  links: [[memory-slug]], chronicle/<path>
```

- **IDs are monotonic and never reused** (`T-1`, `T-2`, …), so chat can say
  "park T-7" unambiguously. The next free ID is whatever the header says.
- Newest items on top within each lane.
- A PARKED decision item may carry its option board indented beneath it —
  the tracker must reproduce the decision as it stood, so the revisit
  session doesn't re-derive it.

## The no-zombie rule

An item with no next-action (NOW/NEXT), no unblock-condition (AWAITING), and
no revisit-condition (PARKED) is a zombie — it will rot. At every sweep,
every zombie gets one of: a next action, a park with condition, or an honest
kill (moved to DONE with "dropped: <why>"). Killing stale intentions is
maintenance, not defeat.

## Rhythm (wired into the rituals)

- **Boot:** read the tracker after the handover. NOW + AWAITING is the day's
  briefing skeleton; surface any PARKED item whose revisit condition looks met.
- **During work:** lane moves happen the moment state changes ("his ruling
  landed" → AWAITING→NOW), not retroactively.
- **Day-close:** sweep — every lane honest, zombies resolved, DONE items
  older than a few days pruned into the session-close chronicle doc, header
  date + next-free-ID updated.

## Boundaries

- **Tracker vs handover:** the handover's "next first task" and "open
  decisions" sections POINT INTO the tracker (by T-id), never duplicate it.
- **Tracker vs memory:** memory holds the knowledge an item produced; the
  tracker holds the item's state. When an item completes, its learnings go
  to memory, its corpse to DONE.
- **Tracker vs chronicle:** a PARKED decision that finally gets ruled
  graduates to a chronicle decision record; the tracker item links to it and
  moves to DONE.

## File header template

```markdown
# TRACKER — the one list · updated <date> · next free ID: T-<n>
```
