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

## End-to-End Optimization (Advanced)
If coordinating optimization across the entire stack:
1. **Performance Profiling & Observability**: Generate flame graphs (CPU) and heap dumps (memory) to identify hot paths. Assess distributed tracing (OpenTelemetry) and APM tool integration.
2. **Database & Backend**: Analyze slow query logs, create missing indexes, optimize execution plans, implement query result caching (Redis). Fix N+1 queries. Implement pagination and response compression.
3. **Frontend & CDN/Edge**: Code split, tree shake, lazy load. Configure edge caching (CloudFlare/CloudFront), HTTP/2/3, Brotli compression, and WebP/AVIF images.
4. **Mobile & PWA**: Implement service workers for offline functionality. Adaptive loading for slow networks. Virtual scrolling for long lists.
5. **Load Testing & Validation**: Design realistic load scenarios using k6/Gatling to test normal, peak, and stress levels before deploying optimizations.
