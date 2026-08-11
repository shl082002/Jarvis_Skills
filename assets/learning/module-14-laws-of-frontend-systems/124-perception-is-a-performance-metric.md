# 124. Law 65: User Perception Is a Performance Metric

> **Think:** *"Does it feel fast — even while still loading?"*

---

## The 4 Questions

| Question | Answer |
|----------|--------|
| **What problem does it solve?** | Blank white screens during load — technically loading in 300ms but feels broken. |
| **What happens if I ignore it?** | Users abandon before content appears. Same LCP, worse conversion without skeletons. |
| **Where would I use it?** | Skeleton screens, progressive loading, optimistic UI, staged content, instant feedback on click. |
| **What companies use it?** | LinkedIn (skeleton feeds), Facebook (placeholder grey boxes), every polished mobile app. |

---

## Mental Movie (60 seconds)

**300ms blank screen** — user wonders if tap registered. Feels slow.

**300ms skeleton layout** — structure visible immediately, content fills in. Feels fast.

**Humans measure perception, not benchmarks.**

Same network time. Different **felt** experience.

---

## How It Works

| Pattern | Perception effect |
|---------|-------------------|
| **Skeleton UI** | Immediate structure |
| **Optimistic update** | Instant feedback on action |
| **Staggered reveal** | Text first, images lazy |
| **Button loading state** | Confirms click registered |
| **Progressive JPEG/blur** | Image "arriving" |

```mermaid
flowchart LR
    A[User Action] --> B[Instant UI Feedback]
    B --> C[Background Load]
    C --> D[Content Replace Skeleton]
```

---

## Real-World Examples

### Your Travel Platform

Search: skeleton cards in 100ms, data fills 400ms later — feels responsive. Booking button → spinner + disabled instantly on click.

### Nykaa

Sale page skeleton grid before products stream in. Cart optimistic add.

### Amazon

Placeholder boxes on search. 1-click immediate acknowledgment.

---

## Connection To Other Laws

| Law | Link |
|-----|------|
| Law 52 | User experiences perception |
| Law 115 | Show cached data instantly |

---

## Key Takeaway

Optimize felt speed — skeletons, optimistic UI, instant feedback. Perceived performance is a product metric, not just Lighthouse scores.

**Next:** [125 — Frontend Is a Distributed System](./125-frontend-is-a-distributed-system.md)
