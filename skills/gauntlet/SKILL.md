---
name: gauntlet
description: Running several assistant sessions in parallel across shared repos — fronts, worktree locks, the Infinity Stones, cross-front coordination, timing and status, and the Collect. Use when work splits into independent initiatives, before opening a gauntlet, and when a parallel run feels uncoordinated or opaque.
---

# 🧤 The Gauntlet

**Several sessions. Own worktrees. One stack. One board.**

Ordinary practice — not an emergency, no ceremony, no special powers. The fleet is
fully available throughout. *(Charter law 19.)*

> Proven in **GAUNTLET-00** — 3 fronts, 3 repos, 6 worktrees, ~44 commits, 2 fronts
> landed end-to-end in a day, **zero collisions**. Everything below that reads like a
> rule was paid for by an incident in that run. The full after-action, with the
> numbers and the failures, is in **`EXPERIENCE.md`** beside this file. Read it before
> your first gauntlet.

---

## 1 · When to open one

Open a gauntlet when work splits into **genuinely independent initiatives** — different
subsystems, different files, no shared dependency chain.

**Do not** open one to parallelise *steps of one thing*. Stages of a single chain are a
pipeline, not a gauntlet: the second front will sit blocked on the first, and you will
have paid all the coordination cost for none of the parallelism.

Sizing: fronts should be **disjoint in territory** and **comparable in weight**. A front
that finishes in an hour makes the Collect cheap; a front that sprawls makes it expensive.

---

## 1b · The cast — and how many fronts

**The number of fronts is not fixed.** You draw as many as the work splits into.

### Who's who

| | who | holds |
|---|---|---|
| 👤 | **The principal** | 🟣 POWER, permanently. **Never a front name.** |
| 🤖 | **The assistant** | Every front *is* the assistant, in a role |
| 🔧 | **The fleet** — DUM-E · U · JOCASTA · FRIDAY · EDITH · PEPPER · HAPPY | nothing — they work under a front's cover |
| 🦸 | **The fronts** | drawn from the roster below, N as needed |
| 👁 | **HEIMDALL** — the spectator | nothing. No front, no stone, no branch. Optional at 3+ |
| 🏛 | **THE COLLECTOR** | 🟡 MIND, at the Collect |

Clean separation: **the fleet are the workshop's staff; the fronts are who gets deployed.**

> ⚠ **Never name a front after the principal.** GAUNTLET-00 ran a front called `STARK`
> while the principal is Mr. Stark — the board read *"stark holds the token"* all day.
> Retired.

### Fronts are N — and they are named when summoned

**There is no standing cast.** A gauntlet opens with however many fronts the work splits
into, and each is **named at the moment it is summoned** — from the work in front of you,
not looked up from a registry. A name that fits today's theatre beats a name inherited
from a table.

What *is* declared at summon — and this is what actually schedules the run:

| field | why it exists |
|---|---|
| **name** | so the board, the branch and the brief can refer to it |
| **character** — one line | what kind of front this is |
| **🔴 appetite** — none · short burst · heavy | predicts contention *before* any work starts |
| **span** — 1 repo · N repos · read-only | tells the Collect how expensive this front will be |
| **territory** | the directories it claims, so the other fronts can see them |

**Character is declared as data, never baked into the name.** GAUNTLET-00 proved character
is a real scheduling primitive — "short burst, take it late" and "static gates most of the
day" both held exactly as written. That value comes from *declaring* the character, not
from owning a permanent name.

**A naming pool, if one doesn't suggest itself** — suggestions only, never a registry:
⚡ THOR (one target, lands hard) · 🌀 STRANGE (deep surgery, most iteration) ·
💫 CAPTAIN MARVEL (autonomous, no live stack) · 🎯 HAWKEYE (precision sweep) ·
🔮 VISION (read and reason) · 💥 HULK (big mechanical transformation).
Or name it after the theatre — `hotels`, `onboarding`, `trips`. Both are fine.

Two hard rules on names:

1. **Never the principal's name.** GAUNTLET-00 ran a front called `STARK` while the
   principal is Mr. Stark — the board read *"stark holds the token"* all day.
2. **One name per front across every repo it touches** (charter law 3a).

### How a front is actually raised — on his ask, never before

**Nothing is pre-assigned.** Opening a gauntlet means arming the machinery and leaving
the board *empty*. A front comes into existence the moment the principal names one —
not when you think the work splits, and never by a session choosing its own target.

*(Paid for on GAUNTLET-01 day one: the assistant pre-seeded three fronts with work
lifted from the principal's own tracker. He struck all of it — "everything you enter is
already done, it's not today's job." Reading his commitments is not the same as being
given one.)*

The whole ceremony is one command, from **any** session — one he just opened, or one
that has been running for hours:

```bash
.jarvis/bin/gauntlet enlist <name> "<character>" <none|burst|heavy> "<territory>" [session-id]
```

It raises the front if it is new, seats the caller, and writes the cold-boot brief. Two
hooks keep every session's identity true without him ever briefing one:

| when | hook | what it does |
|---|---|---|
| a **new** session starts | `SessionStart` | takes a free seat if one waits; else *"unseated — awaiting his ask"* **with the enlist line, session id filled in** |
| **every prompt**, all sessions | `UserPromptSubmit` | re-states who this session is, or how to enlist |

Two hooks and not one, because each covers what the other cannot: `SessionStart` fires
once and misses every session that was already running; `UserPromptSubmit` fires forever
and is what makes a running session summonable and a **compacted** one self-healing.

Seats are exclusive and claimed **atomically** (`set -C` noclobber, keyed on
`session_id`), so simultaneous starts cannot double-book one front. An occupied seat is
never silently taken over — freeing it is a deliberate `unbind`.

### How many?

**The binding constraint is the principal's attention, not the machinery.** In GAUNTLET-00
he personally issued rulings to all three fronts, ran manual passes for two, and answered
scope questions for a third. Three already consumed him.

| fronts | needs |
|---|---|
| **2–3** | the board and 🔴 are enough |
| **4–6** | 🔵 SPACE minted (parallel stacks), HEIMDALL watching, checkpoints enforced, NEEDS-PRINCIPAL queue live |
| **7+** | don't — the Collect cost and his review queue dominate the gains |

What raises the ceiling is **not** more worktrees. It's the things that protect his
attention: the NEEDS-PRINCIPAL queue, checkpoints, and an independent verifier inside each
front so defects stop reaching him at all.

---

## 2 · The front — a commander with a fleet

**This is the defining property, and the one GAUNTLET-00 got wrong.**

A front is the assistant, in that theatre, **with the full workshop team behind it.**
It plans, it rules, it reports to the principal. **It does not do all the typing, and it
is never the only thing grading its own work.**

| role | who | in a front |
|---|---|---|
| recon, inventory, "where does X live" | **DUM-E** · **U** · **JOCASTA** | always — read-only agents can violate nothing |
| build a locked slice | **FRIDAY** | pinned to the front's worktree, one slice at a time, never touches services |
| refute a claim, live e2e | **EDITH** | needs the 🔴 Reality Stone (she drives the running stack) |
| customer-eyes pass | **PEPPER** | needs 🔴 if she drives the app |
| services up/down, ports, env | **HAPPY** | needs 🔴 |

**The rule that makes this safe:** the fleet is gated on **the stones**, never by a
blanket ban. Read-only agents are ungated because they cannot touch either invariant.
Builders are ungated but confined to the front's own worktree. Only the agents that
*drive the running stack* need a stone — which is exactly what the stone is for.

> ⚠ **Anti-pattern, from GAUNTLET-00:** benching the fleet turned every front into a
> soloist. It cost independent verification (the builder trusted its own gate and shipped
> a false pass) and it cost visibility (one undifferentiated voice per log — the principal
> could not tell what was swept, what was built, or by whom). See `EXPERIENCE.md` §3.9.

**Logs name the actor.** *"DUM-E swept X · FRIDAY built Y · EDITH refuted Z."* The
handoffs must be visible without the principal having to ask who did what.

---

## 3 · Territory — the branch is the lock

One **worktree per front per repo**, cut from the declared baseline with an **absolute**
path:

```bash
git -C <repo> worktree add /abs/path/wt/<front>-<repo> -b <branch> origin/<devline>
```

- **One branch NAME across every repo the front touches** (charter law 3a).
- **Main trees stay baseline.** Nobody edits them, nobody checks out in them.
- **Git enforces the territory, not discipline.** It refuses one branch in two worktrees,
  so a collision fails at `worktree add` — before a file is touched. This is the single
  best mechanic in the protocol: it converts a social rule into a mechanical one.

**A worktree carries tracked files only.** `.env`, `node_modules` and `dist` do not come
with it — **symlink them, don't copy** (one source of truth, no stale secrets). And the
**stash, reflog and refs are shared** across worktrees: never `git stash pop` bare.

---

## 4 · The Infinity Stones

Exclusive resources, one bearer each, **taken on a lease with an intent and an ETA.**

| stone | grants | scope |
|---|---|---|
| 🔴 **REALITY** | Start/restart services · claim a **LIVE** result | one per stack |
| 🟢 **TIME** | The migration head — migrations are parented history, two heads is a broken timeline | one per repo |
| 🟡 **MIND** | Write the shared records (tracker · ledger · memory) | the **Collector**, once, at the Collect |
| 🟣 **POWER** | **Push.** The principal's, permanently — asked freshly every time (law 3) | never delegated |
| 🔵 **SPACE** | Own a port profile | *reserved* — mint when parallel stacks land |
| 🟠 **SOUL** | The production green-signal | *reserved* |

**No stone → static gates only, then queue.** A front without 🔴 is not blocked; it is a
front whose claims are correctly scoped. That belief is what makes parallelism possible.

**Leases, not indefinite holds.** Take with an intent and a duration; release on report of
done. *(GAUNTLET-00: 🔴 was held 5h17m by a front that had already finished, with two
fronts static-gated behind it. Nothing prompted a release.)*

---

## 5 · Coordination — fronts cannot talk

They coordinate through **the board**, and only through the board. Three lanes it must
carry, beyond the front list:

**① Cross-front findings — with an owner column.** A front that finds a defect outside its
territory **reports, never touches** — but the finding needs somewhere to go. *(GAUNTLET-00
orphaned eight of these, including a dead IP step in the currency chain affecting every
anonymous visitor. All correctly parked; none routed.)*

| finding | found by | owner | status |
|---|---|---|---|

**② The shared-surface register.** When a front touches a file outside its own subtree — a
shared UI component, a common util — it declares it here so the Collect knows where the
real conflict risk is. Territory is disjoint by directory; shared files are the exception
that needs naming.

**③ NEEDS-PRINCIPAL — one queue, oldest first.** Everything blocked on a ruling, a push,
or a manual pass, across all fronts. **This is the highest-value thing on the board for
him.** *(GAUNTLET-00: one front sat blocked on a scope ruling for hours while another
waited on a "go" — both invisible unless you read the whole file.)*

---

## 6 · Timing and status

**With one session, the principal *is* the status — they just read the chat. With several,
they are blind, and the board becomes their only eyes.** So the board's honesty is not
housekeeping; it is the whole interface.

In GAUNTLET-00 the board lied. Three ways:

| what went wrong | evidence |
|---|---|
| **Status said things that weren't true** | Board read *"awaiting his PR"* for a front already merged, and *"unpushed, nothing sent to dev"* for one merged **and deployed to test**. Free text is written once and never revisited. |
| **No way to tell if a front was alive** | No timestamps anywhere. Establishing whether a front was working or dead meant stat-ing file mtimes by hand. |
| **Work blocked on the principal was invisible** | One front sat on a scope ruling for hours, another on a "go" — both buried inside long logs. Nothing said *"two fronts are stuck on you."* |

**A stale status is worse than no status**, because decisions get made on it.

### The board answers three questions. Nothing else.

```
FRONT            WHERE?           ALIVE?          NEEDS YOU?
thor             LIVE-VERIFIED    4m ago          —
strange          BUILD            12m ago         —
captain-marvel   GATED            71m ago  ⚠      ruling on country list (2h)
```

**① WHERE? — one word from a fixed list, never a sentence.**

```
RECON → DESIGN → BUILD → GATED → LIVE-QUEUED → LIVE-VERIFIED → PUSHED → LANDED
                          │            │              │
                       (TESTED)   (needs 🔴)   (PRINCIPAL-VERIFIED)
```

The vocabulary is the evidence ladder (`skills/verify-live/`) — nothing new to learn, and
a phase cannot claim more than the evidence earns.

**② ALIVE? — when the front last wrote anything.** Flag `⚠ STALE` past 30 minutes.

**③ NEEDS YOU? — the only column that costs the principal time.** Every front's blockers,
oldest first, on one screen. This is the highest-value line on the board.

### Why a fixed word beats a sentence

**Honesty can only be automated on a fixed vocabulary.**

A known phase can be checked against git: *phase says `BUILD`, branch is merged → this
board is lying.* The board catches its own staleness. Prose cannot be checked — which is
exactly why *"awaiting his PR"* sat there wrong for a full day.

### The beat that refreshes them

Fronts cannot talk, so don't attempt continuous sync. Every **~90 minutes** each front
appends four lines — which is also where cross-front findings get routed to §5's lanes:

```
CHECKPOINT 14:30
  DONE      S3 coverage fix, gates green
  NEXT      S4 — itinerary placement
  BLOCKED   nothing
  NEEDS-HIM ruling on the country list (asked 11:05)
```

Three checkpoints read in thirty seconds, instead of three enormous logs.

### Cost

Near zero, which is the point. **ALIVE** is a file mtime we already have and never read.
**WHERE** is one word validated against a list. **NEEDS YOU** is one line the status
command greps.

### Reserve — real, but secondary

- **Stone leases with a clock** (§4) — fixes the five-hour hold that nothing prompted a
  release from.
- **A Collect time declared at open** (§8) — a clock stops fronts sprawling. GAUNTLET-00
  declared none, and the Collect was still owed ten hours later.
- **HEIMDALL at 3+ fronts** (§1b) — a session whose actual job is noticing the board has
  drifted from reality. In GAUNTLET-00 it caught two fronts already merged, a main tree
  off baseline, a stale pid file and a dead agent port. **No front could see any of it.**

---

## 7 · Gate integrity — before trusting any green

**A gate that reports green while doing nothing is the worst failure mode in this
protocol**, because all parallelism rests on "static gates are enough."

Before a front's first claim, prove each gate **runs and can fail**:

- **Capture the tool's OWN exit code.** Never pipe a gate through `grep` — you get grep's
  status. *(A fresh worktree has no `node_modules`, so `npm run build` exits 127; piped
  through grep, 127 read as success.)*
- Establish **baseline parity** first: lint/typecheck the base, then the branch, and prove
  the delta is zero — mapping findings onto diff lines if the totals are noisy.

---

## 8 · The Collect

1. Integration branch per repo.
2. Land fronts in a **declared order**.
3. **Rebase, not merge.**
4. **Re-run gates after EACH landing** — so you know which front broke it.
5. Expect a rebase round: dev lines move during the day, and fronts will be behind.
6. One push per repo, **on the principal's fresh word** (🟣 never delegates).
7. The **Collector** holds 🟡 MIND and writes tracker + ledger + memory **once**.

**Baselines drift within hours.** Either re-announce on the board when a dev line moves,
or require each front to declare and re-verify its actual base. GAUNTLET-00 had three
fronts standing on three different bases in the same two repos by mid-morning.

---

## 9 · The laws this practice earned

Thirteen, each paid for by a named incident — the full table with its evidence is in
`EXPERIENCE.md` §4. The two that matter most:

- **L13 · The builder is never the only verifier.** If that separation is suspended, the
  claim must say so.
- **L1 · Capture the tool's own exit code.** A silently-inert gate invalidates everything
  downstream of it.
