---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-04-data-systems/23-sharding.md
---

# 89. Law 30: Sharding Buys Capacity

> **Lens:** When one node can't grow anymore — and what you pay in query pain. **Canonical:** [23 Sharding](../module-04-data-systems/23-sharding.md)

## The One New Question

*"Which shard key keeps related data together — and which queries become impossible without scatter-gather?"*

## What This Lens Adds

Sharding splits **write capacity** and **storage** — not magic:
- Cross-shard joins → application-level merge or denormalize
- Bad shard key (e.g. `country`) → one hot shard
- Rebalancing → operational event

Scale lens: shard when **one node's ceiling** is the bottleneck, not when queries are slow (indexes first — Law 93).

## Mental Movie (30 seconds)

Shard `bookings` by `user_id`. Admin dashboard: "revenue by hotel today" hits **every shard**. What was one SQL becomes 16 queries + merge.

## Problem Simulation

200M booking rows, single Postgres maxed on disk. Shard by `user_id` vs `booking_id`. Which supports "my trips" vs "hotel occupancy report"? *(user_id for B2C; hotel_id or separate OLAP for ops.)*

## Key Takeaway

Sharding buys **capacity**; you pay in **query shape and operations** — choose the key for your dominant access pattern.

**Next:** [90 — Availability and Consistency Compete](./90-availability-and-consistency-compete.md)
