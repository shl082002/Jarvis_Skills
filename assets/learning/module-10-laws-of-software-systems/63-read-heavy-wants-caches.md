---
mode: lens
read_time: ~3 min
prerequisites:
  - ./62-memory-beats-recalculation.md
---

# 63. Law 5: Read Heavy Systems Want Caches

> **Lens:** ROI diagnostic for caching. **Canonical:** [62 Memory Beats Recalculation](./62-memory-beats-recalculation.md)

## The One New Question

*"What is the read-to-write ratio — and does this dataset change often enough to matter?"*

## What This Lens Adds

| Table | Writes/day | Reads/day | Cache? |
|-------|------------|-----------|--------|
| `bookings` | 500 | 2,000 | Maybe (invalidation hard) |
| `countries` | 0 | 50,000 | **Yes** — tiny, static, hot |

Size matters less than **read frequency** and **change frequency**. Cache gold = high reads + low writes.

## Mental Movie (30 seconds)

You cache `bookings` because it's "important." Every price change invalidates 50 keys. You skip caching `countries` because it's "small" — but it hits the DB 50K times/day. **Wrong priorities.**

## Problem Simulation

Audit three datasets: `countries`, `hotel_prices`, `user_sessions`. Rank by cache ROI. *(Answers: countries first; sessions with TTL; prices only with short TTL + event invalidation.)*

## Key Takeaway

Ask **how often read** and **how often changed** — not how big the row is.

**Next:** [64 — Freshness Fights Speed](./64-freshness-fights-speed.md)
