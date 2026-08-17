# 12. CDN

> **Think:** *"Can content be closer to users?"*

---

## The 4 Questions

| Question | Answer |
|----------|--------|
| **What problem does it solve?** | Geographic latency — users far from your origin server wait hundreds of milliseconds for static assets (images, JS, CSS, videos). |
| **What happens if I ignore it?** | A user in Chennai loads images from a server in Virginia. 500ms per asset × 40 assets = 20 seconds before the page feels usable. |
| **Where would I use it?** | Product images, JavaScript bundles, CSS, fonts, videos, downloadable PDFs (tickets, invoices), any static or cacheable content. |
| **What companies use it?** | Cloudflare, Akamai, AWS CloudFront, Fastly — used by Amazon, Nykaa, Netflix, every major ecommerce and media site. |

---

## Mental Movie (60 seconds)

A user in Mumbai opens your travel app. The homepage needs 30 images, a 2MB JavaScript bundle, and CSS.

**Without CDN:** All assets come from your server in `us-east-1`. Each request crosses the Atlantic and Indian Ocean. 200–500ms latency per asset. Page feels broken on 4G.

**With CDN:** CloudFront has an edge server in Mumbai. First user pulls assets from origin; CDN caches them locally. Next 10,000 Mumbai users get images from ~20ms away. Page loads in 2 seconds, not 12.

CDN = copy static content to servers near your users.

---

## How It Works

```
User (Mumbai) → CDN Edge (Mumbai) → Cache HIT? Serve immediately
                                 → Cache MISS? Fetch from Origin → Cache → Serve
```

### Request Flow

```mermaid
sequenceDiagram
    participant User as User (Mumbai)
    participant Edge as CDN Edge (Mumbai)
    participant Origin as Origin Server (Virginia)

    User->>Edge: GET /images/hotel-goa.jpg
    Edge->>Edge: Check local cache
    alt Cache HIT
        Edge-->>User: 200 OK (20ms)
    else Cache MISS
        Edge->>Origin: GET /images/hotel-goa.jpg
        Origin-->>Edge: 200 OK + image bytes
        Edge->>Edge: Store in edge cache
        Edge-->>User: 200 OK (350ms first time)
    end
```

**Key ingredients:**
1. **Origin** — your actual server or S3 bucket where files live
2. **Edge locations** — CDN PoPs (points of presence) worldwide
3. **Cache headers** — `Cache-Control: max-age=86400` tells CDN how long to keep files
4. **Cache invalidation** — purge specific URLs or paths when you deploy new assets

### What Belongs on a CDN

| Good for CDN | Bad for CDN |
|--------------|-------------|
| Product images | User-specific cart contents |
| JS/CSS bundles (with hashed filenames) | Personalized API responses |
| Fonts, icons | Real-time inventory counts |
| Video streams | Payment processing |
| Static marketing pages | Session-authenticated data |

---

## Real-World Examples

### Your Travel Platform

**Scenario:** Hotel listing page with 20 thumbnail images per result, 50 results.

```
Origin:      s3://travel-platform-assets/hotels/
CDN:         cdn.travelplatform.com (CloudFront)
URL pattern: https://cdn.travelplatform.com/hotels/treebo-goa-thumb.webp
Headers:     Cache-Control: public, max-age=604800 (7 days)
```

Images are WebP, served from the nearest edge. When you add a new hotel, upload to S3; CDN fetches on first request.

**Without CDN:** 1,000 concurrent users searching Goa = 1,000 × 20 image requests hammering your origin from across India.

### Nykaa

**Scenario:** Product grid on mobile during a sale.

Nykaa serves millions of product images through a CDN:
- Multiple image sizes (thumbnail, zoom, swatch) as separate cached objects
- Image URLs include version hashes so new uploads don't serve stale files
- Mobile users on Jio/Airtel 4G get assets from Mumbai or Delhi edges, not Bangalore HQ

A 200KB product image at 400ms latency feels broken. At 30ms from CDN, it feels instant.

### Amazon

**Scenario:** Product page with 8 images, review photos, "similar items" carousel.

Amazon's CDN (CloudFront + custom edge infrastructure) caches:
- Product images at multiple resolutions
- Static JS/CSS for the storefront
- A+ content images from sellers

Prime Day traffic would crush any single origin. CDN absorbs 95%+ of asset requests at the edge.

---

## When To Use It

| Use a CDN when... | Example |
|-------------------|---------|
| Users are geographically distributed | India + US + Europe customers |
| Pages load many static assets | Ecommerce product grids |
| You serve large files | Video tutorials, high-res images |
| Traffic spikes are unpredictable | Flash sales, viral campaigns |
| Origin bandwidth is expensive | Egress from AWS S3 adds up fast |

## When NOT To Use It

| Skip CDN when... | Why |
|------------------|-----|
| All users are in one city, server is local | CDN adds complexity with minimal gain |
| Content is highly dynamic and user-specific | CDN can't cache "your cart" effectively |
| You're serving a pure API with JSON only | CDN helps static assets; use caching (Topic 11) for API |
| MVP with 5 images total | Overkill; optimize images and compress first |
| Content must never be cached (PCI data) | Security/compliance constraints |

---

## CDN vs Related Concepts

| Concept | Difference |
|---------|------------|
| **Caching (Redis)** | Application-level cache for dynamic data; CDN caches files at network edge |
| **Load balancer** | Distributes requests across app servers; CDN distributes static files globally |
| **Compression** | Shrinks file size; CDN reduces distance files travel |
| **Object storage (S3)** | Where files live; CDN sits in front and caches copies |

**Rule of thumb:** Put every static asset behind a CDN before you optimize anything else. It's the highest ROI performance win for global users.

---

## Problem Simulation

**Situation:** You deploy a new homepage JavaScript bundle. Filename: `app.v2.js`. Your CDN has `app.v1.js` cached with `max-age=31536000` (1 year). You update the HTML to reference `app.v2.js` but forget to purge the old file. Some users still have HTML cached locally referencing `app.v1.js`.

**Questions:**
1. Why did you use `max-age=31536000` on JS files?
2. What's the fix for cache-busting going forward?
3. A user in Kerala reports the site "looks broken" after deploy. What's your first check?

<details>
<summary>Answers</summary>

1. **Immutable assets** — JS bundles with content hashes in the filename never change, so aggressive caching is safe and fast.
2. **Content-hashed filenames:** `app.a3f9b2c.js` instead of `app.v2.js`. New deploy = new filename = automatic cache miss. Never reuse filenames for different content.
3. Check CDN cache status and browser cache for that user. Purge CDN if needed. Verify HTML references the correct hashed bundle. Check for mixed old/new asset versions loading together.

</details>

---

## Key Takeaway

CDN doesn't make your server faster — it eliminates the round trip for static content by serving copies from a server near the user. Pair it with hashed filenames and proper cache headers.

**Next:** [13 — Database Indexing](./13-database-indexing.md) — what happens when the slow part is finding data, not delivering it?
