from ds_lib import tok, style

CAPTURED = "2026-10-11"
GF = "https://fonts.googleapis.com/css2?"

# ---------------------------------------------------------------- Julien Pianetti
julien = {
    "slug": "julien-pianetti",
    "title": "Julien Pianetti",
    "namespace": "JulienPianetti",
    "source": {"url": "https://www.julienpianetti.com/", "captured": CAPTURED},
    "fonts_href": GF + "family=Figtree:wght@400;500&display=swap",
    "families": {"sans": "\"Figtree\", \"Suisse Intl\", Arial, sans-serif"},
    "colors": [
        tok("white", "#ffffff", "Page ground."),
        tok("ink", "#0c0c0c", "All text and the dark menu. 19.6:1 on `white`."),
        tok("ash", "#a6a6a6", "Inactive nav items (\"Work\"). 2.4:1 on `white` — the site's own pairing; never the only cue for state."),
        tok("graphite", "#424242", "Secondary text. 10.0:1 on `white`."),
        tok("night", "rgba(12, 12, 12, 0.98)", "Full-screen menu overlay."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("intro", "32px", "33.6px", 400, "The intro statement.", sample="Independent designer based in Dijon, France."),
            style("display", "54px", "54px", 400, "Section heads and project titles."),
            style("display-medium", "54px", "54px", 500, "Emphasised heads."),
            style("display-sm", "45.072px", "45.072px", 500, "Sub-heads."),
            style("ui", "13px", "15.6px", 500, "Nav, email, tags."),
            style("ui-tight", "13px", "13px", 500, "Pill tags."),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Pill padding (vertical)."),
        tok("space-2", "12px", "Page margin."),
        tok("space-3", "24px", "Between nav items."),
        tok("space-4", "96px", "Section padding."),
    ],
    "radius": [
        tok("radius-hair", "1px", "Images."),
        tok("radius-pill", "99px", "Tags and buttons."),
    ],
    "readme": """
Julien Pianetti is an independent designer in Dijon who builds custom interfaces in Webflow and loves motion. The site is clean white with a three-part top line, a calm 32px intro, then a jolt: a hand-cut, blobby black display lettering for "Selected Work". Built from the public site julienpianetti.com; the text face is an open substitute.

## Voice
- First person, matter-of-fact: "Independent designer based in Dijon, France, I create custom digital interfaces. Developing on Webflow and passionate about motion design."

## Colour
- `ink` on `white`; `ash` marks the current nav item at low contrast, as the site does.

## Typography
- The site uses **Suisse Intl**; substitute **Figtree**. The "Selected Work" lettering is custom and is not reproduced; use an image of it or set the words in `display`.

## Layout
- Name left, nav centre-left, email right, all `ui`. Intro block starts at the second column.

## Components
`Header`, `Intro` and `PillTag`.
""",
    "components": {
        "Header": {
            "group": "Navigation", "height": 70,
            "readme": """
Name, nav and email across the top.

- `ui` style. Current nav item `ash`, the rest `ink`.
""",
            "css": """
body{background:var(--white);padding:12px;font:500 13px/15.6px var(--font-sans);color:var(--ink)}
.h{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px}
.a{color:var(--ash)}
.r{text-align:right}
""",
            "html": "<div class=\"h\"><span>Julien Pianetti</span><span><span class=\"a\">Work,</span> About, Playground</span><span class=\"r\">jupian@gmail.com</span></div>",
        },
        "Intro": {
            "group": "Content", "height": 180,
            "readme": """
The intro statement.

- `intro` style in `ink`, max 36ch, starting at the second grid column.
""",
            "css": """
body{background:var(--white);padding:12px}
p{font:400 32px/33.6px var(--font-sans);color:var(--ink);margin:0 0 0 30%;max-width:22ch}
""",
            "html": "<p>Independent designer based in Dijon, France. I create custom digital interfaces.</p>",
        },
        "PillTag": {
            "group": "Content", "height": 80,
            "readme": """
Outlined pill tags for disciplines.

- 1px `ink` border, `ui-tight`, `radius-pill`, padding `space-1` × 10px.
""",
            "css": """
body{background:var(--white);padding:12px;display:flex;gap:6px}
span{border:1px solid var(--ink);border-radius:var(--radius-pill);font:500 13px/13px var(--font-sans);padding:5px 10px;color:var(--ink)}
""",
            "html": "<span>Webflow</span><span>Motion</span><span>Interface</span>",
        },
    },
    "cover": {
        "ground": "white", "ink": "ink", "muted": "graphite", "body_font": "sans",
        "name_font": "sans", "name_size": 72, "name_weight": 500, "name_lines": ["Julien", "Pianetti"],
        "tagline": "Independent designer based in Dijon, France.",
        "css": """
  .ik{fill:var(--ink)} .as{fill:var(--ash)}
""",
        "derivation": """
blocks      ink blobs (the hand-cut display lettering abstracted as discs and slabs), one ash dot
arrangement heavy black shapes clustered low, like "Selected Work" breaking the calm page
pattern     a distinctive display face → oversized blob shapes: four discs and two slabs, all ink
scales      radius-pill rounding, gaps space-2 (12)
""",
        "svg": """
<rect class="ik" x="40" y="120" width="96" height="120" rx="40"/>
<circle class="ik" cx="200" cy="180" r="60"/>
<rect class="ik" x="272" y="96" width="64" height="144" rx="12"/>
<circle class="ik" cx="400" cy="200" r="40"/>
<circle class="ik" cx="400" cy="112" r="24"/>
<circle class="as" cx="96" cy="64" r="6"/>
""",
    },
}

# ---------------------------------------------------------------- Ras Koš
raskos = {
    "slug": "ras-kos",
    "title": "Ras Koš",
    "namespace": "RasKos",
    "source": {"url": "https://raskos.net/comics", "captured": CAPTURED},
    "fonts_href": GF + "family=IBM+Plex+Sans:wght@300&family=IBM+Plex+Mono:wght@300&display=swap",
    "families": {
        "sans": "\"IBM Plex Sans\", sans-serif",
        "mono": "\"IBM Plex Mono\", monospace",
    },
    "colors": [
        tok("paper", "#f5f4f0", "Page ground."),
        tok("panel", "#e8e7e2", "Sidebar and card grounds."),
        tok("ink", "#0a0a0a", "Titles and comic line work. 18.0:1 on `paper`."),
        tok("graphite", "#333333", "Body text. 11.5:1 on `paper`, 10.2:1 on `panel`."),
        tok("pencil", "#888888", "Labels, dates and hairlines. 3.2:1 on `paper` — the site's own pairing, used at tiny sizes; keep content in `graphite`."),
    ],
    "type_groups": [
        {"name": "Mono", "family": "mono", "styles": [
            style("label", "8.06px", "10px", 300, "Uppercase section labels.", ls="0.4836px", sample="WHAT IS IT ABOUT COMICS?"),
            style("meta", "7.54px", "10px", 300, "Issue numbers and dates."),
            style("nav", "9.75px", "12.675px", 300, "Uppercase nav.", sample="COMICS  PILATES  CONTACT  CV"),
            style("title", "10.66px", "14.924px", 300, "Comic titles under cards."),
        ]},
        {"name": "Sans", "family": "sans", "styles": [
            style("body", "10.66px", "17.589px", 300, "Sidebar paragraph."),
            style("body-sm", "8.84px", "14.586px", 300, "Notes."),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Tag padding."),
        tok("space-2", "8px", "Card caption padding."),
        tok("space-3", "16px", "Sidebar padding."),
        tok("space-4", "32px", "Between rows."),
    ],
    "radius": [tok("radius-none", "0px", "Everything; cells meet on hairlines.")],
    "readme": """
Ras Koš makes comics and teaches movement ("comics & movement"). The site is a quiet archive grid on warm paper: a sidebar of tiny mono text explaining why comics matter, then comic covers in a hairline grid with numbered captions. Built from the public site raskos.net; IBM Plex Sans and Mono are the site's own faces.

## Voice
- Thoughtful, slightly academic: "Comics integrate spatial-visual and language processing at the same time…"
- Numbered issues: `No. 007`.

## Colour
- `ink` and `graphite` on `paper`; `panel` for the sidebar; `pencil` for hairlines and tiny meta.

## Typography
- **IBM Plex Mono** 300 for almost everything, uppercase and tracked for labels; **IBM Plex Sans** 300 for paragraphs. Sizes are tiny (7.5–10.7px): keep this system for display contexts, and scale up for long reading.

## Layout
- Fixed sidebar left, a three-column grid of covers separated by 1px `pencil` hairlines; caption cells under each cover.

## Components
`ComicCard`, `TagChips` and `Sidebar`.
""",
    "components": {
        "ComicCard": {
            "group": "Content", "height": 230,
            "readme": """
A cover in a hairline cell with a numbered caption.

- Provide image, number, title, date. Cell borders 1px `pencil`; caption `meta` then `title` in `ink`.
""",
            "css": """
body{background:var(--paper);padding:16px;font-family:var(--font-mono)}
.c{width:180px;border:1px solid var(--pencil)}
.i{height:150px;background:var(--panel);border-bottom:1px solid var(--pencil)}
.cap{padding:8px;font:300 10.66px/14.9px var(--font-mono);color:var(--ink)}
.m{font-size:9px;color:var(--graphite)}
""",
            "html": "<div class=\"c\"><div class=\"i\" role=\"img\" aria-label=\"Comic cover: Efekat posmatrača\"></div><div class=\"cap\"><div class=\"m\">No. 007</div>Efekat posmatrača<div class=\"m\">April 2026</div></div></div>",
        },
        "TagChips": {
            "group": "Content", "height": 90,
            "readme": """
Outlined theme tags.

- 1px `pencil` border, `nav` style lowercase in `graphite`, padding `space-1`.
""",
            "css": """
body{background:var(--panel);padding:16px;display:flex;flex-wrap:wrap;gap:4px;max-width:240px}
span{border:1px solid var(--pencil);padding:2px 4px;font:300 9.75px/12.7px var(--font-mono);color:var(--graphite)}
""",
            "html": "<span>slice of life</span><span>ecology</span><span>philosophy</span><span>experimental</span><span>sport</span>",
        },
        "Sidebar": {
            "group": "Navigation", "height": 220,
            "readme": """
The left column: name, nav, a label and a paragraph.

- `panel` ground; name `title` uppercase in `ink`; nav `nav` in `graphite`; label `label` in `pencil`; paragraph `body` in `graphite`.
""",
            "css": """
body{background:var(--panel);padding:16px;max-width:220px;font-family:var(--font-mono)}
.n{font:300 10.66px/14px var(--font-mono);text-transform:uppercase;color:var(--ink)}
nav{display:flex;gap:10px;font:300 9.75px/12.7px var(--font-mono);text-transform:uppercase;color:var(--graphite);margin:6px 0 16px}
.l{font:300 9px/12px var(--font-mono);letter-spacing:.48px;text-transform:uppercase;color:var(--graphite);margin:0 0 6px}
p{font:300 11px/17.6px var(--font-sans);color:var(--graphite);margin:0}
""",
            "html": "<div class=\"n\">Ras Koš</div><nav><span>Comics</span><span>Pilates</span><span>Contact</span><span>CV</span></nav><p class=\"l\">What is it about comics?</p><p>Comics integrate spatial-visual and language processing at the same time.</p>",
        },
    },
    "cover": {
        "ground": "paper", "ink": "ink", "muted": "graphite", "body_font": "sans",
        "name_font": "mono", "name_size": 96, "name_weight": 300, "name_lines": ["Ras Koš"],
        "tagline": "comics & movement",
        "css": """
  .pa{fill:var(--panel)} .ik{fill:var(--ink)} .gr{fill:var(--graphite)}
  .hair{stroke:var(--pencil);stroke-width:1}
""",
        "derivation": """
blocks      panel 96x288 sidebar · ink 120x150 cover · graphite 120x150 cover — a monochrome archive
arrangement the archive grid: sidebar, then covers in hairline cells
pattern     editorial hairlines: five 1px pencil rules forming the grid
scales      cells 144 pitch, hairline 1px
""",
        "svg": """
<rect class="pa" x="0" y="0" width="96" height="288"/>
<rect class="ik" x="120" y="24" width="120" height="150"/>
<rect class="gr" x="264" y="24" width="120" height="150"/>
<line class="hair" x1="96.5" y1="0" x2="96.5" y2="288"/>
<line class="hair" x1="252.5" y1="0" x2="252.5" y2="288"/>
<line class="hair" x1="396.5" y1="0" x2="396.5" y2="288"/>
<line class="hair" x1="96" y1="196.5" x2="480" y2="196.5"/>
<line class="hair" x1="96" y1="228.5" x2="480" y2="228.5"/>
""",
    },
}

# ---------------------------------------------------------------- Baran Ceylan
baran = {
    "slug": "baran-ceylan",
    "title": "Baran Ceylan",
    "namespace": "BaranCeylan",
    "source": {"url": "https://baranceylan.co/", "captured": CAPTURED},
    "fonts_href": GF + "family=Archivo:wght@400&display=swap",
    "families": {"sans": "\"Archivo\", Helvetica, Arial, sans-serif"},
    "colors": [
        tok("white", "#ffffff", "Page ground."),
        tok("black", "#000000", "All text and hairlines. 21:1 on `white`."),
        tok("hairline", "#d9d9d9", "Row separators (an addition; the site uses black rules at 1px)."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("title", "21px", "21px", 400, "Name and project titles, uppercase.", sample="BEYMEN BEAUTY"),
            style("lead", "13px", "13px", 400, "Occasional larger notes."),
            style("micro", "8px", "9px", 400, "Everything else: descriptions, categories, nav, uppercase.", sample="DESIGN AND ART DIRECTION · BASED IN BASEL"),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Image gap in a strip."),
        tok("space-2", "8px", "Margins."),
        tok("space-3", "24px", "Between project rows."),
    ],
    "radius": [tok("radius-none", "0px", "Everything is square.")],
    "readme": """
Baran Ceylan does design and art direction from Basel. The homepage is a stack of project rows: a title at 21px, a two-line description and category columns at a tiny 8px, then a horizontal strip of images edge to edge. Built from the public site baranceylan.co; the typeface is an open substitute.

## Voice
- Descriptive, plain project blurbs: "WWW is an online magazine with impersonal content without any path."
- Categories in caps: BRANDING, MAGAZINE, WEB DESIGN, VISUAL DESIGN, CONTENT DESIGN.

## Colour
- `black` on `white`, nothing else. The work supplies colour.

## Typography
- One custom grotesk on the site; substitute **Archivo**. Only three sizes: 21, 13 and 8px. The 8px is tiny on purpose: use it only for labels beside larger titles.

## Layout
- Each row: title column, description column, two category columns, then the image strip below, all aligned to the same column grid.

## Components
`ProjectRow`, `Header` and `ImageStrip`.
""",
    "components": {
        "ProjectRow": {
            "group": "Content", "height": 110,
            "readme": """
Title, description and categories on one grid line.

- `title` uppercase; description and categories `micro` uppercase. 1px `black` rule above.
""",
            "css": """
body{background:var(--white);padding:8px;color:var(--black)}
.r{display:grid;grid-template-columns:1.2fr 1.5fr 1fr 1fr;gap:8px;border-top:1px solid var(--black);padding-top:6px}
.t{font:400 21px/21px var(--font-sans)}
.m{font:400 8px/9px var(--font-sans);text-transform:uppercase}
""",
            "html": "<div class=\"r\"><span class=\"t\">BEYMEN BEAUTY</span><span class=\"m\">Content design work for Beymen Beauty, which provides services and consultancy enriched with distinguished brands.</span><span class=\"m\">Visual design</span><span class=\"m\">Content design</span></div>",
        },
        "Header": {
            "group": "Navigation", "height": 70,
            "readme": """
Role and city, name, then nav.

- Name `title`; everything else `micro` uppercase.
""",
            "css": """
body{background:var(--white);padding:8px;color:var(--black)}
.h{display:grid;grid-template-columns:1.2fr 1.5fr 1fr 1fr 1fr;align-items:start;font:400 8px/9px var(--font-sans);text-transform:uppercase}
.n{font:400 21px/21px var(--font-sans)}
""",
            "html": "<div class=\"h\"><span>Design and art direction<br>Based in Basel</span><span class=\"n\">BARAN CEYLAN</span><span>Index</span><span>Info</span><span>Contact</span></div>",
        },
        "ImageStrip": {
            "group": "Media", "height": 150,
            "readme": """
A horizontal strip of project images, edge to edge, 4px gaps.

- Provide 4–8 images of equal height. No radius, no captions inside.
""",
            "css": """
body{background:var(--white);margin:0;padding:8px;display:flex;gap:4px;overflow:hidden}
.i{flex:0 0 90px;height:120px;background:var(--black)}
.i:nth-child(2n){background:var(--hairline)}
""",
            "html": "<div class=\"i\" role=\"img\" aria-label=\"Project image\"></div><div class=\"i\" role=\"img\" aria-label=\"Project image\"></div><div class=\"i\" role=\"img\" aria-label=\"Project image\"></div><div class=\"i\" role=\"img\" aria-label=\"Project image\"></div><div class=\"i\" role=\"img\" aria-label=\"Project image\"></div>",
        },
    },
    "cover": {
        "ground": "white", "ink": "black", "muted": "black", "body_font": "sans",
        "name_font": "sans", "name_size": 72, "name_lines": ["Baran", "Ceylan"],
        "tagline": "Design and art direction, based in Basel.",
        "css": """
  .bk{fill:var(--black)} .hl{fill:var(--hairline)}
  .rule{stroke:var(--black);stroke-width:1}
""",
        "derivation": """
blocks      black and hairline image tiles 72x96 alternating in two strips
arrangement two horizontal image strips edge to edge under rules, like the project rows
pattern     editorial: three 1px black rules marking rows
scales      gap space-1 (4), tiles 72x96
""",
        "svg": """
<line class="rule" x1="0" y1="24.5" x2="480" y2="24.5"/>
<rect class="bk" x="0" y="36" width="72" height="96"/><rect class="hl" x="76" y="36" width="72" height="96"/><rect class="bk" x="152" y="36" width="72" height="96"/><rect class="hl" x="228" y="36" width="72" height="96"/><rect class="bk" x="304" y="36" width="72" height="96"/><rect class="hl" x="380" y="36" width="100" height="96"/>
<line class="rule" x1="0" y1="152.5" x2="480" y2="152.5"/>
<rect class="hl" x="0" y="164" width="72" height="96"/><rect class="bk" x="76" y="164" width="72" height="96"/><rect class="hl" x="152" y="164" width="72" height="96"/><rect class="bk" x="228" y="164" width="72" height="96"/><rect class="hl" x="304" y="164" width="176" height="96"/>
""",
    },
}

# ---------------------------------------------------------------- Funner
funner = {
    "slug": "funner",
    "title": "Funner",
    "namespace": "Funner",
    "source": {"url": "https://www.shopfunner.com/", "captured": CAPTURED},
    "fonts_href": GF + "family=Archivo+Narrow:wght@400;500&display=swap",
    "families": {"sans": "\"Archivo Narrow\", \"Bell Centennial\", \"Helvetica Neue\", sans-serif"},
    "colors": [
        tok("white", "#ffffff", "Page ground."),
        tok("cloud", "oklch(0.967 0.003 264.542)", "Product photography ground (cool off-white)."),
        tok("black", "#000000", "Text and the cookie card. 21:1 on `white`."),
        tok("sky", "#4190de", "Nav pill: SHAMPOO. `black` text 6.3:1."),
        tok("flame", "#fe5100", "Nav pill: CONDITION. `black` text 6.4:1."),
        tok("sun", "#ffcd01", "Nav pill: STYLE. `black` text 14.0:1."),
        tok("lilac", "#b680d2", "Nav pill: TREAT. `black` text 7.0:1."),
        tok("grass", "#009d39", "Nav pill: BY FUNCTION. `black` text 5.9:1."),
        tok("violet", "#7c55c6", "Logo petal colour and hover."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("nav", "14px", "14px", 400, "Pill labels, uppercase.", sample="SHAMPOO  CONDITION  STYLE  TREAT"),
            style("caption", "14px", "14px", 400, "Captions and body."),
            style("lead", "21px", "31.5px", 500, "Lead copy."),
        ]},
    ],
    "spacing": [
        tok("space-1", "6px", "Pill padding (vertical)."),
        tok("space-2", "12px", "Gaps."),
        tok("space-3", "16px", "Margins."),
        tok("space-4", "40px", "Section padding."),
    ],
    "radius": [
        tok("radius-card", "20px", "Cards and the cookie banner."),
        tok("radius-pill", "9999px", "Nav pills and buttons."),
    ],
    "readme": """
Funner makes professional haircare "for hair you want to wear". The site pairs big editorial portraits with clean product shots on cool white, and navigates with a row of colour-coded pills: SHAMPOO in sky, CONDITION in flame, STYLE in sun, TREAT in lilac, BY FUNCTION in grass. The logo is a ring of letters in a blue disc. Built from the public site shopfunner.com; the typeface is an open substitute.

## Voice
- Playful, a bit cheeky: "Professional-grade haircare made for personal style, not perfection." "…or more-of-whatever-you-want hair."

## Colour
- Each category owns a colour and keeps it everywhere: `sky`, `flame`, `sun`, `lilac`, `grass`. Text on them is always `black`.

## Typography
- The site uses **Bell Centennial** (the phone-book face) in its Sub-Caption and Name-and-Number cuts. Substitute: **Archivo Narrow**. Uppercase for navigation.

## Components
`CategoryPills`, `Button` and `ProductCaption`. No logo file ships.
""",
    "components": {
        "CategoryPills": {
            "group": "Navigation", "height": 80,
            "readme": """
Colour-coded category pills.

- One pill per category in its token, `black` `nav` text, `radius-pill`, padding `space-1` × 22px.
""",
            "css": """
body{background:var(--white);padding:16px;display:flex;flex-wrap:wrap;gap:6px}
a{font:400 12px/12px var(--font-sans);text-transform:uppercase;color:var(--black);text-decoration:none;padding:6px 22px;border-radius:var(--radius-pill)}
""",
            "html": "<a href=\"#\" style=\"background:var(--sky)\">Shampoo</a><a href=\"#\" style=\"background:var(--flame)\">Condition</a><a href=\"#\" style=\"background:var(--sun)\">Style</a><a href=\"#\" style=\"background:var(--lilac)\">Treat</a><a href=\"#\" style=\"background:var(--grass)\">By function +</a>",
        },
        "Button": {
            "group": "Actions", "height": 150,
            "readme": """
Outlined pill button on the black cookie card.

- 1px `white` border, `white` uppercase `nav` text, `radius-pill`; card `black`, `radius-card`.
""",
            "css": """
body{background:var(--white);padding:16px}
.c{background:var(--black);color:var(--white);border-radius:var(--radius-card);padding:16px;max-width:260px;font:400 12px/16px var(--font-sans)}
button{margin-top:10px;background:transparent;color:var(--white);border:1px solid var(--white);border-radius:var(--radius-pill);font:400 12px/12px var(--font-sans);text-transform:uppercase;padding:6px 12px}
""",
            "html": "<div class=\"c\">We use cookies to provide and improve services on our website.<br><button>I agree</button></div>",
        },
        "ProductCaption": {
            "group": "Content", "height": 120,
            "readme": """
Short caption over a portrait.

- Title `caption` in `white` over the image; body `caption` max 48ch.
""",
            "css": """
body{background:var(--black);padding:16px;color:var(--white);font:400 12px/16px var(--font-sans)}
b{display:block;font-weight:500;margin-bottom:6px}
""",
            "html": "<b>Wear your hair</b>Professional-grade haircare made for personal style, not perfection. Clean, clinically tested formulas designed to mix, layer and play with.",
        },
    },
    "cover": {
        "ground": "white", "ink": "black", "muted": "black", "body_font": "sans",
        "name_font": "sans", "name_size": 120, "name_weight": 500, "name_lines": ["Funner"],
        "tagline": "Hair you want to wear.",
        "css": """
  .sk{fill:var(--sky)} .fl{fill:var(--flame)} .su{fill:var(--sun)} .li{fill:var(--lilac)} .gr{fill:var(--grass)}
""",
        "derivation": """
blocks      the five category pills at full size: sky, flame, sun, lilac, grass, each 200x40
arrangement a staggered stack of pills, one per category, like the nav row stood on end
pattern     pills (radius-pill), from the colour-coded navigation; plus one sky disc for the logo
scales      pill height 40 (rx 20), gaps space-2 (12)
""",
        "svg": """
<rect class="sk" x="40" y="32" width="200" height="40" rx="20"/>
<rect class="fl" x="96" y="84" width="240" height="40" rx="20"/>
<rect class="su" x="152" y="136" width="176" height="40" rx="20"/>
<rect class="li" x="72" y="188" width="208" height="40" rx="20"/>
<rect class="gr" x="200" y="240" width="240" height="40" rx="20"/>
<circle class="sk" cx="408" cy="80" r="48"/>
""",
    },
}

# ---------------------------------------------------------------- 1-800 Happy Birthday
happybday = {
    "slug": "1-800-happy-birthday",
    "title": "1-800 Happy Birthday",
    "namespace": "HappyBirthday",
    "source": {"url": "https://1800happybirthday.com/", "captured": CAPTURED},
    "fonts_href": GF + "family=Yellowtail&family=Archivo+Black&display=swap",
    "families": {
        "script": "\"Yellowtail\", cursive",
        "sans": "\"Archivo Black\", \"Arial Black\", sans-serif",
    },
    "colors": [
        tok("sky", "#81c9f7", "Page ground behind the clouds."),
        tok("cloud", "#edf5fb", "Cloud highlights and soft panels."),
        tok("sun", "#fbda0f", "The sun disc behind the message. `night` text on it is 14.2:1."),
        tok("amber", "#fdaf13", "Sun's outer glow and hover."),
        tok("toffee", "#744c17", "Script outline and shadow. 5.4:1 on `sun`."),
        tok("night", "#0b0b0b", "Script fill and the ENTER label."),
        tok("candy", "#c35bd6", "The ENTER button gradient's mid-tone (an approximation of the glossy pink–purple badge). `cloud` text on it is 3.3:1: the badge label is large and outlined in `night`, so it passes as large text only."),
    ],
    "type_groups": [
        {"name": "Script", "family": "script", "styles": [
            style("message", "64px", "64px", 400, "The tribute message, rotated −8°.", sample="For Every Life Taken Too Soon"),
            style("body", "16px", "24px", 400, "Small notes."),
        ]},
        {"name": "Sans", "family": "sans", "styles": [
            style("button", "24px", "24px", 400, "The ENTER badge.", ls="1px", sample="ENTER"),
        ]},
    ],
    "spacing": [
        tok("space-1", "8px", "Badge padding."),
        tok("space-2", "16px", "Margins."),
        tok("space-3", "48px", "Message to button."),
    ],
    "radius": [
        tok("radius-badge", "12px", "The ENTER badge."),
        tok("radius-sun", "50%", "The sun."),
    ],
    "readme": """
1-800 Happy Birthday is a tribute: "For every life taken too soon and for every heavenly birthday celebrated." The page is a summer sky with clouds and a glowing yellow sun, a black brush script message tilted across it, and a glossy ENTER badge. Built from the public site 1800happybirthday.com; fonts are open substitutes.

## Voice
- Tender and celebratory at once; title case script, no punctuation beyond what the sentence needs.

## Colour
- `sky` ground, `sun` and `amber` glow, `night` script with a `toffee` outline. `candy` for the badge.

## Typography
- The site uses a custom brush script ("quentineFont"); substitute **Yellowtail**. The badge uses a heavy sans (**Archivo Black**).
- Rotate the message −8°.

## Components
`SunMessage`, `EnterBadge` and `SkyPanel`.
""",
    "components": {
        "SunMessage": {
            "group": "Content", "height": 240,
            "readme": """
The tilted script message on the sun.

- `sun` disc with an `amber` glow; message `message` (scaled) in `night`, rotated −8°, centred.
""",
            "css": """
body{background:var(--sky);margin:0;height:240px;display:grid;place-items:center}
.s{width:210px;height:210px;border-radius:var(--radius-sun);background:var(--sun);box-shadow:0 0 0 14px var(--amber);display:grid;place-items:center}
p{font:400 30px/30px var(--font-script);color:var(--night);transform:rotate(-8deg);text-align:center;margin:0}
""",
            "html": "<div class=\"s\"><p>For Every Life<br>Taken Too Soon</p></div>",
        },
        "EnterBadge": {
            "group": "Actions", "height": 100,
            "readme": """
The glossy ENTER badge.

- `candy` ground, `cloud` `button` text with a 1px `night` outline, `radius-badge`, padding `space-1` × 16px.
""",
            "css": """
body{background:var(--sky);padding:24px}
button{background:var(--candy);color:var(--cloud);font:400 24px/24px var(--font-sans);letter-spacing:1px;border:2px solid var(--night);border-radius:var(--radius-badge);padding:8px 16px;-webkit-text-stroke:1px var(--night)}
""",
            "html": "<button>ENTER</button>",
        },
        "SkyPanel": {
            "group": "Content", "height": 120,
            "readme": """
A soft cloud panel for small notes.

- `cloud` ground, `body` script in `night`, padding `space-2`.
""",
            "css": """
body{background:var(--sky);padding:16px}
p{background:var(--cloud);color:var(--night);font:400 20px/26px var(--font-script);padding:16px;margin:0;border-radius:var(--radius-badge)}
""",
            "html": "<p>And for every heavenly birthday celebrated.</p>",
        },
    },
    "cover": {
        "ground": "sky", "ink": "night", "muted": "night", "body_font": "sans",
        "name_font": "script", "name_size": 72, "name_lines": ["1-800 Happy", "Birthday"],
        "tagline": "For every heavenly birthday celebrated.",
        "css": """
  .am{fill:var(--amber)} .su{fill:var(--sun)} .cl{fill:var(--cloud)} .ca{fill:var(--candy)}
""",
        "derivation": """
blocks      amber glow r=140 bleeding off the right · sun r=104 · three cloud pills · candy 96x36 badge
arrangement one huge sun rising off the right edge with clouds drifting across, as the hero frames it
pattern     a literal motif: the sun and clouds — soft pills from radius-badge and radius-sun
scales      radius-sun, radius-badge 12, gaps space-2 (16)
""",
        "svg": """
<circle class="am" cx="320" cy="144" r="148"/>
<circle class="su" cx="320" cy="144" r="108"/>
<rect class="cl" x="24" y="40" width="160" height="40" rx="20"/>
<rect class="cl" x="60" y="200" width="200" height="44" rx="22"/>
<rect class="cl" x="360" y="244" width="140" height="36" rx="18"/>
<rect class="ca" x="272" y="126" width="96" height="36" rx="12"/>
""",
    },
}

# ---------------------------------------------------------------- The List
thelist = {
    "slug": "the-list",
    "title": "The List",
    "namespace": "TheList",
    "source": {"url": "https://thelist.design/", "captured": CAPTURED},
    "fonts_href": "",
    "families": {"sans": "\"Helvetica Neue\", Helvetica, Arial, sans-serif"},
    "colors": [
        tok("page", "#f7f7f7", "Page ground."),
        tok("panel", "#f0f0f0", "Search field and hover rows."),
        tok("black", "#000000", "Headlines, the giant wordmark and the All tools button. 19.6:1 on `page`."),
        tok("grey", "#6b6b6b", "Tag cloud and nav. 5.0:1 on `page`, 4.8:1 on `panel`."),
        tok("graphite", "#555555", "Body copy. 6.9:1 on `page`."),
        tok("white", "#ffffff", "Text on `black` buttons."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("headline", "48px", "50px", 400, "Hero headline.", ls="-0.96px", sample="The living index of AI tools for designers"),
            style("title", "25px", "32.5px", 400, "Section titles."),
            style("lead", "18px", "21.6px", 400, "Subheads and \"Search tools\".", ls="-0.3px"),
            style("ui", "15px", "17.4px", 400, "Buttons and the wordmark in the nav.", ls="-0.3px"),
            style("body", "14px", "19.6px", 400, "Descriptions."),
            style("tag", "13px", "18.2px", 400, "Tag cloud and category nav.", ls="-0.13px", sample="2D animation  3D  3D Printing  AI detection"),
            style("label", "11px", "12.76px", 500, "Uppercase labels."),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Tag gap."),
        tok("space-2", "12px", "Page margin."),
        tok("space-3", "24px", "Between groups."),
        tok("space-4", "96px", "Hero padding."),
    ],
    "radius": [tok("radius-none", "0px", "Everything is square.")],
    "readme": """
The List is "the living index of AI tools for designers. If it's public, it's indexed." The site is a quiet grey index in Helvetica: a category nav across the top, a light headline, a dense wrapping tag cloud, and an enormous "the list." wordmark bleeding off the bottom of the page. Built from the public site thelist.design; Helvetica Neue is the site's own stack.

## Voice
- Short and declarative: "If it's public, it's indexed." Tags in their natural case (`ai art director`, `PNG`, `Claude`).

## Colour
- `black` and `grey` on `page`. No accent; the only fill is the `black` All tools button.

## Typography
- **Helvetica Neue** 400 at every size; hierarchy from size and grey value only. The wordmark is set lowercase at a huge size with a full stop.

## Components
`CategoryNav`, `TagCloud` and `Wordmark`.
""",
    "components": {
        "CategoryNav": {
            "group": "Navigation", "height": 70,
            "readme": """
Wordmark, category links, Submit a tool, and the black All tools button.

- Wordmark `ui` in `black`; categories `tag` in `grey`; button `black` with `white` text.
""",
            "css": """
body{background:var(--page);padding:12px;font:400 13px/18px var(--font-sans)}
.n{display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.w{font:500 15px/17px var(--font-sans);color:var(--black)}
.c{color:var(--grey)}
.r{margin-left:auto;display:flex;gap:8px;align-items:center;color:var(--black)}
.b{background:var(--black);color:var(--white);padding:2px 6px}
""",
            "html": "<div class=\"n\"><span class=\"w\">the list</span><span class=\"c\">UI/UX Design</span><span class=\"c\">Image Generation</span><span class=\"c\">Video</span><span class=\"r\">Submit a tool <span class=\"b\">All tools</span></span></div>",
        },
        "TagCloud": {
            "group": "Content", "height": 150,
            "readme": """
A dense wrapping cloud of tool tags.

- `tag` in `grey`, gap `space-1` × 12px; hover `black`.
""",
            "css": """
body{background:var(--page);padding:12px;display:flex;flex-wrap:wrap;gap:4px 12px;font:400 13px/18.2px var(--font-sans);max-width:380px}
a{color:var(--grey);text-decoration:none}
a:hover{color:var(--black)}
""",
            "html": "<a href=\"#\">2D animation</a><a href=\"#\">3D</a><a href=\"#\">3D Printing</a><a href=\"#\">AI detection</a><a href=\"#\">AI portfolio</a><a href=\"#\">AI video</a><a href=\"#\">API</a><a href=\"#\">Claude</a><a href=\"#\">Cursor</a><a href=\"#\">Gaming</a><a href=\"#\">branding</a><a href=\"#\">copywriting</a>",
        },
        "Wordmark": {
            "group": "Content", "height": 160,
            "readme": """
The giant lowercase wordmark bleeding off the bottom edge.

- `black`, 400, line-height 0.8, positioned so the bottom quarter is cropped.
""",
            "css": """
body{background:var(--page);margin:0;height:160px;overflow:hidden;position:relative}
p{position:absolute;bottom:-40px;left:12px;margin:0;font:400 170px/.8 var(--font-sans);letter-spacing:-6px;color:var(--black)}
""",
            "html": "<p>the list.</p>",
        },
    },
    "cover": {
        "ground": "page", "ink": "black", "muted": "graphite", "body_font": "sans",
        "name_font": "sans", "name_size": 120, "name_ls": "-4px", "name_lines": ["The List"],
        "tagline": "If it's public, it's indexed.",
        "css": """
  .pa{fill:var(--panel)} .gr{fill:var(--grey)} .bk{fill:var(--black)}
""",
        "derivation": """
blocks      panel 400x48 search field · black 64x20 All tools button · grey tag bars
arrangement the index: search field over a wrapping cloud of tags
pattern     the tag cloud as 24 short grey bars of varied length at a 20px line pitch
scales      gaps space-1 (4)/space-2 (12), radius-none
""",
        "svg": """
<rect class="bk" x="392" y="16" width="64" height="20"/>
<rect class="pa" x="24" y="56" width="432" height="48"/>
<g class="gr">
<rect x="24" y="128" width="60" height="8"/><rect x="96" y="128" width="20" height="8"/><rect x="128" y="128" width="72" height="8"/><rect x="212" y="128" width="64" height="8"/><rect x="288" y="128" width="40" height="8"/><rect x="340" y="128" width="88" height="8"/>
<rect x="24" y="148" width="96" height="8"/><rect x="132" y="148" width="48" height="8"/><rect x="192" y="148" width="28" height="8"/><rect x="232" y="148" width="80" height="8"/><rect x="324" y="148" width="56" height="8"/>
<rect x="24" y="168" width="40" height="8"/><rect x="76" y="168" width="104" height="8"/><rect x="192" y="168" width="60" height="8"/><rect x="264" y="168" width="36" height="8"/><rect x="312" y="168" width="92" height="8"/>
<rect x="24" y="188" width="72" height="8"/><rect x="108" y="188" width="56" height="8"/><rect x="176" y="188" width="88" height="8"/><rect x="276" y="188" width="44" height="8"/>
</g>
""",
    },
}

# ---------------------------------------------------------------- Sam Thies
samthies = {
    "slug": "sam-thies",
    "title": "Sam Thies",
    "namespace": "SamThies",
    "source": {"url": "https://samthies.com/", "captured": CAPTURED},
    "fonts_href": GF + "family=Red+Hat+Mono:wght@400&display=swap",
    "families": {"mono": "\"Red Hat Mono\", \"Quadrant Text Mono\", monospace"},
    "colors": [
        tok("fog", "#f5f5f5", "Page ground."),
        tok("ink", "#2b2728", "All text. 13.5:1 on `fog`."),
        tok("night", "#121212", "Dark sections and footer. `fog` text 17.2:1."),
        tok("haze", "rgba(255, 252, 248, 0.75)", "Caption backing over film stills."),
        tok("dust", "#958d85", "Outback dust tone from the film. Image placeholder only."),
        tok("earth", "#433731", "Shadowed earth tone. Image placeholder only."),
    ],
    "type_groups": [
        {"name": "Mono", "family": "mono", "styles": [
            style("body", "12px", "15.6px", 400, "Everything: nav, tagline, captions.", ls="-0.24px", sample="A collection of visual stories across people, place, and culture."),
            style("small", "10px", "13px", 400, "Credits and uppercase labels.", ls="-0.24px"),
        ]},
    ],
    "spacing": [
        tok("space-1", "6px", "Inline gaps."),
        tok("space-2", "12px", "Page margin."),
        tok("space-3", "24px", "Between captions."),
        tok("space-4", "96px", "Section padding."),
    ],
    "radius": [tok("radius-none", "0px", "Everything is square.")],
    "readme": """
Sam Thies is an Australian filmmaker and photographer: "A collection of visual stories across people, place, and culture." The homepage is a full-bleed still of the outback (a ute on red dust under a pale sky) with one line of small mono text across the top: name left, tagline centred, "Projects . Shop . About" right. Built from the public site samthies.com; the mono is an open substitute.

## Voice
- Calm and descriptive; nav separated by spaced full stops: "Projects . Shop . About".

## Colour
- `ink` on `fog` for text; the photograph carries colour. `dust` and `earth` stand in for it.

## Typography
- The site uses **Quadrant Text Mono**; substitute **Red Hat Mono**. Two sizes: 12px and 10px, tracked −0.24px.

## Components
`TopLine`, `FilmStill` and `Caption`.
""",
    "components": {
        "TopLine": {
            "group": "Navigation", "height": 70,
            "readme": """
Name, centred tagline, nav: one line of `body` mono.

- Three columns; nav items separated by " . ". `ink` on `fog` (or `fog` over dark film).
""",
            "css": """
body{background:var(--fog);padding:12px;font:400 12px/15.6px var(--font-mono);letter-spacing:-.24px;color:var(--ink)}
.t{display:grid;grid-template-columns:1fr 2fr 1fr;gap:12px}
.c{text-align:center}.r{text-align:right}
""",
            "html": "<div class=\"t\"><span>Sam Thies</span><span class=\"c\">A collection of visual stories across people, place, and culture.</span><span class=\"r\">Projects . Shop . About</span></div>",
        },
        "FilmStill": {
            "group": "Media", "height": 200,
            "readme": """
A full-bleed landscape still.

- Provide the image. Sky above a low horizon; `dust` placeholder until loaded.
""",
            "css": """
body{margin:0}
.s{height:200px;background:linear-gradient(var(--fog) 0 55%,var(--dust) 55% 100%)}
""",
            "html": "<div class=\"s\" role=\"img\" aria-label=\"A ute crossing red dust in the outback\"></div>",
        },
        "Caption": {
            "group": "Content", "height": 100,
            "readme": """
Project caption on a `haze` backing over imagery.

- Title `body`, credit `small`, `ink`.
""",
            "css": """
body{background:var(--earth);padding:16px}
.c{background:var(--haze);color:var(--ink);padding:8px 10px;display:inline-block;font:400 12px/15.6px var(--font-mono)}
small{display:block;font-size:10px;line-height:13px}
""",
            "html": "<div class=\"c\">Red Earth<small>Film, 2025 — Pilbara, WA</small></div>",
        },
    },
    "cover": {
        "ground": "fog", "ink": "ink", "muted": "ink", "body_font": "mono",
        "name_font": "mono", "name_size": 72, "name_ls": "-2px", "name_lines": ["Sam Thies"],
        "tagline": "Visual stories across people, place, and culture.",
        "css": """
  .du{fill:var(--dust)} .ea{fill:var(--earth)} .ni{fill:var(--night)}
""",
        "derivation": """
blocks      dust 480x120 ground band · earth 480x24 shadow band · night 40x14 (the ute)
arrangement a low horizon: strips of unequal bands across the bottom, sky (fog) above, as the hero still
pattern     horizontal bands, the outback horizon itself; no other marks
scales      bands 120/24, space-2 (12)
""",
        "svg": """
<rect class="du" x="0" y="168" width="480" height="120"/>
<rect class="ea" x="0" y="160" width="480" height="8"/>
<rect class="ea" x="0" y="248" width="480" height="40"/>
<rect class="ni" x="220" y="150" width="40" height="14"/>
""",
    },
}

SYSTEMS = [julien, raskos, baran, funner, happybday, thelist, samthies]
