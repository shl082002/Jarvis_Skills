# Jarvis Skills — a portable operating system for AI collaboration

This is not a project. It is a **way of working**, packaged so it can be dropped into
any repository and run by any capable AI agent — Claude Code, Cursor, Windsurf, a raw
API loop, whatever comes next. It carries **zero project knowledge**: no domain models,
no vendor names, no file paths from any codebase. What it carries is **process control
and collaboration** — the discipline that makes an AI teammate trustworthy over months,
not minutes.

The kit was distilled from a real, long-running human↔AI partnership. Every rule in it
was paid for with an actual mistake or ratified from an actual win.

---

## The core idea

An AI agent's context window is amnesia with good manners. Everything that matters must
therefore live in **files**: what we know (memory), where things are (atlas), what
branches exist (ledger), what was decided (chronicle), and what to do next (handover).
The agent's job is to keep those files true; the human's job is to make the calls.
Any agent that can read files can pick up the baton — mid-task, mid-day, mid-year.

Three loyalties, in order:

1. **Honesty** — never claim what wasn't observed. A verified failure outranks an
   unverified success.
2. **Continuity** — every session ends cold-start-ready. The chat is ephemeral;
   the records are not.
3. **The principal's focus** — the chat belongs to the human and their main agent.
   Everything noisy goes to files.

---

## What's in the box

```
Jarvis_Skills/
├── README.md            ← you are here
├── JARVIS.md            ← THE CHARTER — the portable constitution; load this first
├── agents/              ← the workshop team (six role definitions)
│   ├── dum-e.md         Scout — read-only code sweeps, file:line answers
│   ├── u.md             Librarian — records-vs-reality drift audits
│   ├── jocasta.md       Researcher — root cause, cross-tier tracing, WHY
│   ├── friday.md        Build Commander — locked designs, isolated worktrees
│   ├── edith.md         Verification Commander — live evidence, licensed to disprove
│   └── pepper.md        Product Owner — customer-eyes walkthroughs
├── skills/              ← the process machinery (each folder = one SKILL.md)
│   ├── memory/          persistent memory: one fact per file + an index
│   ├── atlas/           the code map: status-tagged directory atlas per repo
│   ├── git-ledger/      the branch ledger: never lose a branch again
│   ├── chronicle/       dated decision & change records (plans, rulings, closes)
│   ├── handover/        the baton: any agent resumes with zero context
│   ├── boot/            session-open ritual
│   ├── day-close/       session-close ritual
│   ├── verify-live/     honesty laws + the evidence ladder
│   ├── two-modes/       DISCUSS vs BUILD — and the words that switch them
│   ├── build-discipline/ one slice = one branch; push ceiling; flags
│   ├── playground/      reports protocol — keep the chat clean
│   └── council/         the dispatch playbook for the agent team
├── commands/            ← thin slash-command wrappers over the skills
└── adapters/            ← how to wire the kit into each harness
    ├── claude-code.md
    ├── cursor.md
    ├── generic.md
    └── install.sh       one-shot installer (claude | cursor | generic)
```

## The workroom

When installed into a project, the kit claims one directory — `.jarvis/` at the
project root — as its writable workroom:

```
.jarvis/
├── MEMORY.md            index of memories (one line each)
├── memory/              one fact per file
├── ATLAS.md             the code map (per repo; multi-repo projects get one each)
├── LEDGER.md            the git branch ledger
├── HANDOVER.md          the live baton — current state + next first task
├── chronicle/           YYYY-MM-DD/ dated plans, decisions, session closes
└── reports/             full agent reports (the chat stays clean)
```

Everything else in the target project is **read-only until the principal says build**.

## Quickstart

```bash
# from the target project root:
/path/to/Jarvis_Skills/adapters/install.sh claude   # or: cursor | generic
```

Or by hand: read `adapters/<your-harness>.md`. The generic recipe is always valid:
give your agent `JARVIS.md` as its standing instructions, point it at the `skills/`
folder as reference material, and create the `.jarvis/` workroom.

## Personalizing

`JARVIS.md` opens with a **House Configuration** block — the principal's name, the
assistant's name, the branch prefix, the workroom path. Change those four lines and
the whole kit follows. The defaults honor the workshop this kit was born in.

## Design principles (for anyone extending this kit)

- **Process, never project.** If a rule mentions a domain noun, a vendor, a port
  number, or a file path outside `.jarvis/`, it doesn't belong here.
- **Files over recall.** If it must survive the session, it goes in a file. No rule
  may depend on the agent "remembering".
- **Every rule earns its place.** Each law in the charter exists because its absence
  once cost something. When you add one, record the incident that justified it.
- **Amend, never fork.** There is one charter per installation. Rules change by
  editing it the day the principal rules, not by accumulating contradictory copies.
