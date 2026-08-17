---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-04-data-systems/21-eventual-consistency.md
  - ../module-11-laws-of-data/75-consistency-has-a-cost.md
---

# 90. Law 31: Availability and Consistency Compete

> **Lens:** CAP under peak load — per data type, not globally. **Canonical:** [21 Eventual Consistency](../module-04-data-systems/21-eventual-consistency.md) · [75 Consistency Has a Cost](../module-11-laws-of-data/75-consistency-has-a-cost.md)

## The One New Question

*"During partition or replica lag at peak — do we stay up with stale data, or go down to stay correct?"*

## What This Lens Adds

| Data type | Typical choice at scale |
|-----------|-------------------------|
| Payment / inventory | **CP** — block or queue if unsure |
| Product browse / search | **AP** — stale OK, stay fast |
| User profile | Mixed — short TTL |

Scale makes the tradeoff **visible**: 2s replica lag at 10 users is noise; at 1M users it's revenue leakage or outage.

## Mental Movie (30 seconds)

Flash sale: Virginia replica shows ₹5000, Mumbai primary ₹4800. Book at wrong price — who pays? **You chose availability over consistency.**

## Problem Simulation

Classify: search results, wallet balance, hotel gallery, booking confirmation. CP or AP during regional partition?

## Key Takeaway

CAP isn't academic — it's **per-domain policy** that shows up loudest under load.

**Next:** [91 — Queues Absorb Chaos](./91-queues-absorb-chaos.md)
