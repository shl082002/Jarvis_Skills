# Adapter — Claude Code

The kit's file formats are native to Claude Code; installation is a copy.

## Wiring

From the target project root (or run `install.sh claude` to do all of this):

| Kit source | Destination | Becomes |
|------------|-------------|---------|
| `agents/*.md` | `.claude/agents/` | named subagent types for the Agent tool |
| `commands/*.md` | `.claude/commands/` | `/boot`, `/day-close`, `/remember`, … |
| `skills/*/SKILL.md` | `.claude/skills/<name>/SKILL.md` | auto-triggering skills |
| `hooks/*.sh` | `.claude/hooks/` | gauntlet auto-summon (needs wiring — see below) |
| `bin/*` | `.jarvis/bin/` | `svc` (services) and `gauntlet` (parallel sessions) |
| `JARVIS.md` | project root (or `.claude/`) | referenced from CLAUDE.md |

Then add to the project's `CLAUDE.md` (create it if absent):

```markdown
## Operating charter
This project runs under the Jarvis charter — read `JARVIS.md` at session start
and follow it. Workroom: `.jarvis/` (memory, ledger, chronicle, handover, reports).
```

And scaffold the workroom: `.jarvis/{memory,chronicle,reports}/` plus stub
`MEMORY.md`, `LEDGER.md`, `HANDOVER.md` (the installer does this).

## Hooks — arming gauntlet auto-summon

Copying the hooks is not enough; they must be wired in `.claude/settings.json`.
Both are no-ops with a byte of output when no gauntlet is open, so wiring them is
safe on an ordinary day.

```jsonc
"hooks": {
  "SessionStart": [                                  // a NEW session learns who it is
    { "matcher": "startup|resume|clear|compact",
      "hooks": [{ "type": "command", "timeout": 10,
                  "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/gauntlet-summon.sh" }] }
  ],
  "UserPromptSubmit": [                              // an EXISTING session is re-told
    { "hooks": [{ "type": "command",
                  "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/gauntlet-reminder.sh" }] }
  ]
}
```

**Why two hooks, not one.** `SessionStart` covers a session opened *after* the
gauntlet opened. It cannot help a session that was already running, and it fires
once — so a compacted context can lose the identity. `UserPromptSubmit` re-states
who this session is on **every prompt**, which is what makes an already-running
session summonable and a compacted one self-healing. Both read `session_id` from
the hook payload; that id is the key the seat is held under.

**The rule the mechanic exists to enforce:** a front is raised **only on the
principal's ask** — never pre-assigned, never self-selected. An unseated session is
told the exact one-line command and then waits:

```bash
.jarvis/bin/gauntlet enlist <name> "<character>" <none|burst|heavy> "<territory>" [session-id]
```

Seats are claimed atomically (`set -C` noclobber), so simultaneous starts cannot
double-book one front — verified with 5 concurrent boots against 1 free seat.

⚠ **macOS ships bash 3.2.** Keep these scripts bash-3-clean: no `${var^^}`, no
associative arrays, and guard array expansion under `set -u` with
`${ARR[@]+"${ARR[@]}"}`. A `${var^^}` in the original cost a stone-claim command
that silently errored on every use.

## Claude-Code-specific notes

- **Agent registration:** newly copied agent definitions may need a session
  restart to register as named subagent types. Until then, run the definition
  file's prompt through a general-purpose agent.
- **Native memory:** if the session has Claude's file-based auto-memory, use it
  as the primary store and keep `.jarvis/memory/` as the project-portable mirror
  — same format, so syncing is a copy. The portable copy is what other harnesses
  will read.
- **Permissions (charter law 17) — three tiers. ⚠ Verify `ask` actually prompts
  before you rely on it.** The documented precedence is **deny > ask > allow**, so
  in principle `ask` is un-grantable. **Measured 5 Aug 2026, it did not prompt at
  all** — not from rules, not from a hook. The tell: a command in *neither* `allow`
  nor `ask` also ran silently, which means the session's runtime permission **mode**
  (auto / dontAsk / bypass) auto-approves *above* the rule layer, and no rule can
  reach past it. **`deny` is enforced regardless of mode** — it is the only tier you
  can trust unconditionally.
  **Test it, don't assume:** run a command that is in neither list. If it runs
  without a prompt, `ask` is inert in that session, and anything you need gated must
  go in `deny` instead.
  ```jsonc
  "permissions": {
    "allow": ["Bash"],                        // the routine: everything not named below
    "ask":   ["Bash(git push:*)", "Bash(git -C:*push*)", "Bash(gh pr merge:*)",
              "Bash(ssh:*)", "Bash(scp:*)", "Bash(sftp:*)", "Bash(rsync:*)"],
    "deny":  ["Bash(git push origin main:*)", "Bash(git push origin master:*)",
              "Bash(git push origin dev:*)",  "Bash(git push origin development:*)",
              "Bash(git push --force:*)", "Bash(git push -f:*)",
              "Bash(git push --force-with-lease:*)", "Bash(sudo:*)"]
  }
  ```
  **Prune `settings.local.json` when you set this up.** Accumulated "don't ask again"
  grants pile up there — in one real project it had grown to **1,720 entries, including
  a blanket `Bash(git push *)` and an explicit `push origin main`**. A blanket `Bash`
  allow makes every one of them dead weight, and dead weight is where a dangerous grant
  hides. Strip every `Bash(...)` entry; keep `WebFetch`/`Read`/`additionalDirectories`.
- **Model economy:** DUM-E and U declare `model: haiku` in frontmatter — scouts
  and librarians don't need the big model. Keep that when copying.
