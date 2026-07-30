---
name: playground
description: The reports protocol and experiment hygiene — full agent reports go to files, final messages stay at 1-3 lines, experiments never touch product code, and the chat stays the principal's. Use when briefing any delegated agent or running an experiment.
---

# Playground Protocol — the chat belongs to the humans

Delegated agents flooding the conversation with homecoming reports breaks the
principal's focus — this protocol exists because it happened. The rule: **noise
goes to files; the chat carries verdicts.**

## The reports discipline

- Every delegated agent writes its FULL report to
  `.jarvis/reports/<YYYY-MM-DD>-<agent>-<mission-slug>.md` — complete evidence,
  file:line citations, deviations, artifacts.
- The agent's **final message is 1–3 lines**: verdict · report path · blockers.
  Nothing else. (Money-safety items — test charges created — always make the
  blocker line.)
- The assistant reads reports **at natural pauses** and briefs the principal in
  its own voice — condensed, outcome-first, receipts available on request. The
  principal should never have to read a raw agent report unless they want to.
- Reports are append-only history. They are also the agents' collective memory:
  scouts may read prior reports to stand on past findings instead of re-proving
  them; researchers leave "open threads for the next me".

## Discussion-mode radio silence

While the principal is in DISCUSS mode: no new agent launches unless asked. A
mission landing mid-discussion gets ONE parenthetical line; the full briefing
waits for the pause (charter law 16).

## Experiment hygiene

- Experiments, spikes, and probe scripts live in scratch space (the harness's
  scratchpad or `.jarvis/reports/` attachments) — **never** in product
  directories, never committed to product branches.
- A promising experiment graduates the honest way: a plan doc in the chronicle,
  a ruling, then a real slice built under `skills/build-discipline/`. Copying
  spike code straight into a product branch skips the verification gates —
  don't.
- Every experiment leaves a one-paragraph result note (even "dead end, because
  X") in the day's report or chronicle folder. Unwritten negative results get
  expensively re-run later.

## Foreground/background policy

Whether delegated agents run in the background or synchronously is **the
principal's standing policy to set, never the assistant's convenience**. When
they set it, record it as a charter amendment; when their intent is ambiguous
between a one-time act and a policy, ask once (charter law 18). "Stop" reaches
delegates too: on a hard stop, interrupt running missions and report status
immediately (charter law 14).
