---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-09-apis-for-product-builders/52-rest.md
---

# 97. Law 38: Request-Response Is the Default

> **Lens:** Default conversation — deviate only with evidence. **Canonical:** [52 REST](../module-09-apis-for-product-builders/52-rest.md)

## The One New Question

*"Can the user wait for one answer and move on — or do they need push/stream/async?"*

## What This Lens Adds

80%+ of web traffic is **ask → answer → done**. Use request-response unless:

| Signal | Consider instead |
|--------|------------------|
| Server pushes updates | WebSocket |
| Other system knows first | Webhook |
| Work can wait | Queue |
| Many react to one fact | Events |

## Mental Movie (30 seconds)

Hotel details page: GET once, render. **No WebSocket needed.** Live flight gate changes: maybe push. **Match conversation to need.**

## Problem Simulation

Proposals: WebSocket for order history, Kafka for login, gRPC for static config. Mark each over-engineered or justified.

## Key Takeaway

Request-response is the **default of the web** — simpler, cacheable, debuggable. Earn complexity.

**Next:** [98 — Simplest Conversation Wins](./98-simplest-conversation-wins.md)
