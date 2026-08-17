---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-09-apis-for-product-builders/53-webhooks.md
---

# 100. Law 41: Notifications Reverse the Direction

> **Lens:** When the other party knows first — stop polling. **Canonical:** [53 Webhooks](../module-09-apis-for-product-builders/53-webhooks.md)

## The One New Question

*"Who has the answer first — and should they call us instead of us asking every 2 seconds?"*

## What This Lens Adds

```
Polling:   You → "Ready yet?" → Them  (every 2s)
Webhook:   Them → "It's ready" → You   (once)
```

Reverse direction when: payment gateway, shipping carrier, supplier confirmation, identity provider.

## Mental Movie (30 seconds)

Razorpay payment: poll every second × 10K checkouts = DDoS yourself. Webhook: one POST when captured. **Conversation direction flipped.**

## Problem Simulation

Supplier confirms hotel 30–120s later. Design: poll loop vs webhook vs queue callback. List failure modes for each (missed webhook, duplicate delivery).

## Key Takeaway

When **they** know first, **they** should speak — with idempotency and signature verification ([Module 1](../module-01-reliability/01-idempotency.md)).

**Next:** [101 — Machines Prefer Structured Conversations](./101-machines-prefer-structured-conversations.md)
