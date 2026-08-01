#!/usr/bin/env bash
# Jarvis Skills installer — wires the kit into a target project.
# Usage: install.sh <claude|cursor|generic> [target-project-dir]
# Run from anywhere; target defaults to the current directory.
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
         "$TARGET/.jarvis/bin" "$TARGET/.jarvis/logs" "$TARGET/.jarvis/run"

stub() { [[ -f "$1" ]] || printf '%s\n' "$2" > "$1"; }

# svc butler script is kit-owned code — refreshed on every install
cp "$KIT/bin/svc" "$TARGET/.jarvis/bin/svc"
chmod +x "$TARGET/.jarvis/bin/svc"

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

# ---- The charter (all harnesses) --------------------------------------------
if [[ ! -f "$TARGET/JARVIS.md" ]]; then
  cp "$KIT/JARVIS.md" "$TARGET/JARVIS.md"
  echo "  + JARVIS.md (edit the House Configuration block!)"
else
  echo "  = JARVIS.md already present — left untouched (amend, never fork)"
fi

# ---- Harness-specific wiring -------------------------------------------------
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
    echo "  + .claude/{agents,commands,skills} populated"
    echo "  ! Add the charter pointer to CLAUDE.md (see adapters/claude-code.md)"
    echo "  ! New agent types may need a session restart to register"
    ;;
  cursor)
    mkdir -p "$TARGET/.cursor/rules"
    { printf -- '---\ndescription: The Jarvis operating charter — binds every session\nalwaysApply: true\n---\n\n'
      cat "$KIT/JARVIS.md"
    } > "$TARGET/.cursor/rules/00-jarvis-charter.mdc"
    for d in "$KIT/skills/"*/; do
      name="$(basename "$d")"
      desc="$(sed -n 's/^description: //p' "$d/SKILL.md" | head -1)"
      { printf -- '---\ndescription: %s\nalwaysApply: false\n---\n\n' "$desc"
        awk 'NR==1 && /^---$/ {fm=1; next} fm==1 {if (/^---$/) fm=2; next} {print}' "$d/SKILL.md"
      } > "$TARGET/.cursor/rules/$name.mdc"
    done
    # agents + commands ride along as reference files for inline "hat" use
    mkdir -p "$TARGET/.jarvis/kit"
    cp -R "$KIT/agents" "$KIT/commands" "$TARGET/.jarvis/kit/"
    echo "  + .cursor/rules populated (charter always-on, skills on-demand)"
    echo "  + agents/commands staged at .jarvis/kit/ for inline use"
    ;;
  generic)
    mkdir -p "$TARGET/.jarvis/kit"
    cp -R "$KIT/agents" "$KIT/commands" "$KIT/skills" "$TARGET/.jarvis/kit/"
    echo "  + full kit staged at .jarvis/kit/"
    echo "  ! Load JARVIS.md as the agent's standing instructions (see adapters/generic.md)"
    ;;
esac

echo "Done. First session: run the boot ritual (commands/boot.md)."
