ANDMADE Inc. is a Tokyo design studio for web, CI/VI and graphics: "We uncover what truly matters and give purpose a clear form." The site is a quiet index on warm paper, with small black type, underlined project titles, grey metadata and typewriter dates. Built from the public site andmade.jp; the sans is an open substitute and Courier Prime is the site's own face.

## Voice

- Measured and intentional; full sentences in the statement, fragments everywhere else.
- Nav items are separated by commas: "Projects , About , Studies , Contact".
- Dates are abbreviated month + period + year: `May.2026`, `Aug.2025`.
- Japanese and English sit together; set Japanese with the same sans stack (Noto Sans JP fallback).

## Colour

- `ink` on `paper` for anything that must be read; `ink-50` only for metadata beside an `ink` title.
- `link-blue` is a single accent for one or two special links per page.
- No other colour in the chrome; project images bring their own.

## Typography

- The site uses **Akzidenz-Grotesk Next** (500) and **Courier Prime**. This system substitutes **Hanken Grotesk** for the sans; Courier Prime is used as-is.
- Weight 500 for almost everything; 400 only for `meta` and `date`.
- Track every size slightly negative (see tokens). Underline project titles.

## Layout

- A wide three-column index of projects; each entry is title, one or two meta lines and a date.
- Small vertical side notes run up the right edge ("Sep 1, 2026 — The Art Director / Designer's Approach").
- Generous `space-5` air between the statement and the index.

## Components

`ProjectEntry`, `Statement` and `Header` are static previews built on the tokens above. No logo file ships; set ANDMADE Inc. in `body`.
