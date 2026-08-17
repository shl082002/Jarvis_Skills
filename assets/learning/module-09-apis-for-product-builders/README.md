# Module 9: APIs For Product Builders

*What kind of conversation is happening between these systems?*

> **The wrong question:** Should I use REST, GraphQL, WebSockets, Webhooks, or gRPC?
>
> **The better question:** What kind of conversation is happening between these systems?

Technology is usually the consequence of the conversation, not the cause.

---

## Topics

| # | Topic | Mental Model | Read time |
|---|-------|--------------|-----------|
| 51 | [Conversation Patterns](./51-conversation-patterns.md) | Every API is a type of conversation | ~10 min |
| 52 | [REST](./52-rest.md) | Restaurant order | ~12 min |
| 53 | [Webhooks](./53-webhooks.md) | Pizza delivery notification | ~12 min |
| 54 | [WebSockets](./54-websockets.md) | Phone call | ~12 min |
| 55 | [GraphQL](./55-graphql.md) | Buffet instead of fixed meal | ~12 min |
| 56 | [gRPC](./56-grpc.md) | Private high-speed railway | ~12 min |
| 57 | [API Stack Evolution](./57-api-stack-evolution.md) | How your stack grows with your product | ~12 min |

## Learning Order

```mermaid
flowchart LR
    A[51 Conversation Patterns] --> B[52 REST]
    B --> C[53 Webhooks]
    C --> D[54 WebSockets]
    D --> E[55 GraphQL]
    E --> F[56 gRPC]
    F --> G[57 Stack Evolution]
```

Start with the conversation. End with knowing which protocol your product stage needs.

## Architect's Cheat Sheet

| Ask yourself... | Use |
|---------------|-----|
| Do I need data **right now**? | REST |
| Does **another system know first**? | Webhooks |
| Do I need **continuous realtime** updates? | WebSockets |
| Does the frontend need data from **many services**? | GraphQL |
| Are **internal services** talking at scale? | gRPC |

## Module Simulation

After all 7 topics, answer this:

> You're building a travel super-app. Users search flights (REST), pay via Razorpay (webhook for confirmation), track their cab to the airport (WebSocket), see a dashboard with trips + loyalty + notifications (GraphQL), and your pricing engine talks to inventory 10,000 times/minute (gRPC).

Map each feature to the right protocol. Where would picking the wrong one hurt?

## PDFs

```bash
python3 md_to_pdf.py --dir learning/module-09-apis-for-product-builders --force
```
