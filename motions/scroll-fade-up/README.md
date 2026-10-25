# Scroll fade up

Measured on 2026-10-25 by stepping the live page down at 1440×900 and sampling computed transform, opacity and filter (tools/capture-scroll.js, plus 10–60px fine scans). Values marked *derived* are fitted to those samples.

Used on the problem-cards block and the closing CTA panel. It is a one-shot reveal, not scroll-linked: scrolling back up does not hide them again.

| Property | Value |
| --- | --- |
| hidden state | `opacity:0; transform:translateY(12px)` |
| trigger | element top crosses about 95% of viewport height (opacity began rising at top 843–857 px in a 900px viewport) |
| duration | about 0.45s (opacity reached 0.99 about 0.4s after the first change) |
| easing | opacity and translate follow the same curve (translateY = 12px·(1 − opacity) at every sample); `cubic-bezier(.22,1,.36,1)` used here, *derived*, not read directly |

```js
new IntersectionObserver(es => es.forEach(e => e.isIntersecting && e.target.classList.add('in')),
                         { rootMargin: '0px 0px -5% 0px' });
```

Reduced motion: show at once.
