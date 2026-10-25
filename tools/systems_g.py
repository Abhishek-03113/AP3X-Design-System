from ds_lib import tok, style

CAPTURED = "2026-10-25"
GF = "https://fonts.googleapis.com/css2?"

# Provenance: resurf.so sits behind a bot challenge (stylesheets, scripts, fonts and press images all return 429),
# so nothing here is a computed style from the site. Colours are sampled from the pixels of the app's public App Store
# listing art (quantised, about ±6 per channel); type, radius and spacing are read from those images by eye.
resurf = {
    "slug": "resurf",
    "title": "Resurf",
    "note": "Built from the public App Store listing art for Resurf (pixel-sampled colours); resurf.so was blocked by a bot challenge, so nothing was measured from the site.",
    "namespace": "Resurf",
    "source": {
        "url": "https://apps.apple.com/us/app/resurf-save-organize/id6782162097",
        "site": "https://resurf.so/",
        "captured": CAPTURED,
        "method": "pixel sampling and visual reading of the public App Store listing images; resurf.so itself was blocked by a bot challenge",
    },
    "fonts_href": GF + "family=Inter:wght@500;600;700&display=swap",
    "families": {"sans": "\"Inter\", -apple-system, \"SF Pro Text\", system-ui, sans-serif"},
    "colors": [
        tok("ground", "#f3f3f3", "Page ground at the top of the store art (sampled #f3f3f3, fading to `paper` at the bottom)."),
        tok("paper", "#ffffff", "Chips, cards and the lower end of the ground gradient (sampled)."),
        tok("ink", "#000000", "Headline second line, chip labels and glyphs (sampled). 18.9:1 on `ground`, 21:1 on `paper`."),
        tok("ink-soft", "#727272", "Headline first line (sampled #727272–#787878). 4.3:1 on `ground`: headline sizes only (24px+, 3:1 rule)."),
        tok("ink-faint", "#a2a2a2", "Quiet subtitles over the art (sampled). 2.3:1 on `ground`: decorative only."),
        tok("amber", "#d89024", "Notes and PDFs chip glyph and label (sampled #cc9030–#d89024). 2.6:1 on `paper`: icons and fills; labels use `amber-text`."),
        tok("ember", "#fc480c", "Voice notes glyph and the \"Synced with iCloud\" pill (sampled). 3.5:1 on `paper`: icons and fills; labels use `ember-text`."),
        tok("azure", "#0c78fc", "Screenshots chip and the \"or your own AI key\" pill fill (sampled). 4.1:1 against white text."),
        tok("violet", "#b46cd8", "Links chip glyph and label (sampled). 3.5:1 on `paper`: icons; labels use `violet-text`."),
        tok("leaf", "#30a818", "Videos chip glyph and label (sampled #18b43c–#30a818). 3.1:1 on `paper`: icons; labels use `leaf-text`."),
        tok("amber-text", "#a86a00", "Derived, not sampled: `amber` darkened for text. 4.4:1 on `paper`, use at 18px+ or bold."),
        tok("ember-text", "#d63a05", "Derived: `ember` darkened for text. 4.7:1 on `paper`."),
        tok("violet-text", "#8f3fc0", "Derived: `violet` darkened for text. 5.8:1 on `paper`."),
        tok("leaf-text", "#1f7d0e", "Derived: `leaf` darkened for text. 5.3:1 on `paper`."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("headline", "34px", "36px", 600, "Centred two-line headline over the art: first line `ink-soft`, second `ink`.", ls="-0.02em", sample="Dump it now. Sort it later."),
            style("headline-sm", "26px", "28px", 600, "Headline on phone-width art.", ls="-0.02em"),
            style("chip", "22px", "1", 600, "Tilted chip labels on an 800px-wide artboard (about 2.75% of width).", ls="-0.01em", sample="Voice notes"),
            style("pill", "15px", "1", 600, "Status pills (\"Local first\", \"Synced with iCloud\").", ls="-0.01em"),
            style("ui", "13px", "18px", 500, "Interface text inside the mockups."),
        ]},
    ],
    "spacing": [
        tok("space-1", "6px", "Chip icon-to-label gap (approximated from the art)."),
        tok("space-2", "12px", "Pill vertical rhythm."),
        tok("space-3", "18px", "Chip side padding."),
        tok("space-4", "40px", "Headline to first chip."),
    ],
    "radius": [
        tok("radius-pill", "999px", "Chips and status pills."),
        tok("radius-device", "28px", "Device screen corners in mockups (approximated)."),
    ],
    "radius_note": "Radii are read by eye from the store art; chips are fully round.",
    "shadow": [
        tok("shadow-chip", "0 1px 2px rgba(0,0,0,.10), 0 6px 18px rgba(0,0,0,.10)", "Soft lift under tilted chips. Estimated from the art; no value was measurable."),
    ],
    "readme": """
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
""",
    "components": {
        "TagChip": {
            "group": "Content", "height": 170,
            "subtitle": "Colour-coded, tilted",
            "readme": """
A pill chip naming a content type, tilted slightly and lifted off the page.

- Provide a glyph and a label. Fill `paper`, `radius-pill`, `shadow-chip`, `chip` style scaled to the artboard.
- Glyph uses the type colour (`amber`, `ember`, `violet`, `azure`, `leaf`, or `ink`); the label uses the matching `*-text` colour, or `ink`.
- Tilt each chip by a different angle between -8° and +6°; never rotate a row uniformly.
- Proportions are read from store art: height about 2× the label size, side padding `space-3`.
""",
            "css": """
body{background:linear-gradient(var(--ground),var(--paper));padding:24px;font-family:var(--font-sans)}
.row{display:flex;flex-wrap:wrap;gap:14px 16px;align-items:center}
.c{display:inline-flex;align-items:center;gap:6px;height:44px;padding:0 18px;border-radius:var(--radius-pill);background:var(--paper);box-shadow:var(--shadow-chip);font:600 20px/1 var(--font-sans);letter-spacing:-.01em;color:var(--ink)}
.g{width:20px;height:20px;border-radius:6px;display:inline-block}
""",
            "html": "<div class=\"row\"><span class=\"c\" style=\"transform:rotate(-4deg);color:var(--amber-text)\"><i class=\"g\" style=\"background:var(--amber)\"></i>Notes</span><span class=\"c\" style=\"transform:rotate(2deg);color:var(--ember-text)\"><i class=\"g\" style=\"background:var(--ember)\"></i>Voice notes</span><span class=\"c\" style=\"transform:rotate(-6deg);color:var(--violet-text)\"><i class=\"g\" style=\"background:var(--violet)\"></i>Links</span><span class=\"c\" style=\"transform:rotate(5deg);color:var(--azure)\"><i class=\"g\" style=\"background:var(--azure)\"></i>Screenshots</span><span class=\"c\" style=\"transform:rotate(-2deg)\"><i class=\"g\" style=\"background:var(--ink)\"></i>Images</span><span class=\"c\" style=\"transform:rotate(4deg);color:var(--leaf-text)\"><i class=\"g\" style=\"background:var(--leaf)\"></i>Videos</span></div>",
        },
        "StatusPill": {
            "group": "Content", "height": 120,
            "readme": """
Small reassurance pills that sit under a headline.

- Local pills: `paper` fill, 1px `ink` at 12% border, `ink` glyph and label, `pill` style.
- Emphasis pills: filled with `ember` ("Synced with iCloud") or `azure` ("or your own AI key"), `paper` label (azure 4.1:1; keep at 15px semibold or larger).
""",
            "css": """
body{background:var(--ground);padding:24px;display:flex;gap:10px;flex-wrap:wrap;font-family:var(--font-sans)}
.p{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 14px;border-radius:var(--radius-pill);font:600 15px/1 var(--font-sans);letter-spacing:-.01em}
.l{background:var(--paper);color:var(--ink);box-shadow:0 0 0 1px rgba(0,0,0,.12)}
.e{background:var(--ember);color:var(--paper)}
.a{background:var(--azure);color:var(--paper)}
.d{width:14px;height:14px;border-radius:50%;background:currentColor;display:inline-block}
""",
            "html": "<span class=\"p l\"><i class=\"d\"></i>Local first</span><span class=\"p l\"><i class=\"d\"></i>No account needed</span><span class=\"p e\"><i class=\"d\"></i>Synced with iCloud</span><span class=\"p a\">or your own AI key</span>",
        },
        "TwoToneHeadline": {
            "group": "Type", "height": 150,
            "readme": """
The centred two-line headline: the first line sets the context in `ink-soft`, the second lands the point in `ink`.

- `headline` style, centred, max two lines, tracking -0.02em.
- Examples from the art: "Dump it now. / Sort it later.", "Save on your iPad. / Find it on your Mac.", "Capture the thought / before it escapes."
- `ink-soft` is 4.3:1 on `ground`: fine at headline size, not for body.
""",
            "css": """
body{background:linear-gradient(var(--ground),var(--paper));padding:28px;text-align:center;font-family:var(--font-sans)}
h2{margin:0;font:600 34px/36px var(--font-sans);letter-spacing:-.02em;color:var(--ink)}
h2 span{color:var(--ink-soft)}
""",
            "html": "<h2><span>Save on your iPad.</span><br>Find it on your Mac.</h2>",
        },
        "FadingDevice": {
            "group": "Content", "height": 280,
            "readme": """
A device mockup that dissolves into the page along its lower edge, so the art feels like it floats rather than sits in a frame.

- Frame: dark bezel, `radius-device`, screen content inside.
- Mask the whole device with `linear-gradient(#000 45%, transparent 92%)` (see `effects/fade-to-ground-mask`).
- Supply your own screen image; none is shipped.
""",
            "css": """
body{background:linear-gradient(var(--ground),var(--paper));padding:20px 0 0;display:flex;justify-content:center}
.d{width:240px;height:260px;border:6px solid #1c1c1e;border-bottom:0;border-radius:var(--radius-device) var(--radius-device) 0 0;background:var(--paper);-webkit-mask-image:linear-gradient(#000 45%,transparent 92%);mask-image:linear-gradient(#000 45%,transparent 92%);display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:16px}
.d i{border-radius:8px;background:#e9e9ec;height:56px;display:block}
""",
            "html": "<div class=\"d\" role=\"img\" aria-label=\"Device mockup placeholder\"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>",
        },
    },
    "cover": {
        "ground": "ground", "ink": "ink", "muted": "ink-soft", "body_font": "sans",
        "name_font": "sans", "name_size": 64, "name_weight": 600, "name_ls": "-0.03em", "leading": 0.95,
        "name_lines": ["Resurf"],
        "tagline": "A personal context library.",
        "css": """
  .chip{fill:var(--paper)} .tx{font:600 15px var(--font-sans);fill:var(--ink)}
""",
        "derivation": """
blocks      four white pill chips with colour-coded glyph dots, tilted
arrangement scattered around an empty centre, like the store art's floating chips
pattern     content-type colours (amber, ember, violet, azure) from the sampled palette
scales      pill radius, 6px glyph gap, rotations between -8 and +6 degrees
""",
        "svg": """
<g transform="rotate(-6 150 80)"><rect class="chip" x="90" y="56" width="132" height="44" rx="22"/><circle cx="116" cy="78" r="9" fill="var(--amber)"/><text class="tx" x="134" y="84">Notes</text></g>
<g transform="rotate(4 340 120)"><rect class="chip" x="262" y="98" width="170" height="44" rx="22"/><circle cx="288" cy="120" r="9" fill="var(--ember)"/><text class="tx" x="306" y="126">Voice notes</text></g>
<g transform="rotate(-3 180 200)"><rect class="chip" x="110" y="178" width="124" height="44" rx="22"/><circle cx="136" cy="200" r="9" fill="var(--violet)"/><text class="tx" x="154" y="206">Links</text></g>
<g transform="rotate(7 360 230)"><rect class="chip" x="290" y="208" width="150" height="44" rx="22"/><circle cx="316" cy="230" r="9" fill="var(--azure)"/><text class="tx" x="334" y="236">Screenshots</text></g>
""",
    },
}

SYSTEMS = [resurf]
