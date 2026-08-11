---
name: review
description: Diff review for bugs that pass CI — production-shaped checklist, no ship. Use when asked to review a branch, PR, or uncommitted change.
---

# Review — bugs that pass CI

Assistant or EDITH hat. Read the diff. Hunt what green gates will not catch.
No `/ship`. No merge. No push.

Checklist: `references/ci-blind.md`.

## Procedure

1. Identify the range (`git diff`, `base...HEAD`, or named files). Read the
   surrounding code — not only the hunks.
2. Walk `references/ci-blind.md`. Each hit is a finding with file:line and
   why CI is silent.
3. Grade: defect (will bite) / risk (needs a ruling) / nit (style only if
   it hides a real miss).
4. Write `WORKROOM/reports/<YYYY-MM-DD>-review-<slug>.md`.
5. Chat: 1–3 lines — ship-blocker count · report path · worst finding.

## Honesty

A clean CI is COMPILED/TESTED. Review does not mint LIVE-VERIFIED.
Do not rubber-stamp. Do not invent issues to look busy — empty “no
ci-blind hits” is a valid report if you actually walked the list.
