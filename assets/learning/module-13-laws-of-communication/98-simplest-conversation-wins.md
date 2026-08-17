---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-09-apis-for-product-builders/57-api-stack-evolution.md
---

# 98. Law 39: Simplest Conversation Wins

> **Lens:** Anti-over-engineering for communication. **Canonical:** [57 API Stack Evolution](../module-09-apis-for-product-builders/57-api-stack-evolution.md)

## The One New Question

*"What is the dumbest conversation that still works — and what ops cost am I adding?"*

## What This Lens Adds

| Overkill | Simple enough |
|----------|---------------|
| Kafka for 50 bookings/day | REST + cron |
| WebSocket for hotel static page | GET + cache |
| GraphQL for 3 fields | REST with slim DTO |

Complex protocols need **connection pools, schema registries, replay, monitoring** — pay only when the conversation demands it.

## Mental Movie (30 seconds)

Startup adds event bus before product-market fit. Three consumers, one producer, six months of platform team. **Simple REST would have shipped in week 2.**

## Problem Simulation

Internal admin exports CSV once daily. REST endpoint vs streaming vs event pipeline. Pick simplest. Defend one sentence.

## Key Takeaway

Complexity in communication becomes **permanent operational load** — start simple, evolve when patterns force it.

**Next:** [99 — Real-Time Has a Cost](./99-real-time-has-a-cost.md)
