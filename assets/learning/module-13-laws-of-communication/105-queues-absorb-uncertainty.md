---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-12-laws-of-scale/91-queues-absorb-chaos.md
---

# 105. Law 46: Queues Absorb Uncertainty

> **Lens:** Unknown timing and unknown volume — communication buffer. **Canonical:** [91 Queues Absorb Chaos](../module-12-laws-of-scale/91-queues-absorb-chaos.md) · [27 Message Queue](../module-05-distributed-systems/27-message-queue.md)

## The One New Question

*"When don't I know how long they'll take to respond — or how many responses arrive at once?"*

## What This Lens Adds

| Scale lens (M12) | Communication lens (here) |
|------------------|---------------------------|
| Spike volume | **Unknown duration** (supplier 5s–5min) |
| Protect sync path | **Decouple conversation partners** |

Queue = "I'll listen when you're ready" instead of holding the HTTP connection open.

## Mental Movie (30 seconds)

Partner API: 200ms usually, 90s during their outage. Sync call = user timeout. Queue booking request → worker retries → user gets email when confirmed. **Uncertainty absorbed.**

## Problem Simulation

Hotel confirmation from 40 suppliers, variable latency. Sync vs message per supplier. How does user experience differ on supplier slowdown?

## Key Takeaway

Queues absorb **uncertainty in when and how much** — not just spikes. Same tool, communication framing.

**Next:** [106 — Events Describe Facts](./106-events-describe-facts.md)
