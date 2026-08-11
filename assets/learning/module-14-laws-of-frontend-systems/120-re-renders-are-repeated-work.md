# 120. Law 61: Re-Renders Are Repeated Work

> **Think:** *"Did anything visible actually change — or did we redo layout for nothing?"*

---

## The 4 Questions

| Question | Answer |
|----------|--------|
| **What problem does it solve?** | Unnecessary React re-renders — parent state change re-rendering 200 children, new object refs every render. |
| **What happens if I ignore it?** | Typing in search box re-renders entire page. Context update repaints 500 components. |
| **Where would I use it?** | React.memo, useMemo, useCallback, state colocation, context splitting, React Compiler. |
| **What companies use it?** | Meta (React performance docs), every large React codebase. |

---

## Mental Movie (60 seconds)

Every re-render repeats:
```
Reconcile virtual DOM → diff → style → layout → paint
```

**Parent `count` changes → 200 `HotelCard` children re-render** — same props, same output, full pipeline cost.

**Avoid repeating work that produces the same result.**

> **Module 10: Law 3** — repetition is the enemy. Frontend manifestation: unnecessary re-renders.

---

## How It Works

| Cause | Fix |
|-------|-----|
| Parent re-render | `React.memo` on children |
| New function/object props | `useCallback`, `useMemo` |
| Global context update | Split contexts, colocate state |
| Unstable keys | Stable `key={id}` |
| Too much in one store | Colocate state near usage |

---

## Real-World Examples

### Your Travel Platform

Search input in header — state in header only, not root App. Results list memoized. Expensive map component isolated.

### Nykaa

Filter state colocated to filter panel. Product cards memoized with stable props.

---

## When To Optimize Re-Renders

| Optimize when... | Skip when... |
|--------------------|--------------|
| Profiler shows wasted renders | Premature — measure first |
| Large lists re-render on keystroke | Small forms |
| Measurable jank | Law 116 network is real issue |

---

## Key Takeaway

Measure with React Profiler. Colocate state, memoize expensive children, stabilize props — don't re-render what hasn't changed.

**Next:** [121 — Code Has Weight](./121-code-has-weight.md)
