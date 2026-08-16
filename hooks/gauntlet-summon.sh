#!/bin/bash
# SessionStart hook — identity while a gauntlet is DECLARED (charter law 19).
#
# Closed gauntlet = ordinary charter. Say nothing, cost nothing.
# Open gauntlet: resume a bound seat, or stay UNSEATED until the principal
# names a front (enlist). Never auto-take an empty seat.
#
# THE PROBLEM THIS SOLVES
# The UserPromptSubmit broadcast (gauntlet-reminder.sh) tells every session that a
# gauntlet is open and what the board looks like — but it ends with "if you do not
# know which front you are, ASK Mr. Stark." That means every new session costs him
# a briefing. With N fronts that is N briefings before any work starts.
#
# THE MECHANIC
# Fronts are SEATS. A seat is a front file in .jarvis/gauntlet/<name>.md with no
# claim file beside it. When a session starts, it takes the lowest-order free seat
# — atomically — and is handed that front's cold-boot brief. He opens a terminal;
# it already knows who it is.
#
# Claims are FIRST-COME, and atomic via noclobber (set -C): two sessions starting
# in the same second cannot take the same seat. The claim survives compaction and
# resume because the binding is keyed on session_id, which is stable across both.
#
# STATE
#   .jarvis/run/claims/<front>    = session_id that holds the seat  (forward)
#   .jarvis/run/sessions/<sid>    = front name this session is      (reverse)
# Deleting either by hand is safe: `gauntlet unbind <front>` does both.
#
# NEVER auto-claims when: no gauntlet is open · the session is already bound ·
# every seat is taken (it becomes a spectator and is told to ask before editing).

set -uo pipefail

# Workspace root: the harness sets CLAUDE_PROJECT_DIR; otherwise this hook lives
# at <root>/.claude/hooks/, so two levels up is the root.
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
RUN="$ROOT/.jarvis/run"
DIR="$ROOT/.jarvis/gauntlet"
FLAG="$RUN/GAUNTLET_ACTIVE"
STONES="$RUN/stones"
CLAIMS="$RUN/claims"
SESSIONS="$RUN/sessions"

payload=$(cat 2>/dev/null || true)

# Closed gauntlet = ordinary charter. Say nothing, cost nothing.
[ -f "$FLAG" ] || exit 0

mkdir -p "$CLAIMS" "$SESSIONS" "$STONES"

# ── identity ────────────────────────────────────────────────────────────────
# Dependency-free JSON scrape: this hook must never fail because jq is missing.
field() {
  printf '%s' "$payload" \
    | grep -o "\"$1\"[[:space:]]*:[[:space:]]*\"[^\"]*\"" | head -n1 \
    | sed 's/.*:[[:space:]]*"//; s/"$//'
}
SID=$(field session_id)
SRC=$(field source)
[ -z "$SID" ] && SID="anon-$$"

header() { grep -m1 "^$2:" "$1" 2>/dev/null | sed "s/^$2:[[:space:]]*//" | tr -d '*`'; }
order_of() { local o; o=$(header "$1" order); case "$o" in ''|*[!0-9]*) printf '50' ;; *) printf '%s' "$o" ;; esac; }

# Seats in declared order (order: header, default 50; ties alphabetical).
seats() {
  [ -d "$DIR" ] || return 0
  for f in "$DIR"/*.md; do
    [ -e "$f" ] || continue
    local b; b=$(basename "$f" .md)
    [ "$b" = "BOARD" ] && continue
    printf '%s %s\n' "$(order_of "$f")" "$b"
  done | sort -n -k1,1 -k2,2 | awk '{print $2}'
}

FRONT=""
# ① Already bound? Resume and compact land here — the session re-learns itself.
if [ -s "$SESSIONS/$SID" ]; then
  FRONT=$(head -n1 "$SESSIONS/$SID")
  # Heal a binding whose seat was released out from under it.
  if [ "$FRONT" != "heimdall" ] && [ ! -f "$DIR/$FRONT.md" ]; then FRONT=""; rm -f "$SESSIONS/$SID"; fi
fi

# ② Already bound? Resume and compact land here — the session re-learns itself.
#    Do NOT auto-take a free seat. Fronts are enlisted on the principal's ask.
if [ -z "$FRONT" ]; then
  : # stay unseated
fi

bearer() { if [ -s "$STONES/$1" ]; then head -n1 "$STONES/$1" | cut -d'|' -f1; else echo "free"; fi; }

echo "════════════════════════════════════════════════════════════════════════"
echo "🧤 GAUNTLET OPEN — $(head -n1 "$FLAG" 2>/dev/null)"
echo "════════════════════════════════════════════════════════════════════════"

if [ -z "$FRONT" ]; then
  echo ""
  echo "👉 YOU ARE UNSEATED — no front is yours yet, and that is the normal state."
  echo "   A front is raised ONLY on Mr. Stark's ask. Never seat yourself."
  echo ""
  echo "   THE MOMENT HE NAMES YOU ONE, this is the whole ceremony — one command:"
  echo ""
  echo "     .jarvis/bin/gauntlet enlist <name> \"<character>\" <none|burst|heavy> \"<territory>\" $SID"
  echo ""
  echo "   It raises the front if it is new, seats you in it, and writes your"
  echo "   cold-boot brief to .jarvis/gauntlet/<name>.md — read that in full, then work."
  echo "   Name the front from the work in front of you, never from a registry, and"
  echo "   never after Mr. Stark himself."
  echo ""
  echo "   Until he asks: ordinary charter. No branch, no worktree, no front edits."
  echo "   Board: .jarvis/gauntlet/BOARD.md · Seats: .jarvis/bin/gauntlet seats"
  echo "   (your session id: $SID)"
  exit 0
fi

if [ "$FRONT" = "heimdall" ]; then
  echo ""
  echo "👁  YOU ARE HEIMDALL — the spectator. No front, no stone, no branch."
  echo "    Watch the board for drift; run \`.jarvis/bin/gauntlet doctor\`."
  echo "    Board: .jarvis/gauntlet/BOARD.md"
  exit 0
fi

F="$DIR/$FRONT.md"
echo ""
echo "🦸 YOU ARE FRONT: $(echo "$FRONT" | tr '[:lower:]' '[:upper:]')"
echo "   ▸ FIRST ACTION, BEFORE ANY EDIT: read $F in full."
echo ""
printf '   character : %s\n' "$(header "$F" character)"
printf '   territory : %s\n' "$(header "$F" territory)"
printf '   branch    : %s\n' "$(header "$F" branch)"
printf '   status    : %s\n' "$(header "$F" status)"
printf '   needs him : %s\n' "$(header "$F" needs)"
echo ""
echo "STONES — one bearer each. No stone, no claim."
echo "   🔴 REALITY  $(bearer reality)   ← start services · claim a LIVE result"
echo "   🟢 TIME     $(bearer time)   ← the migration head, one per repo"
echo "   🟡 MIND     $(bearer mind)   ← the records; the Collector's, once"
echo "   🟣 POWER    MR. STARK   ← push. Never delegated, asked freshly every time."
echo "   take: .jarvis/bin/gauntlet take <stone> $FRONT <mins> \"why\""
echo ""
echo "STANDING ORDERS — all of them, every session:"
echo "  1. Your TASK is Mr. Stark's to assign. If the Task section is empty or"
echo "     marked PROPOSED, ASK HIM. Never pick your own target."
echo "  2. Work ONLY in your own worktree. Main trees are baseline — never edit"
echo "     them. The branch is the lock: git refuses one branch in two trees."
echo "  3. ONE branch NAME across every repo you touch (law 3a). Feature branches"
echo "     only. HE pushes — asked freshly, every single time (law 3/11)."
echo "  4. Write ONLY to $F. Never TRACKER, ledger or memory — that is 🟡 MIND,"
echo "     and it belongs to the Collector, once, at the Collect."
echo "  5. YOU ARE A COMMANDER, NOT A SOLOIST (law 13 · gauntlet L13). DUM-E/U/"
echo "     JOCASTA scout, FRIDAY builds in your worktree, EDITH refutes. Live"
echo "     agents (EDITH/PEPPER/HAPPY) need your 🔴. NEVER be the only verifier of"
echo "     your own work. Name the actor in every log line. Foreground only (16)."
echo "  6. EDITH deploys only on his command (law 15). \"wait\"/\"stop\" = hard stop,"
echo "     report immediately (law 14)."
echo "  7. Capture each gate's OWN exit code — never pipe a gate through grep"
echo "     (gauntlet L1: a fresh worktree exits 127 and grep reads it as success)."
echo "  8. status: is ONE WORD from the ladder — never prose:"
echo "     RECON→DESIGN→BUILD→GATED→LIVE-QUEUED→LIVE-VERIFIED→PUSHED→LANDED"
echo "     Keep needs: current. Checkpoint every ~90m (DONE/NEXT/BLOCKED/NEEDS-HIM)."
echo ""
echo "Board: .jarvis/gauntlet/BOARD.md · Status: .jarvis/bin/gauntlet status"
echo "════════════════════════════════════════════════════════════════════════"
exit 0
