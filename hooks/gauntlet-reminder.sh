#!/bin/bash
# UserPromptSubmit hook — GAUNTLET broadcast (charter law 19).
#
# Fires in EVERY session, on EVERY prompt, whenever .jarvis/run/GAUNTLET_ACTIVE
# exists. No heuristics: the flag file IS the signal. Deleting it closes the
# gauntlet for every session at once.
#
# Why a hook and not memory: memory loads at session boot. A session already open
# when a gauntlet opens never sees it, and a compacted context can lose it. This
# fires regardless of what the session remembered or when it started.
#
# Broadcasts the three questions (WHERE? · ALIVE? · NEEDS YOU?) plus who bears
# which stone — the single most dangerous thing for sessions to disagree about.

set -e
payload=$(cat 2>/dev/null || true)   # stdin carries session_id — we use it for identity

# Workspace root: the harness sets CLAUDE_PROJECT_DIR; otherwise this hook lives
# at <root>/.claude/hooks/, so two levels up is the root.
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
FLAG="$ROOT/.jarvis/run/GAUNTLET_ACTIVE"
STONES="$ROOT/.jarvis/run/stones"
DIR="$ROOT/.jarvis/gauntlet"
SESSIONS="$ROOT/.jarvis/run/sessions"

[ -f "$FLAG" ] || exit 0

NOW=$(date +%s)
bearer() { if [ -s "$STONES/$1" ]; then head -n1 "$STONES/$1" | cut -d'|' -f1; else echo "free"; fi; }

SID=$(printf '%s' "$payload" | grep -o '"session_id"[[:space:]]*:[[:space:]]*"[^"]*"' | head -n1 | sed 's/.*:[[:space:]]*"//; s/"$//')
MINE=""; [ -n "$SID" ] && [ -s "$SESSIONS/$SID" ] && MINE=$(head -n1 "$SESSIONS/$SID")

echo "[GAUNTLET OPEN — auto-injected, charter law 19]"
echo "$(head -n1 "$FLAG" 2>/dev/null)"
echo "Board: .jarvis/gauntlet/BOARD.md · Helper: .jarvis/bin/gauntlet status"
echo ""
# Identity, resolved every prompt — so a session that started BEFORE the gauntlet
# opened, or that has since been compacted, still knows exactly who it is.
if [ -n "$MINE" ]; then
  echo "🦸 YOU ARE FRONT: $(echo "$MINE" | tr '[:lower:]' '[:upper:]')  — brief: .jarvis/gauntlet/$MINE.md"
else
  echo "👉 YOU ARE UNSEATED. A front is raised ONLY on Mr. Stark's ask — never seat"
  echo "   yourself. The moment he names you one, that is one command:"
  echo "     .jarvis/bin/gauntlet enlist <name> \"<character>\" <none|burst|heavy> \"<territory>\"${SID:+ $SID}"
  echo "   It raises the front, seats you, and writes your cold-boot brief."
fi
echo ""
echo "STONES — one bearer each. No stone, no claim."
echo "  🔴 REALITY  $(bearer reality)   ← start services · claim a LIVE result"
echo "  🟢 TIME     $(bearer time)   ← the migration head, one per repo"
echo "  🟡 MIND     $(bearer mind)   ← the records; the Collector's, once"
echo "  🟣 POWER    MR. STARK   ← push. Never delegated, asked freshly every time."
echo ""
echo "FRONTS — WHERE? · ALIVE? · NEEDS YOU?"
if [ -d "$DIR" ]; then
  for f in "$DIR"/*.md; do
    [ -e "$f" ] || continue
    b=$(basename "$f" .md); [ "$b" = "BOARD" ] && continue
    ph=$(grep -m1 '^status:' "$f" 2>/dev/null | sed 's/^status:[[:space:]]*//' | tr -d '*`' | awk '{print toupper($1)}')
    nd=$(grep -m1 '^needs:'  "$f" 2>/dev/null | sed 's/^needs:[[:space:]]*//'  | tr -d '*`')
    mt=$(stat -f %m "$f" 2>/dev/null || echo "$NOW"); age=$(( (NOW - mt) / 60 ))
    flag=""; [ "$age" -ge 30 ] && flag=" ⚠STALE"
    printf '  • %-16s %-14s %sm ago%s   %s\n' "$b" "${ph:-UNSET}" "$age" "$flag" "${nd:+· needs you: $nd}"
  done
fi
echo ""
echo "STANDING ORDERS while a gauntlet is open:"
echo "  1. You are ONE front. Read .jarvis/gauntlet/<your-front>.md before editing."
echo "     Unseated is a valid state: wait for his ask, then enlist. Never guess."
echo "  2. Work ONLY in your own worktree. Main repo trees are baseline."
echo "  3. Write ONLY to your own front file. Never TRACKER, ledger, or memory —"
echo "     that is 🟡 MIND, and it belongs to the Collector, once, at the Collect."
echo "  4. YOU ARE A COMMANDER, NOT A SOLOIST. Your fleet is available: DUM-E scouts,"
echo "     FRIDAY builds in your worktree, EDITH refutes. Live agents (EDITH/PEPPER/"
echo "     HAPPY) work under your 🔴 cover. NEVER be the only verifier of your own"
echo "     work. Name the actor in your log lines."
echo "  5. Status is ONE WORD from the ladder — never prose:"
echo "     RECON→DESIGN→BUILD→GATED→LIVE-QUEUED→LIVE-VERIFIED→PUSHED→LANDED"
echo "     Keep a 'needs:' line current. Checkpoint every ~90m."
echo "  6. Base off the declared baseline; never branch off another front."
echo "  7. Rules 3/3a/11 unchanged: one branch name across repos, feature branches"
echo "     only, and HE pushes — asked freshly, every single time."
echo "[end gauntlet reminder]"

exit 0
