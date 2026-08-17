---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-03-performance/13-database-indexing.md
  - ../module-10-laws-of-software-systems/62-memory-beats-recalculation.md
---

# 79. Law 20: Indexes Are Memory for Databases

> **Lens:** Index = the database's remembered lookup map. **Canonical:** [13 Database Indexing](../module-03-performance/13-database-indexing.md)

## The One New Question

*"Is the DB scanning every page like a book without a table of contents — and which columns are the chapter titles?"*

## What This Lens Adds

```
Book:     Table of Contents → Chapter → Page
Database: Index (B-tree)    → Pointer → Row
```

Indexes are **memory at the storage layer** — same force as Redis, different durability tradeoff. Pair with [Law 19](./78-every-query-is-a-question.md): a perfect index on a bad question still wastes work.

## Mental Movie (30 seconds)

`WHERE user_id = 101` on 5M rows: 8s scan vs 3ms index lookup. The index is the DB remembering where user 101's rows live.

## Problem Simulation

Top slow query: `SELECT * FROM bookings WHERE status = 'pending' ORDER BY created_at`. Missing index on `(status, created_at)`? Run EXPLAIN. Add index. Re-measure.

## Key Takeaway

Indexes are not DBA trivia — they are **memory for tables**. Law 19 asks the question; Law 20 remembers the answer.

**Next:** [80 — Moving Data Is More Expensive](./80-moving-data-is-more-expensive-than-storing-it.md)
