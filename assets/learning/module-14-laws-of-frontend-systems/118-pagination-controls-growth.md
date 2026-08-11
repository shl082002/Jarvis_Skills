---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-03-performance/17-pagination.md
---

# 118. Law 59: Pagination Controls Growth

> **Lens:** UI/API payload stays bounded as user data grows. **Canonical:** [17 Pagination](../module-03-performance/17-pagination.md)

## The One New Question

*"What happens to response size when this user has 10× more rows — in 5 years?"*

## What This Lens Adds

```
Year 1:  10 bookings  → ~5KB
Year 10: 5000 bookings → timeout without pages
```

Pagination isn't a UI nicety — it's **growth insurance**. Pair with [119 Virtualization](./119-virtualization-controls-rendering.md) when the list is long but on screen.

## Mental Movie (30 seconds)

Power user opens order history — 2.5MB JSON, mobile browser tab dies. `limit=20` → always ~10KB. **Growth decoupled from single request.**

## Problem Simulation

Admin table: 50K hotels. Offset pagination vs cursor for infinite scroll. Which breaks on mid-scroll inserts?

## Key Takeaway

Paginate every **growing** list — API and UI — before the power user becomes your incident.

**Next:** [119 — Virtualization Controls Rendering](./119-virtualization-controls-rendering.md)
