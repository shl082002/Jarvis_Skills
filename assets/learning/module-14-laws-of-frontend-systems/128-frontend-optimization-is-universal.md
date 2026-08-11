---
mode: capstone
read_time: ~5 min
prerequisites:
  - ../module-10-laws-of-software-systems/71-the-unifying-principle.md
---

# 128. Law 69: Frontend Optimization Is the Same Optimization

> **Capstone:** Module 10 laws in the browser. **Canonical:** [71 The Unifying Principle](../module-10-laws-of-software-systems/71-the-unifying-principle.md)

## The One Question (everywhere)

*"Can I avoid doing this again?"*

## Backend ↔ Frontend Map

| Backend | Frontend | Law |
|---------|----------|-----|
| Cache query | React Query cache | Memory beats recalculation |
| Avoid N+1 | Avoid re-renders | Repetition is enemy |
| Paginate SQL | Paginate / virtualize UI | Bounded work |
| CDN edge | Browser cache | Closest copy wins |
| Lazy API fields | Code-split routes | Load when needed |
| Async queue | Deferred non-critical UI | Move work off critical path |

**Principles are universal. Only manifestations differ.**

## Mental Movie (30 seconds)

Backend team ships Redis caching playbook. Frontend team reinvents from scratch. **Same laws** — shared vocabulary saves quarters of duplicated learning.

## Problem Simulation

Pick one slow screen. Apply the unifying question at each layer: network, cache, render, bundle. Which layer wins most ms?

## Key Takeaway

Module 14 isn't a different physics — it's **Module 10 in a browser**. When in doubt: avoid repeating work, bound payloads, put copies closer to the user.

**Handbook complete.** Revisit [CONCEPT-INDEX](../CONCEPT-INDEX.md) for any cluster you want to deepen.
