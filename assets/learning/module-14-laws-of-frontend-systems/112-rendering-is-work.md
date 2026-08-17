# 112. Law 53: Rendering Is Work

> **Think:** *"What does the browser actually do to show this page?"*

---

## The 4 Questions

| Question | Answer |
|----------|--------|
| **What problem does it solve?** | Treating UI as free — adding components, animations, and DOM nodes without CPU/memory cost. |
| **What happens if I ignore it?** | 500-component page, main thread blocked 2s, scroll jank, mobile devices heat up and lag. |
| **Where would I use it?** | Large lists, heavy dashboards, animation design, React performance, mobile optimization. |
| **What companies use it?** | Facebook (virtualized feeds), Airbnb (list virtualization), any data-heavy UI. |

---

## Mental Movie (60 seconds)

Every pixel on screen requires browser pipeline:

```
JavaScript → Style → Layout → Paint → Composite
```

**Each UI element:**
- Participates in layout calculation
- May trigger paint
- Consumes memory in DOM

**10,000 hotel cards in DOM** = massive layout + paint work, even if CSS hides them.

**Every element on the screen has a cost.**

---

## How It Works

```mermaid
flowchart LR
    JS[JavaScript / React] --> ST[Style]
    ST --> LY[Layout]
    LY --> PA[Paint]
    PA --> CO[Composite]
    CO --> SCR[Screen]
```

| Stage | Triggered by | Cost |
|-------|--------------|------|
| **Style** | Class/state change | All affected nodes |
| **Layout** | Geometry change | Reflow — expensive |
| **Paint** | Visual change | Repaint pixels |
| **Composite** | Transform/opacity only | Cheapest animation |

---

## Real-World Examples

### Your Travel Platform

**Heavy:** Render 500 search results as full card components with images — 2s main thread block on mid-range Android.

**Lighter:** Virtualized list — 20 DOM nodes, smooth scroll (Law 119).

### Nykaa

Product grid virtualization on mobile. Infinite scroll without infinite DOM.

### Amazon

Search results paginated + lazy images. Rendering budget managed per page.

---

## When Rendering Cost Bites

| Signal | Fix direction |
|--------|---------------|
| Long tasks in Performance tab | Reduce DOM, memo, virtualize |
| Scroll jank | Virtualization, `will-change` sparingly |
| Fan-out re-renders | Law 120 |
| Large lists | Law 119 |

---

## Connection To Other Laws & Modules

| Connection | Link |
|------------|------|
| Law 119 | Virtualization |
| Law 120 | Re-renders |
| Law 121 | Less JS = less render trigger |

---

## Problem Simulation

Search page mounts 200 `<HotelCard>` with full image load. LCP 4.8s, scroll FPS 30 on mobile.

**Questions:**
1. Which law applies?
2. Two fixes?
3. Paint vs layout — animating `width` vs `transform`?

<details>
<summary>Answers</summary>

1. **Law 53** — rendering work scales with DOM and paint.
2. **Virtualize** (Law 119), **lazy images** (Law 123), **pagination** (Law 118).
3. **`transform` compositor-only** — cheaper. `width` triggers layout every frame.

</details>

---

## Key Takeaway

Rendering is real CPU and memory work — style, layout, paint, composite. Fewer nodes, smarter updates, virtualize long lists.

**Next:** [113 — State Is Memory](./113-state-is-memory.md)
