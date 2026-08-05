#!/bin/bash
# UserPromptSubmit — broadcasts the live permission policy to EVERY session.
#
# THE PROBLEM THIS SOLVES
# The principal reports friction as they hit it, you fix it once, and every
# session already running must see the change without them repeating themselves.
# Memory loads at boot, and a settings edit is invisible to a session that is
# already open — a hook fires on every prompt regardless of when the session
# started, so this is the only channel that reaches all of them at once.
#
# THE CONTENT LIVES IN A FILE, NOT IN THIS SCRIPT.
# Edit <root>/.jarvis/POLICY.md; this hook never needs changing. Absent or empty
# file = silence, zero cost. Keep it SHORT — it is injected on every prompt in
# every session, so every line is paid for many times a day.
#
# Companion to hooks/guard-push-ssh.sh: that one ENFORCES the policy mechanically,
# this one keeps every session's understanding of it current. (Charter law 17.)

set -e
cat >/dev/null   # drain stdin; no input signals needed

# Workspace root: the harness sets CLAUDE_PROJECT_DIR; otherwise this hook lives
# at <root>/.claude/hooks/, so two levels up is the root. POLICY_FILE overrides
# both, for harnesses that place hooks elsewhere.
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
POLICY="${POLICY_FILE:-$ROOT/.jarvis/POLICY.md}"

[ -s "$POLICY" ] || exit 0

echo "[PERMISSIONS — auto-injected, charter law 17]"
cat "$POLICY"
echo "[end permission policy]"

exit 0
