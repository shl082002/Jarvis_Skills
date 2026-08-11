#!/usr/bin/env bash
# Jarvis Skills installer — wires the kit into a target project.
# Usage: install.sh <claude|cursor|generic> [target-project-dir]
# Run from anywhere; target defaults to the current directory.
#
# PORTABILITY: every harness gets the same workroom + .jarvis/kit/ (agents,
# commands, skills, assets). Claude/Cursor extras are *projections* of that
# kit, not a second copy of the truth. New skills/commands are picked up by
# the globs below — do not add per-skill install lines. New *kinds* of
# artifact (sidecars, extra bins): see adapters/adding-surface.md.
set -euo pipefail

HARNESS="${1:-}"
TARGET="$(cd "${2:-.}" && pwd)"
KIT="$(cd "$(dirname "$0")/.." && pwd)"

if [[ ! "$HARNESS" =~ ^(claude|cursor|generic)$ ]]; then
  echo "Usage: install.sh <claude|cursor|generic> [target-project-dir]" >&2
  exit 1
fi

echo "Installing Jarvis Skills ($HARNESS) into: $TARGET"

# ---- The workroom (all harnesses) -------------------------------------------
mkdir -p "$TARGET/.jarvis/memory" "$TARGET/.jarvis/chronicle" "$TARGET/.jarvis/reports" \
         "$TARGET/.jarvis/bin" "$TARGET/.jarvis/logs" "$TARGET/.jarvis/run" \
         "$TARGET/.jarvis/live" "$TARGET/.jarvis/inbox"

stub() { [[ -f "$1" ]] || printf '%s\n' "$2" > "$1"; }

# Butler scripts are kit-owned code — refreshed on every install.
cp "$KIT/bin/svc" "$TARGET/.jarvis/bin/svc"
cp "$KIT/bin/gauntlet" "$TARGET/.jarvis/bin/gauntlet"
chmod +x "$TARGET/.jarvis/bin/svc" "$TARGET/.jarvis/bin/gauntlet"

# NB: no gauntlet.repos stub on purpose — with no config the gauntlet auto-detects
# sibling git repos and their dev lines. Write one only to override that.

stub "$TARGET/.jarvis/services.yml" "# services.yml — HAPPY's service registry (format: skills/services/SKILL.md)
# example-service:
#   dir: path/from/workspace/root
#   cmd: venv/bin/uvicorn app.main:app --port 8000
#   port: 8000
#   health: http://localhost:8000/health
#   notes: contested ports, env requirements, sharp edges"

stub "$TARGET/.jarvis/MEMORY.md" "# MEMORY — index (one line per memory; content lives in memory/)
<!-- - [Title](memory/file.md) — hook for when to open it -->"

stub "$TARGET/.jarvis/LEDGER.md" "# GIT LEDGER — every working branch, per repo (newest first)
<!-- Never rely on recall for branch names. Format: skills/git-ledger/SKILL.md -->"

stub "$TARGET/.jarvis/TRACKER.md" "# TRACKER — the one list · updated: never · next free ID: T-1
## NOW — being worked
## AWAITING — blocked on the principal or external
## NEXT — open, queued
## PARKED — deliberately deferred (each with a revisit condition)
## DONE — recent (pruned at day-close)"

# Broadcast to every running session on every prompt (hooks/policy-notice.sh).
# Keep it SHORT — it is injected many times a day. Empty or absent = silence.
stub "$TARGET/.jarvis/POLICY.md" "# PERMISSION POLICY — live. Edit freely; every session sees it on its next prompt.
- Ordinary commands run without a prompt.
- PUSH is gated (law 17): no push without a fresh one-shot grant —
  \`.jarvis/bin/gauntlet push-ok \"<what and why>\"\`. One grant, one push, 10 minutes.
- Mainline pushes, force-pushes and sudo are refused even with a grant open.
- Remote shells (ssh/scp/sftp/rsync) have no grant path — the principal runs those."

stub "$TARGET/.jarvis/HANDOVER.md" "# HANDOVER — last updated: NEVER (fresh install)
## 1. Mission
(not yet set — first session should establish it with the principal)
## 2. State of the world
## 3. Next first task
Run the boot ritual; brief the principal; ask what we're building.
## 4. Open decisions
## 5. Landmines
## 6. Where everything is
MEMORY.md · LEDGER.md · chronicle/ · reports/ — all under .jarvis/"

# ---- Portable kit stage (all harnesses) -------------------------------------
# File-first copy so Claude, Cursor, and a raw agent share one tree.
stage_portable_kit() {
  mkdir -p "$TARGET/.jarvis/kit"
  rm -rf "$TARGET/.jarvis/kit/agents" "$TARGET/.jarvis/kit/commands" "$TARGET/.jarvis/kit/skills"
  cp -R "$KIT/agents" "$KIT/commands" "$KIT/skills" "$TARGET/.jarvis/kit/"
  if [[ -d "$KIT/assets" ]]; then
    rm -rf "$TARGET/.jarvis/kit/assets"
    mkdir -p "$TARGET/.jarvis/kit/assets"
    cp -R "$KIT/assets/." "$TARGET/.jarvis/kit/assets/"
  fi
  echo "  + .jarvis/kit/{agents,commands,skills} staged (portable)"
}

# ---- The charter (all harnesses) --------------------------------------------
if [[ ! -f "$TARGET/JARVIS.md" ]]; then
  cp "$KIT/JARVIS.md" "$TARGET/JARVIS.md"
  echo "  + JARVIS.md (edit the House Configuration block!)"
else
  echo "  = JARVIS.md already present — left untouched (amend, never fork)"
fi

# Cursor always-on rule must follow the *installed* charter so House Config
# (principal name, project lines) is not clobbered by the portable default.
cursor_charter_src() {
  if [[ -f "$TARGET/JARVIS.md" ]]; then
    echo "$TARGET/JARVIS.md"
  else
    echo "$KIT/JARVIS.md"
  fi
}

# ---- Wiring the hooks into .claude/settings.json ------------------------------
# MERGE, NEVER OVERWRITE. A target's settings.json may hold permissions, other
# hooks, MCP config, anything — all of it must survive. The rules:
#   · existing file is read and re-written whole; only our hook entries are added
#   · a timestamped .bak is taken before any write
#   · idempotent: a hook already wired (by basename) is left alone, never doubled
#   · ANY doubt — no python3, unreadable/malformed/non-object JSON — and we write
#     nothing at all and fall back to printing the manual block. A broken install
#     is recoverable; a destroyed settings.json is not.
wire_claude_hooks() {
  local settings="$1"
  command -v python3 >/dev/null 2>&1 || return 1
  python3 - "$settings" <<'PY'
import json, os, shutil, sys, time

path = sys.argv[1]

# event, matcher (None = no matcher key), hook scripts in order, timeout or None
WIRING = [
    ("SessionStart",     "startup|resume|clear|compact", ["gauntlet-summon.sh"],                    10),
    ("UserPromptSubmit", None,                           ["gauntlet-reminder.sh",
                                                          "policy-notice.sh"],                    None),
    ("PreToolUse",       "Bash",                         ["guard-push-ssh.sh"],                      10),
]
CMD = "$CLAUDE_PROJECT_DIR/.claude/hooks/%s"

try:
    data = {}
    existed = os.path.exists(path)
    if existed:
        with open(path) as f:
            raw = f.read().strip()
        if raw:
            data = json.loads(raw)          # malformed → exception → shell falls back
    if not isinstance(data, dict):
        raise ValueError("settings.json is not a JSON object")

    hooks = data.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        raise ValueError("existing 'hooks' key is not an object")

    added, kept = [], []
    for event, matcher, scripts, timeout in WIRING:
        entries = hooks.setdefault(event, [])
        if not isinstance(entries, list):
            raise ValueError("existing hooks.%s is not an array" % event)
        for script in scripts:
            # Already wired? Match on basename so a differently-rooted path counts.
            wired = any(
                script in (h.get("command") or "")
                for g in entries if isinstance(g, dict)
                for h in (g.get("hooks") or []) if isinstance(h, dict)
            )
            if wired:
                kept.append("%s/%s" % (event, script))
                continue
            hook = {"type": "command", "command": CMD % script}
            if timeout:
                hook["timeout"] = timeout
            group = next((g for g in entries
                          if isinstance(g, dict) and g.get("matcher") == matcher), None)
            if group is None:
                group = {"hooks": []} if matcher is None else {"matcher": matcher, "hooks": []}
                entries.append(group)
            group.setdefault("hooks", []).append(hook)
            added.append("%s/%s" % (event, script))

    if added:
        if existed:
            shutil.copy2(path, path + ".bak-" + time.strftime("%Y%m%d-%H%M%S"))
        tmp = path + ".tmp"
        with open(tmp, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        os.replace(tmp, path)               # atomic: never a half-written settings file
        print("wired: " + ", ".join(added))
        if existed:
            print("backup: " + os.path.basename(path) + ".bak-*")
    else:
        print("already wired: " + ", ".join(kept))
    if added and kept:
        print("left as-is: " + ", ".join(kept))
except Exception as e:
    print("merge refused: %s" % e, file=sys.stderr)
    sys.exit(1)
PY
}

# ---- Harness-specific wiring -------------------------------------------------
stage_portable_kit

case "$HARNESS" in
  claude)
    mkdir -p "$TARGET/.claude/agents" "$TARGET/.claude/commands" "$TARGET/.claude/skills"
    cp "$KIT/agents/"*.md "$TARGET/.claude/agents/"
    cp "$KIT/commands/"*.md "$TARGET/.claude/commands/"
    for d in "$KIT/skills/"*/; do
      name="$(basename "$d")"
      mkdir -p "$TARGET/.claude/skills/$name"
      cp "$d/SKILL.md" "$TARGET/.claude/skills/$name/SKILL.md"
    done
    mkdir -p "$TARGET/.claude/hooks"
    cp "$KIT/hooks/"*.sh "$TARGET/.claude/hooks/"
    chmod +x "$TARGET/.claude/hooks/"*.sh
    echo "  + .claude/{agents,commands,skills,hooks} populated (Claude projection)"
    if out="$(wire_claude_hooks "$TARGET/.claude/settings.json")"; then
      printf '%s\n' "$out" | sed 's/^/  + settings.json: /'
      echo "    (merged in place — every pre-existing key was preserved)"
    else
      echo "  ! Could NOT safely merge .claude/settings.json — nothing was written."
      echo "    Needs python3 and a valid JSON object; yours is missing or malformed."
      echo "    Hooks are COPIED but not WIRED — paste the settings.json block from"
      echo "    adapters/claude-code.md (§ Hooks) by hand."
    fi
    echo "  ! Add the charter pointer to CLAUDE.md (see adapters/claude-code.md)"
    echo "  ! New agent types may need a session restart to register"
    echo "  ! Hooks take effect on the NEXT session (settings are read at start)"
    ;;
  cursor)
    mkdir -p "$TARGET/.cursor/rules"
    _charter="$(cursor_charter_src)"
    { printf -- '---\ndescription: The Jarvis operating charter — binds every session\nalwaysApply: true\n---\n\n'
      cat "$_charter"
    } > "$TARGET/.cursor/rules/00-jarvis-charter.mdc"
    echo "  + .cursor/rules/00-jarvis-charter.mdc from $_charter"
    for d in "$KIT/skills/"*/; do
      name="$(basename "$d")"
      desc="$(sed -n 's/^description: //p' "$d/SKILL.md" | head -1)"
      { printf -- '---\ndescription: %s\nalwaysApply: false\n---\n\n' "$desc"
        awk 'NR==1 && /^---$/ {fm=1; next} fm==1 {if (/^---$/) fm=2; next} {print}' "$d/SKILL.md"
      } > "$TARGET/.cursor/rules/$name.mdc"
    done
    echo "  + .cursor/rules populated (charter always-on, skills on-demand)"
    echo "  + .jarvis/kit already staged for hats/commands (same as Claude/generic)"
    ;;
  generic)
    echo "  + generic: .jarvis/kit is the only projection — load JARVIS.md (see adapters/generic.md)"
    ;;
esac

echo "Done. First session: run the boot ritual (commands/boot.md)."
