An endless strip of client marks.

- Track is `display:flex; width:max-content`, content duplicated once, animated `translateX(0 → -50%)` over 46s linear.
- Wrapper masks both ends: `linear-gradient(90deg, transparent, #000 10%, #000 90%, transparent)`.
- Marks sit at 64px gaps, tinted to `ink` at 92%; hovering the strip pauses it and dims every mark to 40%, the hovered mark returns to full.
- Reduced motion: no animation.
