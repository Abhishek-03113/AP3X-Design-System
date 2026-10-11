Brik builds a custom design tool around your idea: "Brief it. Control it. Use it." The site is a quiet grey-on-white instrument panel with square corners, a monospace eyebrow voice and one electric-blue action, interrupted by loud, saturated tool output. Built from the public site brik.space; fonts are open substitutes.

## Voice

- Direct and a little cheeky: "Go On, Make Something", "Other design tools stop at export."
- Headlines are two-tone: the claim in `ink`, the rest in `ink-3`.
- Section eyebrows are mono, uppercase, often in brackets: `[ 01 ]`, `YOURS TO KEEP`.

## Colour

- Chrome is greyscale: `canvas`, `surface`, `panel`, `ink`, `ink-2`. Let the user's output carry the colour.
- `electric` is the single action colour (send arrow, links, active slider). `dark` is the primary button.
- The `tag-*` colours label use cases only. Always `dark` text on them (4.6:1 or better).
- `ink-3` is below 3:1 on purpose (the faded half of a headline). Never use it for content that has to be read on its own.

## Typography

- The site uses **HAL Matex** and **Proto Mono**; this system substitutes **Geist** and **Geist Mono**.
- One weight (400) for the sans; size and colour do the hierarchy. Track tight: −2.5px at `display`, −0.45px at `body`.
- Mono only for eyebrows, step numbers and values.

## Layout and shape

- Square corners everywhere (`radius-none`), 1px `panel` borders, no shadows.
- Tool panels are compact: `space-3` padding, `body-loose` rows.

## Components

`PromptBox`, `SliderControl` and `Button` are static previews built on the tokens above. No logo file ships; set "Brik" in `title` style.
