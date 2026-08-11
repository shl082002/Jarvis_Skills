---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-02-scale/06-vertical-scaling.md
---

# 83. Law 24: A Faster Horse Does Not Fix Traffic

> **Lens:** Vertical scaling buys time, not architecture. **Canonical:** [06 Vertical Scaling](../module-02-scale/06-vertical-scaling.md)

## The One New Question

*"Am I hitting a hardware ceiling — and what architectural change is actually required?"*

## What This Lens Adds

Bigger CPU/RAM is a **faster horse** on a crowded road. It works until:
- Single-threaded bottlenecks (one hot partition)
- Disk/network limits on one box
- Cost curve goes exponential

Then you need **more horses** (horizontal) or **less traffic on the road** (cache, queue, batch).

## Mental Movie (30 seconds)

Search DB at 95% CPU. Ops doubles RAM. Works 3 months. Traffic doubles. Still one writer, one disk. **Horse is faster; road is still one lane.**

## Problem Simulation

API p99 spikes. Team proposes 32-core upgrade. Bottleneck is single PostgreSQL primary for writes. **Verdict:** vertical helps reads (replicas); writes need sharding or async — not a bigger horse alone.

## Key Takeaway

Scale vertically to **buy time**; scale architecturally to **remove the ceiling**.

**Next:** [84 — Parallel Work Creates Scale](./84-parallel-work-creates-scale.md)
