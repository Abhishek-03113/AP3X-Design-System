Decimals is "a scout network for hiring designers". The site is a warm paper world: cream ground, brown-black ink instead of black, tightly tracked serif headlines, tiny quiet sans, and soft pill buttons with real depth. Torn-paper cards, halftone photography and a handwritten annotation make recruiting feel crafted. A dotted globe arcs behind the hero, a logo ticker drifts under it, and two blush glows wander the page. Built from the public site decimals.co; fonts are open substitutes where the originals are licensed.

## Voice
- Plain, warm and slightly wry: "Hire designers who care through scouts that can tell." "Traditional recruiting stopped working."
- Sentence case everywhere; headings state a claim, not a label.

## Colour
- Everything is ink on cream: `ink` `#4d4638` for text and fills, `cream` for the ground, `card` and `paper` for lifted surfaces.
- `blush` and `rose` appear only as soft glows and portrait grounds; `pin-red` is a graphic accent.
- The site dims secondary text to 58% ink (`ink-soft`, 2.8:1); this system keeps that value but sets content in `ink-muted`.

## Typography
- Headlines use **martina** (licensed); substitute **Newsreader** 400–500 with tight tracking (-0.04em at display size, -0.03em at heading size).
- UI and body are **Geist** 400/500 at 14px with -0.14px tracking; the script tag is **La Belle Aurore**.

## Depth and motion
- Buttons are pills with a layered shadow stack (`shadow-pill-ink`, `shadow-pill-glass`); the glass variant adds `backdrop-filter: blur(10px)`.
- Press feedback is a multiply radial that follows the pointer (see `effects/cta-press-glow`).
- Hero content enters from `blur(12px)` at 30% opacity (`motions/hero-blur-reveal`); the logo strip is a 46s linear ticker under edge masks (`motions/logo-ticker`); two ambient blobs drift over 52s and 64s (`motions/ambient-drift`).
- Easing is `cubic-bezier(0.22, 1, 0.36, 1)` for movement and plain `ease` for colour and opacity; durations are 0.15–0.34s. Reduced motion removes the ticker, drift and blur reveal.

## Imagery
- No logos, portraits or illustrations were copied. Torn edges, halftone and cut-out portraits are described in the README of each component, not reproduced.

## Components
`PillButton`, `NavBar`, `TestimonialRow`, `LogoTicker` and `ProblemCard`.
