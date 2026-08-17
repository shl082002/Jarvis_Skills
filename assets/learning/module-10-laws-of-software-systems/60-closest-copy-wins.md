---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-03-performance/11-caching.md
  - ../module-03-performance/12-cdn.md
---

# 60. Law 2: The Closest Copy Wins

> **Lens:** Distance — put data near where it is consumed. **Canonical:** [Caching](../module-03-performance/11-caching.md) · [CDN](../module-03-performance/12-cdn.md)

## The One New Question

*"How far does this data travel on every request — and can a closer copy answer instead?"*

## What This Lens Adds

| Layer | Closest copy |
|-------|----------------|
| Browser | HTTP cache, service worker |
| Edge | CDN for static assets |
| App | Redis / in-process cache |
| DB | Read replica in same region |

**Distance is latency.** Moving bits across the internet is never free — even when you cache at the origin, the user still waits for a round trip.

## Mental Movie (30 seconds)

Hotel images served from US origin to Mumbai user: **~400ms**. Same images on Mumbai CDN edge: **~40ms**. Same law as Redis at the app layer — different distance.

## Problem Simulation

Search page loads 40 hotel thumbnails from origin API. Users are 80% in India. **Fix:** CDN + long `Cache-Control` on images. **Estimate:** 40 × 350ms saved ≈ 14s of serial image latency removed (parallel helps, but bytes still cross oceans).

## Key Takeaway

Before optimizing query plans, ask where the **nearest copy** of each byte lives.

**Next:** [61 — Repetition Is The Enemy](./61-repetition-is-the-enemy.md)
