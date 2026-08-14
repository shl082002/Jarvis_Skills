# Adding surface to the kit — keep every harness working

The kit is **one tree**. Claude Code, Cursor, and a generic agent must all
see the same skills, commands, agents, and assets after `install.sh`.

## What install already does

`adapters/install.sh` **globs**:

- `agents/*.md`
- `commands/*.md`
- `skills/*/SKILL.md`
- `hooks/*.sh` (Claude projection)
- `bin/svc`, `bin/gauntlet`, `bin/heimdall`, `bin/cockpit`, `bin/voice-inbox`, `bin/voice-say`, `bin/browse-env`
- `assets/` if the directory exists

**Do not** add a per-skill `cp` line for a new `skills/foo/` or `commands/foo.md`.
Re-run install; the glob picks it up.

## Checklist when you add something

| You added | Also do |
|-----------|---------|
| `skills/<name>/SKILL.md` | `commands/<name>.md` if it is a typed/slash command; mention it in `README.md` tree; **re-run install for each harness you care about** |
| `commands/<name>.md` | List the word in charter “command words” only if you change `JARVIS.md` (portable default). Project `JARVIS.md` House Config is never overwritten |
| `agents/<name>.md` | One line in `skills/council/SKILL.md` |
| `bin/<tool>` | add the name to the `for b in svc gauntlet …` loop in `install.sh` + document in all three adapters |
| `assets/…` | Nothing in install (directory copy is automatic) |
| `sidecars/…` | New kind — update `install.sh` **and** `claude-code.md` / `cursor.md` / `generic.md` in the **same commit** |

## Harness projections (not a second source of truth)

| Harness | Extra projection | Shared truth |
|---------|------------------|--------------|
| `claude` | `.claude/{agents,commands,skills,hooks}` + settings merge | `.jarvis/kit/` + `.jarvis/` |
| `cursor` | `.cursor/rules/*.mdc` (charter from **project** `JARVIS.md` if present) | `.jarvis/kit/` + `.jarvis/` |
| `generic` | none | `.jarvis/kit/` + `.jarvis/` + load `JARVIS.md` |

A Cursor session and a Claude session on the same repo must boot from the same
handover. Never write standing process only into `.claude/` or `.cursor/`.

## Commands per host

- Claude: `/boot` from `.claude/commands/boot.md`
- Cursor: typed `boot` → `.jarvis/kit/commands/boot.md` (charter command words)
- Generic: same typed words → same files

Keep command bodies harness-agnostic (no `~/.claude/skills/…` paths). Point at
`WORKROOM` / `.jarvis/kit/`.
