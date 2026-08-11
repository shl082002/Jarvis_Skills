---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-09-apis-for-product-builders/51-conversation-patterns.md
  - ../module-09-apis-for-product-builders/57-api-stack-evolution.md
---

# 107. Law 48: Different Conversations Need Different Languages

> **Lens:** Protocol picker — one table, no re-tutorial. **Canonical:** [Module 9 — APIs](../module-09-apis-for-product-builders/)

## The One New Question

*"Which conversation am I having — and which protocol is the native fit?"*

## What This Lens Adds

| Conversation | Protocol | Deep dive |
|--------------|----------|-----------|
| Ask → answer | REST | [52 REST](../module-09-apis-for-product-builders/52-rest.md) |
| They notify you | Webhooks | [53 Webhooks](../module-09-apis-for-product-builders/53-webhooks.md) |
| Ongoing push | WebSockets | [54 WebSockets](../module-09-apis-for-product-builders/54-websockets.md) |
| Flexible fetch | GraphQL | [55 GraphQL](../module-09-apis-for-product-builders/55-graphql.md) |
| Machine-to-machine | gRPC | [56 gRPC](../module-09-apis-for-product-builders/56-grpc.md) |

No universal winner — **context picks the language** (Laws 38–41).

## Mental Movie (30 seconds)

Mobile home screen: GraphQL one round-trip. Internal pricing service: gRPC. Razorpay callback: webhook. Hotel static page: REST GET. **Four conversations, four tools.**

## Problem Simulation

Pick protocol for: (a) customer search, (b) payment callback, (c) live cab map, (d) service→service inventory check. One line each.

## Key Takeaway

Learn protocols in Module 9; here remember **match language to conversation**, not trend.

**Next:** [108 — Reliability Over Speed](./108-reliability-over-speed.md)
