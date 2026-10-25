# Stacking sticky cards

Measured on 2026-10-25 by stepping the live page down at 1440×900 and sampling computed transform, opacity and filter (tools/capture-scroll.js, plus 10–60px fine scans). Values marked *derived* are fitted to those samples.

Each row is `position:sticky; top:120px` with `will-change:transform; transform-origin:center top`. When the *next* row rises into it, the pinned row recedes. The last row never recedes.

## Progress
`p` is how far the next row has climbed into the pinned one: `p = clamp(1 − (nextTop − stickTop) / rowHeight, 0, 1)` (*derived*: p is 0 when the next row sits one row-height (about 472px at 1440) below the pin line and 1 when it reaches it).

| Property | Value |
| --- | --- |
| scale | `1 − 0.035·p` (1 → 0.965) |
| translateY | `−8px·p` |
| blur | `2px · clamp((p − 0.6) / 0.4, 0, 1)`: blur only starts after 60% (*derived* from four samples, error < 0.02px) |
| origin | `center top` |
| easing | none; the value follows scroll directly |

Measured samples (row 1): scale 0.9877 / ty −2.82 / no blur, scale 0.9705 / ty −6.74 / blur 1.21px, scale 0.965 / ty −8 / blur 2px.

Reduced motion: leave the cards stacked with no transform.
