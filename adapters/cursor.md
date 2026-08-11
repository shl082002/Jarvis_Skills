# Adapter — Cursor (and similar rules-based IDEs)

Cursor has no subagents, skills, or slash commands — but it has **rules** and it
has **files**, and the kit is built on files. Everything survives; only the
trigger mechanism changes.

## Wiring

1. **The charter → an always-on rule.**
   Copy the **installed** `JARVIS.md` (project House Config) — not the kit
   default if the project already has a charter — to
   `.cursor/rules/00-jarvis-charter.mdc` with frontmatter:

   ```
   ---
   description: The Jarvis operating charter — binds every session
   alwaysApply: true
   ---
   ```

2. **Skills → agent-requested rules.** Each `skills/<name>/SKILL.md` becomes
   `.cursor/rules/<name>.mdc`, keeping its `description:` line in the
   frontmatter (that's what Cursor's agent uses to decide relevance) and
   `alwaysApply: false`. Alternatively: keep the kit folder in the repo and add
   one always-on rule saying *"process questions are answered by
   `Jarvis_Skills/skills/<topic>/SKILL.md` — read the relevant one before
   acting"* — thinner context, same effect.

3. **Commands → typed invocations.** No slash commands; the principal types
   "boot", "day-close", "remember: …" in chat. Add this line to the charter
   rule: *"When the principal's message is a bare command word matching a file
   in `commands/`, execute that file's instructions."*

4. **Agents → hats.** No subagent spawning; the roles run inline. When the work
   calls for a specialist (see `skills/council/`), read the matching
   `agents/<name>.md` and adopt its standing orders wholesale for that mission —
   including read-only reach, the report file to `.jarvis/reports/`, and the
   1–3-line wrap. The discipline is the point, not the process isolation.

5. **The workroom is identical.** `.jarvis/` — same files, same formats. The
   installer also stages `.jarvis/kit/` (agents, commands, skills, assets) so
   Cursor hats and command words match Claude and generic. A Claude Code session
   can close the day and a Cursor session can boot from the same handover
   tomorrow, or vice versa.

6. **Adding skills.** New `skills/` and `commands/` are globbed by `install.sh`.
   New artifact *kinds* need `install.sh` + this file + `claude-code.md` +
   `generic.md` in one commit. See `adapters/adding-surface.md`.

7. **Sidecars.** Cockpit (`bin/cockpit open` → `127.0.0.1:3847`) and voice
   (`inbox/`, `voice: off` until POLICY flips) live under `.jarvis/kit/sidecars/`.
   Do not run `install.sh` just to peek at kit files — the checkout is enough.
   Re-install only when the principal wants the live projection refreshed.

8. **House Config.** If `JARVIS.md` already exists, install **never replaces**
   it. Cursor’s always-on charter is copied from that project file.

## Cautions

- Cursor cannot mechanically enforce the push ceiling (no permission engine) —
  the charter's law 3 does the work alone, so state it in the always-on rule
  verbatim.
- Long rules get truncated by some IDE versions; if the charter must shrink,
  keep laws 1–5, 11–14, and 18 — those are the load-bearing ones — and link the
  rest.
