Resurf is "a personal context library": notes, links, voice notes, screenshots, PDFs and video in one local library, on Mac, iPhone and iPad, with an MCP/CLI hand-off to agents. The marketing look is airy and Apple-native: a near-white gradient ground, big two-tone headlines, device mockups that dissolve into the background, and colour-coded pill chips scattered at slight angles around them.

> **Provenance, read first.** resurf.so serves its stylesheets, scripts, fonts and press images behind a bot challenge (HTTP 429), so this system could not be measured from the site's CSS. It is built from the app's public App Store listing art: colours are pixel-sampled (quantised, about ±6 per channel), and type, radius and spacing are read by eye from those images. No motion was captured. `*-text` colours are derived, not sampled. Verify against the site's own CSS before using this for production work.

## Voice
- Short, imperative, two-beat: "Dump it now. Sort it later." "Capture the thought before it escapes." "One library for everything you save."
- Reassurance pills state facts: "Local first", "No account needed", "Synced with iCloud".

## Colour
- Neutral first: `ground` to `paper`, `ink` for type, `ink-soft` for the first headline line.
- Colour belongs to content types: `amber` Notes/PDFs, `ember` Voice notes, `violet` Links, `azure` Screenshots, `leaf` Videos. Images, Meetings, Memos and Lectures stay `ink`.
- Sampled accents are 2.6–4.1:1 on white. Use them for glyphs and fills; set label text in the matching `*-text` colour.

## Typography
- The art looks like Apple's system sans in semibold (SF Pro, possibly Rounded). This system substitutes **Inter** 600; on Apple platforms prefer `-apple-system`.
- Headlines are centred, tightly leaded, two lines, first line grey and second black.

## Shape and depth
- Chips are full pills with a glyph and label, 6px gap, rotated about -8° to +6°, lifted by a soft diffuse shadow (`shadow-chip`).
- Device mockups fade to the ground along their lower edge (see `effects/fade-to-ground-mask`).

## Components
`TagChip`, `StatusPill`, `TwoToneHeadline` and `FadingDevice`.
