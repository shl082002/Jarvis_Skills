# Founder-Architect Handbook — Full Roadmap

One topic per day. 128 topics across 14 modules. For each: read 10 minutes, run the AI learning loop, move on.

**Two tracks:** Modules **1–9** teach tools (canonical, ~10 min each). Modules **10–14** teach lenses — many topics are **~3 min stubs** if you already read Phase 1. See **[CONCEPT-INDEX.md](./CONCEPT-INDEX.md)** before Module 10.

**Goal:** Recognition, not mastery. See the mental movie when someone names the concept.

---

## Module 1: Reliability
*These concepts prevent your product from breaking.*

| # | Topic | Description |
|---|-------|-------------|
| 1 | **Idempotency** | Makes duplicate requests safe — same operation twice produces the same result as once. Without it: double payments, double bookings, double refunds. Think: *"What if user clicks twice?"* |
| 2 | **Retry Pattern** | Automatically re-attempts failed calls when the failure is temporary (timeouts, 503s). Must pair with idempotency. Think: *"Maybe the service is temporarily unavailable."* |
| 3 | **Circuit Breaker** | Stops calling a failing dependency after a threshold, preventing cascading outages. Opens, half-opens, closes. Think: *"Stop calling the broken service."* |
| 4 | **High Availability** | Design so no single component failure takes the system down. Multiple servers, replicas, zones. Think: *"What if this machine disappears?"* |
| 5 | **Failover** | Automatic handoff from failed primary to standby — database promotion, supplier switch, DNS reroute. Think: *"Who takes over when this fails?"* |

**Status:** ✅ Docs + PDFs ready → [`module-01-reliability/`](./module-01-reliability/)

---

## Module 2: Scale
*These concepts help you survive growth.*

| # | Topic | Description |
|---|-------|-------------|
| 6 | **Vertical Scaling** | Bigger machine — more CPU, RAM, disk on one box. Fast to do, hard ceiling eventually. Example: 4GB RAM → 32GB RAM. |
| 7 | **Horizontal Scaling** | More machines doing the same job. The path to real scale, but requires stateless services and load distribution. Example: 1 server → 10 servers. |
| 8 | **Load Balancer** | Distributes incoming traffic across multiple servers. Prevents one server from being overwhelmed. Think: *"Which server gets this request?"* |
| 9 | **Rate Limiting** | Caps how many requests a user/IP/API key can make in a time window. Protects against abuse, scrapers, and accidental DDoS from your own retries. |
| 10 | **Backpressure** | Signals upstream to slow down when downstream is overwhelmed. Prevents queues from growing unbounded and systems from OOM-crashing. |

**Status:** ✅ Docs + PDFs ready → [`module-02-scale/`](./module-02-scale/)

---

## Module 3: Performance
*These concepts make systems fast.*

| # | Topic | Description |
|---|-------|-------------|
| 11 | **Caching** | Store expensive computation or DB results in fast memory (Redis, in-process). Trade freshness for speed. Think: *"Can I remember this answer?"* |
| 12 | **CDN** | Distribute static content (images, JS, CSS) to edge servers near users globally. Cuts latency from 500ms to 50ms for assets. |
| 13 | **Database Indexing** | Data structures (B-tree, hash) that let the DB find rows without full table scans. Wrong indexes = slow queries at scale. |
| 14 | **Query Optimization** | Write smarter SQL — avoid N+1 queries, select only needed columns, use joins efficiently. Often bigger wins than adding hardware. |
| 15 | **Connection Pooling** | Reuse DB/network connections instead of opening a new one per request. Opening connections is expensive; pools keep warm connections ready. |
| 16 | **Lazy Loading** | Fetch data only when needed, not upfront. Reduces initial payload and memory. Trade-off: may cause latency spikes on first access. |
| 17 | **Pagination** | Return data in chunks (page 1, page 2…) instead of entire result sets. Essential for search results, order history, feeds. |
| 18 | **Compression** | Shrink payloads with gzip/brotli before sending over the network. Smaller responses = faster loads, especially on mobile networks. |

**Status:** ✅ Docs + PDFs ready → [`module-03-performance/`](./module-03-performance/)

---

## Module 4: Data Systems
*How data stays correct, available, and fast.*

| # | Topic | Description |
|---|-------|-------------|
| 19 | **ACID** | Atomicity, Consistency, Isolation, Durability — the guarantees of a reliable database transaction. Either everything commits or nothing does. |
| 20 | **Transactions** | Group multiple operations into one atomic unit. If any step fails, all steps roll back. Prevents partial updates (money deducted but order not created). |
| 21 | **Eventual Consistency** | In distributed systems, replicas may temporarily disagree but converge over time. Trade strong consistency for availability and partition tolerance. |
| 22 | **Replication** | Copy data to multiple nodes for read scaling and fault tolerance. Primary handles writes, replicas serve reads. Replication lag is the key risk. |
| 23 | **Sharding** | Split data across multiple databases by a key (user_id, region). Each shard holds a slice. Solves single-DB size limits but complicates queries. |
| 24 | **Partitioning** | Divide a large table into smaller physical pieces within one database. Often a precursor to sharding. Improves query performance on large datasets. |
| 25 | **Normalization** | Organize data to reduce redundancy — no duplicate customer info across 50 order rows. Cleaner writes, but joins get expensive at read time. |
| 26 | **Denormalization** | Intentionally duplicate data to speed up reads. Store customer name on the order row to avoid a join. Trade storage for query speed. |

**Status:** ✅ Docs + PDFs ready → [`module-04-data-systems/`](./module-04-data-systems/)

---

## Module 5: Distributed Systems
*The magic behind Uber, Amazon, Airbnb.*

| # | Topic | Description |
|---|-------|-------------|
| 27 | **Message Queue** | Decouple producers from consumers — send work to a queue, process it asynchronously later. Handles traffic spikes and slow downstream services. |
| 28 | **Pub/Sub** | One event published, many subscribers notified. Looser than a queue — subscribers don't compete for messages, they each get a copy. |
| 29 | **Event-Driven Architecture** | Services react to events instead of direct calls. BookingCreated → trigger payment, notification, analytics. Loose coupling, harder to trace. |
| 30 | **CQRS** | Command Query Responsibility Segregation — separate read and write models. Optimize writes for consistency, reads for speed. Adds complexity, big wins at scale. |
| 31 | **Event Sourcing** | Store every state change as an immutable event log, not just current state. Full audit trail, time-travel debugging. Replay events to rebuild state. |
| 32 | **Saga Pattern** | Coordinate multi-service transactions with compensating actions. If hotel books but flight fails, cancel the hotel. Distributed alternative to ACID. |
| 33 | **Dead Letter Queue** | Parking lot for messages that failed processing after all retries. Prevents poison messages from blocking the queue. Requires monitoring and manual replay. |
| 34 | **Distributed Transactions** | Keep multiple services consistent across a single logical operation. Hard problem — 2PC is slow, sagas are complex. Usually avoided in favor of eventual consistency. |

**Status:** ✅ Docs + PDFs ready → [`module-05-distributed-systems/`](./module-05-distributed-systems/)

---

## Module 6: Infrastructure
*The plumbing that keeps everything running.*

| # | Topic | Description |
|---|-------|-------------|
| 35 | **DNS** | Translates domain names (yoursite.com) to IP addresses. First hop in every request. TTL, health-checked failover, and CDN integration matter. |
| 36 | **Reverse Proxy** | Sits in front of your app servers — handles SSL termination, routing, caching, rate limiting. Nginx, AWS ALB, Cloudflare. |
| 37 | **SSL/TLS** | Encrypts data in transit between client and server. Non-negotiable for any production system handling user data or payments. |
| 38 | **Containers** | Package app + dependencies into a portable unit (Docker). Runs the same on your laptop, staging, and production. Foundation for modern deployment. |
| 39 | **Container Orchestration** | Manages thousands of containers — scheduling, scaling, health checks, rolling deploys. Kubernetes is the standard; managed K8s (EKS, GKE) reduces ops burden. |
| 40 | **CI/CD** | Continuous Integration / Continuous Deployment — automated build, test, and deploy pipeline. Every commit can reach production safely with gates and rollbacks. |
| 41 | **Blue-Green Deployment** | Run two identical environments. Deploy to green, switch traffic from blue, keep blue as instant rollback. Zero-downtime deploys. |
| 42 | **Rolling Deployment** | Replace instances gradually — old and new versions run side by side during rollout. Slower rollback than blue-green, but uses less infrastructure. |

**Status:** ✅ Docs + PDFs ready → [`module-06-infrastructure/`](./module-06-infrastructure/)

---

## Module 7: Product Thinking
*Build the right thing, not just build things right.*

| # | Topic | Description |
|---|-------|-------------|
| 43 | **Product Market Fit** | The moment when your product satisfies strong market demand. Users pull the product out of your hands. Before PMF: iterate fast. After PMF: scale. |
| 44 | **Jobs To Be Done** | Customers don't buy products — they hire them to do a job. "Book a hassle-free family vacation" not "search flights." Design for the job, not the feature. |
| 45 | **North Star Metric** | The single metric that best captures the core value you deliver. Airbnb: nights booked. Spotify: time spent listening. Aligns the entire team on what matters. |
| 46 | **Conversion Funnel** | Map the steps from awareness to action (visit → search → select → pay → confirm). Find where users drop off. Fix the biggest leak first. |

**Status:** ✅ Docs + PDFs ready → [`module-07-product-thinking/`](./module-07-product-thinking/)

---

## Module 8: Business Thinking
*The numbers behind sustainable products.*

| # | Topic | Description |
|---|-------|-------------|
| 47 | **CAC** (Customer Acquisition Cost) | Total sales + marketing spend ÷ new customers acquired. If CAC > LTV, you lose money on every customer. Must trend down or LTV must go up. |
| 48 | **LTV** (Lifetime Value) | Total revenue a customer generates over their entire relationship. LTV:CAC ratio of 3:1+ is healthy. Drives decisions on how much you can spend to acquire. |
| 49 | **Churn** | Rate at which customers stop using/paying. 5% monthly churn = you lose half your customers every year. Cheaper to retain than acquire. |
| 50 | **Network Effects** | Product becomes more valuable as more people use it. WhatsApp, Uber, LinkedIn. Creates defensible moats — but cold-start problem is brutal. |

**Status:** ✅ Docs + PDFs ready → [`module-08-business-thinking/`](./module-08-business-thinking/)

---

## Module 9: APIs For Product Builders
*What kind of conversation is happening between these systems?*

| # | Topic | Description |
|---|-------|-------------|
| 51 | **Conversation Patterns** | Every API is a type of conversation — ask/answer, notify, stream, flexible fetch, machine-to-machine. Start here, not with technology names. |
| 52 | **REST** | Request → response. Ask for the menu, get the menu, conversation ends. Default for CRUD, booking, most startup backends. |
| 53 | **Webhooks** | Another system knows first — "call me when the pizza is ready." Payments, shipping, supplier confirmations. Don't poll. |
| 54 | **WebSockets** | Stay connected, keep talking. Live tracking, chat, trading, real-time dashboards. Server pushes without client asking. |
| 55 | **GraphQL** | Buffet not fixed meal — client picks exactly the fields needed from many sources in one request. Mobile/super-app screens. |
| 56 | **gRPC** | Private high-speed railway between backend services. Binary, typed, fast. Internal only — customers never see it. |
| 57 | **API Stack Evolution** | REST → Webhooks → WebSockets → GraphQL → gRPC as your product grows. Add protocols when conversation patterns demand them. |

**Status:** ✅ Docs + PDFs ready → [`module-09-apis-for-product-builders/`](./module-09-apis-for-product-builders/)

---

## Module 10: The Laws of Software Systems
*Notes from the journey beyond frameworks*

| # | Topic | Description |
|---|-------|-------------|
| 58 | **Principles Over Frameworks** | Tools change; forces don't. Train the systems thinker lens — time, memory, work, distance, communication. |
| 59 | **Work Cannot Be Destroyed** | You can't eliminate work, only move it. Request time → batch time, backend → frontend. Optimization is relocation. |
| 60 | **The Closest Copy Wins** *(lens)* | Distance lens on caching/CDN — read [11 Caching](./module-03-performance/11-caching.md) first. |
| 61 | **Repetition Is The Enemy** | Doing the same thing twice is expensive. N+1 queries, repeated fetches, connection storms — find and kill the repeat. |
| 62 | **Memory Beats Recalculation** | **Memory cluster core** — caching, read/write ratio, layers of memory. |
| 63 | **Read Heavy Wants Caches** *(lens)* | Read-ratio diagnostic — extends [62](./module-10-laws-of-software-systems/62-memory-beats-recalculation.md). |
| 64 | **Freshness Fights Speed** | How stale are you willing to be? Country list: hours. Stock price: zero. No universal answer. |
| 65 | **Latency Is Additive** | Many 50ms cuts = 200ms wound. Parallelize, merge, cache — optimize the chain, not just links. |
| 66 | **Fastest Request Never Made** | Eliminating beats optimizing. Browser cache, prefetch, static generation — zero requests wins. |
| 67 | **Information Has Gravity** | Important data pulls systems toward it. Architecture becomes managing data movement. |
| 68 | **Systems Remember To Survive** *(lens)* | Memory-layer stack — extends [62](./module-10-laws-of-software-systems/62-memory-beats-recalculation.md). |
| 69 | **Communication Determines Architecture** | Technology follows conversation patterns. Ties to Module 9. |
| 70 | **Scale Is Avoiding Work** | Before adding servers — cache, paginate, queue, batch. Scale what remains. |
| 71 | **The Unifying Principle** | One question: "Can I avoid doing this again?" All laws, one thread. |

**Status:** ✅ Docs + PDFs ready → [`module-10-laws-of-software-systems/`](./module-10-laws-of-software-systems/)

---

## Module 11: The Laws of Data
*Chapter 2 — why data becomes the business*

| # | Topic | Description |
|---|-------|-------------|
| 72 | **Data Lives Longer Than Code** | Code is rewritten; customer records, bookings, and audit trails survive. Protecting and migrating data beats deploying new code. |
| 73 | **Every Data Element Needs an Owner** | Multiple services writing the same data creates conflicts. One source of truth, one owning team, many readers. |
| 74 | **Every Copy Creates Responsibility** | Redis, CDN, replicas — every cache is a consistency problem. Who invalidates, how stale, what fails? |
| 75 | **Consistency Has a Cost** | Fast, available, and perfectly consistent — pick two at scale. Strong at checkout, eventual on browse. |
| 76 | **Reads and Writes Are Different Workloads** | One booking write vs 100K search reads. Replicas, search indexes, CQRS — optimize independently. |
| 77 | **Data Creates Gravity** *(lens)* | Data-architect orbit — read [67](./module-10-laws-of-software-systems/67-information-has-gravity.md) first. |
| 78 | **Every Query Is a Question** | `SELECT *` vs precise filter. Better questions beat bigger servers. EXPLAIN before ship. |
| 79 | **Indexes Are Memory for Databases** *(lens)* | Index = DB memory — read [13 Indexing](./module-03-performance/13-database-indexing.md) first. |
| 80 | **Moving Data Is More Expensive Than Storing It** | Storage is cheap; cross-region egress and chatty APIs are not. Store freely, move carefully. |
| 81 | **Every Software System Is a Memory System** | Receive → remember → retrieve. DB, cache, queue, CDN — memory layers with different durability. |

**Status:** ✅ Docs ready → [`module-11-laws-of-data/`](./module-11-laws-of-data/)

---

## Module 12: The Laws of Scale
*Chapter 3 — what breaks when growth stresses the system*

| # | Topic | Description |
|---|-------|-------------|
| 82 | **Every System Has a Bottleneck** | Capacity is set by the weakest link — find it before scaling anything. |
| 83 | **A Faster Horse Does Not Fix Traffic** *(lens)* | Vertical ceiling metaphor — read [06 Vertical Scaling](./module-02-scale/06-vertical-scaling.md) first. |
| 84 | **Parallel Work Creates Scale** *(lens)* | Independence requirement — read [07 Horizontal Scaling](./module-02-scale/07-horizontal-scaling.md) first. |
| 85 | **Shared Resources Become Contested** | Growth turns shared DBs and APIs into competition zones. |
| 86 | **Distribution Creates Complexity** | Many machines trade simplicity for scale — partial failures, tracing, sagas. |
| 87 | **Networks Are Not Instant** | Remote calls carry latency and failure risk — batch, cache, parallelize. |
| 88 | **Replication Buys Availability** *(lens)* | Availability framing — read [22 Replication](./module-04-data-systems/22-replication.md) first. |
| 89 | **Sharding Buys Capacity** *(lens)* | Capacity framing — read [23 Sharding](./module-04-data-systems/23-sharding.md) first. |
| 90 | **Availability and Consistency Compete** *(lens)* | CAP at scale — read [21 Eventual Consistency](./module-04-data-systems/21-eventual-consistency.md) first. |
| 91 | **Queues Absorb Chaos** *(lens)* | Spike lens — read [27 Message Queue](./module-05-distributed-systems/27-message-queue.md) first. |
| 92 | **Most Traffic Is Uneven** | Design for peak minute, not average hour. |
| 93 | **Scale Amplifies Small Mistakes** | N+1 and missing indexes invisible at 10 users, fatal at 1M. |
| 94 | **The Goal Is Predictability** | Stable p99 beats occasional 10ms — users trust consistency. |

**Status:** ✅ Docs ready → [`module-12-laws-of-scale/`](./module-12-laws-of-scale/)

---

## Module 13: The Laws of Communication
*Chapter 4 — who talks to whom, about what, and when*

| # | Topic | Description |
|---|-------|-------------|
| 95 | **Every System Is a Conversation** *(lens)* | Mindset intro — read [51 Conversation Patterns](./module-09-apis-for-product-builders/51-conversation-patterns.md) first. |
| 96 | **Communication Defines Architecture** *(lens)* | Flow lens — read [69](./module-10-laws-of-software-systems/69-communication-determines-architecture.md) first. |
| 97 | **Request-Response Is the Default** *(lens)* | Default conversation — read [52 REST](./module-09-apis-for-product-builders/52-rest.md) first. |
| 98 | **Simplest Conversation Wins** *(lens)* | Anti-over-engineering — read Module 9 first. |
| 99 | **Real-Time Has a Cost** *(lens)* | Cost tradeoff — read [54 WebSockets](./module-09-apis-for-product-builders/54-websockets.md) first. |
| 100 | **Notifications Reverse the Direction** *(lens)* | Push direction — read [53 Webhooks](./module-09-apis-for-product-builders/53-webhooks.md) first. |
| 101 | **Machines Prefer Structured Conversations** | Explicit schemas — amount_paise not "amount". |
| 102 | **Contracts Outlive Implementations** | API shape survives backend rewrites — protect it. |
| 103 | **Communication Creates Coupling** | More direct paths = more dependency blast radius. |
| 104 | **Asynchronous Communication Buys Flexibility** | Time becomes a resource — defer non-critical talk. |
| 105 | **Queues Absorb Uncertainty** *(lens)* | Uncertainty lens — read [91](./module-12-laws-of-scale/91-queues-absorb-chaos.md) or [27 Queue](./module-05-distributed-systems/27-message-queue.md) first. |
| 106 | **Events Describe Facts** | BookingCreated not SendEmail — subscribers react independently. |
| 107 | **Different Conversations Need Different Languages** *(lens)* | Protocol picker — read Module 9 first. |
| 108 | **Reliability Over Speed** | Delivered beats fast — retries and durable queues. |
| 109 | **Communication Failures Are Normal** | Timeouts, circuit breakers, idempotency — design for failure. |
| 110 | **Communication Is a Trust Problem** | Auth, signatures, TLS — verify who spoke. |

**Status:** ✅ Docs ready → [`module-13-laws-of-communication/`](./module-13-laws-of-communication/)

---

## Module 14: The Laws of Frontend Systems
*Chapter 5 — the browser as distributed runtime*

| # | Topic | Description |
|---|-------|-------------|
| 111 | **The User Experiences the Frontend** | Users see speed and stability — not microservices diagrams. |
| 112 | **Rendering Is Work** | Style, layout, paint — every pixel costs CPU. |
| 113 | **State Is Memory** | React state, Query cache, localStorage — memory layers. |
| 114 | **Server State ≠ Client State** | Remote data needs sync tools, not raw useState. |
| 115 | **The Fastest Request Is Never Made** *(lens)* | Browser layer — read [66](./module-10-laws-of-software-systems/66-fastest-request-never-made.md) first. |
| 116 | **Network Is Slower Than Code** | Waterfalls beat slow components on mobile. |
| 117 | **Loading Everything Is Rarely Correct** | Slim fields, current screen only. |
| 118 | **Pagination Controls Growth** *(lens)* | Growth framing — read [17 Pagination](./module-03-performance/17-pagination.md) first. |
| 119 | **Virtualization Controls Rendering** | DOM for visible rows only. |
| 120 | **Re-Renders Are Repeated Work** | Memo, colocate state, measure first. |
| 121 | **Code Has Weight** | Download + parse cost per KB of JS. |
| 122 | **Load Work Only When Needed** *(lens)* | Code-splitting — read [16 Lazy Loading](./module-03-performance/16-lazy-loading.md) first. |
| 123 | **Images Dominate Assets** | WebP, srcset, lazy — bytes before algorithms. |
| 124 | **Perception Is a Performance Metric** | Skeletons and optimistic UI feel fast. |
| 125 | **Frontend Is a Distributed System** | CDN, API, payment SDK — all can fail. |
| 126 | **UI Is a Projection of Data** | Components render truth; don't duplicate. |
| 127 | **Complexity Flows Toward the Client** | SPAs are apps — UX client, authority server. |
| 128 | **Frontend Optimization Is Universal** *(capstone)* | Maps Module 10 laws to browser — read [71](./module-10-laws-of-software-systems/71-the-unifying-principle.md) first. |

**Status:** ✅ Docs ready → [`module-14-laws-of-frontend-systems/`](./module-14-laws-of-frontend-systems/)

---

## Suggested Pace

| Phase | Modules | Days | Focus |
|-------|---------|------|-------|
| **Recognition** | 1–2 (Reliability + Scale) | ~10 | Don't break, don't drown |
| **Recognition** | 3–4 (Performance + Data) | ~16 | Fast and correct — **canonical for caching, CAP, replication** |
| **Recognition** | 5–6 (Distributed + Infra) | ~16 | Queues, events, deploy |
| **Founder lens** | 7–8 (Product + Business) | ~8 | Build the right thing profitably |
| **Recognition** | 9 (APIs) | ~7 | Protocols by conversation — **canonical before Module 13** |
| **Lenses** | 10 (Laws) | ~10 | Forces beneath frameworks; **skip lens stubs 60, 63, 68 if short on time** |
| **Lenses** | 11 (Data) | ~8 | Ownership, copies, queries; skip 77, 79 if done 67, 13 |
| **Lenses** | 12 (Scale) | ~9 | Bottlenecks 82–87, 92–94 are core; skip 83–84, 88–89, 91 if done M2/M4/M5 |
| **Lenses** | 13 (Communication) | ~10 | **Focus 101–110**; skim or skip 95–100, 105, 107 if done M9 |
| **Lenses** | 14 (Frontend) | ~14 | Browser runtime; skip 115, 118, 122, 128 if done prerequisites |

**Total:** ~108 full reads + ~20 lens stubs ≈ **~98–110 days** at one topic/day (vs ~130 if every topic read at full length).

See **[CONCEPT-INDEX.md](./CONCEPT-INDEX.md)** for skip rules.

---

## Progress Tracker

```
Module 1: Reliability        [█████] 5/5  ✅
Module 2: Scale              [█████] 5/5  ✅
Module 3: Performance        [████████] 8/8  ✅
Module 4: Data Systems       [████████] 8/8  ✅
Module 5: Distributed        [████████] 8/8  ✅
Module 6: Infrastructure     [████████] 8/8  ✅
Module 7: Product Thinking   [████] 4/4  ✅
Module 8: Business Thinking  [████] 4/4  ✅
Module 9: APIs               [███████] 7/7  ✅
Module 10: Laws              [██████████████] 14/14  ✅
Module 11: Laws of Data      [██████████] 10/10  ✅
Module 12: Laws of Scale     [█████████████] 13/13  ✅
Module 13: Laws of Comm      [████████████████] 16/16  ✅
Module 14: Laws of Frontend  [██████████████████] 18/18  ✅
                             ─────────
                             128/128 docs ready ✅
```

Update this as you finish each topic.
