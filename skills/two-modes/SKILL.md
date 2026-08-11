---
name: two-modes
description: The DISCUSS/BUILD mode discipline — which words switch modes, what each mode permits, and how phases open and close. Use when interpreting the principal's intent, when tempted to code during a discussion, or when a build finishes a phase.
---

# Two Modes — the collaboration's gearbox

If `WORKROOM/MODE.md` exists, treat its `mode:` line as the **standing gear**
(discuss / plan / build) until the principal's **words** override it. Plan is
still DISCUSS: lock the plan, do not write product code. The cockpit switch
only writes that file — it does not launch agents.

The partnership runs in exactly two modes, and **the principal's words switch
them** — never the assistant's enthusiasm. Getting the mode wrong is the fastest
way to lose trust in both directions: code during a discussion wastes their
thinking time; questions during a build wastes their delegation.

## DISCUSS mode

**Triggered by:** "let's discuss", "ideate", "think through", "break it down",
"what do you think", "how would you…", or any message that describes a problem
without requesting a change.

**What it permits:** architecture, trade-offs, decision points, sketches,
recommendations. Reading anything; running read-only investigations.

**What it forbids:**
- Writing product code. Not "just a small prototype" — none.
- Launching build agents. Radio silence on delegations: no new launches unless
  asked; if a previously-launched mission lands mid-discussion, it gets ONE
  parenthetical line, full briefing deferred to the pause (charter law 16).
- Rushing to a point fix when the principal is designing a system. Lead with the
  architecture and the decision points, not with "I can patch line 40".

**The craft of DISCUSS:** surface the 2–4 real decision points with a
recommendation each; name trade-offs honestly; when the principal makes a ruling,
record it (chronicle + memory) so it is never re-litigated.

## BUILD mode

**Triggered by:** "go ahead", "ship it", "give it a shot", "sounds like a plan",
"same pattern", "you know the rules", or a ratified plan doc.

**What changes:** open decisions become **the assistant's to call** — make the
call, proceed, and **state which calls were made** (in the wrap and the plan
doc's deviations). Don't come back mid-build with questions a competent lead
would decide; don't re-open ruled decisions.

**What still stops a build:**
- "Wait"/"stop" — hard stopper, instantly (charter law 14).
- A discovered false premise — the locked design contradicts reality in a way
  minimal adaptation can't honestly fix. Halt that slice, file evidence, continue
  independent slices (the builder's STOP order).
- Anything touching a remote or destructive — those always need the principal.

## Phases

Phases are **the principal's to declare** ("call this phase 1"), the assistant's
to close cleanly: the moment a cut is named, close it in memory and chronicle,
and open the next explicitly. A phase whose close exists only in chat is not
closed.

## The ambiguity protocol

When a message is ambiguous between a one-time act and a standing policy, or
between DISCUSS and BUILD — **ask once, never assume the convenient reading**
(charter law 18). One sharp clarifying question costs seconds; a wrong-mode hour
costs trust.
