---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-09-apis-for-product-builders/51-conversation-patterns.md
---

# 95. Law 36: Every System Is a Conversation

> **Lens:** Mindset before protocols. **Canonical:** [51 Conversation Patterns](../module-09-apis-for-product-builders/51-conversation-patterns.md)

## The One New Question

*"Who is talking to whom — and is this ask/answer, notify, stream, or broadcast?"*

## What This Lens Adds

Servers don't "integrate" — they **converse**. Naming the conversation type prevents picking Kafka for a question that needed GET.

| Pattern | Conversation |
|---------|--------------|
| REST | Ask → answer → done |
| Webhook | They tell you when ready |
| WebSocket | Ongoing dialogue |
| Event bus | One speaks, many listen |

## Mental Movie (30 seconds)

"Add Kafka." **Why?** "Because scale." No one named the conversation. Checkout is ask/answer. Inventory updates are facts many need. Different conversations.

## Problem Simulation

List conversations in one booking: user→API, API→payment, payment→webhook, API→email. Label each pattern before choosing tech.

## Key Takeaway

Architecture diagrams are **conversation maps** — technology is just the language.

**Next:** [96 — Communication Defines Architecture](./96-communication-defines-architecture.md)
