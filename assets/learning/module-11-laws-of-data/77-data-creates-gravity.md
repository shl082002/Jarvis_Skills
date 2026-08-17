---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-10-laws-of-software-systems/67-information-has-gravity.md
---

# 77. Law 18: Data Creates Gravity

> **Lens:** Data architect's orbit — who may query the core, and how you escape direct DB coupling. **Canonical:** [67 Information Has Gravity](../module-10-laws-of-software-systems/67-information-has-gravity.md)

## The One New Question

*"If I change this schema, how many teams stop shipping — and can consumers react to events instead of querying the core?"*

## What This Lens Adds (beyond Law 9)

| Strategy | Data-architect move |
|----------|---------------------|
| **Ownership** (Law 14) | One team owns `bookings` writes |
| **Published events** | `BookingCreated` — no cross-service SQL |
| **Read models** | Search/analytics projections, not shared tables |
| **API boundary** | HTTP/events only — no foreign keys across services |

Same gravity force as Module 10 — here the decision is **governance**: who orbits, who gets pushed to event-driven edges.

## Mental Movie (30 seconds)

Year 4: nine teams query `bookings` directly. Column rename = nine deploys. **Fix:** booking service owns writes; everyone else subscribes to facts or calls `GET /bookings/{id}`.

## Problem Simulation

List systems that read `bookings` today. For each, mark: direct SQL / API / event. Target state: zero direct SQL outside booking service.

## Key Takeaway

Gravity is inevitable — **design the orbit** (events, read models, contracts) before the schema becomes immovable.

**Next:** [78 — Every Query Is a Question](./78-every-query-is-a-question.md)
