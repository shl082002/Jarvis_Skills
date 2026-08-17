# 125. Law 66: Frontend Is a Distributed System

> **Think:** *"What can fail between the user and confirmed booking?"*

---

## The 4 Questions

| Question | Answer |
|----------|--------|
| **What problem does it solve?** | Treating frontend as isolated UI — ignoring CDN, API, auth, payment, analytics failure modes. |
| **What happens if I ignore it?** | Razorpay script fails to load — checkout dead. API timeout — blank page no error boundary. |
| **Where would I use it?** | Error boundaries, retry UI, offline states, third-party script fallbacks, timeout handling. |
| **What companies use it?** | Resilient checkout flows — Stripe.js load failure handling, graceful degradation. |

---

## Mental Movie (60 seconds)

Modern frontend talks to:
```
Browser runtime
CDN (images, JS)
Your API
Auth provider (OAuth)
Razorpay/Stripe.js
Google Analytics
Map provider
Supplier widget
```

**Any can fail.** Network partition on mobile. CDN 503. Payment SDK blocked by ad blocker.

**Frontend applications are distributed systems with user interfaces.**

> **Module 13: Law 36** — every system is conversations. **Module 13: Law 50** — failures normal. Frontend is a **node** in that distributed graph.

---

## How It Works

| Failure | UX response |
|---------|-------------|
| API timeout | Retry button + message |
| Payment SDK fail | "Try again" + support link |
| Image CDN fail | Fallback placeholder |
| Auth expired | Redirect login |
| Partial data | Render what loaded |

Error boundaries, React Query retry, offline detection, circuit-breaker-style "degraded mode."

---

## Real-World Examples

### Your Travel Platform

Checkout: API down → "Can't reach server, bookings saved locally?" no — clear error, retry. Razorpay blocked → detect, show alternate payment message.

### Nykaa

Graceful catalog degradation if recommendations API fails — show catalog without "you may also like."

---

## Key Takeaway

Design frontend for partial failure — error boundaries, retries, fallbacks, clear user messaging. The browser is one node in a distributed system.

**Next:** [126 — UI Is a Projection of Data](./126-ui-is-a-projection-of-data.md)
