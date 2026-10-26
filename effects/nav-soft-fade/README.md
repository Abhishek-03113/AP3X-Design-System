# Nav soft fade

Provenance: read from five screenshots of resurf.so taken in the owner's browser on 2026-10-25 (the site blocks automated browsers). Colours are pixel-sampled; sizes are measured at about 1:1 (anchored to the 56rem container), good to ±1–2px; radii and shadows are *estimated*. Typefaces could not be confirmed (Garamond-like serif, Inter-like sans). No motion timings exist: motion is inferred from UI states only.

When content scrolls under the nav it dissolves into a soft white band instead of meeting a border. In the screenshots the column under the nav steps `#fdfdfd` → `#fcfbfc` → `#fafafa` → `#f9f9f9` → ground (`#f8f8f8`) over about 50px.

```css
.nav::before {
  content:""; position:absolute; inset:0 0 -24px; z-index:-1; pointer-events:none;
  background:linear-gradient(#fff, rgba(248,248,248,0));   /* fade length estimated from the sampled column */
}
```

Whether the site also blurs what is underneath could not be determined from stills; add `backdrop-filter` only if you want it.
