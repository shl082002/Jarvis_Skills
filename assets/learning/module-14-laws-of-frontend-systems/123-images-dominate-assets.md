# 123. Law 64: Images Are Usually the Largest Assets

> **Think:** *"Is this 2MB hero JPEG the real LCP problem?"*

---

## The 4 Questions

| Question | Answer |
|----------|--------|
| **What problem does it solve?** | Optimizing JavaScript while 3MB of images dominate LCP — wrong layer. |
| **What happens if I ignore it?** | LCP 4s on hotel photos. Mobile data exhaustion. Poor Core Web Vitals. |
| **Where would I use it?** | Image CDN, WebP/AVIF, responsive `srcset`, lazy loading, compression. |
| **What companies use it?** | Every image-heavy site — Cloudinary, Imgix, Next/Image. |

---

## Mental Movie (60 seconds)

Typical travel search page weight:
```
JavaScript:  200KB
CSS:          50KB
Images:     2,500KB  ← 90% of bytes
```

Optimizing React `useMemo` won't fix LCP if hero image is 800KB PNG.

**Optimize bytes before optimizing algorithms.**

---

## How It Works

| Technique | Savings |
|-----------|---------|
| **WebP/AVIF** | 30–50% vs JPEG |
| **Responsive srcset** | Right size per viewport |
| **Lazy load** below fold | Defer offscreen |
| **CDN resize** | `?w=400&q=80` |
| **Blur placeholder** | Law 124 perception |
| **Compression** | Module 3 |

---

## Real-World Examples

### Your Travel Platform

Hotel cards: 400px thumbnail WebP 40KB not 1200px JPEG 400KB. LCP image `priority` + preload.

### Nykaa

CDN transforms. Lazy below fold.

### Amazon

Dynamic image sizing per device.

---

## Key Takeaway

Profile page weight — images usually dominate. Compress, modern formats, responsive sizes, lazy load before tuning algorithms.

**Next:** [124 — Perception Is a Performance Metric](./124-perception-is-a-performance-metric.md)
