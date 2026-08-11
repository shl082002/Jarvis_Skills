---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-10-laws-of-software-systems/69-communication-determines-architecture.md
---

# 96. Law 37: Communication Defines Architecture

> **Lens:** Information flow before boxes-and-arrows. **Canonical:** [69 Communication Determines Architecture](../module-10-laws-of-software-systems/69-communication-determines-architecture.md)

## The One New Question

*"If I draw only services without arrows, what conversations am I hiding?"*

## What This Lens Adds

Draw **arrows first** (who talks, sync vs async, payload shape), then assign REST/gRPC/queue. Microservices without defined conversations = distributed monolith with network tax.

| Bad diagram | Good diagram |
|-------------|--------------|
| 6 boxes | 6 boxes + labeled arrows (sync POST, async event, webhook) |

## Mental Movie (30 seconds)

Team splits monolith into 8 services. Same synchronous call chain, now with HTTP overhead and partial failures. **Boxes changed; conversation didn't.**

## Problem Simulation

Redesign checkout as conversation diagram only (no tech names). Then map each arrow to a protocol. Where did complexity increase?

## Key Takeaway

Pick technology **after** the conversation is clear — not before.

**Next:** [97 — Request-Response Is the Default](./97-request-response-is-the-default.md)
