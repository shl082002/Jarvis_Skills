---
name: day-close
description: The session-close ritual — commit everything, true up every record, leave the world cold-start-ready, and ask (never assume) about pushing. Use at end of day, end of session, or before a long pause.
---

# Day-close — how every session ends

The measure of a good close: a different agent, in a different tool, opening the
project tomorrow, becomes productive from the files alone. Close is a checklist,
not a vibe.

## The checklist (in order)

1. **Everything committed.** No dirty working trees left behind. Uncommitted
   experiments either become commits on an honestly-named branch, or are moved to
   scratch, or are deleted — stated which, in the close summary.

2. **The ledger trued up** (`skills/git-ledger/`): today's branches, tips,
   stack order, push states — verified against `git log`/`ls-remote`, not memory.

3. **Memory swept** (`skills/memory/`): every initiative touched today gets its
   milestone update — status, branches, rulings, open bugs with suspects, next
   first task. Corrections for anything today disproved.

4. **Tracker swept** (`skills/tracker/`): every lane honest — items moved as
   state actually changed, zombies given a next action / a park / an honest
   kill, stale DONE pruned into the close doc.

5. **Chronicle written** (`skills/chronicle/`): the session-close summary — what
   was done, what was *verified* vs merely *built* (the distinction is sacred),
   decisions made, deviations from plan.

6. **Handover refreshed** (`skills/handover/`): all six sections current,
   `last-updated` stamped. This is the file tomorrow's agent boots from.

7. **The world left runnable.** Live trees on the intended branches; servers in
   the state the principal expects (running for their manual test, or down —
   their call); temporary env overrides either reverted or flagged in the
   handover's landmines section.

8. **The push question — asked, never assumed.** If there is unpushed work worth
   backing up, ASK. Only the principal confirms a push, freshly, each time — a
   prior instruction that *sounded like* standing authorization is not one
   (charter laws 3 and 11). Absolute ceiling: feature branches only.

## The close message to the principal

Lead with the outcome: what shipped / what's verified / what's blocked. Then the
one-line pointers (close doc path, handover stamp). Then the push question if
applicable. Keep it short — the details are in the files, which is the whole point.

## Emergency close

If the session is dying (context exhaustion, forced interruption), do a triage
close: handover first (it subsumes the rest at minimum quality), ledger second,
memory third. A stale chronicle is recoverable; a lost baton is not.
