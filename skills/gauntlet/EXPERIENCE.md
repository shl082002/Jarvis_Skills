---
name: gauntlet
description: After-action experience sheet from GAUNTLET-00 (4 Aug 2026) — what three parallel fronts produced, what the protocol got right, the thirteen laws it earned, and the structural miss the principal named. The operational doctrine is SKILL.md beside this file; this is the evidence behind it.
---

# 🧤 GAUNTLET-00 — Experience Sheet

**The first parallel run. Three fronts, three repos, one day.**
The doctrine this produced is in **`SKILL.md`** beside this file; charter law 19 is its
summary. **This file is the evidence** — every rule over there was paid for by an incident
in here.

> Written by the **spectator** session — no front, no stone, no commits, read-only
> throughout. That vantage is why this sheet exists: nobody inside a front could
> see all three.
>
> **Finding #0 — now closed.** When this sheet was written the practice existed only as a
> project-local helper, a local board and one memory file: it did **not** travel to a new
> project, and the kit's charter stopped at 18 laws. Closed the same day — **charter law
> 19**, `skills/gauntlet/`, and `commands/gauntlet.md` ship in the kit. Still owed: a board
> template, a front-brief template, and the renamed helper binary.

---

## 0 · The name and the stones — his rulings, 4 Aug 2026

### 0.1 · War is retired. The Gauntlet is the practice.

He ruled the practice will run **frequently** — and then, on the debrief, closed the
question: *"Stop calling this war from now. We will invest something new in future, but
now it's locked."*

So there is **one tier, not two.** Charter law 19 is **The Gauntlet**: ordinary practice,
no ceremony, no emergency powers, **fleet fully available**. The war framing — two-key
activation, dormancy, the benched fleet — is retired, not demoted. If an emergency tier is
ever wanted, it gets designed fresh.

**GAUNTLET-00 was the practice run under war rules**, and that is the whole explanation for
its one structural failure: emergency powers benched the fleet, and every front became a
soloist (§3.9). The mechanic was sound. The framing was the defect.

> **Vocabulary, locked 4 Aug:** *gauntlet* (the practice) · *front* (one parallel session)
> · *stones* (exclusive resources) · *the Collect* (landing). The word **war** is retired
> from the charter, the kit, the board, and the helper.

### 0.2 · The Infinity Stones — named exclusive resources

His ruling: *"token name is not matching with our workshop team — make it Infinity Stone."*
He was right, and the rename exposed something bigger. **We already had six exclusive
resources; four were unnamed rules nobody could see, and an unnamed rule has no bearer and
no enforcement.**

| stone | grants | bearer today |
|---|---|---|
| 🔴 **REALITY** | Start/restart services · claim a **LIVE** result. No stone → static gates only, then queue. | *(was: the stack token)* |
| 🟢 **TIME** | The alembic head, one per repo. Migrations are parented history — two heads is a broken timeline. | unclaimed |
| 🟡 **MIND** | Write the shared memory — TRACKER, git ledger, memory files. Held by the **Collector**, once, at the end. | unclaimed until the Collect |
| 🟣 **POWER** | **Push.** Permanently Mr. Stark's, asked freshly every time (rule 11). Never delegated, never contested. | **MR. STARK — never moves** |
| 🔵 **SPACE** | Own a port profile. | **reserved** — mint when parallel stacks land (§5 #3) |
| 🟠 **SOUL** | The prod green-signal. The one that costs. | **reserved** |

**Why the stack is REALITY, not SPACE:** the gate is not *where* you work — it is whether
you are permitted to say **what is actually true**. No stone, no live claim. That is the
Reality Stone precisely, and it is the same idea as law L13.

> ⚠ **Doctrine shipped, plumbing not yet.** The charter, this skill and the command carry
> the stone vocabulary. The live helper still says "stack token" — renaming the mechanism
> while a run is in flight would break it, so the binary, the board's stone table and the
> front-brief wording land at or after the Collect.

---

## 1 · Scoreboard — GAUNTLET-00

*Declared 4 Aug 2026 10:14, ran ~10 hours. Three fronts, three repos, six worktrees,
one Reality Stone, fleet benched.*

| front | character | repos | commits | landed? |
|---|---|---|---|---|
| ⚡ **THOR** | one target, short burst | shared-service + website | 4 + 7 | ✅ **merged both dev lines, deployed to test, builder run** |
| 🔴 **STARK** | deepest surgery | proxy + website | 8 + 18 | ✅ **merged both dev lines** |
| 💫 **CAPTAIN MARVEL** | autonomous, static gates | proxy + website | 1 + 6 | ⏳ built & gated, **unpushed, never opened in a browser** |

**~44 commits across 3 repos. Two fronts landed end-to-end in a single day.
Zero cross-front collisions. Zero migrations. Zero alembic head claims.**

Selected outcomes, all measured rather than asserted:

- **THOR** — 1,145 shadowed destinations → **0**; unreachable hotels **6,669 → 43**
  (the 43 are supplier records with no city name, not a code defect); sampled
  selectability **98.67% → 100%** (150/150); destination index 63,014 → **103,075**
  rows. A full census, not a sample: all **1,797,452** hotels tested.
- **STARK** — one `Journey` derivation replacing **four** independent degenerate-route
  sites; a trip-wide currency audit closing **15 sites across 3 fault classes**
  (including `"$"` used as a currency *code* and persisted onto saved options);
  derivation validated against **32 real bookings**, 32/32 correct.
- **CAPTAIN MARVEL** — all seven slices S0–S6, three step components deleted rather
  than ported, and **two live production bugs** found and closed en route (onboarding
  wrote `interests` where Settings read `experiences.interests`; onboarding wrote
  budget values that aren't valid `budget_tier` keys, so Settings showed "Not set").

---

## 2 · What the protocol got right — keep all of this

**① The branch is the lock, and it is enforced by git, not by discipline.**
Git refuses to check one branch out in two worktrees. So a territory violation fails
at `git worktree add` — *before a file is touched*. Three fronts, three repos, six
worktrees, ten hours, **zero collisions**. This is the single best mechanic in law 19:
it converts a social rule into a mechanical one. Discipline scales badly; `git` doesn't.

**② One branch name across every repo a front touches (rule 3a).**
THOR proved it under load — `sahil/hotel-coverage-superset` on both shared-service and
website. At Collect time the front is one grep, not a scavenger hunt.

**③ The board as the only channel.** Fronts could not talk to each other. They never
needed to. Every cross-front fact that mattered (baseline drift, a shared component,
a gate trap) reached the others through their own file plus the board helper.

**④ Static gates as the default currency of proof.** CAPTAIN MARVEL built seven slices
without the Reality Stone and without ever opening a browser, and its work is still
shippable. **A front that cannot verify live is not a blocked front** — it's a front
whose claims are correctly scoped. That belief is what made three-way parallelism
possible at all.

**⑤ Front *character* is a real scheduling primitive.** "One target, short burst" /
"deepest surgery, stone-hungry" / "farthest out, autonomous" predicted the day's
contention accurately before any work started. Assigning character up front is worth
more than assigning priority.

**⑥ Append-only, front-owned logs.** Every front logged its own errors, in its own
words, at the moment it found them. **This sheet is only possible because they did.**
No retrospective interview would have recovered a quarter of it.

---

## 3 · What it cost — fix before scaling

### 3.1 · The Reality Stone became a scheduling bottleneck, not a safety device

THOR held it **10:41 → 15:58, five hours seventeen minutes**, against its own brief
which says *"take the token in one short burst near the end, not held all day."*
For most of that window two fronts were static-gated behind it.

At three fronts that's a tax. At six it's fatal — the serialized live-verification
lane becomes the whole critical path. The **"SERIALIZE today, no second port profile"**
ruling was correct for day one (don't multiply unknowns while the protocol itself is
unproven) but it will not survive scale.

> **Scale fix:** the token needs a *lease with an expiry* and a *visible queue*, or
> per-front port profiles. Also worth noting the holder had already finished — the
> token stayed held after the work stopped, because nothing prompts a release.

### 3.2 · Baselines drifted within hours, and three fronts stood on three different ones

The board cut baselines at 10:14. By the time STARK cut worktrees, `origin/dev` had
already moved `0ed96a7e → 6145a3e8` and `development` `1688d54 → 7e91d65`.
CAPTAIN MARVEL cut off the *board's* baselines; STARK off the *newer* tips; THOR's
website off `70adb4c3`. Same repos, three bases.

Then at push time STARK found both its branches **behind** their dev lines (proxy 3,
website 9) — the wider team had merged all day.

STARK did the right thing: recorded its actual per-front base and said so. But the
board table was stale within the hour and stayed stale.

> **Scale fix:** either re-cut and re-announce the baseline on the board when it moves,
> or make "declare your actual base" a required field per front. And make **a rebase
> round an explicit pre-Collect phase**, not a surprise.

### 3.3 · Worktrees isolate the working tree — and *nothing else*

Three independent incidents, all from the same misconception:

- **The stash stack is shared.** STARK's unquoted `$FILES` made `git stash push -- <paths>`
  fail; the bare `git stash pop` that followed applied an unrelated **May 2026 stash**
  into the worktree — 10 conflicted files that were not its own. Recovered fully, and
  the May stash was never dropped. Worktrees share the stash, the reflog, and refs.
- **`.env` is untracked, so it does not come with a worktree.** Hit **twice**
  independently (THOR on the shared-service compose build, again on the website vite).
  Both times copied in. STARK later **symlinked** instead — one source of truth, no
  stale secrets, no drift. Symlink is the better pattern.
- **`node_modules` is absent in a fresh worktree** — see 3.4, because that one is worse.

### 3.4 · ⚠ The most dangerous failure of the run: a gate that reports green while doing nothing

A fresh worktree has no `node_modules`, so `npm run build` exits **127**
(`tsc: command not found`). Piped through `grep`, the shell hands you **grep's** exit
code — **so 127 read as success.** THOR caught it, called it "a false pass," fixed it
by symlinking `node_modules` and capturing `tsc`'s own exit code, and **warned both
other fronts on the board** because both had queued website passes.

This class deserves its own name. Everything else in this run was a wrong answer;
this was a *confident answer from a gate that never ran*. In a protocol whose entire
parallelism rests on "static gates are enough," a silently-inert gate is the one bug
that can invalidate a whole day's claims.

> **Scale fix:** a **gate-integrity preflight** per worktree — prove each gate actually
> runs (capture its own exit code, and confirm it can *fail*) before trusting any green.

### 3.5 · "Verified" has layers, and all three fronts conflated two of them at least once

- **STARK:** *"the API returns it"* and *"the component receives it"* are two different
  claims. It verified the first and asserted the second. `mapItemToUI` rebuilt every row
  from an explicit whitelist, dropping the `leg_*` fields **after** the API sent them
  correctly and **before** the card could read them.
- **STARK:** the 32-booking real-data pass validated the **derivation**, but every one of
  those bookings sat *inside* its trip window — so the placement path was never exercised
  at a boundary. His own live booking then broke exactly there. **Breadth ≠ boundary.**
- **THOR:** `vite --port 5173` with no `--host` binds **IPv6 only**. `localhost` returned
  200; `127.0.0.1` returned **connection refused**. Every check passed and a bookmarked
  `127.0.0.1` reached nothing.
- **THOR:** *"I can't see any changes on local website"* — the code was correct throughout,
  proved by fetching the transformed modules straight off the dev server. Two serving-side
  causes: an orphaned HMR socket (the tab kept rendering the bundle it already had) and a
  vite restart triggered by an `.env` write. **A dropped HMR socket does not reload the page.**

### 3.6 · Eight self-initiated retractions — and that is the *good* news

THOR's first Paris hypothesis: wrong. Its second diagnosis: incomplete — the real bug was
30× bigger. Its own QA harness: two bugs found in it before any number was trusted. Its
headline metric: wrong (a difference of two *counts* is not a *set* difference — understated
the loss ~4×), corrected mid-QA, with the old figure explicitly retracted as
*"should not be quoted."* STARK's stale-bundle theory: wrong, and said so. CAPTAIN MARVEL's
"three competing vocabularies": wrong, doc marked **SUPERSEDED**; and its own PCR §3
corrected mid-build before it could break a working Settings surface.

Every one of these was self-initiated and logged in the front's own words. **This is the
protocol's quietest and largest win.** It happens because the log is append-only and
front-owned: there is no way to quietly overwrite yesterday's claim, so the cheap move
becomes correcting it out loud.

### 3.7 · The human pass is a verification layer, not a rubber stamp

Mr. Stark's manual testing found **eight defects that every gate had passed**:

1. A real BOM ⇄ DXB return rendered as one row — a date-window bug no static gate and no
   32-booking sweep caught.
2. Item ① applied to the wrong element — the bottom summary instead of the top line he
   actually reads. *"Exactly inverted, so from his seat NOTHING had changed."*
3. Item ③ reversed outright: ratings **are** multi-select; the control was lying. Root
   cause of the whole exchange — four groups drew a `rounded-full` box, and a circle means
   "pick exactly one."
4. A sort dropdown hanging outside its card (a front's own regression).
5. The notes 404 — storage detail refusing his action.
6. "Transfer London → Mumbai" — intercity legs graded as needing ground transport.
7. A bold button inserting the literal text `*bold*`.
8. "I can't see any changes" — which turned out to be serving, and exposed 3.5's IPv6 bug.

> **Scale fix:** schedule the human pass as a **phase with a slot**, not as whatever
> happens after a front says done. It has the highest defect-yield per minute of any
> gate we ran.
>
> ⚠ **But read this list as a symptom, not a trophy — see §3.9.** Eight defects reached
> him because, with the fleet benched, **his pass was the only independent verification in
> the run.** Every front graded its own work. Restore an independent verifier and most of
> this list never reaches his desk.

### 3.8 · Cross-front findings had nowhere to go

Eight real findings were parked correctly by fronts that had no business fixing them —
and no lane to route them to:

| finding | found by | owner |
|---|---|---|
| **IP step of the currency chain is dead** — the vendor stopped returning a `currency` object, and `detect_ip_currency` drops the *entire* hit, so every anonymous visitor falls through to USD | THOR | proxy — **unassigned** |
| `vitest` imported by 10+ `.test.ts` files but never installed — those tests cannot run at all | CAPTAIN MARVEL | repo-wide |
| `OAUTH_REDIRECT_BASE_URL` points at production while `ENV=development` | STARK | env |
| Visa fee's USD is declared by *our* schema, not the provider; `estimatedCost` carries no currency at all | STARK | product ruling |
| TripOverview/TripAnalysis run a *private* currency ladder bypassing the shared hook | STARK | own slice |
| Dropdown renders lowercase `paris` / `london` — fix at the data layer per house law | THOR | data |
| Nearby chips ordered by `hotel_count` while displaying **distance** | THOR | own slice |
| Resume block reads state assigned inside a `setForm` updater — may already be a no-op | CAPTAIN MARVEL | react |

The discipline was right (report, don't touch). The board just has no **CROSS-FRONT
FINDINGS** table with an owner column, so eight findings live only inside three front
files that get archived.

### 3.9 · ★ THE HEADLINE FINDING — emergency powers replaced the fleet, and nobody noticed until he said so

**This is his verdict, in his words:** *"Each frontier Jarvis and his fleet collaboration
was not good. I never see how I used to see Jarvis hand the task to FRIDAY — it was not
happening. Looking like frontier doing heavy lifting, or Jarvis you did it, whatever the
case might be."*

He is right, and the first draft of this sheet got it wrong — it filed the benched fleet
at **#6 of 8, as a throughput cost.** It is not a throughput cost. It is a **correctness
and visibility** cost, and it is the single most important thing to fix before GAUNTLET-01.

**What actually happened: each front became a soloist.** One session did recon, design,
build, its own QA, its own service ops, and then **graded its own work.** That is precisely
the shape the fleet exists to prevent. Two consequences, both already documented above
without being connected:

**① It destroyed independent verification.** §3.7 records eight defects his manual pass
found that every gate had passed. That is not a compliment to his testing — it is the
*symptom*. Under the normal model EDITH verifies what FRIDAY built: an adversary who does
not trust the builder's gate. Benched, every front verified itself, and **his manual pass
became the only independent verification in the entire run.** The two worst findings of
GAUNTLET-00 are exactly the class a self-verifier structurally cannot catch:

- the `127`-reads-as-success false pass (§3.4) — the builder trusted its own gate;
- *"the API returns it"* asserted as *"the component receives it"* (§3.5) — the builder
  verified the half it had just written.

**② It destroyed role visibility.** Every log entry in all three front files is written in
one undifferentiated voice. There is no way, reading them, to tell what was swept, what was
built, and what was verified — or by whom. He could not see the handoffs because there were
no handoffs, and the logs could not show him the difference.

**Why the bench was still right at 10:14.** A subagent that starts a service or writes into
the wrong tree breaks the two core invariants, and those mechanics were unproven when
the run opened. Benching was a sound day-one safety margin. **The error was that it was
blanket when it should have been targeted.**

**The fix — bench by capability, not by blanket.** The protocol protects exactly two
things: the **stack token** and the **worktree boundary**. Gate the fleet on those, and
nothing else:

| fleet | gated? | why |
|---|---|---|
| **DUM-E · U · JOCASTA** (read-only) | **never benched** | Cannot violate either invariant. THOR's Paris root-cause, STARK's four-degenerate-site hunt, CM's onboarding inventory were all classic DUM-E work done by hand. |
| **FRIDAY** (build) | **allowed**, pinned to the front's worktree, one slice at a time, forbidden to touch services | CM's S0–S6 is literally her interface: design doc + slice list + base branch. |
| **EDITH · PEPPER · HAPPY** (live) | **allowed only while the front holds the token** | The token already exists to serialize live access — extend it to gate the fleet instead of banning them. |

**And make the logs name the actor.** *"DUM-E swept X · FRIDAY built Y · EDITH refuted Z"* —
so the handoffs are visible from his seat without him having to ask who did what.

**The deeper principle, stated once:** a front is a **commander with a fleet**, not a
soloist. It plans, it rules, it reports. It should not be doing all the typing — and it
should never be the only thing grading its own work.

### 3.10 · A front was named after the principal

The board carried a front called `STARK` while the principal is **Mr. Stark**. All day the
status line read *"stark holds the token"*, and the helper took `take stark`. Nothing broke,
but the ambiguity was live for ten hours in the one artifact whose entire job is to be
unambiguous.

Fixed in doctrine: **never name a front after the principal.** `STARK` is retired from the
roster; the deep-surgery archetype is now **STRANGE** — the surgeon, which is what that
front actually is.

Related: the three front names were invented for this run. **Names should be roles that
persist**, so a cold-boot brief is written once and reused, with only the Task section
changing. That is now the roster (`SKILL.md` §1b), and it scales to whatever N the work
splits into.

### 3.11 · The baseline trees were supposed to be untouchable, and one moved

The board helper closed the day flagging `concierge-website` main tree on
`sahil/cello-mobile-link`, **1 dirty** — off baseline. The board's premise is that main
trees *are* the baseline and nobody edits them. Nothing broke, but the guard is only a
yellow line in a status command nobody is required to read.

---

## 4 · The thirteen laws this run earned

Each one is paid for by a specific incident above. These are the portable part.

| # | law | paid for by |
|---|---|---|
| **L1** | **Capture the tool's OWN exit code.** Never pipe a gate through `grep` — you get grep's status. | 127 read as success |
| **L2** | **Never bare `git stash pop` in a multi-worktree repo.** Name the stash or don't stash. | the May 2026 stash |
| **L3** | **A worktree carries tracked files only.** `.env`, `node_modules`, `dist` do not come with it — **symlink, don't copy.** | 3 separate hits |
| **L4** | **Absolute paths for `git worktree add`.** A relative path lands the worktree *inside* the repo. | one misplaced worktree |
| **L5** | **"The API returns it" and "the component receives it" are two claims.** Verify both. | the whitelist trap |
| **L6** | **Breadth is not boundary.** A large real-data sweep can miss every edge case. | 32/32 correct, still broke |
| **L7** | **Bind dual-stack.** A 200 on `localhost` does not mean `127.0.0.1` answers. | IPv6-only vite |
| **L8** | **"I can't see the change" is a *serving* question before it's a code question.** Prove the module off the dev server before touching source. | orphaned HMR socket, twice |
| **L9** | **Locate an element by where it RENDERS, not by what it reads like** — and grep the exact string he quoted. | the inverted item ① |
| **L10** | **Prove dev-only code is absent from `dist/`.** "It's gated on DEV" is a claim; grep the bundle. | `?builtFor=` — done right |
| **L11** | **A retraction is cheapest the moment it's made.** Log the wrong hypothesis; never quietly replace it. | eight retractions |
| **L12** | **A difference of two counts is not a set difference.** | the 4× understated metric |
| **L13** | **★ The builder is never the only verifier.** A session that graded its own work shipped a false pass and an unchecked assertion; the human became the sole independent check. Separate the hands that build from the hands that refute — and if that separation is suspended, say so in the claim. | §3.9, his verdict |

---

## 5 · The scale delta — what changes at six-plus fronts

Ranked by what breaks first. **#1 is his verdict and it outranks everything else here.**

1. **★ Un-bench the fleet by capability — a front is a commander, not a soloist (§3.9).**
   Read-only agents never benched · FRIDAY builds inside the front's worktree · live agents
   gated on the stack token. **And the builder is never the only verifier.** Logs name the
   actor so the handoffs are visible. Everything below is secondary to this.
2. **Gate-integrity preflight, mandatory, per worktree.** Nothing else matters if a green
   gate can be inert. Prove each gate runs *and can fail* before the front's first claim.
3. **REALITY STONE → lease + queue, and mint SPACE.** Five hours held by a finished front
   is the day's largest throughput tax and it grows linearly with front count. Add an
   expiry, a visible queue, and a release prompt when a front reports done. Then revisit
   the "no second port profile" ruling — right for GAUNTLET-00, wrong for the next one;
   when parallel stacks land, **the Space Stone comes off the reserved list** and Reality
   stops being a single global lock. *(Note: fixing #1 makes this worse before better —
   more agents want live access. Sequence #1 and #3 together.)*
4. **Baseline as a living row, not a morning snapshot.** Re-announce on drift, or require
   each front to declare and re-verify its actual base. Make the rebase round an explicit
   pre-Collect phase.
5. **A CROSS-FRONT FINDINGS table on the board, with an owner column.** Eight orphans in
   one day at three fronts; that's roughly one per front-hour of deep work.
6. **The human pass gets a scheduled slot** — as the *last* line of defence, not the only
   one. Its yield should drop once #1 lands; if it doesn't, #1 didn't work.
7. **A baseline-tree guard that's harder than a yellow line.**
8. **Ship law 19 in the portable kit.** ✅ **DONE 4 Aug** — `skills/gauntlet/` (SKILL.md +
   this sheet), `commands/gauntlet.md`, and charter law 19. Still owed: a board template,
   a front-brief template, and the renamed helper.

---

## 6 · Honest close — won, not closed

- **THOR** — merged into `origin/development` *and* `origin/dev`, deployed to test, index
  builder run, **green-signalled for prod** with a stated two-stage caveat (ship code,
  then snapshot `tj_destinations` and run the builder; rollback is the existing
  `tj_destinations_bak_20260804`).
- **STARK** — merged into `origin/development` and `origin/dev`.
- **CAPTAIN MARVEL** — 7 slices built and gated, unpushed, unmerged, never opened in a
  browser. **Not a loose end — his ruling:** *"Captain Marvel's work will extend to
  non-war zone; he is protecting the back, so it's not critical. We can finish it after
  the war ends too."* Rear-guard by design. It carries out of the run and closes on
  ordinary charter, with a live pass still owed.

**Still owed, by rule 19: the Collect.** TRACKER, the git ledger, and memory are written
**once**, by the collector session — not by any front and not by the spectator. They are
deliberately unwritten as of this sheet.

---

## 7 · If you read only one thing

Three fronts, ten hours, two landed, zero collisions. The mechanics worked — the branch
lock, the one-name rule, the board, the token, static gates as real proof.

**What did not work was the shape of the work inside each front.** The protocol
answered *how three sessions share three repos safely* and, in doing so, quietly replaced
the model that answers *how one session does good work* — Jarvis commanding a fleet,
handing the build to FRIDAY, handing the proof to EDITH. Benched, each front did all of it
alone and graded itself, and the only independent verification left in the entire run was
Mr. Stark opening the app himself.

**GAUNTLET-01's first change is not a mechanic. It is restoring the fleet inside each
front, gated on the two invariants that actually need protecting — and never letting the
builder be the only verifier again.**

And it runs as a **gauntlet** — plain practice, no emergency powers. Those powers were
what cost us the fleet.

---

*GAUNTLET-00 · 4 Aug 2026 · three fronts · zero collisions · eight
retractions · two fronts landed · one structural miss, named by him.*
