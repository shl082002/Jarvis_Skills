# Concept Index — Canonical vs Lens

Use this map to avoid reading the same idea twice. **128 topic IDs are preserved** for PDFs and the learning skill; ~22 topics are **lens stubs** (~3 min) that apply a principle you already learned elsewhere.

## How To Read

| Mode | What it is | Read time |
|------|------------|-----------|
| **canonical** | Full topic — tool, pattern, or first-principles law | ~10–12 min |
| **lens** | Same force, new domain question — skip if you did the prerequisite | ~3 min |
| **capstone** | Synthesis across modules | ~5 min |

**Rule for Modules 10–14:** If a topic is marked `lens`, read the **prerequisite canonical** first (or skip the lens if you already know the tool).

---

## Phase 1 — Recognition (Modules 1–9)

Own the **what** and **how** of each tool. These are canonical.

| Module | Owns uniquely |
|--------|---------------|
| 1 Reliability | Idempotency, retry, circuit breaker, HA, failover |
| 2 Scale | Vertical/horizontal scaling, load balancer, rate limiting, backpressure |
| 3 Performance | **Caching, CDN, indexing, query optimization, pagination, lazy load** |
| 4 Data Systems | **ACID, transactions, eventual consistency, replication, sharding** |
| 5 Distributed | **Queues, pub/sub, CQRS, event sourcing, saga** |
| 6 Infrastructure | DNS, reverse proxy, TLS, containers, CI/CD |
| 7–8 | Product and business thinking (no technical overlap) |
| 9 APIs | **REST, webhooks, WebSockets, GraphQL, gRPC, conversation patterns** |

---

## Phase 2 — Lenses (Modules 10–14)

Own the **why** and **decision framing**. Do not re-teach tools from Phase 1.

| Module | Lens | Unique questions |
|--------|------|------------------|
| 10 Laws of Software Systems | Meta-forces: work, memory, distance, time, communication | "Where is work happening?" "Can I avoid doing this again?" |
| 11 Laws of Data | Data architect | "Who owns this?" "What does each copy cost?" |
| 12 Laws of Scale | Bottleneck under load | "What breaks first?" "What happens at peak?" |
| 13 Laws of Communication | Information flow | "Who couples to whom?" "What is the contract?" |
| 14 Laws of Frontend | Browser runtime | "What does the user wait for?" "What is client vs server state?" |

---

## Concept Clusters

### Caching & memory

| Concept | Canonical | Lens applications (read order) |
|---------|-----------|-------------------------------|
| Caching | [11 — Caching](./module-03-performance/11-caching.md) | [62 Memory Beats Recalculation](./module-10-laws-of-software-systems/62-memory-beats-recalculation.md) → [74 Every Copy Creates Responsibility](./module-11-laws-of-data/74-every-copy-creates-responsibility.md) → [115 Fastest Request Never Made](./module-14-laws-of-frontend-systems/115-fastest-request-is-never-made.md) |
| Read-heavy vs write-heavy | [62](./module-10-laws-of-software-systems/62-memory-beats-recalculation.md) (included) | [63 Read Heavy Wants Caches](./module-10-laws-of-software-systems/63-read-heavy-wants-caches.md) — lens only |
| Freshness vs speed | [64 Freshness Fights Speed](./module-10-laws-of-software-systems/64-freshness-fights-speed.md) | [60 Closest Copy Wins](./module-10-laws-of-software-systems/60-closest-copy-wins.md) — distance lens |
| Memory layers | [62](./module-10-laws-of-software-systems/62-memory-beats-recalculation.md) | [68 Systems Remember](./module-10-laws-of-software-systems/68-systems-remember-to-survive.md), [81 Every System Is Memory](./module-11-laws-of-data/81-every-software-system-is-a-memory-system.md), [113 State Is Memory](./module-14-laws-of-frontend-systems/113-state-is-memory.md) |
| CDN / edge | [12 — CDN](./module-03-performance/12-cdn.md) | [60 Closest Copy Wins](./module-10-laws-of-software-systems/60-closest-copy-wins.md) |

### Avoiding repeated work

| Concept | Canonical | Lens |
|---------|-----------|------|
| Repetition | [61 Repetition Is The Enemy](./module-10-laws-of-software-systems/61-repetition-is-the-enemy.md) | [14 Query Optimization](./module-03-performance/14-query-optimization.md), [120 Re-Renders](./module-14-laws-of-frontend-systems/120-re-renders-are-repeated-work.md) |
| Scale = avoid work | [70 Scale Is Avoiding Work](./module-10-laws-of-software-systems/70-scale-is-avoiding-work.md) | [128 Frontend Optimization](./module-14-laws-of-frontend-systems/128-frontend-optimization-is-universal.md) — capstone pointer |
| Unifying principle | [71 The Unifying Principle](./module-10-laws-of-software-systems/71-the-unifying-principle.md) | — |

### Pagination & bounded payloads

| Concept | Canonical | Lens |
|---------|-----------|------|
| Pagination | [17 — Pagination](./module-03-performance/17-pagination.md) | [118 Pagination Controls Growth](./module-14-laws-of-frontend-systems/118-pagination-controls-growth.md) |
| UI-only bounds | — | [117 Loading Everything](./module-14-laws-of-frontend-systems/117-loading-everything-is-rarely-correct.md), [119 Virtualization](./module-14-laws-of-frontend-systems/119-virtualization-controls-rendering.md) |

### Lazy loading / defer work

| Concept | Canonical | Lens |
|---------|-----------|------|
| Lazy load (data/API) | [16 — Lazy Loading](./module-03-performance/16-lazy-loading.md) | [122 Load Work Only When Needed](./module-14-laws-of-frontend-systems/122-load-work-only-when-needed.md) — code-splitting |
| Work cannot be destroyed | [59 Work Cannot Be Destroyed](./module-10-laws-of-software-systems/59-work-cannot-be-destructed.md) | — |

### Indexing & queries

| Concept | Canonical | Lens |
|---------|-----------|------|
| Database indexes | [13 — Database Indexing](./module-03-performance/13-database-indexing.md) | [79 Indexes Are Memory](./module-11-laws-of-data/79-indexes-are-memory-for-databases.md) |
| Query shape | [78 Every Query Is a Question](./module-11-laws-of-data/78-every-query-is-a-question.md) | [93 Scale Amplifies Mistakes](./module-12-laws-of-scale/93-scale-amplifies-small-mistakes.md) |

### Consistency & CAP

| Concept | Canonical | Lens |
|---------|-----------|------|
| Eventual consistency | [21 — Eventual Consistency](./module-04-data-systems/21-eventual-consistency.md) | [75 Consistency Has a Cost](./module-11-laws-of-data/75-consistency-has-a-cost.md), [90 Availability vs Consistency](./module-12-laws-of-scale/90-availability-and-consistency-compete.md) |

### Replication & sharding

| Concept | Canonical | Lens |
|---------|-----------|------|
| Replication | [22 — Replication](./module-04-data-systems/22-replication.md) | [88 Replication Buys Availability](./module-12-laws-of-scale/88-replication-buys-availability.md) |
| Sharding | [23 — Sharding](./module-04-data-systems/23-sharding.md) | [89 Sharding Buys Capacity](./module-12-laws-of-scale/89-sharding-buys-capacity.md) |
| Read/write split | [76 Reads and Writes](./module-11-laws-of-data/76-reads-and-writes-are-different-workloads.md) | [30 — CQRS](./module-05-distributed-systems/30-cqrs.md) |

### Scale mechanics

| Concept | Canonical | Lens (unique to M12) |
|---------|-----------|----------------------|
| Vertical scaling | [06 — Vertical Scaling](./module-02-scale/06-vertical-scaling.md) | [83 Faster Horse](./module-12-laws-of-scale/83-a-faster-horse-does-not-fix-traffic.md) |
| Horizontal scaling | [07 — Horizontal Scaling](./module-02-scale/07-horizontal-scaling.md) | [84 Parallel Work](./module-12-laws-of-scale/84-parallel-work-creates-scale.md) |
| Bottleneck | — | [82 Every System Has a Bottleneck](./module-12-laws-of-scale/82-every-system-has-a-bottleneck.md) |
| Contention | — | [85 Shared Resources](./module-12-laws-of-scale/85-shared-resources-become-contested.md) |
| Distribution cost | — | [86 Distribution Creates Complexity](./module-12-laws-of-scale/86-distribution-creates-complexity.md) |
| Peaks | [09 Rate Limiting](./module-02-scale/09-rate-limiting.md) | [92 Most Traffic Is Uneven](./module-12-laws-of-scale/92-most-traffic-is-uneven.md) |
| Predictability | — | [94 Goal Is Predictability](./module-12-laws-of-scale/94-the-goal-is-predictability.md) |

### Queues

| Concept | Canonical | Lens |
|---------|-----------|------|
| Message queue | [27 — Message Queue](./module-05-distributed-systems/27-message-queue.md) | [91 Queues Absorb Chaos](./module-12-laws-of-scale/91-queues-absorb-chaos.md), [105 Queues Absorb Uncertainty](./module-13-laws-of-communication/105-queues-absorb-uncertainty.md) |
| Async coupling | — | [104 Async Communication](./module-13-laws-of-communication/104-asynchronous-communication-buys-flexibility.md) |

### Communication & APIs

| Concept | Canonical | Lens (M13 unique starts at 102) |
|---------|-----------|--------------------------------|
| Conversation patterns | [51 — Conversation Patterns](./module-09-apis-for-product-builders/51-conversation-patterns.md) | [95 Every System Is a Conversation](./module-13-laws-of-communication/95-every-system-is-a-conversation.md) |
| Architecture from comms | [69 Communication Determines Architecture](./module-10-laws-of-software-systems/69-communication-determines-architecture.md) | [96 Communication Defines Architecture](./module-13-laws-of-communication/96-communication-defines-architecture.md) |
| REST | [52 — REST](./module-09-apis-for-product-builders/52-rest.md) | [97 Request-Response Default](./module-13-laws-of-communication/97-request-response-is-the-default.md) |
| Webhooks | [53 — Webhooks](./module-09-apis-for-product-builders/53-webhooks.md) | [100 Notifications Reverse Direction](./module-13-laws-of-communication/100-notifications-reverse-direction.md) |
| WebSockets | [54 — WebSockets](./module-09-apis-for-product-builders/54-websockets.md) | [99 Real-Time Has a Cost](./module-13-laws-of-communication/99-real-time-has-a-cost.md) |
| Protocol choice | [57 — API Stack Evolution](./module-09-apis-for-product-builders/57-api-stack-evolution.md) | [98 Simplest Wins](./module-13-laws-of-communication/98-simplest-conversation-wins.md), [107 Different Languages](./module-13-laws-of-communication/107-different-conversations-need-different-languages.md) |
| Contracts, coupling, trust | — | [102–110](./module-13-laws-of-communication/) — **canonical for M13** |

### Data gravity

| Concept | Canonical | Lens |
|---------|-----------|------|
| Information gravity | [67 Information Has Gravity](./module-10-laws-of-software-systems/67-information-has-gravity.md) | [77 Data Creates Gravity](./module-11-laws-of-data/77-data-creates-gravity.md) — data ownership orbit |

### Latency & network

| Concept | Lens by layer |
|---------|---------------|
| Additive latency | [65 Latency Is Additive](./module-10-laws-of-software-systems/65-latency-is-additive.md) — call chains |
| Network is not instant | [87 Networks Are Not Instant](./module-12-laws-of-scale/87-networks-are-not-instant.md) — distributed |
| Browser waterfalls | [116 Network Slower Than Code](./module-14-laws-of-frontend-systems/116-network-is-slower-than-code.md) — frontend |

### Reliability ↔ communication

| Concept | Canonical | Lens |
|---------|-----------|------|
| Retry, idempotency, circuit breaker | [01–03](./module-01-reliability/) | [108–109](./module-13-laws-of-communication/) — link, don't re-teach |

---

## Lens Stub Topics (skip if prerequisite done)

| # | Topic | Prerequisite |
|---|-------|--------------|
| 60 | Closest Copy Wins | 11 Caching or 12 CDN |
| 63 | Read Heavy Wants Caches | 62 Memory Beats Recalculation |
| 68 | Systems Remember To Survive | 62 Memory Beats Recalculation |
| 77 | Data Creates Gravity | 67 Information Has Gravity |
| 79 | Indexes Are Memory | 13 Database Indexing |
| 83 | Faster Horse | 06 Vertical Scaling |
| 84 | Parallel Work | 07 Horizontal Scaling |
| 88 | Replication Buys Availability | 22 Replication |
| 89 | Sharding Buys Capacity | 23 Sharding |
| 95–100 | Communication intro/protocols | Module 9 |
| 105 | Queues Absorb Uncertainty | 91 or 27 Message Queue |
| 107 | Different Languages | Module 9 |
| 115 | Fastest Request Never Made | 66 or 11 Caching |
| 118 | Pagination Controls Growth | 17 Pagination |
| 122 | Load Work Only When Needed | 16 Lazy Loading |
| 128 | Frontend Optimization Universal | 71 Unifying Principle |

---

## Suggested Paths

**Path A — Linear (first-time reader):** Modules 1 → 9 → 10 → 11 → 12 → 13 → 14. Skip lens stubs marked above.

**Path B — Experienced engineer:** Module 10 → pick lens modules by gap (11 data, 12 scale, 13 comms, 14 frontend). Use Phase 1 topics as deep dives when needed.

**Path C — Founder focus:** 7 → 8 → 9 → 10 → 13 (topics 102–110 only) → skim 14 for product conversations with eng.
