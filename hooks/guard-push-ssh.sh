#!/bin/bash
# PreToolUse(Bash) — charter law 17 + law 3. The one-shot push gate.
#
# THE POLICY:
#   · Every ordinary command runs with NO prompt.
#   · A feature-branch push runs ONLY against a fresh one-shot grant, opened on
#     the principal's ask and CONSUMED by that single push. No grant → refused.
#   · Mainline pushes, force-pushes and sudo are hard-denied. A grant NEVER
#     clears them.
#   · Remote shells are refused (no grant path; the principal runs them).
#
# WHY A HOOK, NOT PERMISSION RULES:
#   `allow: ["Bash"]` keeps the day promptless, but it OUTRANKS every `ask` — from
#   rules AND from hooks (measured twice, 5 Aug 2026). Rules are prefix matches too,
#   so `Bash(git push:*)` cannot match `git -C <path> push`. A hook sees the whole
#   string and its deny is honoured unconditionally.
#
# THE BARE-PUSH HOLE (found live, 5 Aug — the most dangerous bug in this gate):
#   `git push` with no refspec targets the CURRENT branch's upstream. The branch
#   name never appears in the command, so text matching cannot see it — a bare push
#   from a `development`-tracking tree sailed through. Fix: when no explicit refspec
#   is given, RESOLVE the real target from the repo (HEAD + @{u}) and judge that.
#   Resolution failure is treated as mainline: refuse rather than guess.
#
# PORTABILITY: nothing here is project-bound. The grant token and the audit log
#   live under the workroom (`<root>/.jarvis/run/`), and the root is resolved from
#   CLAUDE_PROJECT_DIR, falling back to two levels up from this hook file.

set -e
INPUT=$(cat)

# Workspace root: the harness sets CLAUDE_PROJECT_DIR; otherwise this hook lives
# at <root>/.claude/hooks/, so two levels up is the root.
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"

# The gate is written in python3 (no third-party imports). If python3 is missing the
# gate cannot evaluate anything — so it must FAIL CLOSED on the commands that leave
# this machine, never fail open. Everything else still runs untouched.
if ! command -v python3 >/dev/null 2>&1; then
  case "$INPUT" in
    *push*|*ssh*|*scp*|*sftp*|*rsync*|*sudo*)
      printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"GATE UNAVAILABLE — python3 is not installed, so the law 17 push gate cannot evaluate this command. Refusing rather than guessing. Install python3, or have the principal run this command."}}'
      ;;
  esac
  exit 0
fi

python3 - "$INPUT" "$ROOT" <<'PY'
import json, os, re, shlex, subprocess, sys, time

ROOT    = sys.argv[2] if len(sys.argv) > 2 else os.getcwd()
GRANT   = os.path.join(ROOT, ".jarvis", "run", "PUSH_GRANT")
PUSHLOG = os.path.join(ROOT, ".jarvis", "run", "push-log")
CLI     = os.path.join(ROOT, ".jarvis", "bin", "gauntlet")
TTL     = 600
MAINLINE = {"main", "master", "dev", "development", "trunk", "release", "prod", "production"}

try:
    payload = json.loads(sys.argv[1])
    cmd = payload.get("tool_input", {}).get("command", "") or ""
except Exception:
    sys.exit(0)

def out(decision, reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": reason}}))
    sys.exit(0)

SEP = r'(?:^|[;&|(\n]|\$\()\s*'
ANY_PUSH = re.compile(SEP + r'git\s+(?:(?:-C|-c)\s+\S+\s+|--\S+(?:=\S+)?\s+)*push(?:\s|$)')
REMOTE   = re.compile(SEP + r'(?:ssh|scp|sftp|rsync)(?:\s|$)')
WRAPPED  = re.compile(SEP + r'(?:timeout\s+\S+|env(?:\s+\w+=\S+)+|nohup|nice(?:\s+-n\s*\S+)?'
                            r'|stdbuf\s+\S+|xargs(?:\s+-\S+)*|command|exec)\s+(?:ssh|scp|sftp|rsync)(?:\s|$)')
SUDO     = re.compile(SEP + r'sudo(?:\s|$)')

if SUDO.search(cmd):
    out("deny", "sudo is hard-denied by charter law 17.")

def push_segment(text):
    """The single statement containing the push."""
    m = ANY_PUSH.search(text)
    if not m:
        return ""
    start = m.start()
    end = len(text)
    for sep in (';', '&&', '||', '|', '\n'):
        i = text.find(sep, m.end())
        if i != -1:
            end = min(end, i)
    return text[start:end]

def target_dir(text, seg):
    """Where the push will actually run."""
    m = re.search(r'git\s+-C\s+(\S+|"[^"]*"|\'[^\']*\')', seg)
    if m:
        return m.group(1).strip('"\'')
    m = re.search(r'(?:^|[;&|(\n])\s*cd\s+(\S+|"[^"]*"|\'[^\']*\')', text)
    if m:
        return m.group(1).strip('"\'')
    return payload.get("cwd") or os.getcwd()

def git(d, *args):
    try:
        r = subprocess.run(["git", "-C", d, *args], capture_output=True, text=True, timeout=5)
        return r.stdout.strip() if r.returncode == 0 else ""
    except Exception:
        return ""

def explicit_refspecs(seg):
    """Non-flag args after `push`, minus the remote → the refspecs actually named."""
    try:
        toks = shlex.split(seg)
    except Exception:
        toks = seg.split()
    if "push" not in toks:
        return None
    rest = toks[toks.index("push") + 1:]
    VALUED = {"--repo", "-o", "--push-option", "--receive-pack", "--exec"}
    pos, skip = [], False
    for t in rest:
        if skip:
            skip = False; continue
        if t in VALUED:
            skip = True; continue
        if t.startswith("-"):
            continue
        pos.append(t)
    return pos[1:] if len(pos) >= 1 else []      # drop the remote

if ANY_PUSH.search(cmd):
    seg = push_segment(cmd)

    # ── hard denials that no grant can clear ──────────────────────────────────
    if re.search(r'--force(?:-with-lease)?(?:\s|$)|(?:^|\s)-f(?:\s|$)', seg):
        out("deny", "Force-push is hard-denied by law 17. A push grant does NOT clear this.")

    refspecs = explicit_refspecs(seg)

    if refspecs:
        # judge every named destination (handles src:dst and bare branch names)
        for rs in refspecs:
            dst = rs.split(":")[-1].lstrip("+")
            dst = re.sub(r'^refs/heads/', '', dst)
            if dst.lower() in MAINLINE:
                out("deny", f"Direct push to a mainline ('{dst}') is hard-denied "
                            f"(law 3: feature branches only). A push grant does NOT clear this.")
    else:
        # ── NO refspec → resolve the real target. This is the bare-push hole. ──
        d = target_dir(cmd, seg)
        head = git(d, "rev-parse", "--abbrev-ref", "HEAD")
        up   = git(d, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
        upbr = up.split("/", 1)[1] if "/" in up else ""
        if not head:
            out("deny",
                "PUSH REFUSED — this push names no branch, and the target repository "
                f"could not be resolved (looked in: {d}). Refusing rather than guessing: "
                "a bare push follows the current branch's upstream, which may be a "
                "mainline. Name the branch explicitly:  git push origin <feature-branch>")
        if head.lower() in MAINLINE or upbr.lower() in MAINLINE:
            out("deny",
                f"Direct push to a mainline is hard-denied (law 3). This push names no "
                f"branch, so it would follow HEAD → '{head}'"
                + (f" (upstream '{up}')" if up else "") +
                ". A push grant does NOT clear this. Push a feature branch instead.")

    # ── the one-shot grant ────────────────────────────────────────────────────
    if os.path.exists(GRANT):
        age = time.time() - os.path.getmtime(GRANT)
        try:
            reason = open(GRANT).read().strip() or "(no reason recorded)"
        except Exception:
            reason = "(unreadable)"
        os.remove(GRANT)                       # CONSUMED — one push, one grant
        if age <= TTL:
            try:
                os.makedirs(os.path.dirname(PUSHLOG), exist_ok=True)
                with open(PUSHLOG, "a") as f:
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | GRANTED ({int(age)}s old) "
                            f"| {reason} | {' '.join(cmd.split())[:300]}\n")
            except Exception:
                pass
            sys.exit(0)                        # silent → the blanket allow runs it
        out("deny", f"PUSH REFUSED — the grant was {int(age//60)}m old and grants expire "
                    f"after {TTL//60}m. It has been cleared. Ask the principal again.")

    out("deny",
        "PUSH REFUSED — law 3: the principal pushes, asked freshly every single time.\n"
        "No grant is open. If the principal has JUST asked for this push, open a "
        "one-shot grant and retry:\n"
        f"  {CLI} push-ok \"<what is being pushed and why>\"\n"
        "The grant covers ONE push, expires in 10 minutes, and is consumed on use. "
        "Mainline and force-pushes are refused even with a grant.")

if REMOTE.search(cmd) or WRAPPED.search(cmd):
    out("deny",
        "REMOTE SHELL REFUSED — law 17: entering another host is always asked for, "
        "and nothing can prompt while every command is allowed. Command:\n  "
        + cmd.strip())

# everything else → silent, so the blanket allow keeps the day promptless.
PY

exit 0
