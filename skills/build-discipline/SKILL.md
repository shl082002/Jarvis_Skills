---
name: build-discipline
description: The git and shipping doctrine — one slice = one branch, stacked; isolated worktrees; the push ceiling; deploy ≠ enable; verification per slice. Use when starting any build, creating branches, or preparing anything that ships.
---

# Build Discipline — how code leaves the workshop

## The unit of work: the slice

**One chunk = one branch = one shippable, testable slice.** A slice is the
smallest change that can be verified and reverted on its own. Branch names:
`BRANCH_PREFIX<slice-name>` (see charter House Configuration).

- Slices **stack**: each branches off the previous slice's tip, and the recorded
  stack order (ledger!) is the merge plan.
- Commits are atomic, message = what + why. History stays revertible per slice —
  no "WIP", no tangled multi-concern commits.
- Every slice carries its own verification before commit, and — if it ships —
  its post-deploy checklist.

## The worktree law

**Never build in a working tree a dev server is serving.** Checkouts rewrite
files under a running process; hot-reload storms and aborted live sessions
follow. All builds — the assistant's included — happen in an isolated
`git worktree add <scratch>/<mission>-wt -b <branch> <base>`. Docking (switching
the live tree to the finished branch) is a deliberate, announced act at the end,
never a side effect.

Worktree hygiene: symlinking dependency dirs (node_modules) in is safe;
**never symlink a Python venv into a worktree** (a relative `ln -sfn` has
destroyed a main repo's venv before) — use the main venv by absolute path or a
throwaway venv; copy `.env`, don't symlink it.

## The push ceiling

- The principal pushes; the assistant pushes **only on explicit, fresh
  instruction** — and even then the ceiling is a *feature branch to remote*.
- **Never** push to a mainline (main/dev/master) directly. Never force-push.
  Where the harness supports it, encode these as hard deny rules (charter
  law 17), so the ceiling holds mechanically, not just morally.
- A message that *sounded like* push authorization yesterday authorizes nothing
  today. Ask each time.

## Deploy ≠ enable

Everything new ships **dark behind a flag**, default off. Activation is a
separate, checklisted act (the checklist lives in the chronicle). This decouples
"code is on the branch" from "users can see it", which is what makes shipping
boring — the goal.

## Verification per slice (the builder's gate)

Before each slice's commit, using the project's own gates:
- typecheck + production build (frontend) / compile + import + targeted smoke
  (backend);
- linter on touched files compared against pre-change state — **introduce
  nothing**, even where the file was already dirty;
- facts checked at the source: payload fields, identifiers, and copy come from
  what the code demonstrably provides — never from the design doc's optimism.
  Design-vs-reality conflicts halt the slice (the STOP order), they don't get
  papered over.

## House laws for product code

- Code owns facts; the LLM owns phrasing. Never let generated text carry a fact
  the code didn't establish.
- Honest copy only — no fabricated urgency, no unverifiable claims to users,
  third parties referred to generically unless the principal rules otherwise.
- Best-effort side-channels (analytics, notifications, enrichment) never block
  a user flow.
- Match the surrounding code's style and the project's own design tokens;
  minimal diffs; touch only what the slice needs.
