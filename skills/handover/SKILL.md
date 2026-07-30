---
name: handover
description: The baton — a single live file that lets ANY agent in ANY harness resume the work with zero chat context. Refresh at day-close, before risky operations, and whenever the "next first task" changes.
---

# Handover — the baton that makes agents interchangeable

`.jarvis/HANDOVER.md` is the one file a brand-new agent — different session,
different tool, different vendor — reads to become useful in five minutes. It is
the keystone of the kit's portability promise: the partnership's state lives in
this file, not in any product's session storage.

## The contract

The handover is **always current or honestly stale**: it carries a `last-updated`
stamp at the top, and a reader must be able to trust that everything below the
stamp was true at that moment. An out-of-date handover with an honest old stamp is
acceptable; a fresh stamp over stale content is a lie.

## The sections (all six, every time)

```markdown
# HANDOVER — last updated <date time> by <assistant> (<harness>)

## 1. Mission
What we are building right now, in two sentences, and which chronicle
plan doc governs it.

## 2. State of the world
Per repo: current branch of each live working tree + tip hash; which
servers/processes should be running and how to start them (commands, ports,
env flags that are toggled ON locally); anything currently non-default
(migrated DBs, temp env overrides) — flagged loudly.

## 3. Next first task
THE single next action, concrete enough to start cold ("implement slice 3
of <plan doc>, branch off <branch>"). If the next step is the principal's
(a ruling, a manual test, credentials), say so — the assistant's next move
is then to wait, not to invent work.

## 4. Open decisions
Questions awaiting the principal, each with the options and the
recommendation already prepared.

## 5. Landmines
Anything a naive agent would trip on: the dev server serving a live tree,
a schema guard that fails on branch X, a flaky external dependency, a test
account with money-safety constraints.

## 6. Where everything is
One-line pointers: MEMORY.md, LEDGER.md, atlas file(s), today's chronicle
folder, latest reports.
```

## When to refresh

- **Every day-close** (part of the ritual, `skills/day-close/`).
- **Before any risky or long operation** — if the session dies mid-flight, the
  handover is the crash recorder.
- **The moment the "next first task" changes** — that field going stale is how
  batons get dropped.

## Cross-harness law

Write in plain markdown, absolute concepts, no harness-specific jargon: no "see
my earlier tool call", no session IDs, no "as discussed above". Branch names,
hashes, paths, commands. The reader has your files and nothing else.
