# Module 2: Scale

These concepts help you survive growth.

> **Think like this:** *"Can I just get a bigger machine? Can I clone this service? Which server gets the request? How many is too many? How do I slow things down before we drown?"*

## Topics

| # | Topic | One-line mental model | Read time |
|---|-------|----------------------|-----------|
| 6 | [Vertical Scaling](./06-vertical-scaling.md) | "Can I just get a bigger machine?" | ~12 min |
| 7 | [Horizontal Scaling](./07-horizontal-scaling.md) | "Can I clone this service?" | ~12 min |
| 8 | [Load Balancer](./08-load-balancer.md) | "Which server gets the request?" | ~12 min |
| 9 | [Rate Limiting](./09-rate-limiting.md) | "How many requests are too many?" | ~12 min |
| 10 | [Backpressure](./10-backpressure.md) | "How do I slow incoming work?" | ~12 min |

## Suggested Learning Order

These five concepts stack on each other:

```mermaid
flowchart LR
    A[Vertical Scaling] --> B[Horizontal Scaling]
    B --> C[Load Balancer]
    C --> D[Rate Limiting]
    D --> E[Backpressure]
```

1. **Vertical Scaling** — make the machine bigger (first move, fast ceiling)
2. **Horizontal Scaling** — add more machines (the real path to scale)
3. **Load Balancer** — spread traffic across those machines
4. **Rate Limiting** — cap how much traffic any client can send
5. **Backpressure** — slow upstream when downstream is overwhelmed

## Module Simulation

After finishing all 5 topics, run this scenario (answers at bottom of each topic doc):

> **Diwali sale weekend.** Your travel platform runs on a single 8GB server. Traffic jumps 20×. Search is slow. Checkout queues up. A partner scraper hammers your hotel API. Your payment service retries flood the booking service. CPU hits 100%. Memory spikes. Users see timeouts.

Trace the failure through each concept. Where does vertical scaling buy time? When must you go horizontal? What does the load balancer do? Where does rate limiting stop the scraper? Where does backpressure prevent the queue from eating all RAM?

## PDFs

Generated PDFs live in [pdf/](./pdf/). Regenerate:

```bash
python3 md_to_pdf.py --dir learning/module-02-scale --force
```
