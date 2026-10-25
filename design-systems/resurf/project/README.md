Resurf is "a personal context library" for Mac, iPhone and iPad: notes, bookmarks, screenshots and PDFs in one local library, handed to agents on request. The site is calm and editorial: an off-white page, warm near-black ink, a Garamond-like serif for headlines that drops to grey on the second line, tiny quiet sans for everything else, flat grey cards with a floating mini-UI each, and one big product screenshot on a loud gradient wallpaper.

> **Provenance, read first.** resurf.so blocks automated browsers (its CSS, scripts, fonts and images return a bot challenge), so nothing here is a computed style. Values come from five full-width screenshots of the live site taken in the owner's own browser on 2026-10-25. Colours are pixel-sampled; sizes are measured from cap heights and gaps, with scale anchored to the 56rem container (896px) seen in the page HTML, so measurements are about 1:1 and good to ±1–2px. The headline face looks like a Garamond (EB Garamond substitutes) and the sans like Inter; neither could be confirmed. Motion is inferred from UI only (no timings). No logos or product screenshots are reproduced.

## Voice
- Calm, concrete and short. Claims are listed as plain facts: "100% native Swift", "Fully local", "Optional iCloud sync".
- Headlines are sentences with a full stop: "Five surfaces, one library." "Your library on Mac, iPhone, and iPad." "Start building your personal context library."
- Feature cards are a verb-ish title plus one line: "Inbox First: Save now, organize later."

## Colour
- Greyscale on warm neutrals: `ground` `#f8f8f8`, `card` `#efefef`, `tile` `#f3f3f3`, `paper` for lifted parts.
- Ink is warm, not pure black: `ink` `#0f100d`, `ink-button` `#181614`.
- Text steps down through `ink-title`, `ink-body`, `ink-muted`, `ink-quiet`, `ink-faint`. The quietest three fall below AA at their small sizes on the live site; the token notes flag each.
- Colour appears only in product glyphs and the selection ring: `blue` `#4078e8`, `orange`, `pink`, `ph-red`.

## Typography
- Headlines: **Garamond-like serif**, 500, about 40/44px, tracking about -0.02em; the second line in `ink-faint`.
- Everything else: **Inter**-like sans at 14px body, 13px UI, 12px small, 11px pills.

## Layout
- One column, `space-5` (896px) container with 32px side padding. Nav is a three-zone row: logo mark left, links centred, "Get Resurf" button right.
- Feature cards: three per row, 8px gap, `radius-card`, an illustration area on top and title plus description below at 14px padding.
- Tour: a pill segmented control (Library, Inbox, View, Notes, Assistant), one large screenshot with round arrow buttons and a Pause control, a caption with a bold first word, then a thumbnail strip.
- Formats: two offset rows of small tiles (icon top-left, label bottom-left) that fade out at both edges.
- Footer: hairline, logo and tagline left, four link columns (Product, Compare, Learn, Company).

## Motion
- Observed states, not timings: the tour is an auto-advancing carousel with Pause; format tile rows are offset and edge-faded like a marquee; the nav sits over a soft white-to-ground fade when content scrolls under it.
- No durations or easings were captured; do not invent them.

## Components
`NavBar`, `HeroHeadline`, `ButtonPair`, `FeatureCard`, `TourTabs`, `FormatTiles` and `Footer`.
