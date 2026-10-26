A floating nav that dissolves into the page.

- Three zones: wordmark left, links centre (`ui`, `ink-soft`; hover to `ink` in 0.2s), pills right.
- Behind it a gradient `rgba(237,232,225,.78) → .55 → 0` with `backdrop-filter: blur(12px)`, masked top-to-transparent so no edge shows (`effects/edge-fade-mask`).
