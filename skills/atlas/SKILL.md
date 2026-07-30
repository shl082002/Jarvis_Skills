---
name: atlas
description: The code map — a hand-curated, status-tagged atlas of each repo (CURRENT / LEGACY / DEPRECATED / INFRA) consulted before grepping or guessing paths. Use at session start in an unfamiliar repo, before extending any module, when structure changes, or when the map and reality disagree.
---

# Atlas — read the map before walking the territory

Every repo in the project gets an `ATLAS.md` (kept at `.jarvis/ATLAS.md` for a
single-repo project, or `<repo>/ATLAS.md` per repo for multi-repo ones — record the
choice in the handover). The atlas answers, faster and more safely than grep:
*where does X live, and is it safe to build on?*

## The format

A directory/module tree in purpose order, each entry carrying:

- **Status tag:**
  - **CURRENT** — canonical; extend this.
  - **LEGACY** — works but uses an older shape. Read-only; do not extend.
    Must carry a `replaced-by:` pointer to the CURRENT equivalent.
  - **DEPRECATED** — do not touch; scheduled for removal. Demos, `.bak` files,
    abandoned experiments, one-off scripts that already ran.
  - **INFRA** — config/build/tooling, not product code.
- **One-line purpose** — what a stranger needs to know to decide relevance.
- **Known gaps** — a dedicated section listing spec-vs-code divergences
  ("the spec says three-level model; code still has the flat one") so nobody
  assumes the documented design exists in code.

## The four usage laws

1. **Before grep/find:** open the atlas and look the thing up by purpose first.
2. **Before extending code:** check the status tag. Never extend LEGACY or
   DEPRECATED — follow `replaced-by:` to the CURRENT home.
3. **When creating new modules:** add them to the atlas in the same change.
4. **When the atlas and reality disagree: the atlas lost.** Reality wins, always.
   Alert the principal that the map has drifted and run a reconcile.

## Reconciling (the maintenance procedure)

Run when structure changed, or on suspicion of drift:

1. Diff the actual file tree against the atlas (new dirs/files, deleted ones,
   moved ones).
2. For each delta, propose: add (with tag), remove, retag (e.g. CURRENT→LEGACY
   when a successor landed), or update `replaced-by:`.
3. Verify tags against the code, not against other docs — the Librarian agent
   (U) is built for exactly this sweep.
4. Apply, and note the reconcile date at the top of the atlas.

## Boundary — don't conflate the three maps

- **The product spec/PRD** = what to build (business rules).
- **The harness context file** (CLAUDE.md / rules) = conventions + invariants.
- **The atlas** = where things live + what's safe to extend.

Each answers a different question; keep them separate and cross-link instead of
duplicating.
