# Dot globe

**Recreation, not a copy.** On decimals.co a canvas globe (`.v2-globe canvas`, observed by an `IntersectionObserver`) sits behind the hero. Measured: its frame changes while idle (it rotates) and changes again when the pointer moves (it reacts). Its source was not extracted, so this preview is an original implementation of that behaviour; the dot density, speed and lean are my choices. The site's globe is denser on its right limb; this one is evenly distributed.

- Fibonacci-sphere points, perspective-projected, back-face dots dimmed.
- Slow Y rotation; pointer position adds a small eased X/Y offset.
- Draws only while visible (IntersectionObserver) and stops under `prefers-reduced-motion`.
- Ink `#4d4638` dots over a hairline meridian at 22% ink.
