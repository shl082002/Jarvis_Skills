---
name: browse
description: Drive a headed browser for LIVE evidence — Cursor IDE browser first. Use when QA or verify-live needs a real page, screenshot, or click path. Optional $B daemon is a later adapter, not the default.
---

# Browse — hands, not a second browser company

Default path: **Cursor browser MCP** (or the host’s equivalent headed tab).
The IDE tab is headed by definition — lock it, then act. Do not vendor
Chromium into this kit. Do not start a 58MB binary unless `references/daemon.md`
applies and the principal asked.

## When

- `qa` / EDITH needs LIVE-VERIFIED on a UI path
- `verify` cannot be settled by HTTP alone
- The principal says “open the app” / “click through”

Not for: reading docs you already have as files; inventing a second tracker.

## Sequence (Cursor / IDE browser)

1. **List tabs** — know what is already open.
2. **Navigate** to the named URL (or reuse the tab if it is already there).
3. **Lock** the tab before a multi-step walk.
4. **Snapshot** (accessibility tree) → decide → **act** (click / type / fill).
5. **Screenshot** after each meaningful state change.
6. Save evidence under `WORKROOM/reports/` and/or `WORKROOM/evidence/`
   (`<date>-<slug>-<step>.png` plus a short notes md).
7. **Unlock** when the walk is finished.

If four attempts fail or a blocker needs the principal (login, captcha,
permission), stop and report. Do not brute-force.

## Evidence

LIVE-VERIFIED requires a screenshot path or a quoted HTTP body from the
real system (`skills/verify-live/`). “I navigated” without a file is CLAIMED.

## Optional daemon

Persistent headed Chromium (`$B connect`) is a separate adapter, off unless
asked. Binary stays **outside** the kit. If `references/daemon.md` exists,
that is the only setup path.
