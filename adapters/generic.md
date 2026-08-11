# Adapter — any agent, anywhere

The kit assumes exactly three capabilities: the agent can **read files**, **write
files**, and **run shell commands** (git). Anything with those three can run the
whole system — an API loop, a new IDE, a CLI that doesn't exist yet.

## The minimal recipe

1. **Load the charter.** Put `JARVIS.md` (with House Configuration filled in)
   into the agent's standing instructions — system prompt, rules file, first
   message, whatever the harness calls it.

2. **Point at the skills.** Add one standing line:
   *"Process doctrine lives in `<kit-path>/skills/<topic>/SKILL.md` — consult the
   relevant skill before memory work, atlas work, ledger/chronicle/handover
   writes, session open/close, builds, verification claims, or delegation."*
   Agents that support tool/document retrieval can index the folder instead.

3. **Scaffold the workroom.** `install.sh generic` creates `.jarvis/` stubs and
   stages the full portable kit at `.jarvis/kit/` (agents, commands, skills,
   assets, sidecars, bin). That directory is the same tree Claude and Cursor
   get — they only add harness projections on top. Heimdall and voice are
   localhost sidecars; POLICY defaults `voice: off` and `heimdall: localhost`.

4. **Roles as hats.** Without subagent support, specialists run inline: read
   `agents/<name>.md`, adopt its standing orders for the mission, write the
   report file, return to being the assistant. With subagent support, register
   the files as agent definitions.

5. **Commands as phrases.** "boot", "day-close", "remember: X" → execute the
   matching `.jarvis/kit/commands/<name>.md` (or the kit checkout's `commands/`).

6. **Adding skills.** See `adapters/adding-surface.md` — globs, not per-skill
   install lines. Keep command/skill bodies free of `~/.claude/…` paths.

## The portability contract

State lives in `.jarvis/`, in plain markdown, written for a stranger. Follow
three rules and any mix of tools can share one project:

- **Boot from files, not from session memory** — even if the harness has
  session persistence, the files are the source of truth (another tool may
  have moved the world since).
- **Close to files, every time** — a session that ends without day-close (or
  at minimum a handover refresh) has orphaned its work.
- **Never write project state anywhere harness-private** if it matters to the
  partnership; mirror it into the workroom.

## Degradation table

| Missing capability | What changes |
|--------------------|--------------|
| No subagents | Roles run inline as hats (discipline intact) |
| No slash commands | Command words typed in chat |
| No permission engine | Push ceiling enforced by charter alone — restate law 3 prominently |
| No browser automation | EDITH's live verification degrades to curl + logs; say so on the evidence ladder |
| No shell | The kit is not for this harness — files + git are the floor |
