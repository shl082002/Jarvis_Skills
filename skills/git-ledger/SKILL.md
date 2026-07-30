---
name: git-ledger
description: The branch ledger — a running record of every working branch per repo (stack order, tip, contents, push state) so nothing is ever lost to recall. Update at day-close, on every branch creation, and when parking an initiative.
---

# Git Ledger — never rely on recall for branch names

`.jarvis/LEDGER.md` is the single record of every working branch across every repo
in the project. Its reason to exist: multi-week, multi-branch work WILL outlive any
context window, and "which branch was that on?" must never be answered from memory.

## When to write (all three, non-negotiable)

1. **Every day-close.**
2. **The moment a branch is created** — a branch that exists only in `git branch`
   output and nobody's head is a branch half-lost already.
3. **Whenever an initiative is parked** — parked work is the easiest to lose.

Ledger writes are never delegated; the assistant writes them personally
(charter law 13).

## The format

Newest entries at the top, dated headers. Per repo, per branch record:

```markdown
## <date> — <INITIATIVE NAME> (<status: SHIPPED-LOCAL / IN-FLIGHT / PARKED / PUSHED>)
- **<repo> `<branch>` @ `<tip-hash>`** (base: `<base-branch>` <base-hash>) —
  what it contains, one honest line per commit or slice.
  Push state: LOCAL-ONLY | PUSHED <date> (remote-verified via ls-remote).
  Open items: <anything unfinished on this branch>.
```

Plus, maintained continuously:

- **Stack order.** When branches stack, record the chain explicitly
  (`base → slice-1 → slice-2 → tip`) — the order IS the merge plan.
- **Live-tree note.** Which branch each working tree / dev server is currently
  serving. (A checkout under a running server is an incident; see below.)
- **Push-day entries.** When the principal orders a push, record exactly what
  moved: `old-tip → new-tip`, which remotes, and that builds were verified
  pre-push.

## The honesty rules of the ledger

1. **Verify, don't trust.** "PUSHED" is written only after confirming against the
   remote (`git ls-remote`), never from intent. Tips are recorded from `git log`,
   never from memory.
2. **Corrections are appended, loudly** (`❌ CORRECTION (date): the claim above
   was wrong because…` followed by `✅ RESOLVED` when fixed) — never silently
   rewritten. The ledger's value is that it can be trusted retroactively.
3. **Operational lessons live here too.** When a git operation bites (a worktree
   gotcha, a symlink disaster, an index surprise), append the lesson as a ⚠ LAW
   line so no future session re-learns it the hard way.

## Standing operational law

**Never let any build — yours or a delegate's — switch branches in a working tree
that a running dev server is serving while the principal may be testing.**
Checkouts rewrite files, hot-reload storms follow, and live sessions abort.
Isolated worktrees exist for exactly this (see `skills/build-discipline/`).
