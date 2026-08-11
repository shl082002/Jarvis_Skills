# 121. Law 62: Code Has Weight

> **Think:** *"What does shipping this 400KB library cost on 4G?"*

---

## The 4 Questions

| Question | Answer |
|----------|--------|
| **What problem does it solve?** | Bundle bloat — importing all of lodash, moment, chart library on homepage. |
| **What happens if I ignore it?** | 800KB JS bundle, 3s parse on mid Android, high bounce before user sees content. |
| **Where would I use it?** | Bundle analysis, tree-shaking, dependency audits, framework choice. |
| **What companies use it?** | Every perf-conscious web team — bundle budgets in CI. |

---

## Mental Movie (60 seconds)

Every JavaScript byte costs:
```
Download (network) → Parse (CPU) → Compile (CPU) → Execute (CPU)
```

**2MB bundle on 4G:** 4s download + 1s parse = **5s before interactive**.

**200KB bundle:** 0.8s + 0.2s = **1s interactive**.

**Ship less code.**

---

## How It Works

| Technique | Effect |
|-----------|--------|
| Tree-shaking | Dead code elimination |
| Dynamic import | Split chunks (Law 122) |
| Replace heavy libs | `date-fns` not `moment` |
| Analyze bundle | `webpack-bundle-analyzer` |
| Bundle budget CI | Fail PR if > 250KB |

---

## Real-World Examples

### Your Travel Platform

Homepage accidentally imports admin chart library — 300KB. Fix: route-level code split, admin only.

### Nykaa

Strict bundle budgets. Third-party scripts audited.

### Amazon

Minimal critical path JS. Defer non-essential.

---

## Key Takeaway

Audit bundle size like backend audits query time. Every dependency has download + parse cost — ship less.

**Next:** [122 — Load Work Only When Needed](./122-load-work-only-when-needed.md)
