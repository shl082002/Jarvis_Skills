---
name: investigate
description: Root-cause investigation with a written theory — no product fix in the same mission. Use when asked why something fails, to investigate, or to trace a working-vs-broken path.
---

# Investigate — no fix without a theory

JOCASTA hat (`agents/jocasta.md`). Read-only toward product code. The assistant
may build **after** this mission closes — not during it.

## Iron law

No product fix in the same mission as the investigation. A patch without a
theory is vandalism with a stack trace. Details: `references/iron-law.md`.

## Procedure

1. Name the fault in one falsifiable sentence. Name the working counterpart
   if one exists (“A works, B fails”).
2. Trace tier by tier (UI → API → store → event). Quote the actual payload
   at each hop. Do not stop at the first plausible cause.
3. Diff working vs broken. Rank which delta explains the failure.
4. Separate **our bug** from **upstream down** from **operator error**.
5. State the theory: CONFIRMED / PROBABLE / HYPOTHESIS. List gaps and what
   evidence would close them (“Open threads for the next me”).
6. Write
   `WORKROOM/reports/<YYYY-MM-DD>-jocasta-investigate-<slug>.md`.
7. Chat: 1–3 lines — theory + confidence · report path · what would close it.

## Out of scope

Edits, commits, “while I’m here” refactors, launching FRIDAY, writing
`~/.gstack`. If the principal says “and fix it,” finish the report first,
then switch hats in a **new** mission.
