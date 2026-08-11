# 117. Law 58: Loading Everything Is Rarely Correct

> **Think:** *"Does the user need all 50,000 rows — or the first 20?"*

---

## The 4 Questions

| Question | Answer |
|----------|--------|
| **What problem does it solve?** | Shipping entire datasets to the client — all hotels, all orders, all countries with full objects. |
| **What happens if I ignore it?** | 2MB JSON, 8s parse on mobile, OOM on low-end devices, users abandon. |
| **Where would I use it?** | API design, field selection, pagination, infinite scroll, search limits. |
| **What companies use it?** | Google search (10 results/page), Amazon (paginated lists), every scalable list UI. |

---

## Mental Movie (60 seconds)

Search returns **50,000 hotels** in one response for Goa.

User sees **20** on screen.

**49,980 hotels** downloaded, parsed, and held in memory for no reason.

**Transfer only what users need** — fields and rows for current view.

---

## How It Works

| Anti-pattern | Fix |
|--------------|-----|
| `SELECT *` API | Field selection, card DTO |
| All rows | Pagination (Law 118) |
| Full nested objects | IDs + lazy detail fetch |
| 50 images upfront | Lazy load (Law 123) |

---

## Real-World Examples

### Your Travel Platform

**Bad:** `GET /hotels?city=goa` → 50MB, 12,000 hotels full detail.

**Good:** `GET /hotels?city=goa&limit=20&fields=id,name,price,thumbnail,rating` → 40KB.

Detail page: `GET /hotels/55` full object on demand.

### Nykaa

Listing API returns card fields only. PDP fetches full product.

### Amazon

Search results minimal. Product page loads depth.

---

## Connection To Other Laws & Modules

| Connection | Link |
|------------|------|
| Law 118 | Pagination |
| Law 119 | Virtualization |
| Module 11: Law 19 | Better API questions |
| Module 3: Pagination | Tactical |

---

## Key Takeaway

Request and render only what the current screen needs — slim fields, paginated rows, lazy detail loads.

**Next:** [118 — Pagination Controls Growth](./118-pagination-controls-growth.md)
