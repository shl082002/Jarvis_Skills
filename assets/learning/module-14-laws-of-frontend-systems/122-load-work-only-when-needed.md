---
mode: lens
read_time: ~3 min
prerequisites:
  - ../module-03-performance/16-lazy-loading.md
---

# 122. Law 63: Load Work Only When Needed

> **Lens:** Code-splitting and route-level deferral — not data lazy load. **Canonical:** [16 Lazy Loading](../module-03-performance/16-lazy-loading.md)

## The One New Question

*"Does every user download the admin bundle, PDF library, and chart code on the homepage?"*

## What This Lens Adds

| Module 3 lazy load | Module 14 lazy load |
|--------------------|---------------------|
| Fetch data when needed | **Fetch JS when route opens** |
| API `?fields=` | `React.lazy()` / dynamic `import()` |
| Deferred images | Route-based chunks |

90% of users never open admin — don't ship admin JS in the main bundle.

## Mental Movie (30 seconds)

Main bundle: 800KB including admin dashboards. Route split: homepage 180KB, admin loads on `/admin` only. **TTI drops 2s on 4G.**

## Problem Simulation

Identify three features to lazy-load: admin, invoice PDF, analytics charts. Estimate KB saved from initial load.

## Key Takeaway

Lazy loading in the browser is **deferring JavaScript work** — same principle as deferring data, different asset.

**Next:** [123 — Images Dominate Assets](./123-images-dominate-assets.md)
