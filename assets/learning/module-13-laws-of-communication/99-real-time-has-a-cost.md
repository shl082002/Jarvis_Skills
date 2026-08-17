---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-09-apis-for-product-builders/54-websockets.md
---

# 99. Law 40: Real-Time Has a Cost

> **Lens:** Persistent connections — when they're worth the ops tax. **Canonical:** [54 WebSockets](../module-09-apis-for-product-builders/54-websockets.md)

## The One New Question

*"Does the user need updates faster than polling every N seconds — and can we pay for N open connections?"*

## What This Lens Adds

| Cost | Why |
|------|-----|
| Connection memory | 1M users = 1M sockets |
| Sticky routing | Load balancer complexity |
| Reconnect storms | Deploys drop everyone |
| No HTTP cache | Different tooling |

Real-time wins for: live tracking, chat, trading, collaborative edits. Loses for: static catalog, order history refresh.

## Mental Movie (30 seconds)

1M users on hotel browse — WebSocket "just in case." Connection table explodes. **Polling or SSE for rare updates would have worked.**

## Problem Simulation

Live bus tracking vs monthly statement PDF. Which needs WebSocket? Estimate connection count at 100K concurrent users.

## Key Takeaway

Real-time is a **capacity and ops decision**, not a freshness badge.

**Next:** [100 — Notifications Reverse the Direction](./100-notifications-reverse-direction.md)
