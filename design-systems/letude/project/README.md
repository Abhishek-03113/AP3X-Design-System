L'Étude is a modular creative studio ("From French *study*: a methodical application of the mind in pursuit of learning and understanding"). The site is built from loose modules floating on a periwinkle-grey ground, with cobalt type and one red hero field. Built from the public site letude.group; the typeface is an open substitute.

## Voice

- Confident, plural and international: "We've always believed…", "We are an international boutique studio…".
- Projects carry catalogue codes: `LET.27`, `LET.16`. Always write them uppercase with a period.
- Small labels are uppercase; headlines are sentence case.

## Colour

- Default ground is `haze`; text and graphics are `cobalt`. That pairing *is* the brand.
- `signal` red is a whole ground for the hero and project openers, never a small accent on `haze`. On `signal`, set large type in `cobalt` and small type in `ink`.
- `paper` only appears on photography and inside `cobalt` badges.
- `cobalt` on `haze` is 4.4:1, a hair under the 4.5:1 floor. The site sets 13px labels in it anyway; this system keeps the colour exact but asks for `ink` on anything under 24px (19px bold).

## Typography

- One family, heavy and tight. The original is **Indivisible** (variable, 1–999); this system substitutes **Manrope**. Use weights 550–700 only.
- Track display sizes negatively: −2.16px at 72px+, −1.12px at 32–56px.
- Break manifesto lines with intent; the site sets them as huge, ragged, left-aligned paragraphs.

## Layout

- Modules float on a loose grid: image tiles with a caption under them (`↗ THE DEEP END`), separated by `space-5`.
- Vertical project codes run beside images (rotated 90°).
- Circular icon badges hug the right edge as a fixed rail.

## Iconography

- Simple bold glyphs inside `cobalt` outline circles (`radius-pill`). No icon set ships here; draw glyphs as plain text or a single-colour SVG in `cobalt`.
- No logo file ships; set the name L'ÉTUDE in `display-xxl`.

## Components

`ProjectCard`, `IconBadge` and `Definition` are static previews built on the tokens above.
