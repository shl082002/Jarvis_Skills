---
name: qa
description: Evidence-first walkthrough of a running product — tiers, workroom report, no auto-ship. Use when asked to qa, qa-only, test the site, or find bugs. Never auto-launch after a build (law 15).
---

# QA — walk it, write it, do not ship it

EDITH hat (`agents/edith.md`) unless the principal named another. Machine QA
runs **only on explicit ask**. Default is **report-only**. Fix only if they
said “qa and fix.” Never auto-commit. Never `/ship`. Never write `~/.gstack`.

## Tiers

| Tier | Scope | When |
|------|--------|------|
| **Quick** | Critical / high only | Smoke, “is it up” |
| **Standard** (default) | + medium | Feature ready for eyes |
| **Exhaustive** | + cosmetic / copy / empty states | Pre-demo, principal asked |

Details: `references/tiers.md`.

## Mode

| Words | Mode |
|-------|------|
| `qa-only` / “report only” / default | Report. No product edits. |
| “qa and fix” | Fix after the report exists. One bug, one commit, re-verify that bug. |

Law 15 still binds: this skill does not launch because a build finished.

## Procedure

1. Name the claim, URL/port, and tier. Confirm services are actually up
   (`bin/svc status` if a registry exists).
2. Drive the **real** UI or HTTP — see `skills/browse/` if a browser is needed.
   Snapshot → act → evidence. No polling as a substitute for events the product
   already emits.
3. Grade each finding: critical / high / medium / cosmetic. Quote the actual
   output (status, body, console). Screenshots go under
   `WORKROOM/reports/` or `WORKROOM/evidence/`.
4. Write the full report to
   `WORKROOM/reports/<YYYY-MM-DD>-edith-qa-<slug>.md`
   (template: `references/report.md`).
5. Chat wrap: 1–3 lines — verdict · report path · blockers. Money-safety
   leftovers always on the blocker line.

## Honesty

LIVE-VERIFIED requires browser or real HTTP evidence (`skills/verify-live/`).
Tests passing is TESTED, not done. Do not invent a health score. Do not
claim ship-ready.
