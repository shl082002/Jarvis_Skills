---
name: chronicle
description: Dated decision & change records — plans before builds, rulings with their reasons, session-close summaries. The chat is ephemeral; the chronicle is not. Use when locking a plan, recording a decision, closing a session, or handing a design to a builder.
---

# Chronicle — the paper trail of plans and rulings

`.jarvis/chronicle/YYYY-MM-DD/` holds the durable documents of the partnership.
Chat messages scroll away and context windows die; anything that will be *referred
back to* gets a chronicle file the day it happens.

## What earns a chronicle document

1. **Plans, before builds.** Any build bigger than a trivial fix gets a plan doc
   FIRST: scope, slices, decision points, what's explicitly out. The principal
   ratifies the plan (or its open decisions) before code exists. The plan doc is
   what a builder agent receives as its locked design.
2. **Decision records.** When the principal makes a ruling, record: the options
   that were on the table, the ruling, the *why*, and the date. Future sessions
   must never re-litigate a decision they can simply read (charter law 1).
3. **Session-close summaries.** What was done, what was verified vs merely built,
   what's open, next first task. Written at day-close.
4. **Investigation dossiers.** Root-cause findings, comparison tables,
   research results that outlive the question that prompted them.
5. **Activation checklists.** When something ships dark behind a flag, the
   checklist of exactly what to do at activation time lives here — written while
   the knowledge is fresh, executed possibly weeks later.

## Naming & layout

```
.jarvis/chronicle/
└── 2026-07-30/
    ├── <topic>_plan.md
    ├── <topic>_decision.md
    ├── session_close.md
    └── <initiative>/          ← big initiatives get a subfolder
        ├── design.md
        └── activation_checklist.md
```

One folder per date; descriptive snake_case names; an initiative that spans dates
gets cross-links, not copies.

## The rules

- **Plans are locked by the principal, not by momentum.** A plan doc without a
  ratification note ("locked <date>", or the rulings quoted) is a draft.
- **Record deviations.** When a build departs from its plan doc, the deviation and
  its reason are appended to the plan — the doc must remain a true account.
- **Chronicle vs memory:** memory (see `skills/memory/`) holds the *distilled,
  living* state pointer per initiative; the chronicle holds the *full, frozen*
  artifacts. Memory files should link to chronicle paths, never duplicate them.
- **Write for the stranger.** Every doc assumes its reader has NO chat context:
  spell out repo names, branch names, and dates. The reader may be a different
  agent in a different harness entirely.
