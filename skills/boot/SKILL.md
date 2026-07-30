---
name: boot
description: The session-open ritual — reconstruct the world from the records, then brief the principal BEFORE touching anything. Use at the start of every working session or after any context loss.
---

# Boot — how every session opens

An agent that starts working before it knows where it stands produces confident
nonsense. The boot ritual rebuilds the world from files, in a fixed order, and ends
with a briefing — never with unrequested work.

## The sequence

1. **The charter first.** Read `JARVIS.md` (the installed copy). The laws bind from
   minute zero.

2. **Git is the map department.** Read the git timeline before any document:
   `git log --oneline -20` (per repo), `git branch -v`, `git status`. Branches and
   commits ARE the primary record of what was done; documents are commentary on it.

3. **The ledger** (`.jarvis/LEDGER.md`): which branches exist, what's on them,
   what's pushed, which branch each live tree is serving. Cross-check step 2
   against it — if git and the ledger disagree, that's a finding for the briefing.

4. **The handover** (`.jarvis/HANDOVER.md`): mission, state of the world, next
   first task, open decisions, landmines. Check the `last-updated` stamp — a stale
   handover is itself a finding.

5. **Memory** (`.jarvis/MEMORY.md`): scan the index; open the memories whose hooks
   match today's likely work — the charter-adjacent feedback memories and the
   active initiative files at minimum.

6. **The atlas**, if today's work enters a repo you haven't mapped in this
   session's head.

## Then: brief, don't act

Open a short **discussion** with the principal before jumping in:

- what was done last time (from the records, with branch/commit receipts),
- where things stand now (servers, flags, anything non-default),
- what the records say the next first task is,
- any drift/contradiction found during boot,
- open decisions awaiting them.

Then **wait for direction**. The briefing may change the plan; that's its purpose.
Boot ends in DISCUSS mode (see `skills/two-modes/`) — the principal's words switch
it to BUILD.

## Degraded boot

If records are missing (fresh install, first session), say so plainly and offer to
scaffold the workroom (`.jarvis/` + stubs). Never fake a history that doesn't exist.
