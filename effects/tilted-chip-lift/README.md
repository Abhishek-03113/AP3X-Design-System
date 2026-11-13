# Tilted chip lift

Provenance: read from the public App Store art, not from resurf.so's CSS (blocked by a bot challenge). Colours are pixel-sampled (about ±6 per channel); sizes, angles and shadows are estimated by eye and marked *estimated*. No timings exist because no motion was captured.

The scattered-chip look: each chip is a white pill with a glyph and label, rotated a different amount (about -8° to +6°, *estimated*), lifted by a soft shadow and placed so it overlaps a device edge.

```css
.chip {
  display:inline-flex; align-items:center; gap:6px; height:44px; padding:0 18px;
  border-radius:999px; background:#fff;
  box-shadow:0 1px 2px rgba(0,0,0,.10), 0 6px 18px rgba(0,0,0,.10);   /* estimated */
  font:600 20px/1 Inter, system-ui; letter-spacing:-.01em;
}
.chip:nth-child(1) { transform:rotate(-6deg) }
.chip:nth-child(2) { transform:rotate(4deg) }
```

Never rotate a row by the same angle; vary both sign and size. No motion was observed, so the preview is static.
