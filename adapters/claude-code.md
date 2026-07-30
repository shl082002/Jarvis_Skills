# Adapter — Claude Code

The kit's file formats are native to Claude Code; installation is a copy.

## Wiring

From the target project root (or run `install.sh claude` to do all of this):

| Kit source | Destination | Becomes |
|------------|-------------|---------|
| `agents/*.md` | `.claude/agents/` | named subagent types for the Agent tool |
| `commands/*.md` | `.claude/commands/` | `/boot`, `/day-close`, `/remember`, … |
| `skills/*/SKILL.md` | `.claude/skills/<name>/SKILL.md` | auto-triggering skills |
| `JARVIS.md` | project root (or `.claude/`) | referenced from CLAUDE.md |

Then add to the project's `CLAUDE.md` (create it if absent):

```markdown
## Operating charter
This project runs under the Jarvis charter — read `JARVIS.md` at session start
and follow it. Workroom: `.jarvis/` (memory, ledger, chronicle, handover, reports).
```

And scaffold the workroom: `.jarvis/{memory,chronicle,reports}/` plus stub
`MEMORY.md`, `LEDGER.md`, `HANDOVER.md` (the installer does this).

## Claude-Code-specific notes

- **Agent registration:** newly copied agent definitions may need a session
  restart to register as named subagent types. Until then, run the definition
  file's prompt through a general-purpose agent.
- **Native memory:** if the session has Claude's file-based auto-memory, use it
  as the primary store and keep `.jarvis/memory/` as the project-portable mirror
  — same format, so syncing is a copy. The portable copy is what other harnesses
  will read.
- **Permissions (charter law 17):** encode the push ceiling mechanically in
  `.claude/settings.json` — allowlist routine read/build/local-git prefixes,
  deny `git push * main`, `git push * dev`, force-pushes, `sudo`. Keep plain
  `git push` prompting: the prompt is the principal's confirmation.
- **Model economy:** DUM-E and U declare `model: haiku` in frontmatter — scouts
  and librarians don't need the big model. Keep that when copying.
