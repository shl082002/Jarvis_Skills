---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-02-scale/07-horizontal-scaling.md
---

# 84. Law 25: Parallel Work Creates Scale

> **Lens:** Horizontal scale requires **independent** work units. **Canonical:** [07 Horizontal Scaling](../module-02-scale/07-horizontal-scaling.md)

## The One New Question

*"Can this request be handled by any worker without talking to the others first?"*

## What This Lens Adds

Parallel scale fails when work is **coupled**:
- Shared mutable session on server → sticky sessions (fragile)
- Global counter on one row → single hot shard
- Chat room state on one node → can't freely load-balance

Stateless API + external store (Redis/DB) = workers interchangeable.

## Mental Movie (30 seconds)

10 app servers, but every booking increments `global_sequence` on one DB row. **10 horses, one bridle.** Horizontal boxes don't help the contested row.

## Problem Simulation

Checkout flow holds session cart in server memory. Plan: add 5 more pods. **What breaks?** *(Cart lost on different pod — need Redis session or client-side cart ID.)*

## Key Takeaway

Horizontal scale is parallel **independent** work — coupling collapses you back to one bottleneck.

**Next:** [85 — Shared Resources Become Contested](./85-shared-resources-become-contested.md)
