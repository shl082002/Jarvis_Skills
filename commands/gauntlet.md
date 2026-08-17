---
description: Open, run, or close a gauntlet — ONLY if the principal declared one. Never self-start.
---

Apply `skills/gauntlet/SKILL.md`. Determine which of the four you are being asked for
and do only that one.

## OPEN

0. **Declaration gate.** If this message is not an explicit declare/open from the
   principal, **do not open**. One-line recommend at most, then wait. Independent
   tickets in one chat are not a gauntlet.
1. **Check the work actually splits.** Independent initiatives — disjoint territory, no
   shared dependency chain. Steps of one thing are a pipeline, not a gauntlet: say so and
   stop.
1b. **Do NOT pre-assign fronts.** A front is raised only when the principal asks for
   one — never seeded with work you chose, never self-selected by a session, never
   auto-claimed by SessionStart. Opening a gauntlet means arming the machinery and leaving
   the board empty. When he does name
   one, it is a single command from any session, new or already running:
   `.jarvis/bin/gauntlet enlist <name> "<character>" <none|burst|heavy> "<territory>"`
   — which raises the front, seats that session, and writes its cold-boot brief. Name it
   *now, from the work*; there is no standing cast. Past 3 fronts, say what the extra
   coordination will cost. **Never name a front after the principal.**
2. **Cut baselines** — record the dev-line tip per repo, and note that they will move.
3. **Write the board:** front list, baseline table, the three coordination lanes
   (cross-front findings · shared-surface register · NEEDS-PRINCIPAL), stone table, and
   **a declared Collect time**.
4. **Write one cold-boot brief per front** — who it is, its task, its territory, and the
   reminder that it is a commander with a fleet, not a soloist.
5. Report to the principal: fronts, territories, Collect time, and what each front is
   blocked on before it can start.

## RUN (as a front)

1. Read the board, then your own front file. **Never guess which front you are.** The
   hooks tell you: if you are seated they name your front, and if you are not they say
   so and print the enlist line. Unseated is a valid state — wait for his ask.
2. Cut your worktree per repo with an **absolute** path; one branch name across all repos.
   Symlink `.env` / `node_modules`; never bare `git stash pop`.
3. **Prove your gates run and can fail** before your first claim (§7). Capture each
   tool's own exit code.
4. **Use your fleet** — DUM-E for recon, FRIDAY for the build, EDITH to refute. Name the
   actor in every log line. Never be the only verifier of your own work.
5. Take a stone only when you need it, with an intent and an ETA; release on done.
6. Heartbeat every log append. Post a CHECKPOINT (~90 min): DONE / NEXT / BLOCKED /
   NEEDS-HIM.
7. Findings outside your territory: **report to the board's cross-front lane, never
   touch.** Declare any shared surface you had to edit.
8. Write only your own file. Never the tracker, ledger, or memory — those are 🟡 MIND,
   and they belong to the Collector.

## STATUS

Render the board: per front — phase (fixed enum), since, stones held with lease
remaining, last beat with a staleness flag, ETA, blocked-on. Then the NEEDS-PRINCIPAL
queue, oldest first. Then drift checks: baselines vs current dev tips, main trees off
baseline, and any front whose declared phase contradicts its git state.

## COLLECT

Integration branch per repo → land in a declared order → **rebase, not merge** → re-run
gates after EACH landing → expect a rebase round → one push per repo on the principal's
**fresh** word → the Collector writes tracker + ledger + memory ONCE.

Close by appending to `skills/gauntlet/EXPERIENCE.md`: what the run produced, what it
cost, and any new law with the incident that paid for it.
