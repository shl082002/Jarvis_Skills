# Module 1: Reliability

These concepts prevent your product from breaking.

> **Think like this:** *"What if the user clicks twice? What if the network blinks? What if one supplier dies?"*

## Topics

| # | Topic | One-line mental model | Read time |
|---|-------|----------------------|-----------|
| 1 | [Idempotency](./01-idempotency.md) | "What if user clicks twice?" | ~12 min |
| 2 | [Retry Pattern](./02-retry-pattern.md) | "Maybe the service is temporarily unavailable." | ~12 min |
| 3 | [Circuit Breaker](./03-circuit-breaker.md) | "Stop calling the broken service." | ~12 min |
| 4 | [High Availability](./04-high-availability.md) | "What if this machine disappears?" | ~12 min |
| 5 | [Failover](./05-failover.md) | "Who takes over when this fails?" | ~12 min |

## Suggested Learning Order

These five concepts stack on each other:

```mermaid
flowchart LR
    A[Idempotency] --> B[Retry Pattern]
    B --> C[Circuit Breaker]
    C --> D[High Availability]
    D --> E[Failover]
```

1. **Idempotency** — safe to repeat an operation
2. **Retry** — repeat when things fail temporarily
3. **Circuit Breaker** — stop repeating when things fail permanently
4. **High Availability** — no single point of failure
5. **Failover** — automatic handoff when something dies

## Module Simulation

After finishing all 5 topics, run this scenario (answers at bottom of each topic doc):

> **Friday 11 PM.** A user books a flight + hotel on your travel platform. Payment succeeds. Hotel API times out. User clicks "Pay" again. Payment gateway retries internally. Hotel supplier is down for 20 minutes.

Trace the failure through each concept. Where would idempotency save you? Where would retry hurt you without a circuit breaker?

## PDFs

Generated PDFs live in [pdf/](./pdf/). Regenerate:

```bash
python3 md_to_pdf.py --dir learning/module-01-reliability --force
```
