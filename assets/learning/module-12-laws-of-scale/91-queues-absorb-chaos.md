---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-05-distributed-systems/27-message-queue.md
---

# 91. Law 32: Queues Absorb Chaos

> **Lens:** Spikes and slow consumers — sync path stays thin. **Canonical:** [27 Message Queue](../module-05-distributed-systems/27-message-queue.md)

## The One New Question

*"What must complete before the user sees success — and what can wait in line?"*

## What This Lens Adds

| Sync (user waits) | Async (queue absorbs) |
|-------------------|----------------------|
| Charge card | Send confirmation email |
| Reserve inventory | Update analytics |
| Return booking ID | Notify partner API |

Queues turn **spike-shaped work** into **steady consumption** — chaos becomes backlog you can monitor.

## Mental Movie (30 seconds)

Flash sale: 10K bookings/min. Email service handles 200/min. Without queue: timeouts cascade. With queue: users get "booked" in 200ms; emails drain over 50 minutes.

## Problem Simulation

Checkout does 8 downstream calls synchronously. p99 = sum of all latencies. Move 5 to queue. **What's still sync?** *(Payment + inventory hold only.)*

## Key Takeaway

Queues don't add speed — they **absorb chaos** so the critical path stays predictable.

**Next:** [92 — Most Traffic Is Uneven](./92-most-traffic-is-uneven.md)
