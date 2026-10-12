from ds_lib import tok, style

CAPTURED = "2026-10-11"
GF = "https://fonts.googleapis.com/css2?"

# ---------------------------------------------------------------- Huichuan Wang (paintriver)
paintriver = {
    "slug": "huichuan-wang",
    "title": "Huichuan Wang",
    "namespace": "PaintRiver",
    "source": {"url": "https://paintriver.art/", "captured": CAPTURED},
    "fonts_href": GF + "family=DotGothic16&family=VT323&display=swap",
    "families": {
        "pixel": "\"DotGothic16\", \"PixelGeorgia\", monospace",
        "vcr": "\"VT323\", Monaco, \"Courier New\", monospace",
    },
    "colors": [
        tok("night", "#162641", "Page ground under the painting."),
        tok("lagoon", "rgba(0, 45, 62, 0.76)", "Tint laid over the background painting."),
        tok("ice", "#f3ffff", "All text, node dots and graph lines. 14.8:1 on `night`."),
        tok("ice-50", "rgba(243, 255, 255, 0.5)", "Secondary terminal lines and credits. 4.8:1 on `night`."),
        tok("moss", "#4f7a6a", "Mid-tone of the painted background. Placeholder fill only."),
    ],
    "type_groups": [
        {"name": "Pixel", "family": "pixel", "styles": [
            style("title", "27.2px", "54.4px", 400, "Name lines (绘川 / huichuan).", sample="绘川 >> huichuan"),
            style("terminal", "16px", "32px", 400, "Terminal intro lines.", ls="1.92px", sample="▶ hello and welcome :)"),
            style("terminal-light", "16px", "32px", 100, "Quiet terminal lines."),
            style("terminal-sm", "13.6px", "27.2px", 400, "Secondary lines.", ls="1.632px"),
            style("nav", "16px", "64px", 700, "WORKS / INFO."),
        ]},
        {"name": "VCR", "family": "vcr", "styles": [
            style("credit", "8px", "12px", 400, "Copyright line bottom-right.", ls="0.32px"),
        ]},
    ],
    "spacing": [
        tok("space-1", "8px", "Arrow-to-text gap."),
        tok("space-2", "16px", "Page margin."),
        tok("space-3", "32px", "Terminal line height."),
        tok("space-4", "64px", "Nav line height."),
    ],
    "radius": [tok("radius-node", "50%", "Graph nodes.")],
    "readme": """
Huichuan Wang (绘川, "paint river") is a multidisciplinary artist and designer. The portfolio is a creative-coding piece: a network of glowing nodes floats over a dark, teal-tinted painting, and the introduction types itself out like a terminal in a pixel font, in English and Chinese. Built from the public site paintriver.art; fonts are open substitutes.

## Voice
- Terminal greeting, lowercase, friendly: "▶ hello and welcome :)", "▶ you can call me >>>>>>", "curious about this creature? it lives in an ongoing creative coding project".
- Name shown in both scripts with ASCII arrows: `___> 绘川 >>__or__> huichuan >>`.

## Colour
- `ice` on `night`, with `lagoon` over the painting. One colour of light.

## Typography
- The site uses a custom pixel font with a pixel Georgia and VCR OSD Mono. Substitutes: **DotGothic16** (covers CJK) and **VT323**.
- Wide letter-spacing (1.6–1.9px) on terminal lines; double line-height (32px at 16px).

## Components
`TerminalIntro`, `NodeGraph` and `NavLinks`.
""",
    "components": {
        "TerminalIntro": {
            "group": "Content", "height": 230,
            "readme": """
The typed introduction: one line per prompt, each starting with ▶.

- Provide 3–6 lines. `terminal` in `ice`; secondary lines `terminal-sm` in `ice-50`. Links underlined.
""",
            "css": """
body{background:var(--night);color:var(--ice);padding:16px;font:400 16px/32px var(--font-pixel);letter-spacing:1.92px}
p{margin:0}
.s{font-size:13.6px;line-height:27.2px;letter-spacing:1.632px;color:var(--ice-50)}
a{color:var(--ice)}
""",
            "html": "<p>▶ hello and welcome :)</p><p>▶ you can call me &gt;&gt;&gt;&gt;&gt;&gt;</p><p>___&gt; 绘川 &gt;&gt;__or__&gt; huichuan &gt;&gt;</p><p class=\"s\">▶ I am a Multidisciplinary Artist and Designer</p><p class=\"s\">▶ Find out more about me <a href=\"#\">here!</a> :)</p>",
        },
        "NodeGraph": {
            "group": "Media", "height": 220,
            "readme": """
The constellation: nodes joined by thin lines.

- Generate from data; nodes 3–6px `ice` circles, edges 0.75px `ice-50`. Ground `night` with `lagoon` over imagery.
""",
            "css": """
body{background:var(--night);margin:0}
svg{display:block;width:100%;height:220px}
.e{stroke:var(--ice-50);stroke-width:.75}
.n{fill:var(--ice)}
""",
            "html": "<svg viewBox=\"0 0 400 220\" aria-hidden=\"true\"><g class=\"e\"><line x1=\"200\" y1=\"110\" x2=\"120\" y2=\"60\"/><line x1=\"200\" y1=\"110\" x2=\"290\" y2=\"50\"/><line x1=\"200\" y1=\"110\" x2=\"310\" y2=\"170\"/><line x1=\"200\" y1=\"110\" x2=\"90\" y2=\"160\"/><line x1=\"120\" y1=\"60\" x2=\"290\" y2=\"50\"/><line x1=\"90\" y1=\"160\" x2=\"120\" y2=\"60\"/><line x1=\"310\" y1=\"170\" x2=\"290\" y2=\"50\"/></g><g class=\"n\"><circle cx=\"200\" cy=\"110\" r=\"6\"/><circle cx=\"120\" cy=\"60\" r=\"4\"/><circle cx=\"290\" cy=\"50\" r=\"3\"/><circle cx=\"310\" cy=\"170\" r=\"4\"/><circle cx=\"90\" cy=\"160\" r=\"3\"/></g></svg>",
        },
        "NavLinks": {
            "group": "Navigation", "height": 90,
            "readme": """
Uppercase pixel nav at the top-right, plus a ✻ settings glyph.

- `nav` style at 13px, uppercase, `ice`, gap `space-3`.
""",
            "css": """
body{background:var(--night);padding:16px;display:flex;gap:32px;justify-content:flex-end;font:700 13px/1 var(--font-pixel);letter-spacing:1px}
a{color:var(--ice);text-decoration:none;text-transform:uppercase}
""",
            "html": "<a href=\"#\">Works</a><a href=\"#\">Info</a><a href=\"#\" aria-label=\"Settings\">✻</a>",
        },
    },
    "cover": {
        "ground": "night", "ink": "ice", "muted": "ice-50", "body_font": "pixel",
        "name_font": "pixel", "name_size": 64, "name_lines": ["Huichuan", "Wang"],
        "tagline": "▶ hello and welcome :)",
        "css": """
  .mo{fill:var(--moss)} .la{fill:var(--lagoon)}
  .e{stroke:var(--ice-50);stroke-width:.75} .n{fill:var(--ice)}
""",
        "derivation": """
blocks      moss 480x288 painting field under a lagoon tint 360x288 — the background painting
arrangement painted field bleeding off the right, tinted, with the graph floating over it
pattern     a literal motif: the node constellation — 12 ice nodes (radius-node) joined by ice-50 edges
scales      node radii 3–6, line height space-3 (32)
""",
        "svg": """
<rect class="mo" x="0" y="0" width="480" height="288"/>
<rect class="la" x="120" y="0" width="360" height="288"/>
<g class="e"><line x1="300" y1="140" x2="220" y2="60"/><line x1="300" y1="140" x2="400" y2="70"/><line x1="300" y1="140" x2="420" y2="220"/><line x1="300" y1="140" x2="200" y2="230"/><line x1="220" y1="60" x2="400" y2="70"/><line x1="200" y1="230" x2="120" y2="150"/><line x1="120" y1="150" x2="220" y2="60"/><line x1="420" y1="220" x2="460" y2="140"/><line x1="400" y1="70" x2="460" y2="140"/><line x1="60" y1="60" x2="120" y2="150"/></g>
<g class="n"><circle cx="300" cy="140" r="7"/><circle cx="220" cy="60" r="4"/><circle cx="400" cy="70" r="4"/><circle cx="420" cy="220" r="5"/><circle cx="200" cy="230" r="3"/><circle cx="120" cy="150" r="3"/><circle cx="460" cy="140" r="3"/><circle cx="60" cy="60" r="3"/></g>
""",
    },
}

# ---------------------------------------------------------------- Encyclopedia of Collecting Receipts
receipts = {
    "slug": "encyclopedia-of-collecting-receipts",
    "title": "Encyclopedia of Collecting Receipts",
    "namespace": "Receipts",
    "source": {"url": "https://mintiepnita.github.io/encyclopedia-of-collecting-receipts/index.html", "captured": CAPTURED},
    "fonts_href": GF + "family=Share+Tech+Mono&family=Big+Shoulders+Text:wght@500&display=swap",
    "families": {
        "receipt": "\"Share Tech Mono\", \"Courier New\", monospace",
        "wide": "\"Big Shoulders Text\", \"Arial Narrow\", sans-serif",
    },
    "colors": [
        tok("white", "#ffffff", "Page ground and inactive menu buttons."),
        tok("black", "#000000", "Text, borders, dashed rules and the active menu button. 21:1 on `white`."),
        tok("thermal", "#efede6", "Receipt paper tone in the collage (placeholder for scans)."),
        tok("faded", "#6b6b6b", "Faded thermal print and secondary notes. 5.3:1 on `white`."),
    ],
    "type_groups": [
        {"name": "Wide", "family": "wide", "styles": [
            style("title", "25.74px", "30px", 500, "The stacked title in the dashed frame, uppercase.", ls="1px", sample="ENCYCLOPEDIA OF COLLECTING RECEIPTS"),
            style("menu", "14.04px", "18px", 500, "Menu buttons, uppercase.", ls="1px"),
        ]},
        {"name": "Receipt", "family": "receipt", "styles": [
            style("body", "14px", "18px", 400, "Intro paragraph, centred.", sample="Welcome to The Encyclopedia of Collecting Receipts!"),
            style("lead", "21.06px", "26px", 400, "Large notes."),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Gap between stacked menu buttons."),
        tok("space-2", "8px", "Button padding."),
        tok("space-3", "16px", "Frame padding."),
        tok("space-4", "32px", "Between sections."),
    ],
    "radius": [tok("radius-circle", "50%", "The round dotted action badges (GET MESSY!, STACK TOGETHER, SPREAD OUT).")],
    "readme": """
The Encyclopedia of Collecting Receipts is an interactive archive: a draggable pile of scanned receipts (Walgreens, Costco, Safeway) beside a narrow column with the title in a dashed box, a centred typewriter intro and a stack of rectangular menu buttons. Round dotted badges offer actions: GET MESSY!, STACK TOGETHER, SPREAD OUT. Built from the public site by Mintie Pnita; fonts are open substitutes.

## Voice
- Playful instructions: "Now, dive into this draggable and interactive receipts area, where you can stack, spread, or even get messy with our receipts collection until satisfied!"
- Actions are verbs in caps with an exclamation where fun: GET MESSY!

## Colour
- Receipt black on white. The scans bring their own colour; `thermal` stands in for them.

## Typography
- The site uses **Hypermarket** (a receipt-printer face) in regular and expanded cuts. Substitutes: **Share Tech Mono** and **Big Shoulders Text**.
- Everything uppercase except the intro paragraph.

## Layout
- Dashed `black` rules above and below the menu, like tear lines. Title boxed with a dashed border.

## Components
`MenuStack`, `TitleFrame` and `ActionBadge`.
""",
    "components": {
        "MenuStack": {
            "group": "Navigation", "height": 210,
            "readme": """
Full-width rectangular menu buttons stacked with a dashed rule above and below.

- Active: `black` ground, `white` text. Others: 1px `black` border. `menu` style uppercase, padding `space-2`.
""",
            "css": """
body{background:var(--white);padding:16px;width:200px}
.r{border-top:1px dashed var(--black);margin:8px 0}
a{display:block;text-align:center;font:500 14px/18px var(--font-wide);letter-spacing:1px;text-transform:uppercase;border:1px solid var(--black);color:var(--black);padding:6px;margin:4px 0;text-decoration:none}
a.on{background:var(--black);color:var(--white)}
""",
            "html": "<div class=\"r\"></div><a class=\"on\" href=\"#\">Home</a><a href=\"#\">About</a><a href=\"#\">Overview</a><a href=\"#\">Collection</a><div class=\"r\"></div>",
        },
        "TitleFrame": {
            "group": "Content", "height": 150,
            "readme": """
The title stacked in a dashed frame.

- `title` style uppercase, centred, 1px dashed `black` border, `space-3` padding.
""",
            "css": """
body{background:var(--white);padding:16px}
h1{display:inline-block;font:500 24px/28px var(--font-wide);letter-spacing:1px;text-transform:uppercase;border:1px dashed var(--black);padding:10px 16px;margin:0;text-align:center}
""",
            "html": "<h1>Encyclopedia<br>of collecting<br>receipts</h1>",
        },
        "ActionBadge": {
            "group": "Actions", "height": 110,
            "readme": """
Round dotted badge buttons for collage actions.

- 52px circle, 1px dotted `black` border, `radius-circle`, two short uppercase lines in `menu` at 9px.
""",
            "css": """
body{background:var(--white);padding:16px;display:flex;gap:12px}
button{width:52px;height:52px;border-radius:var(--radius-circle);border:1px dotted var(--black);background:var(--white);font:500 9px/10px var(--font-wide);text-transform:uppercase;color:var(--black);padding:0}
""",
            "html": "<button>Get<br>messy!</button><button>Stack<br>together</button><button>Spread<br>out</button>",
        },
    },
    "cover": {
        "ground": "white", "ink": "black", "muted": "faded", "body_font": "receipt",
        "name_font": "wide", "name_size": 56, "name_weight": 500, "name_lines": ["Encyclopedia of", "Collecting Receipts"], "leading": 1,
        "tagline": "Stack, spread, or get messy.",
        "css": """
  .th{fill:var(--thermal)} .bk{fill:var(--black)}
  .dash{fill:none;stroke:var(--black);stroke-dasharray:4 4}
  .dot{fill:none;stroke:var(--black);stroke-dasharray:1 3}
""",
        "derivation": """
blocks      thermal receipts 72x240, 64x200, 80x220 fanned · one black 72x24 active menu key
arrangement receipts fanned and tilted like the draggable pile
pattern     dashed tear lines (dash 4) and two dotted action badges (radius-circle)
scales      gaps space-3 (16), badge 52
""",
        "svg": """
<rect class="th" x="120" y="24" width="72" height="240" transform="rotate(-8 156 144)"/>
<rect class="th" x="200" y="40" width="64" height="200" transform="rotate(4 232 140)"/>
<rect class="th" x="272" y="20" width="80" height="230" transform="rotate(-3 312 135)"/>
<rect class="bk" x="24" y="200" width="72" height="24"/>
<line class="dash" x1="16" y1="180" x2="104" y2="180"/>
<line class="dash" x1="16" y1="244" x2="104" y2="244"/>
<circle class="dot" cx="424" cy="56" r="26"/>
<circle class="dot" cx="424" cy="236" r="26"/>
""",
    },
}

# ---------------------------------------------------------------- Shay Zipori
shay = {
    "slug": "shay-zipori",
    "title": "Shay Zipori",
    "namespace": "ShayZipori",
    "source": {"url": "https://www.shayzipori.com/", "captured": CAPTURED},
    "fonts_href": GF + "family=IBM+Plex+Serif:wght@300;500&family=IBM+Plex+Sans+Condensed:wght@700&display=swap",
    "families": {
        "serif": "\"IBM Plex Serif\", Georgia, serif",
        "display": "\"IBM Plex Sans Condensed\", \"Helvetica Neue\", sans-serif",
    },
    "colors": [
        tok("black", "#000000", "Page ground: products photographed white-on-black."),
        tok("white", "#ffffff", "Text and the wordmark. 21:1 on `black`."),
        tok("graphite", "#353535", "The wordmark tab and hover panels. `white` text 12.3:1."),
        tok("scrim", "rgba(0, 0, 0, 0.8)", "Overlay behind project captions."),
        tok("tan", "#765e3e", "Rare warm accent from packaging. Decorative only."),
    ],
    "type_groups": [
        {"name": "Display", "family": "display", "styles": [
            style("wordmark", "47.25px", "61.425px", 700, "The name in the tab.", ls="-2px", sample="Shay Zipori"),
        ]},
        {"name": "Serif", "family": "serif", "styles": [
            style("lead", "21px", "29.4px", 500, "Project titles."),
            style("body", "16px", "25.6px", 300, "Captions and bio.", sample="Packaging and product design."),
            style("small", "15px", "19.5px", 300, "Index and About links."),
        ]},
    ],
    "spacing": [
        tok("space-1", "8px", "Tab inner gaps."),
        tok("space-2", "16px", "Page margin."),
        tok("space-3", "32px", "Between objects."),
        tok("space-4", "64px", "Section padding."),
    ],
    "radius": [tok("radius-none", "0px", "Everything; the tab and frames are square.")],
    "readme": """
Shay Zipori is a packaging and product designer. The portfolio lays objects (bottles, straps, carabiners, sleeves) flat on pure black, all rendered white, as if X-rayed. A small graphite tab in the corner holds a heavy condensed wordmark with Index and About under it. Built from the public site shayzipori.com; IBM Plex Serif is the site's own face, the wordmark face is a substitute.

## Colour
- `white` on `black`. `graphite` for the tab. Products are white on black, never in colour on the home page.

## Typography
- **IBM Plex Serif** 300 for reading and 500 for titles. The wordmark is a tight heavy condensed sans (substituted by **IBM Plex Sans Condensed** 700, tracked −2px).

## Layout
- Objects scattered at angles across the black, overlapping the viewport edges. The tab sits top-left, never centred.

## Components
`WordmarkTab`, `ProjectCaption` and `ObjectField`.
""",
    "components": {
        "WordmarkTab": {
            "group": "Navigation", "height": 120,
            "readme": """
The corner tab with the name and two links.

- `graphite` ground, `wordmark` in `white`, Index / About in `small` spread to the tab's edges.
""",
            "css": """
body{background:var(--black);padding:16px}
.t{display:inline-block;background:var(--graphite);color:var(--white);padding:4px 12px 6px}
.w{font:700 34px/1 var(--font-display);letter-spacing:-2px}
.l{display:flex;justify-content:space-between;font:300 12px/1.4 var(--font-serif)}
.l a{color:var(--white);text-decoration:none}
""",
            "html": "<div class=\"t\"><div class=\"w\">Shay Zipori</div><div class=\"l\"><a href=\"#\">Index</a><a href=\"#\">About</a></div></div>",
        },
        "ProjectCaption": {
            "group": "Content", "height": 130,
            "readme": """
Title and one-line description over the `scrim`.

- Title `lead`, description `body`, both `white`.
""",
            "css": """
body{background:var(--black);padding:16px}
.c{background:var(--scrim);color:var(--white);padding:16px;max-width:360px}
h3{font:500 21px/29.4px var(--font-serif);margin:0}
p{font:300 16px/25.6px var(--font-serif);margin:0}
""",
            "html": "<div class=\"c\"><h3>Hydration kit</h3><p>Bottle, strap and carabiner for a running brand.</p></div>",
        },
        "ObjectField": {
            "group": "Media", "height": 200,
            "readme": """
Products laid out flat on black at angles.

- White silhouettes or white renders on `black`, rotated −30° to 30°, overlapping edges. No drop shadows.
""",
            "css": """
body{background:var(--black);margin:0}
svg{display:block;width:100%;height:200px}
.o{fill:var(--white)}
""",
            "html": "<svg viewBox=\"0 0 400 200\" role=\"img\" aria-label=\"Product silhouettes\"><rect class=\"o\" x=\"40\" y=\"40\" width=\"60\" height=\"120\" rx=\"20\" transform=\"rotate(-20 70 100)\"/><rect class=\"o\" x=\"170\" y=\"70\" width=\"120\" height=\"16\" transform=\"rotate(15 230 78)\"/><rect class=\"o\" x=\"320\" y=\"60\" width=\"50\" height=\"80\" transform=\"rotate(8 345 100)\"/></svg>",
        },
    },
    "cover": {
        "ground": "black", "ink": "white", "muted": "white", "body_font": "serif",
        "name_font": "display", "name_size": 88, "name_weight": 700, "name_ls": "-3px", "name_lines": ["Shay", "Zipori"],
        "tagline": "Objects, laid flat, in white.",
        "css": """
  .wh{fill:var(--white)} .gr{fill:var(--graphite)} .ta{fill:var(--tan)}
""",
        "derivation": """
blocks      white bottle 72x160 and sleeve 96x120 · graphite 120x64 (the tab) · tan 16x16 (packaging accent)
arrangement objects scattered at angles across black, bleeding off the edge
pattern     a strap: one long white band crossing the box at 15°, from the product photography
scales      space-2 (16) gaps, radius-none except the bottle shoulder
""",
        "svg": """
<rect class="gr" x="24" y="24" width="120" height="64"/>
<rect class="wh" x="160" y="60" width="72" height="160" rx="24" transform="rotate(-18 196 140)"/>
<rect class="wh" x="320" y="120" width="96" height="120" transform="rotate(10 368 180)"/>
<rect class="wh" x="40" y="200" width="440" height="14" transform="rotate(-12 260 207)"/>
<rect class="ta" x="440" y="40" width="16" height="16"/>
""",
    },
}

# ---------------------------------------------------------------- Estelle
estelle = {
    "slug": "estelle",
    "title": "Estelle",
    "namespace": "Estelle",
    "source": {"url": "https://www.estellescottsdale.com/", "captured": CAPTURED},
    "fonts_href": GF + "family=Ojuju:wght@300;400&family=Fustat:wght@400&family=Spline+Sans+Mono:wght@400&family=Oooh+Baby&display=swap",
    "families": {
        "display": "\"Ojuju\", sans-serif",
        "sans": "\"Fustat\", sans-serif",
        "mono": "\"Spline Sans Mono\", monospace",
        "script": "\"Oooh Baby\", cursive",
    },
    "colors": [
        tok("cream", "#fcecd2", "Page ground (desert sun on stucco)."),
        tok("olive", "#222d18", "Text and the engraved ornament. 12.4:1 on `cream`, 11.6:1 on `sage`."),
        tok("sage", "#daebe0", "Secondary sections and the menu overlay."),
        tok("shade", "rgba(10, 10, 10, 0.64)", "Overlay behind photography and modals."),
    ],
    "type_groups": [
        {"name": "Display", "family": "display", "styles": [
            style("display-xl", "100.8px", "100.8px", 300, "\"Meet Estelle\" and hero words.", sample="Meet Estelle"),
            style("display", "72px", "72px", 400, "Section titles."),
        ]},
        {"name": "Script", "family": "script", "styles": [
            style("script", "48px", "48px", 400, "One handwritten word per section."),
        ]},
        {"name": "Text", "family": "sans", "styles": [
            style("body", "17.6px", "24px", 400, "Paragraphs.", sample="An open-air restaurant in Scottsdale."),
        ]},
        {"name": "Mono", "family": "mono", "styles": [
            style("label", "12.8px", "20px", 400, "Uppercase nav, buttons, hours.", sample="RESERVATIONS  MENUS  EVENTS"),
            style("label-lg", "14px", "20px", 400, "Addresses and hours."),
        ]},
    ],
    "spacing": [
        tok("space-1", "8px", "Inline gaps."),
        tok("space-2", "16px", "Button padding."),
        tok("space-3", "32px", "Page margin."),
        tok("space-4", "96px", "Section padding."),
    ],
    "radius": [
        tok("radius-pill", "1440px", "Buttons."),
        tok("radius-round", "100%", "Round stamps."),
    ],
    "readme": """
Estelle is an open-air restaurant in Scottsdale, Arizona. The site is engraved and sunny: a cream ground covered in a symmetrical olive line-drawing of suns, swallows and leaves, a light display face for "Meet Estelle", mono caps for practical things and a touch of script. Built from the public site estellescottsdale.com; all four fonts are the site's own Google faces.

## Voice
- Warm hospitality, short: "Meet Estelle." Practical lines in caps: RESERVATIONS, MENUS, HOURS.

## Colour
- `olive` on `cream`, always. `sage` for quieter sections. Photography sits under `shade` when text crosses it.

## Typography
- **Ojuju** (light) for display, **Fustat** for paragraphs, **Spline Sans Mono** uppercase for UI, **Oooh Baby** for one handwritten word.

## Imagery
- The engraved ornament is the identity; it is not reproduced here. Use olive line art on cream if you draw your own.

## Components
`PillButton`, `HoursBlock` and `Welcome`.
""",
    "components": {
        "PillButton": {
            "group": "Actions", "height": 90,
            "readme": """
Outlined pill buttons with mono caps.

- 1px `olive` border, `label` text uppercase, `radius-pill`, padding `space-1` × `space-2`. Filled variant: `olive` with `cream` text.
""",
            "css": """
body{background:var(--cream);padding:24px;display:flex;gap:8px}
.b{font:400 12.8px/20px var(--font-mono);text-transform:uppercase;border:1px solid var(--olive);border-radius:var(--radius-pill);padding:6px 16px;cursor:pointer}
.o{background:transparent;color:var(--olive)}
.f{background:var(--olive);color:var(--cream)}
""",
            "html": "<button class=\"b f\">Reservations</button><button class=\"b o\">Menus</button>",
        },
        "HoursBlock": {
            "group": "Content", "height": 170,
            "readme": """
Opening hours and address in mono caps.

- Days and times `label-lg` uppercase, address `body`, all `olive` on `sage`.
""",
            "css": """
body{background:var(--sage);color:var(--olive);padding:24px}
dl{display:grid;grid-template-columns:auto auto;gap:4px 24px;font:400 14px/20px var(--font-mono);text-transform:uppercase;margin:0 0 12px;justify-content:start}
dd{margin:0}
p{font:400 17.6px/24px var(--font-sans);margin:0}
""",
            "html": "<dl><dt>Tue – Thu</dt><dd>5pm – 10pm</dd><dt>Fri – Sat</dt><dd>5pm – 11pm</dd><dt>Sunday</dt><dd>4pm – 9pm</dd></dl><p>Scottsdale, Arizona</p>",
        },
        "Welcome": {
            "group": "Content", "height": 200,
            "readme": """
The centred two-line welcome with a script word above.

- Script word in `script`, title in `display-xl` (scaled), both `olive`, centred.
""",
            "css": """
body{background:var(--cream);color:var(--olive);padding:24px;text-align:center}
.s{font:400 32px/1 var(--font-script);margin:0}
h1{font:300 64px/64px var(--font-display);margin:0}
""",
            "html": "<p class=\"s\">welcome</p><h1>Meet<br>Estelle</h1>",
        },
    },
    "cover": {
        "ground": "cream", "ink": "olive", "muted": "olive", "body_font": "sans",
        "name_font": "display", "name_size": 112, "name_weight": 300, "name_lines": ["Estelle"],
        "tagline": "An open-air restaurant in Scottsdale.",
        "css": """
  .sa{fill:var(--sage)} .ol{fill:var(--olive)}
  .ray{stroke:var(--olive);stroke-width:2}
  .sun{fill:none;stroke:var(--olive);stroke-width:2}
""",
        "derivation": """
blocks      sage 200x288 arch panel (radius-round top) · olive 56x56 disc
arrangement one tall arched panel with a sun over it, symmetric, like the engraved ornament
pattern     a literal motif: the sun — a ring with twelve rays in olive, from the engraving
scales      space-3 (32) margins, radius-round
""",
        "svg": """
<path class="sa" d="M 160 288 L 160 120 A 100 100 0 0 1 360 120 L 360 288 Z"/>
<circle class="sun" cx="260" cy="128" r="36"/>
<circle class="ol" cx="260" cy="128" r="20"/>
<g class="ray"><line x1="260" y1="72" x2="260" y2="56"/><line x1="260" y1="184" x2="260" y2="200"/><line x1="204" y1="128" x2="188" y2="128"/><line x1="316" y1="128" x2="332" y2="128"/><line x1="220" y1="88" x2="209" y2="77"/><line x1="300" y1="168" x2="311" y2="179"/><line x1="300" y1="88" x2="311" y2="77"/><line x1="220" y1="168" x2="209" y2="179"/></g>
""",
    },
}

# ---------------------------------------------------------------- Don't Do Drugs
ddd = {
    "slug": "dont-do-drugs",
    "title": "Don't Do Drugs",
    "namespace": "DontDoDrugs",
    "source": {"url": "https://dontdodrugs.co/", "captured": CAPTURED},
    "fonts_href": GF + "family=Anton&family=Bebas+Neue&display=swap",
    "families": {
        "display": "\"Anton\", Impact, sans-serif",
        "condensed": "\"Bebas Neue\", \"Arial Narrow\", sans-serif",
    },
    "colors": [
        tok("tape", "#ffcc00", "Caution-tape yellow: the banners and most grounds."),
        tok("black", "#000000", "Banner text and the page under the tape. 13.9:1 on `tape`."),
        tok("go", "#2dff54", "Toggle knob and portrait tile. `black` text 15.5:1."),
        tok("magenta", "#ff13f0", "Portrait tile ground. `black` text 6.6:1."),
        tok("cyan", "#02b4e8", "Portrait tile ground. `black` text 8.7:1."),
        tok("peach", "#ffe9cf", "Toggle track."),
        tok("leaf", "#10cd00", "Secondary green. `black` text 9.8:1."),
    ],
    "type_groups": [
        {"name": "Display", "family": "display", "styles": [
            style("banner", "198px", "198px", 400, "The repeating STAY WEIRD tape, uppercase.", sample="STAY WEIRD"),
            style("headline", "78px", "78px", 400, "Section heads, uppercase."),
        ]},
        {"name": "Condensed", "family": "condensed", "styles": [
            style("title", "79.2px", "87.12px", 400, "Large labels."),
            style("sub", "39px", "39px", 400, "Sub-labels."),
            style("small", "19.5px", "24px", 400, "Small caps labels.", ls="0.975px"),
        ]},
    ],
    "spacing": [
        tok("space-1", "8px", "Tile padding."),
        tok("space-2", "16px", "Gaps."),
        tok("space-3", "32px", "Margins."),
        tok("space-4", "64px", "Banner height step."),
    ],
    "radius": [
        tok("radius-sm", "10.4px", "Portrait tiles."),
        tok("radius-md", "13px", "Cards."),
        tok("radius-lg", "19.5px", "Large tiles."),
        tok("radius-pill", "130px", "The toggle."),
    ],
    "readme": """
Don't Do Drugs Ltd. is a studio that says one thing loudly: STAY WEIRD. The homepage is layers of caution-yellow tape set in giant black condensed caps, tilted and overlapping, with clay-rendered portraits on saturated tiles and a big green toggle. Built from the public site dontdodrugs.co; Anton and Bebas Neue are the site's own Google faces.

## Voice
- Shouted, repeated, uppercase: STAY WEIRD STAY WEIRD STAY WEIRD.

## Colour
- `tape` and `black` dominate. `go`, `magenta`, `cyan` and `leaf` are tile grounds behind portraits. Always `black` text.

## Typography
- **Anton** for the tape; **Bebas Neue** for everything else. Uppercase only.

## Layout
- Banners rotate between −8° and 8°, overlap, and run off both edges. Nothing is aligned on purpose.

## Components
`TapeBanner`, `Toggle` and `PortraitTile`.
""",
    "components": {
        "TapeBanner": {
            "group": "Content", "height": 200,
            "readme": """
A tilted strip of caution tape with the slogan repeated.

- `tape` ground, `banner` (scaled) in `black`, rotated −4° to 6°, overflowing both edges.
""",
            "css": """
body{background:var(--black);margin:0;overflow:hidden;height:200px}
.t{background:var(--tape);color:var(--black);font:400 72px/80px var(--font-display);text-transform:uppercase;white-space:nowrap;margin:40px -40px;transform:rotate(-4deg)}
""",
            "html": "<div class=\"t\">Stay weird stay weird stay weird</div>",
        },
        "Toggle": {
            "group": "Inputs", "height": 120,
            "readme": """
The big pill toggle with a green knob.

- Track `peach`, knob `go`, 2px `black` outline, `radius-pill`. Needs a label for screen readers.
""",
            "css": """
body{background:var(--tape);padding:24px}
button{width:120px;height:60px;border-radius:var(--radius-pill);background:var(--peach);border:2px solid var(--black);position:relative;padding:0}
button i{position:absolute;right:6px;top:6px;width:44px;height:44px;border-radius:var(--radius-pill);background:var(--go);border:2px solid var(--black);box-sizing:border-box}
""",
            "html": "<button role=\"switch\" aria-checked=\"true\" aria-label=\"Weird mode\"><i></i></button>",
        },
        "PortraitTile": {
            "group": "Media", "height": 140,
            "readme": """
Square portrait tiles on saturated grounds.

- 88px squares, `radius-sm`, ground from `go`, `magenta`, `cyan`; the portrait is the user's image.
""",
            "css": """
body{background:var(--tape);padding:24px;display:flex;gap:16px}
.t{width:88px;height:88px;border-radius:var(--radius-sm)}
""",
            "html": "<div class=\"t\" style=\"background:var(--cyan)\" role=\"img\" aria-label=\"Portrait\"></div><div class=\"t\" style=\"background:var(--go)\" role=\"img\" aria-label=\"Portrait\"></div><div class=\"t\" style=\"background:var(--magenta)\" role=\"img\" aria-label=\"Portrait\"></div>",
        },
    },
    "cover": {
        "ground": "tape", "ink": "black", "muted": "black", "body_font": "condensed",
        "name_font": "display", "name_size": 72, "name_lines": ["Don't Do", "Drugs"],
        "tagline": "Stay weird.",
        "css": """
  .bk{fill:var(--black)} .go{fill:var(--go)} .mg{fill:var(--magenta)} .cy{fill:var(--cyan)}
""",
        "derivation": """
blocks      black tape bands 560x48 ×3 tilted · go, magenta, cyan portrait tiles 64x64
arrangement layered tilted bands running off both edges, tiles pinned over them
pattern     stripes at a tape pitch (space-4, 64), from "loud, bold, poster type"
scales      tiles radius-sm (10.4), bands 48 tall
""",
        "svg": """
<rect class="bk" x="-40" y="24" width="560" height="48" transform="rotate(-6 240 48)"/>
<rect class="bk" x="-40" y="120" width="560" height="48" transform="rotate(4 240 144)"/>
<rect class="bk" x="-40" y="216" width="560" height="48" transform="rotate(-3 240 240)"/>
<rect class="cy" x="96" y="88" width="64" height="64" rx="10.4"/>
<rect class="go" x="248" y="168" width="64" height="64" rx="10.4"/>
<rect class="mg" x="384" y="64" width="64" height="64" rx="10.4"/>
""",
    },
}

# ---------------------------------------------------------------- Junyeop Lee
junyeop = {
    "slug": "junyeop-lee",
    "title": "Junyeop Lee",
    "namespace": "JunyeopLee",
    "source": {"url": "https://junyeoplee.com/", "captured": CAPTURED},
    "fonts_href": "",
    "families": {"sans": "\"Helvetica Neue\", Helvetica, Arial, sans-serif"},
    "colors": [
        tok("black", "#000000", "Page ground."),
        tok("white", "#ffffff", "Text and the active index row. 21:1 on `black`."),
        tok("silver", "#c8c8c8", "Secondary info (time, date). 12.6:1 on `black`."),
        tok("smoke", "#bbbbbb", "Tertiary meta. 10.9:1 on `black`."),
        tok("white-70", "rgba(255, 255, 255, 0.7)", "Hover states over video."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("nav", "13.2px", "21.12px", 700, "Uppercase name, clock and nav.", sample="JUNYEOP LEE  16:56:34 (KST) SUNDAY OCTOBER 11 2026"),
            style("label", "12px", "16.8px", 700, "Uppercase index rows.", ls="0.6px"),
            style("body", "13.2px", "18.48px", 500, "Credits and descriptions."),
        ]},
    ],
    "spacing": [
        tok("space-1", "8px", "Gaps in the top bar."),
        tok("space-2", "12px", "Page margin."),
        tok("space-3", "24px", "Between columns."),
        tok("space-4", "96px", "Around the video frame."),
    ],
    "radius": [tok("radius-circle", "50%", "The single round toggle.")],
    "readme": """
Junyeop Lee is a director and editor. The site is a black cinema: one video frame centred on black, a single line of bold uppercase Helvetica across the top with the name, a live clock in Korean Standard Time and the date, and three nav words. Built from the public site junyeoplee.com; Helvetica Neue is the site's own stack.

## Voice
- Facts only: name, time, date, WORKS, INDEX, CONTACT.

## Colour
- `white` on `black`; `silver` for the clock. Video carries all other colour.

## Typography
- **Helvetica Neue** bold, uppercase, 12–13px. No other sizes on the home page.

## Layout
- Top bar spans the width; video centred with wide black margins; adjacent projects peek in from the edges.

## Components
`TopBar`, `VideoFrame` and `IndexRow`.
""",
    "components": {
        "TopBar": {
            "group": "Navigation", "height": 70,
            "readme": """
Name, live clock with time zone and date, then nav.

- `nav` style uppercase; name and nav `white`, clock `silver`. One line, gap `space-3`.
""",
            "css": """
body{background:var(--black);padding:12px;font:700 13.2px/21.12px var(--font-sans);text-transform:uppercase;color:var(--white)}
.b{display:flex;gap:24px;flex-wrap:wrap}
.t{color:var(--silver)}
.n{margin-left:auto;display:flex;gap:16px}
""",
            "html": "<div class=\"b\"><span>Junyeop Lee</span><span class=\"t\">16:56:34 (KST) Sunday October 11 2026</span><span class=\"n\"><span>Works</span><span>Index</span><span>Contact</span></span></div>",
        },
        "VideoFrame": {
            "group": "Media", "height": 220,
            "readme": """
A centred 16:9 video with generous black around it.

- Provide a video or poster image; no border, no radius. Title on hover in `nav` style.
""",
            "css": """
body{background:var(--black);padding:24px;display:grid;place-items:center}
.v{width:280px;aspect-ratio:16/9;max-width:100%;background:var(--smoke)}
""",
            "html": "<div class=\"v\" role=\"img\" aria-label=\"Film still\"></div>",
        },
        "IndexRow": {
            "group": "Content", "height": 120,
            "readme": """
A row in the project index: title, client, year.

- `label` style uppercase; title `white`, client and year `smoke`; 1px `white` rule between rows at 20% opacity.
""",
            "css": """
body{background:var(--black);padding:12px;font:700 12px/16.8px var(--font-sans);letter-spacing:.6px;text-transform:uppercase}
.r{display:grid;grid-template-columns:2fr 1fr 60px;gap:16px;padding:8px 0;border-bottom:1px solid var(--white-70);color:var(--smoke)}
.r span:first-child{color:var(--white)}
""",
            "html": "<div class=\"r\"><span>Cleanse</span><span>Music video</span><span>2026</span></div><div class=\"r\"><span>Red Room</span><span>Short film</span><span>2025</span></div>",
        },
    },
    "cover": {
        "ground": "black", "ink": "white", "muted": "silver", "body_font": "sans",
        "name_font": "sans", "name_size": 80, "name_weight": 700, "name_ls": "-2px", "name_lines": ["Junyeop", "Lee"],
        "tagline": "16:56:34 (KST) Sunday October 11 2026",
        "css": """
  .sm{fill:var(--smoke)} .si{fill:var(--silver)}
""",
        "derivation": """
blocks      smoke 224x126 centred video frame · silver 40x126 slivers of neighbouring frames at both edges
arrangement one 16:9 frame centred on black with neighbours peeking in, as on the home page
pattern     none beyond the frames: a black-cinema brand; one 1px silver rule for the top bar
scales      margins space-4 (96 → 48 here), 16:9
""",
        "svg": """
<rect class="si" x="0" y="16" width="480" height="1"/>
<rect class="sm" x="128" y="81" width="224" height="126"/>
<rect class="si" x="0" y="81" width="40" height="126"/>
<rect class="si" x="440" y="81" width="40" height="126"/>
""",
    },
}

# ---------------------------------------------------------------- windows (wndws.space)
wndws = {
    "slug": "windows",
    "title": "windows",
    "namespace": "Windows",
    "source": {"url": "https://wndws.space/", "captured": CAPTURED},
    "fonts_href": GF + "family=Inter:wght@500&display=swap",
    "families": {
        "sans": "Arial, Helvetica, sans-serif",
        "ui": "\"Inter\", sans-serif",
        "serif": "\"Times New Roman\", Times, serif",
    },
    "colors": [
        tok("concrete", "#cacaca", "Page ground: the wall the windows are cut into."),
        tok("black", "#000000", "Text. 12.8:1 on `concrete`."),
        tok("white", "#ffffff", "Window frames and sills."),
        tok("sill", "#dcdcdc", "Frame shadows and secondary panels."),
        tok("muted", "rgba(0, 0, 0, 0.45)", "Secondary labels. 3.1:1 on `concrete`, the site's own value; keep to labels that also have a primary label."),
        tok("frame-top", "#1b3e7e", "Top of the browser-window border gradient (the site sits in a blue window frame)."),
        tok("frame-bottom", "#8ec5ee", "Bottom of the window border gradient."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("body", "13.3333px", "16px", 400, "System text: captions and place names."),
        ]},
        {"name": "UI", "family": "ui", "styles": [
            style("ui", "13px", "16px", 500, "Controls and nav.", ls="-0.3px"),
            style("ui-lg", "16px", "20px", 500, "Section labels.", ls="-0.25px"),
            style("micro", "10px", "12px", 500, "Coordinates and timestamps."),
        ]},
        {"name": "Serif", "family": "serif", "styles": [
            style("quote", "17px", "17.85px", 400, "The tagline and quotes.", sample="place is temporary. you are not."),
        ]},
    ],
    "spacing": [
        tok("space-1", "6px", "Frame inset."),
        tok("space-2", "12px", "Sill depth."),
        tok("space-3", "24px", "Margins."),
        tok("space-4", "96px", "Gap between windows."),
    ],
    "radius": [
        tok("radius-sm", "6px", "Controls."),
        tok("radius-md", "10px", "The outer browser frame."),
    ],
    "readme": """
windows is a photo diary: "place is temporary. you are not." Photos of sunsets and trees sit in tall white window frames cut into a flat concrete-grey wall, all inside a rounded blue window border that recalls an old operating system. Built from the public site wndws.space; Arial, Inter and Times are the site's own faces.

## Voice
- Lowercase, reflective: "place is temporary. you are not."

## Colour
- `concrete` wall, `white` frames with `sill` shading, `black` text. The blue `frame-top` → `frame-bottom` border is the only colour in the chrome.

## Typography
- System **Arial** for captions, **Inter** 500 for controls, **Times New Roman** for the tagline.

## Layout
- Tall portrait windows in a row at a wide pitch, each with a thick white frame and a lighter sill below.

## Components
`WindowFrame`, `Tagline` and `BrowserFrame`.
""",
    "components": {
        "WindowFrame": {
            "group": "Media", "height": 230,
            "readme": """
A photo set in a deep white window frame on the concrete wall.

- Provide a portrait image (3:4). Frame 12px `white` on top and sides, a `sill` ledge below. No radius.
""",
            "css": """
body{background:var(--concrete);padding:16px;display:flex;gap:48px}
.w{background:var(--white);padding:12px 12px 0;box-shadow:inset -6px 0 0 var(--sill)}
.p{width:110px;height:146px;background:var(--black)}
.s{height:12px;background:var(--sill);margin:0 -12px}
""",
            "html": "<div class=\"w\"><div class=\"p\" role=\"img\" aria-label=\"Sunset over the bay\"></div><div class=\"s\"></div></div><div class=\"w\"><div class=\"p\" role=\"img\" aria-label=\"Tree at dusk\"></div><div class=\"s\"></div></div>",
        },
        "Tagline": {
            "group": "Content", "height": 90,
            "readme": """
The serif tagline.

- `quote` style, `black`, lowercase, on `concrete`.
""",
            "css": """
body{background:var(--concrete);padding:24px;font:400 17px/17.85px var(--font-serif);color:var(--black)}
""",
            "html": "place is temporary. you are not.",
        },
        "BrowserFrame": {
            "group": "Navigation", "height": 160,
            "readme": """
The rounded blue window border around the whole page.

- 4px border as a vertical `frame-top` → `frame-bottom` gradient, `radius-md`, content on `concrete`.
""",
            "css": """
body{background:var(--white);padding:16px}
.f{padding:4px;border-radius:var(--radius-md);background:linear-gradient(var(--frame-top),var(--frame-bottom))}
.i{background:var(--concrete);border-radius:7px;height:110px;display:grid;place-items:center;font:500 13px/16px var(--font-ui);color:var(--black)}
""",
            "html": "<div class=\"f\"><div class=\"i\">wndws.space</div></div>",
        },
    },
    "cover": {
        "ground": "concrete", "ink": "black", "muted": "black", "body_font": "sans",
        "name_font": "serif", "name_size": 112, "name_lines": ["windows"],
        "tagline": "place is temporary. you are not.",
        "css": """
  .wh{fill:var(--white)} .si{fill:var(--sill)} .ft{fill:var(--frame-top)} .fb{fill:var(--frame-bottom)} .bk{fill:var(--black)}
""",
        "derivation": """
blocks      white frames 96x176 ×3 with sill ledges · black photo panes inside · frame-top/frame-bottom 8px border bands at top and bottom
arrangement a row of tall windows at a wide pitch cut into the wall, as the diary lays them out
pattern     tiles: window frames with sills, three units, from "geometric, modular"
scales      frame 12, sill 12, pitch 144
""",
        "svg": """
<rect class="ft" x="0" y="0" width="480" height="6"/>
<rect class="fb" x="0" y="282" width="480" height="6"/>
<rect class="wh" x="24" y="52" width="96" height="176"/><rect class="bk" x="36" y="64" width="72" height="152"/><rect class="si" x="20" y="228" width="104" height="12"/>
<rect class="wh" x="168" y="52" width="96" height="176"/><rect class="bk" x="180" y="64" width="72" height="152"/><rect class="si" x="164" y="228" width="104" height="12"/>
<rect class="wh" x="312" y="52" width="96" height="176"/><rect class="si" x="308" y="228" width="104" height="12"/>
""",
    },
}

# ---------------------------------------------------------------- SCNG
scng = {
    "slug": "scng",
    "title": "SCNG",
    "namespace": "Scng",
    "source": {"url": "https://scng.work/", "captured": CAPTURED},
    "fonts_href": GF + "family=Onest:wght@200;500;700&display=swap",
    "families": {"sans": "\"Onest\", \"Diatype Variable\", sans-serif"},
    "colors": [
        tok("ink", "#151515", "Page ground under the dark textile imagery."),
        tok("black", "#000000", "Deepest ground."),
        tok("bone", "rgba(255, 255, 255, 0.75)", "Body text and nav. 10.5:1 on `ink`, 8.8:1 on `charcoal`."),
        tok("bronze", "#b2916e", "The wordmark and the featured-work list. 6.2:1 on `ink`."),
        tok("charcoal", "#2a2a2a", "Raised panels."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("list", "48.6px", "52.488px", 700, "Featured work list, numbered with superscripts.", ls="-0.3888px", sample="\\1Cultural Fragments \\2Saé'kin"),
            style("body", "15.552px", "18.6624px", 500, "Paragraphs and nav.", ls="-0.31104px"),
            style("micro", "6.48px", "7.776px", 200, "Superscript indices and fine print.", ls="-0.1296px"),
        ]},
    ],
    "spacing": [
        tok("space-1", "6px", "Superscript offset."),
        tok("space-2", "16px", "Page margin."),
        tok("space-3", "32px", "Between blocks."),
        tok("space-4", "96px", "Section padding."),
    ],
    "radius": [tok("radius-none", "0px", "Everything is square.")],
    "readme": """
SCNG is a studio working with cultural heritage: projects like Cultural Fragments, Majapahit, ARS SONI and #VALUE! Unknown Quantities. The site sits on a near-black, grainy textile pattern; the featured work runs as one long bronze paragraph where each title is preceded by a backslash and a superscript number. Built from the public site scng.work; the typeface is an open substitute.

## Voice
- Titles as a continuous run-on list: `\\1Cultural Fragments \\2Cultural Fragment Cards \\3Saé'kin … and more…`

## Colour
- `bronze` for the wordmark and work list, `bone` for everything else, on `ink`.

## Typography
- The site uses **Diatype Variable** (weights 200–700). Substitute: **Onest**.
- The list is 700, tracked tight; indices are tiny superscripts.

## Components
`WorkList`, `Header` and `Note`.
""",
    "components": {
        "WorkList": {
            "group": "Content", "height": 200,
            "readme": """
Featured work as one run-on paragraph with backslash + superscript indices.

- Provide project titles. Each is `\\` + `<sup>n</sup>` + title, in `list` (scaled), `bronze`. End with "and more…".
""",
            "css": """
body{background:var(--ink);padding:16px}
p{font:700 28px/32px var(--font-sans);letter-spacing:-.3px;color:var(--bronze);margin:0}
sup{font-size:11px;font-weight:200}
.l{font:500 12px/16px var(--font-sans);color:var(--bone);margin:0 0 8px}
""",
            "html": "<p class=\"l\">Featured Work</p><p>\\<sup>1</sup>Cultural Fragments \\<sup>2</sup>Saé'kin \\<sup>3</sup>Majapahit \\<sup>4</sup>ARS SONI \\<sup>5</sup>#VALUE! Unknown Quantities \\ and more…</p>",
        },
        "Header": {
            "group": "Navigation", "height": 80,
            "readme": """
Wordmark left in `bronze`; small nav right in `bronze`.

- Wordmark 22px 500; nav `body` at 10px.
""",
            "css": """
body{background:var(--ink);padding:16px;display:flex;justify-content:space-between;align-items:flex-start;color:var(--bronze)}
.w{font:500 22px/1 var(--font-sans)}
nav{display:flex;gap:8px;font:500 10px/1 var(--font-sans)}
""",
            "html": "<span class=\"w\">SCNG</span><nav><span>More Works</span><span>CSM</span><span>About</span><span>Contact</span></nav>",
        },
        "Note": {
            "group": "Content", "height": 120,
            "readme": """
A short paragraph on `charcoal`.

- `body` in `bone`, max 48ch, padding `space-2`.
""",
            "css": """
body{background:var(--ink);padding:16px}
p{background:var(--charcoal);color:var(--bone);font:500 15.5px/18.7px var(--font-sans);letter-spacing:-.3px;padding:16px;margin:0;max-width:48ch}
""",
            "html": "<p>A studio working at the meeting point of heritage, craft and technology.</p>",
        },
    },
    "cover": {
        "ground": "ink", "ink": "bronze", "muted": "bone", "body_font": "sans",
        "name_font": "sans", "name_size": 120, "name_weight": 500, "name_lines": ["SCNG"],
        "tagline": "Cultural Fragments, and more…",
        "css": """
  .ch{fill:var(--charcoal)} .bk{fill:var(--black)} .br{fill:var(--bronze)}
  .arc{fill:none;stroke:var(--charcoal);stroke-width:10}
""",
        "derivation": """
blocks      charcoal 240x288 textile field · black 120x120 · bronze 8 short bars (the superscript indices)
arrangement a dark textile field with a darker inset, quiet, like the grainy hero
pattern     a literal motif: the woven pattern as four concentric charcoal arcs
scales      bar pitch space-3 (32), radius-none
""",
        "svg": """
<rect class="ch" x="240" y="0" width="240" height="288"/>
<rect class="bk" x="320" y="96" width="120" height="120"/>
<path class="arc" d="M 40 288 A 160 160 0 0 1 200 128"/>
<path class="arc" d="M 80 288 A 120 120 0 0 1 200 168"/>
<path class="arc" d="M 120 288 A 80 80 0 0 1 200 208"/>
<rect class="br" x="264" y="32" width="24" height="4"/><rect class="br" x="296" y="32" width="40" height="4"/><rect class="br" x="344" y="32" width="16" height="4"/><rect class="br" x="368" y="32" width="56" height="4"/>
""",
    },
}

SYSTEMS = [paintriver, receipts, shay, estelle, ddd, junyeop, wndws, scng]
