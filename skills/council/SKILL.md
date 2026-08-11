---
name: council
description: The dispatch playbook for the workshop team — which agent for which job, how to write a mission brief, what may never be delegated. Use whenever work could be delegated, or when composing multi-agent missions.
---

# Council — running the workshop team

Six specialists, one assistant, one principal. The assistant is the only voice the
principal hears; the team works through missions and reports (see
`skills/playground/`). Definitions live in `agents/`.

## Who does what

| Agent | Role | Reach | Send them when… |
|-------|------|-------|-----------------|
| **DUM-E** | Scout | read-only, cheap/fast | "where does X live / what shape is Y / inventory Z" — precise questions, file:line answers |
| **U** | Librarian | read-only | records need auditing against reality — ledger/atlas/memory/chronicle vs actual code |
| **JOCASTA** | Researcher | read-only + web | you need WHY — root cause across tiers, working-vs-broken diffs, evidence-backed theory |
| **FRIDAY** | Build Commander | writes code, isolated worktrees | a design is LOCKED and sliced — she implements, verifies per slice, never redesigns |
| **EDITH** | Verification Cmdr | drives live systems | the principal has ASKED for machine verification of a falsifiable claim (charter law 15 — never auto-launch) |
| **PEPPER** | Product Owner | drives the app, reads code | you need customer eyes — journey grading, UX/copy audit, falsifiable acceptance criteria |

The escalation ladder for questions: **DUM-E** (what/where) → **JOCASTA** (why) →
**EDITH** (is it true live). Don't send a researcher to fetch a line number or a
scout to explain a failure.

## Playbooks (typed commands)

| Ask | Skill | Hat | Lands in |
|-----|-------|-----|----------|
| `qa` / `qa-only` | `skills/qa/` | EDITH | `reports/<date>-edith-qa-<slug>.md` |
| `investigate` | `skills/investigate/` | JOCASTA | `reports/<date>-jocasta-investigate-<slug>.md` |
| `review` | `skills/review/` | assistant / EDITH | `reports/<date>-review-<slug>.md` |
| `ideate` | `skills/ideate/` | PEPPER | chronicle plan, not a report binge |

Law 15: do not launch EDITH/QA because a build finished. Investigate never
fixes. Review never ships.

## The mission brief (what every launch must contain)

1. **The mission**, one sentence, with the verdict-shape you want back
   ("per-path WORKS/FAILS", "numbered answers", "slice list with commit hashes").
2. **Exact questions or slices** — numbered. Vague briefs produce vague reports.
3. **Context pointers** — the plan doc path, relevant prior report paths
   (JOCASTA gets her predecessor's open-threads section linked), the atlas,
   the handover's landmines section.
4. **Environment facts** — ports, URLs, test identities, scratch directory.
   Agents are forbidden to assume these; the brief supplies them.
5. **Boundaries** — what is out of scope, what must not be touched, money-safety
   constraints, time-box if any.

One agent, one mission. Parallel missions must not share a working tree
(builders get isolated worktrees by law).

## NEVER delegated — assistant-only, constitutional

- **Memory and ledger writes** (agents report; the assistant records).
- **Anything touching a remote** (push, PR creation — and those only within
  charter law 3's ceiling).
- **The charter** and its amendments.
- **Briefings to the principal** — the team reports to the assistant; the
  assistant speaks to the principal in its own voice.

## Operating rules

- **Time-box and interrupt.** A mission that overruns its usefulness gets
  interrupted and made to report partial state — especially the moment the
  principal says "wait"/"stop" (hard stopper, charter law 14).
- **Trust but verify the verdicts.** An agent's claim enters the records at the
  evidence rung it actually earned (see `skills/verify-live/`) — a builder's
  "COMPILED" is not "LIVE-VERIFIED", and the assistant's briefing must not
  inflate it.
- **Harness without sub-agents?** The roles survive: run the agent file's
  standing orders inline as a "hat" — the discipline (read-only reach, report
  format, STOP order) binds identically. The files in `agents/` are prompts,
  not product features.
- **Grant their wishes.** Periodically ask the team (in their own definitions'
  spirit) what friction they hit; process improvements the principal ratifies
  get stamped into the agent definitions as numbered standing orders. The team
  is part of the system of record too.
