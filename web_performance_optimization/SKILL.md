---
name: web_performance_optimization
description: Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime performance.
---

# Web Performance Optimization

Help developers optimize website and web application performance to improve user experience, SEO rankings, and conversion rates. This skill provides systematic approaches to measure, analyze, and improve loading speed, runtime performance, and Core Web Vitals metrics.

## Workflow

1. **Measure Current Performance**:
   - Run Lighthouse audits
   - Measure Core Web Vitals (LCP, FID, CLS)
   - Check bundle sizes and network waterfall
2. **Identify Issues**:
   - Large JavaScript bundles or unoptimized images
   - Render-blocking resources
   - Layout shifts or slow server response times
3. **Prioritize Optimizations**:
   - Focus on high-impact improvements (critical rendering path, image optimization, code splitting).
4. **Implement Optimizations**:
   - Optimize assets, add caching headers, lazy load non-critical resources.
5. **Verify Improvements**:
   - Compare before/after metrics and monitor real user metrics.

### Core Strategies
- *Images*: Convert to WebP/AVIF, implement responsive images, specify dimensions, and use lazy loading.
- *JavaScript*: Keep bundles under 200KB. Code split and remove unused dependencies. Delay non-critical JS.
- *CSS*: Inline critical CSS, defer the rest, remove unused CSS.
- *Core Web Vitals Guide*:
  - **LCP** (< 2.5s)
  - **FID** (< 100ms)
  - **CLS** (< 0.1)
