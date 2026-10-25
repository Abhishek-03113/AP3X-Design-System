# Fade to ground mask

Provenance: read from the public App Store art, not from resurf.so's CSS (blocked by a bot challenge). Colours are pixel-sampled (about ±6 per channel); sizes, angles and shadows are estimated by eye and marked *estimated*. No timings exist because no motion was captured.

In the store art every phone, tablet and laptop mockup is cut off by the artboard and fades into the background, so the product feels like it floats up out of the page.

```css
.device {
  -webkit-mask-image: linear-gradient(#000 45%, transparent 92%);
          mask-image: linear-gradient(#000 45%, transparent 92%);
}
```

The 45% / 92% stops are *estimated*. Match the page ground behind it (`#f3f3f3` to `#ffffff`); if the ground is a gradient, use a mask, not an overlay, so shadows and blur fade too.
