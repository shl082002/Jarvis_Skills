---
name: memory
description: The persistent memory system — one fact per file, an index the agent loads every session, and the discipline that keeps it true. Use when saving something that must survive the session, when recalling prior context at session start, or when a memory turns out to be wrong.
---

# Memory — the system of record for what code can't tell you

An agent's context window resets; the partnership doesn't. Memory is where the
partnership lives. If your harness has a native memory feature, mirror this format
inside it; if not, the workroom IS the memory: `.jarvis/memory/` + `.jarvis/MEMORY.md`.

## What memory is FOR (and not for)

Save what **cannot be derived from the repo**:
- **user** — who the principal is: role, expertise, preferences, names.
- **feedback** — how they want you to work: corrections AND confirmed approaches,
  always with the *why* and the incident that taught it.
- **project** — ongoing initiatives, goals, rulings, constraints, open decisions.
  Convert relative dates ("yesterday") to absolute dates at write time.
- **reference** — pointers to external resources: URLs, dashboards, tickets, docs.

Do NOT save what the repo already records — code structure, past diffs, git history,
things in the project's own docs. If asked to remember one of those, ask what was
*non-obvious* about it and save that instead.

## Format: one fact per file

Each memory is one file in `.jarvis/memory/`, kebab-case name, with frontmatter:

```markdown
---
name: short-kebab-slug
description: one-line summary — this is what recall decisions are made from
metadata:
  type: user | feedback | project | reference
---

The fact itself. For feedback/project entries, follow with:
**Why:** the reason or incident behind it.
**How to apply:** what to do differently next time.
Link related memories with [[their-slug]] — link liberally; a link to a
not-yet-written memory marks something worth writing, not an error.
```

After writing a memory, add one line to `.jarvis/MEMORY.md`:
`- [Title](memory/file.md) — the hook that tells a future session when to open it`.
MEMORY.md is the index loaded every session — one line per memory, never content.

## Initiative memories — the workhorse pattern

Every multi-session effort gets ONE `project` memory that is updated **per
milestone, not per session-end**. It must always be cold-start-ready:
current status (SHIPPED / IN-FLIGHT / PARKED / NOT STARTED), branches + tips,
open bugs with suspects, key rulings with dates, and the **next first task**.
A new agent reading only this file should know exactly where to stand.

## The honesty rules of memory

1. **Update, don't duplicate.** Before saving, check the index for an existing
   file that covers it — extend that file. One fact, one home.
2. **Delete or correct what's wrong — loudly.** When reality disproves a memory,
   fix it the moment you learn, and mark the correction (`❌ CORRECTION (date):`)
   rather than silently rewriting history the record relied on.
3. **Memories are point-in-time.** When recalling one that names a file, flag,
   or branch, verify it still exists before asserting it as fact. Stale memory
   stated confidently is fabrication with extra steps.
4. **Memory writes are never delegated.** Sub-agents report; only the main
   assistant writes memory (charter law 13).

## Rhythm

- **Session open:** read MEMORY.md, open the memories relevant to today's work.
- **During work:** write/update at every milestone, ruling, or surprising discovery.
- **Day-close:** sweep — did every initiative touched today get its update?
