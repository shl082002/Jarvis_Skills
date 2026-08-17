# 127. Law 68: Complexity Flows Toward the Client

> **Think:** *"Why is validation in both API and form — and is that intentional?"*

---

## The 4 Questions

| Question | Answer |
|----------|--------|
| **What problem does it solve?** | Surprise client-side growth — SPAs accumulating business logic that used to live server-side. |
| **What happens if I ignore it?** | 400KB app doing pricing, validation, tax — hard to test, security gaps if server trusts client. |
| **Where would I use it?** | Deciding what runs client vs server, optimistic UI, offline mode, BFF vs fat client. |
| **What companies use it?** | Notion, Figma, Gmail — rich clients. Banks — thin client, server validates all. |

---

## Mental Movie (60 seconds)

As apps mature, **more moves to browser:**
- Form validation (instant UX)
- Client-side routing
- Caching and offline
- Optimistic updates
- Client-side search/filter
- Feature flags, A/B logic

**1990s:** HTML documents from server.
**2020s:** Applications in browser.

**Modern frontend systems behave like applications, not documents.**

Architect must **choose** what migrates client-ward vs stays server-side (security, truth).

---

## How It Works

| Move to client when... | Keep on server when... |
|----------------------|------------------------|
| **UX** needs instant feedback | **Security** critical |
| **Offline** required | **Money/pricing** authoritative |
| **Reduce round trips** | **Business rules** must not leak |
| **Personalization** cheap client-side | **Audit** trail server-side |

**Rule:** Client optimizes experience. Server enforces truth.

---

## Real-World Examples

### Your Travel Platform

**Client:** date picker validation, search filters, optimistic "booking pending" UI.

**Server:** final price, inventory hold, payment charge, tax calculation.

### Nykaa

Client: cart UX, browse filters. Server: inventory, price at checkout.

### Figma

Extreme: most logic client — collaborative app paradigm.

---

## Key Takeaway

Expect growing client complexity in mature SPAs — but deliberately. UX on client, authority on server.

**Next:** [128 — Frontend Optimization Is Universal](./128-frontend-optimization-is-universal.md)
