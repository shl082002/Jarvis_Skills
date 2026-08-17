---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-10-laws-of-software-systems/66-fastest-request-never-made.md
  - ../module-03-performance/11-caching.md
---

# 115. Law 56: The Fastest Request Is the One Never Made

> **Lens:** Browser layer — React Query, HTTP cache, prefetch. **Canonical:** [66 Fastest Request Never Made](../module-10-laws-of-software-systems/66-fastest-request-never-made.md)

## The One New Question

*"Can the user see this without another network round-trip?"*

## What This Lens Adds

| Layer | Never-fetch tactic |
|-------|-------------------|
| React Query / SWR | `staleTime`, cache key by query |
| HTTP | `Cache-Control`, ETag |
| Prefetch | Load next route on hover |
| Service worker | Offline repeat visits |

Same law as backend — **eliminate** before tuning 400ms → 350ms.

## Mental Movie (30 seconds)

Trips list: fetch on every back-navigation. React Query cache: 0ms network, background revalidate. User feels instant; server load drops 50%.

## Problem Simulation

Map three endpoints to cache strategy: countries (24h CDN), profile (5min stale), search (2min keyed by query). What invalidates each?

## Key Takeaway

Frontend perf wins are often **zero-request wins** — not faster requests.

**Next:** [116 — Network Is Slower Than Code](./116-network-is-slower-than-code.md)
