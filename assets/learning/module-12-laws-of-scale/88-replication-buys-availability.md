---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-04-data-systems/22-replication.md
---

# 88. Law 29: Replication Buys Availability

> **Lens:** Under load — what survives when a node dies? **Canonical:** [22 Replication](../module-04-data-systems/22-replication.md)

## The One New Question

*"If this node disappears at peak traffic, do we fail over or fail completely — and how much lag is acceptable?"*

## What This Lens Adds

| Benefit | Cost at scale |
|---------|----------------|
| Survive disk/host failure | Failover seconds–minutes |
| Read scaling via replicas | Replication lag |
| Multi-AZ resilience | Split-brain risk |

Scale lens: replicas aren't free copies — they're **contested sync** under write pressure (see Law 90).

## Mental Movie (30 seconds)

Primary dies during Diwali sale. Replica promoted. 30s of writes "in flight" — did they replicate? Finance reconciliation at 2 AM finds the gap.

## Problem Simulation

Read replica lag hits 45s during flash sale. Search shows "available" rooms that booking service already sold. **Fix options:** stronger consistency on inventory path, or CP partition for stock — not more replicas alone.

## Key Takeaway

Replication buys **availability and read headroom**; it trades **complexity and lag** — especially visible at peak.

**Next:** [89 — Sharding Buys Capacity](./89-sharding-buys-capacity.md)
