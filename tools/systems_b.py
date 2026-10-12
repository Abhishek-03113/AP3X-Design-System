from ds_lib import tok, style

CAPTURED = "2026-10-11"

# ---------------------------------------------------------------- 6. Surfer's Journal Archives
surfers = {
    "slug": "surfers-journal-archives",
    "title": "Surfer's Journal Archives",
    "namespace": "SurfersJournal",
    "source": {"url": "https://archives.surfersjournal.com/", "captured": CAPTURED},
    "fonts_href": "https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500&display=swap",
    "families": {"serif": "\"EB Garamond\", Georgia, serif"},
    "colors": [
        tok("sea-glass", "#b1ded3", "Default ground (the current issue's colourway). `ink` text 14.3:1."),
        tok("ink", "#000000", "All text and rules, on every colourway."),
        tok("paper", "#ffffff", "Text on photography only."),
        tok("tangerine", "#ffa400", "Issue colourway ground. `ink` text 10.6:1."),
        tok("blush", "#fce8f1", "Issue colourway ground. `ink` text 18.0:1."),
        tok("olive", "#96916c", "Issue colourway ground. `ink` text 6.6:1."),
        tok("butter", "#fff8a3", "Issue colourway ground. `ink` text 19.2:1."),
        tok("harbour", "#aec1ce", "Issue colourway ground. `ink` text 11.3:1."),
        tok("sand", "#f2deb7", "Issue colourway ground. `ink` text 15.9:1."),
        tok("deep-water", "#152243", "Cover-photo shadow tone. Placeholder fill for unloaded covers; `paper` text on it is 15.7:1."),
    ],
    "type_groups": [
        {"name": "Serif", "family": "serif", "styles": [
            style("display", "56px", "56px", 400, "Year and issue numbers at the page corners.", sample="2026 · 35.5"),
            style("headline", "54px", "62px", 400, "Issue and article titles on detail pages."),
            style("body", "20px", "24px", 400, "Nav, captions and running text — the site is set almost entirely at this size.", sample="Issues  Collections  Search"),
            style("body-tight", "20px", "22px", 400, "Two-line captions and lists."),
            style("masthead", "14px", "16px", 500, "The centred masthead, uppercase and tracked.", ls="0.6px", sample="THE SURFER'S JOURNAL"),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Underline offset."),
        tok("space-2", "8px", "Between nav items' baseline and underline."),
        tok("space-3", "16px", "Page margin and nav gaps."),
        tok("space-4", "32px", "Gap between covers in the grid."),
        tok("space-5", "64px", "Top padding above the cover stage."),
    ],
    "radius": [tok("radius-none", "0px", "Covers, tiles and buttons. Nothing is rounded.")],
    "readme": """
The Surfer's Journal Archives is the digital library of every issue of *The Surfer's Journal*. Each page takes the colourway of the issue on show: a flat pastel ground, black serif type at the corners, and the cover photograph as the only image. Built from the public site archives.surfersjournal.com; the typeface is an open substitute.

## Voice

- Librarian-quiet. Nav words are single nouns: Issues, Collections, Search, Library.
- Numbers carry the content: the year (2026), the issue (35.5), the count ("All (188)").

## Colour

- Pick ONE colourway per page from `sea-glass`, `tangerine`, `blush`, `olive`, `butter`, `harbour`, `sand`, and fill the whole viewport with it. Never place two colourways side by side except in the issue index.
- Everything else is `ink`. `paper` appears only on photography.
- `deep-water` is a placeholder for a cover still loading.

## Typography

- One serif family. The site uses **Practice**; this system substitutes **EB Garamond**.
- Corners carry `display` numerals; nav is `body` (20px); the masthead is the only uppercase line.
- Underline the current nav item (1px, offset `space-1`).

## Layout

- A fixed three-part top bar (nav left, masthead centre, Library right) and a three-part bottom bar (year left, "All (188)" centre, issue number right).
- The cover is centred on the stage at roughly 30% of the viewport width with a flat edge; no shadow, no radius.

## Imagery

- Only the issue's own cover art. No logo file ships; set the masthead in type.

## Components

`TopBar`, `IssueStage` and `ColourwayIndex` are static previews built on the tokens above.
""",
    "components": {
        "TopBar": {
            "group": "Navigation", "height": 80,
            "readme": """
The three-part top bar: nav left, masthead centre, Library right.

- Provide nav items, the current one, and the masthead text.
- Nav `body` in `ink`, current item underlined. Masthead `masthead`, uppercase. Ground is the page's colourway.
- Padding `space-3`. Collapse nav into "Menu" below 640px.
""",
            "css": """
body{background:var(--sea-glass);color:var(--ink);padding:16px;font:400 20px/24px var(--font-serif)}
.bar{display:grid;grid-template-columns:1fr auto 1fr;align-items:baseline;gap:16px}
nav{display:flex;gap:16px}
a{color:var(--ink);text-decoration:none}
a.on{text-decoration:underline;text-underline-offset:4px;text-decoration-thickness:1px}
.m{font:500 14px/16px var(--font-serif);letter-spacing:.6px;text-transform:uppercase}
.r{text-align:right}
""",
            "html": """
<div class="bar"><nav><a class="on" href="#">Issues</a><a href="#">Collections</a><a href="#">Search</a></nav><span class="m">The Surfer's Journal</span><a class="r" href="#">Library</a></div>
""",
        },
        "IssueStage": {
            "group": "Content", "height": 300,
            "readme": """
The issue view: a centred cover on the colourway ground with year, count and issue number at the bottom corners.

- Provide the cover image (3:4), year, issue number and total count.
- Cover centred, no radius, no shadow; `deep-water` until loaded. Corners in `display`; centre count in `body`, underlined.
""",
            "css": """
body{background:var(--tangerine);color:var(--ink);margin:0;padding:16px;font-family:var(--font-serif)}
.stage{display:grid;place-items:center;height:200px}
.cover{width:132px;height:176px;background:var(--deep-water);color:var(--paper);display:flex;align-items:flex-end;justify-content:flex-end;padding:8px;box-sizing:border-box;font:400 20px/1 var(--font-serif)}
.foot{display:grid;grid-template-columns:1fr auto 1fr;align-items:end}
.d{font:400 56px/56px var(--font-serif)}
.c{font:400 20px/24px var(--font-serif);text-decoration:underline;text-underline-offset:4px}
.r{text-align:right}
""",
            "html": """
<div class="stage"><div class="cover" role="img" aria-label="Issue 35.5 cover">35.5</div></div>
<div class="foot"><span class="d">2026</span><span class="c">All (188)</span><span class="d r">35.5</span></div>
""",
        },
        "ColourwayIndex": {
            "group": "Content", "height": 160,
            "readme": """
The issue index: a strip of colourway tiles, one per issue, labelled with the issue number.

- Provide the issues with their colourway token.
- Tiles are equal-width bands with no gap and no radius; label `body-tight` in `ink`, bottom-left inside the band.
- This is the only place two colourways may touch.
""",
            "css": """
body{margin:0;background:var(--paper)}
.s{display:flex;height:160px}
.s div{flex:1;color:var(--ink);font:400 20px/22px var(--font-serif);padding:8px;display:flex;align-items:flex-end}
""",
            "html": """
<div class="s"><div style="background:var(--sea-glass)">35.5</div><div style="background:var(--tangerine)">35.4</div><div style="background:var(--blush)">35.3</div><div style="background:var(--olive)">35.2</div><div style="background:var(--butter)">35.1</div><div style="background:var(--harbour)">34.6</div><div style="background:var(--sand)">34.5</div></div>
""",
        },
    },
    "cover": {
        "ground": "sea-glass", "ink": "ink", "muted": "ink", "body_font": "serif",
        "name_font": "serif", "name_size": 96, "name_lines": ["Surfer's", "Journal"],
        "tagline": "Every issue, in its own colourway.",
        "css": """
  .t{fill:var(--tangerine)} .bl{fill:var(--blush)} .bu{fill:var(--butter)} .h{fill:var(--harbour)} .dw{fill:var(--deep-water)}
  .arc{fill:none;stroke:var(--ink);stroke-width:1.5}
""",
        "derivation": """
blocks      tangerine, blush, butter, harbour as full-height bands of unequal width (the colourway index) · deep-water cover 112x150
arrangement a strip of unequal bands bleeding top and bottom, with one cover set on them
pattern     a literal wave: three concentric quarter arcs in ink, from the surf subject
scales      bands in space-4 (32) multiples, radius-none
""",
        "svg": """
<rect class="t" x="96" y="0" width="96" height="288"/>
<rect class="bl" x="192" y="0" width="64" height="288"/>
<rect class="bu" x="256" y="0" width="128" height="288"/>
<rect class="h" x="384" y="0" width="96" height="288"/>
<rect class="dw" x="272" y="64" width="112" height="150"/>
<path class="arc" d="M 0 288 A 96 96 0 0 1 96 192"/>
<path class="arc" d="M 0 288 A 64 64 0 0 1 64 224"/>
<path class="arc" d="M 0 288 A 128 128 0 0 1 128 160"/>
""",
    },
}

# ---------------------------------------------------------------- 7. Celine Ka Wing Lau
celine = {
    "slug": "celine-ka-wing-lau",
    "title": "Celine Ka Wing Lau",
    "namespace": "CelineLau",
    "source": {"url": "https://celinelkw.com/", "captured": CAPTURED},
    "fonts_href": "https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@400;700&family=Archivo:wdth,wght@125,400;125,700&display=swap",
    "families": {
        "sans": "\"Familjen Grotesk\", Helvetica, sans-serif",
        "wide": "\"Archivo\", \"Arial Black\", sans-serif",
    },
    "colors": [
        tok("highlighter", "#ffee00", "The page. Every screen is this yellow."),
        tok("ink", "rgba(0, 0, 0, 0.85)", "Body text and line work. 13.1:1 on `highlighter`."),
        tok("line", "#000000", "Outlines of drawn shapes and the wide captions."),
        tok("lilac", "#d39fed", "Illustration fill (the dog, the hand-lettered name). `line` text on it 10.0:1."),
        tok("sky", "#a1e3fc", "Illustration fill (the jumper, glasses lenses). `line` text 14.9:1."),
        tok("tomato", "#f25048", "Illustration fill (the SHOP lettering, the frame of the glasses). `line` text 6.0:1."),
        tok("tangerine", "#fd6e00", "Illustration fill (the ABOUT key fob). `line` text 7.4:1."),
        tok("frog", "#00de5c", "Illustration fill (the frog). `line` text 11.7:1."),
        tok("bubblegum", "#fa82c8", "Illustration fill (the down arrow, small pops). `line` text 9.1:1."),
        tok("paper", "#ffffff", "Inside of drawn objects (the shopping bag) and the round menu button."),
    ],
    "type_groups": [
        {"name": "Text", "family": "sans", "styles": [
            style("body", "16.848px", "21.9024px", 400, "Body copy on project pages.", sample="Illustrator based between Hong Kong and London."),
        ]},
        {"name": "Wide", "family": "wide", "styles": [
            style("caption", "14.256px", "28.512px", 400, "Wide captions and credits under images.", sample="WORK + FEATURES + EXHIBITIONS"),
            style("caption-bold", "14.256px", "28.512px", 700, "Caption titles."),
        ]},
    ],
    "spacing": [
        tok("space-1", "6px", "Outline stroke and small nudges."),
        tok("space-2", "12px", "Caption gaps."),
        tok("space-3", "24px", "Page margin."),
        tok("space-4", "48px", "Between drawn objects."),
    ],
    "radius": [
        tok("radius-sticker", "18px", "Hand-cut sticker labels (an addition: the site's shapes are drawn, not CSS)."),
        tok("radius-round", "999px", "The round menu button and discs."),
    ],
    "readme": """
Celine Ka Wing Lau is an illustrator working between Hong Kong and London. Her portfolio is a single highlighter-yellow page where every navigation item is a hand-drawn object: a dog wearing "WORK + FEATURES + EXHIBITIONS", a SHOP bag, an ABOUT key fob, glasses that say HONG KONG / LONDON. Built from the public site celinelkw.com; fonts are open substitutes.

## Voice

- First person, warm, a bit silly. Labels are short and hand-lettered: WORK, SHOP, ABOUT, HOME PAGE.
- The `+` joins categories: "WORK + FEATURES + EXHIBITIONS".

## Colour

- `highlighter` is the page, always. Drawn objects use flat fills from `lilac`, `sky`, `tomato`, `tangerine`, `frog`, `bubblegum` and `paper`, each outlined in `line`.
- Put text inside a drawn object in `line`; all of those fills pass 4.5:1 with it.
- Never use the illustration colours as text on the yellow.

## Typography

- The site uses **Diatype** for text and **Routed Gothic Wide** for captions. Substitutes: **Familjen Grotesk** and **Archivo** (width 125).
- The headline type on the site is hand-lettered inside the drawings. Do not imitate it with a font; commission or reuse drawings.

## Layout

- A loose collage of objects scattered across the yellow, each one a link. No grid, no header bar; just a round menu button top-right.

## Imagery

- Flat-colour drawings with a black outline of uneven weight. No gradients, no shadows, no photos on the home page.
- No logo or illustration files ship here. `StickerLink` stands in for a drawn object with a CSS sticker; flag it as a placeholder.

## Components

`StickerLink`, `MenuButton` and `Caption` are static previews built on the tokens above.
""",
    "components": {
        "StickerLink": {
            "group": "Navigation", "height": 180,
            "readme": """
A navigation item drawn as a sticker: a flat fill, a heavy black outline and a slight tilt. Stand-in for a hand-drawn object.

- Provide the label and one illustration fill token.
- 3px `line` border, `radius-sticker`, rotate between −6° and 6°. Label `caption-bold` uppercase in `line`.
- Swap for the real drawing whenever one exists.
""",
            "css": """
body{background:var(--highlighter);padding:32px;display:flex;gap:32px;flex-wrap:wrap;align-items:center}
.s{border:3px solid var(--line);border-radius:var(--radius-sticker);padding:12px 20px;font:700 14.256px/1.4 var(--font-wide);text-transform:uppercase;color:var(--line);text-decoration:none;display:inline-block}
""",
            "html": """
<a class="s" href="#" style="background:var(--lilac);transform:rotate(-4deg)">Work + features</a>
<a class="s" href="#" style="background:var(--paper);color:var(--line);transform:rotate(5deg)">Shop</a>
<a class="s" href="#" style="background:var(--tangerine);transform:rotate(-2deg)">About</a>
<a class="s" href="#" style="background:var(--sky);transform:rotate(3deg)">Hong Kong / London</a>
""",
        },
        "MenuButton": {
            "group": "Navigation", "height": 90,
            "readme": """
The small round menu button fixed top-right.

- 28px circle, `paper` fill, 1.5px `line` border, three short `line` bars.
- Needs an accessible label ("Menu").
""",
            "css": """
body{background:var(--highlighter);padding:24px}
.m{width:28px;height:28px;border-radius:var(--radius-round);background:var(--paper);border:1.5px solid var(--line);display:grid;place-items:center;padding:0}
.m i{display:block;width:12px;height:1.5px;background:var(--line);box-shadow:0 -4px 0 var(--line),0 4px 0 var(--line)}
""",
            "html": """
<button class="m" aria-label="Menu"><i></i></button>
""",
        },
        "Caption": {
            "group": "Content", "height": 120,
            "readme": """
Wide uppercase caption under a piece of work.

- Provide a title and a credit line.
- Title `caption-bold`, credit `caption`, both `line`, uppercase. Max 48ch.
""",
            "css": """
body{background:var(--highlighter);padding:24px;color:var(--line);font:400 14.256px/28.512px var(--font-wide);text-transform:uppercase}
b{font-weight:700}
""",
            "html": """
<div><b>Frog lunch</b><br>Editorial illustration for a weekend supplement, 2025</div>
""",
        },
    },
    "cover": {
        "ground": "highlighter", "ink": "line", "muted": "line", "body_font": "sans",
        "name_font": "wide", "name_size": 64, "name_weight": 700, "name_lines": ["Celine Ka", "Wing Lau"],
        "tagline": "Illustrator, Hong Kong and London.",
        "css": """
  .li{fill:var(--lilac);stroke:var(--line);stroke-width:3} .sk{fill:var(--sky);stroke:var(--line);stroke-width:3}
  .to{fill:var(--tomato);stroke:var(--line);stroke-width:3} .fr{fill:var(--frog);stroke:var(--line);stroke-width:3}
  .st{rx:var(--radius-sticker)}
""",
        "derivation": """
blocks      lilac 160x200 sticker · sky 120x120 disc · tomato 128x72 sticker · frog 56x56 disc — all outlined in line, as every drawn object is
arrangement a loose collage, slightly tilted, like objects scattered on the yellow
pattern     discs and stickers from "soft, friendly": radius-sticker (18) corners and radius-round discs, outline space-1-ish 3px
scales      gaps space-4 (48), radius-sticker 18, radius-round
""",
        "svg": """
<rect class="li st" x="48" y="40" width="160" height="200" rx="18" transform="rotate(-6 128 140)"/>
<circle class="sk" cx="300" cy="96" r="60"/>
<rect class="to st" x="248" y="184" width="128" height="72" rx="18" transform="rotate(5 312 220)"/>
<circle class="fr" cx="420" cy="232" r="28"/>
""",
    },
}

# ---------------------------------------------------------------- 8. ANDMADE
andmade = {
    "slug": "andmade",
    "title": "ANDMADE",
    "namespace": "Andmade",
    "source": {"url": "https://andmade.jp/", "captured": CAPTURED},
    "fonts_href": "https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500&family=Courier+Prime&display=swap",
    "families": {
        "sans": "\"Hanken Grotesk\", \"Helvetica Neue\", Helvetica, Arial, \"Noto Sans JP\", sans-serif",
        "mono": "\"Courier Prime\", \"Courier New\", monospace",
    },
    "colors": [
        tok("paper", "#f6f6f4", "Page ground."),
        tok("ink", "#000000", "Titles, statement text and links. 19.4:1 on `paper`."),
        tok("ink-50", "rgba(0, 0, 0, 0.5)", "Project metadata (type, role) and dates — the site's secondary text. Composites to 3.9:1 on `paper`: keep it to 12px metadata next to an `ink` title, never for content read on its own. Source value kept exactly."),
        tok("link-blue", "#0022ff", "The \"Colors of Sound\" link and active states. 7.3:1 on `paper`."),
        tok("white", "#ffffff", "Text on `ink` (the dark sound-player bar)."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("statement", "33px", "34.65px", 500, "The mission statement and page openers.", ls="-0.66px", sample="We uncover what truly matters and give purpose a clear form."),
            style("headline", "28px", "29.4px", 500, "Section headers.", ls="-0.66px"),
            style("lead", "18px", "18.9px", 500, "Lead lines and the studio name in large layouts.", ls="-0.36px"),
            style("body", "14px", "21px", 500, "Navigation and short paragraphs.", ls="-0.28px", sample="Projects, About, Studies, Contact"),
            style("small", "12px", "18px", 500, "Project titles in the index (underlined)."),
            style("meta", "12px", "15px", 400, "Project type and role lines, in `ink-50`."),
        ]},
        {"name": "Mono", "family": "mono", "styles": [
            style("date", "12px", "15px", 400, "Dates under projects (`May.2026`).", ls="-0.6px", sample="Aug.2025"),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Title to meta line."),
        tok("space-2", "12px", "Between meta lines and the date."),
        tok("space-3", "24px", "Page margin."),
        tok("space-4", "48px", "Between index rows."),
        tok("space-5", "96px", "Between statement and index."),
    ],
    "radius": [tok("radius-pill", "30px", "The sound-player toggle and pill links; nothing else is rounded.")],
    "readme": """
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
""",
    "components": {
        "ProjectEntry": {
            "group": "Content", "height": 200,
            "readme": """
One project in the index: underlined title, meta lines, typewriter date.

- Provide `title`, `type` (e.g. Brand site), `roles`, `date`.
- Title `small`, `ink`, underlined. Meta `meta` in `ink-50`. Date `date` in `ink-50`.
- Lay out three per row on desktop, gap `space-4`.
""",
            "css": """
body{background:var(--paper);padding:24px;font-family:var(--font-sans)}
.g{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:48px}
a{font:500 12px/18px var(--font-sans);color:var(--ink);text-decoration:underline;text-underline-offset:2px;display:block}
.m{font:400 12px/15px var(--font-sans);color:var(--ink-50)}
.d{font:400 12px/15px var(--font-mono);letter-spacing:-.6px;color:var(--ink-50)}
""",
            "html": """
<div class="g">
<div><a href="#">Dots by GEEK PICTURES</a><div class="m">Brand site<br>Art Direction, Design</div><div class="d">May.2026</div></div>
<div><a href="#">SATOYAMA TERRACE</a><div class="m">Identity, Brand site, Signs<br>Art Direction, Design</div><div class="d">Aug.2025</div></div>
<div><a href="#">Belle idée pÂtisserie!</a><div class="m">Brand site<br>Art Direction, Design</div><div class="d">Aug.2025</div></div>
</div>
""",
        },
        "Statement": {
            "group": "Content", "height": 170,
            "readme": """
The studio statement: two sentences in `statement`, then a small arrow link.

- Provide the statement text and one link label.
- Statement max 60ch, `ink`. Link `small`, underlined, followed by `→`.
""",
            "css": """
body{background:var(--paper);padding:24px;color:var(--ink)}
p{font:500 33px/34.65px var(--font-sans);letter-spacing:-.66px;margin:0 0 16px;max-width:30ch}
a{font:500 12px/18px var(--font-sans);color:var(--ink);text-underline-offset:2px}
""",
            "html": """
<p>We uncover what truly matters and give purpose a clear form.</p>
<a href="#">Who we are</a> →
""",
        },
        "Header": {
            "group": "Navigation", "height": 80,
            "readme": """
The top line: studio name left, comma-separated nav centre, a sound note right.

- Provide the studio name, nav items and the right-hand note.
- All `meta`-sized; name and nav in `ink` weight 500, the note in `ink-50`. One line, `space-3` padding.
""",
            "css": """
body{background:var(--paper);padding:24px;font:500 12px/15px var(--font-sans);color:var(--ink)}
.h{display:grid;grid-template-columns:1fr auto 1fr;gap:16px}
.r{text-align:right;color:var(--ink-50);font-weight:400}
.c{display:flex;gap:4px}
""",
            "html": """
<div class="h"><span>ANDMADE Inc.</span><span class="c">Projects , About , Studies , Contact</span><span class="r">No music playing.</span></div>
""",
        },
    },
    "cover": {
        "ground": "paper", "ink": "ink", "muted": "ink", "body_font": "sans",
        "name_font": "sans", "name_size": 80, "name_weight": 500, "name_ls": "-2px", "name_lines": ["ANDMADE"],
        "tagline": "We uncover what truly matters and give purpose a clear form.",
        "css": """
  .ink{fill:var(--ink)} .bl{fill:var(--link-blue)}
  .rule{stroke:var(--ink);stroke-width:1}
""",
        "derivation": """
blocks      ink 120x200 slab · link-blue 120x24 pill (the one accent link) — a two-colour brand, so the paper does the rest
arrangement index columns: three columns at space-4 gaps, the slab in the middle one
pattern     editorial: four hairlines (1px ink) marking the index rows, from "small black type, underlined titles"
scales      columns 120 wide, gaps space-4 (48 → 40 here to fit), pill rx 12 (radius-pill drawn as half the 24px height)
""",
        "svg": """
<line class="rule" x1="16" y1="48.5" x2="464" y2="48.5"/>
<line class="rule" x1="16" y1="120.5" x2="136" y2="120.5"/>
<line class="rule" x1="344" y1="120.5" x2="464" y2="120.5"/>
<line class="rule" x1="16" y1="192.5" x2="136" y2="192.5"/>
<rect class="ink" x="176" y="64" width="120" height="200"/>
<rect class="bl pill" x="344" y="152" width="120" height="24" rx="12"/>
""",
    },
}

# ---------------------------------------------------------------- 9. United Carriers
united = {
    "slug": "united-carriers",
    "title": "United Carriers",
    "namespace": "UnitedCarriers",
    "source": {"url": "https://unitedcarriers.com/", "captured": CAPTURED},
    "fonts_href": "https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700&family=Martian+Mono:wght@400&display=swap",
    "themes": [{"id": "light", "name": "Light"}, {"id": "dark", "name": "Dark"}],
    "families": {
        "display": "\"Unbounded\", \"Arial Black\", sans-serif",
        "sans": "\"Helvetica Neue\", Helvetica, Arial, sans-serif",
        "mono": "\"Martian Mono\", \"Courier New\", monospace",
    },
    "colors": [
        tok("bg", {"light": "#ffffff", "dark": "#000000"}, "Section ground. Light sections for services and copy; dark for the hero and the planet."),
        tok("bg-raised", {"light": "#f3f3f3", "dark": "#111111"}, "Cards and the footer band."),
        tok("fg", {"light": "#111111", "dark": "#ffffff"}, "Primary text. 18.9:1 light, 21:1 dark."),
        tok("fg-muted", {"light": "rgba(17, 17, 17, 0.72)", "dark": "rgba(255, 255, 255, 0.7)"}, "Secondary paragraphs and nav. 7.6:1 light and 9.9:1 dark on `bg`."),
        tok("fg-subtle", {"light": "rgba(17, 17, 17, 0.6)", "dark": "rgba(255, 255, 255, 0.6)"}, "Mono meta labels. 5.0:1 light, 7.4:1 dark."),
        tok("hairline", {"light": "rgba(17, 17, 17, 0.16)", "dark": "rgba(255, 255, 255, 0.24)"}, "Dividers and outline-button borders. Decorative; pair outlines with a text label."),
        tok("horizon", "#2d4aa7", "The blue atmosphere glow on the planet hero and on light-section gradients' edge. White text on it 7.9:1."),
        tok("sky", "#6d9dd9", "Lighter atmosphere band. Decorative fill only."),
        tok("indigo", "#1c225f", "Deep night-sky fill behind the planet."),
        tok("lavender-wash", "rgba(166, 134, 224, 0.3)", "Soft highlight behind photography and quotes."),
    ],
    "type_groups": [
        {"name": "Display", "family": "display", "styles": [
            style("display-xl", "133.333px", "140px", 700, "One-line hero statements, uppercase.", sample="EVERY LEG OF THE JOURNEY"),
            style("display-lg", "60px", "63px", 700, "Section heads, uppercase."),
            style("display-sm", "24px", "30px", 700, "Card titles, uppercase."),
            style("display-xs", "20px", "22px", 700, "Small uppercase heads."),
            style("label", "13.3333px", "16px", 500, "Button text, uppercase."),
        ]},
        {"name": "Text", "family": "sans", "styles": [
            style("lead", "26.6667px", "32px", 500, "Lead paragraphs.", sample="With every service under one roof and one accountable team."),
            style("lead-sm", "23.3333px", "28px", 500, "Secondary leads."),
            style("body", "13.3333px", "16px", 400, "Paragraphs."),
            style("body-sm", "11.6667px", "15.1667px", 400, "Footnotes and card copy."),
        ]},
        {"name": "Mono", "family": "mono", "styles": [
            style("mono", "10px", "14px", 400, "Uppercase nav, eyebrows, ticker.", sample="NEWS · UC COURTSIDE IS HERE"),
            style("mono-sm", "8.33333px", "11.6667px", 400, "Tiny meta under labels."),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Inside mono labels."),
        tok("space-2", "8px", "Button vertical padding."),
        tok("space-3", "16px", "Button horizontal padding; nav gaps."),
        tok("space-4", "24px", "Page margin."),
        tok("space-5", "48px", "Between blocks."),
        tok("space-6", "120px", "Section padding."),
    ],
    "radius": [
        tok("radius-pill", "1440px", "Every button (TALK WITH US, OUR SERVICES)."),
        tok("radius-circle", "50%", "Round icon buttons and the planet."),
    ],
    "readme": """
United Carriers does freight forwarding, land transport and customs brokerage across APAC "under one accountable team". The site opens on a black hero with a glowing planet horizon and enormous wide uppercase type, then moves into clean white sections set in Helvetica, with tiny monospace labels everywhere. Built from the public site unitedcarriers.com; display and mono fonts are open substitutes, Helvetica Neue is the site's own stack.

## Voice

- Plainspoken operator: "One operator. Every leg of the journey." "No finger-pointing between vendors."
- Headlines are uppercase and short; paragraphs are full sentences addressed to "your supply chain".
- Mono labels are uppercase and dotted: `NEWS · UC COURTSIDE IS HERE`, `CARBON CALCULATOR · LIVE TRACKING PORTAL`.

## Colour

- Two themes. `dark` is the hero and brand moments (pure black, the planet); `light` carries the services and copy. Use the semantic `bg` / `fg` tokens so components work in both.
- Muted levels are alpha on `fg` (`fg-muted` 72%/70%, `fg-subtle` 60%), exactly as the site does.
- `horizon`, `sky` and `indigo` belong to the planet artwork; don't use them for UI states.

## Typography

- Display is **BT Steinhart** on the site (wide, bold); this system substitutes **Unbounded**. Mono is **BT Steinhart Mono**, substituted by **Martian Mono**. Body is **Helvetica Neue** as on the site.
- All display text uppercase. Body sentence case. Mono uppercase, 10px.

## Shape

- Buttons are pills (`radius-pill`), white-filled on dark or outlined with `hairline`.
- Everything else is square.

## Components

`Button`, `Ticker` and `HeroStatement` are static previews built on the tokens above. No logo file ships; set UNITEDCARRIERS in `display-xs`.
""",
    "components": {
        "Button": {
            "group": "Actions", "height": 100,
            "readme": """
Pill buttons with uppercase mono labels.

- Primary: `fg` fill, `bg` text (white pill on the dark hero). Secondary: transparent with a 1px `hairline` border and `fg` text.
- Label `mono` uppercase. Padding `space-2` × `space-3`. `radius-pill`.
- Focus: 2px `fg` outline offset 2px.
""",
            "css": """
body{background:var(--bg);padding:24px}
.row{display:flex;gap:8px}
.b{font:400 10px/14px var(--font-mono);text-transform:uppercase;padding:8px 16px;border-radius:var(--radius-pill);cursor:pointer;border:1px solid var(--hairline)}
.p{background:var(--fg);color:var(--bg);border-color:var(--fg)}
.s{background:transparent;color:var(--fg)}
.b:focus-visible{outline:2px solid var(--fg);outline-offset:2px}
""",
            "html": """
<div class="row"><button class="b p">Talk with us</button><button class="b s">Our services</button></div>
""",
        },
        "Ticker": {
            "group": "Navigation", "height": 70,
            "readme": """
The thin mono strip across the very top of the page: news left, utility links right.

- Provide one news item and 2–3 utility links.
- `mono-sm`, uppercase, `fg-subtle`; separate items with ` · `. Bottom border 1px `hairline`.
""",
            "css": """
body{background:var(--bg);margin:0}
.t{display:flex;justify-content:space-between;gap:16px;padding:8px 24px;border-bottom:1px solid var(--hairline);font:400 8.33333px/11.6667px var(--font-mono);text-transform:uppercase;color:var(--fg-subtle);flex-wrap:wrap}
""",
            "html": """
<div class="t"><span>News · UC Courtside is here</span><span>Carbon calculator · Live tracking portal · Careers</span></div>
""",
        },
        "HeroStatement": {
            "group": "Content", "height": 260,
            "readme": """
The hero block: a mono eyebrow, a stacked uppercase statement and a short paragraph.

- Provide eyebrow, statement (2–4 short lines) and a sentence.
- Eyebrow `mono` in `fg`; statement `display-lg` (or `display-xl` at full width) uppercase in `fg`; paragraph `body-sm` in `fg-muted`, max 36ch.
- Designed for the `dark` theme over the planet; works in light.
""",
            "css": """
body{background:var(--bg);color:var(--fg);padding:24px}
.e{font:400 10px/14px var(--font-mono);text-transform:uppercase;margin:0 0 8px}
h1{font:700 40px/42px var(--font-display);text-transform:uppercase;margin:0 0 16px}
p{font:400 11.6667px/15.1667px var(--font-sans);color:var(--fg-muted);max-width:36ch;margin:0}
""",
            "html": """
<p class="e">One operator</p>
<h1>Every leg<br>of the<br>journey</h1>
<p>Freight forwarding, land transport, and customs brokerage, unified across APAC under one accountable team.</p>
""",
        },
    },
    "cover": {
        "ground": "bg", "ink": "fg", "muted": "fg-muted", "body_font": "sans",
        "name_font": "display", "name_size": 64, "name_weight": 700, "name_lines": ["United", "Carriers"], "leading": .95,
        "tagline": "One operator. Every leg of the journey.",
        "css": """
  .ind{fill:var(--indigo)} .hz{fill:var(--horizon)} .sk{fill:var(--sky)} .fg{fill:var(--fg)}
  .orbit{fill:none;stroke:var(--hairline);stroke-width:1}
""",
        "derivation": """
blocks      indigo night 240x288 · the planet as a horizon disc bleeding off the right edge: horizon ring + sky rim · fg pill 96x32 (the white button)
arrangement one tall field with a disc rising from the lower right, as the hero composes it
pattern     a literal motif — orbit arcs: three hairline circles around the planet, from the space-and-journey hero
scales      pill rx 16 (radius-pill drawn as half the 32px height), gaps space-4 (24), space-5 (48)
""",
        "svg": """
<rect class="ind" x="240" y="0" width="240" height="288"/>
<circle class="sk" cx="456" cy="296" r="182"/>
<circle class="hz" cx="456" cy="296" r="176"/>
<circle class="orbit" cx="456" cy="296" r="208"/>
<circle class="orbit" cx="456" cy="296" r="240"/>
<circle class="orbit" cx="456" cy="296" r="280"/>
<rect class="fg pill" x="48" y="48" width="96" height="32" rx="16"/>
""",
    },
}

# ---------------------------------------------------------------- 10. Seventeen
seventeen = {
    "slug": "seventeen",
    "title": "Seventeen",
    "namespace": "Seventeen",
    "source": {"url": "https://www.seventeenagency.com/", "captured": CAPTURED},
    "fonts_href": "https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400&display=swap",
    "families": {"condensed": "\"Barlow Condensed\", \"Arial Narrow\", Arial, sans-serif"},
    "colors": [
        tok("white", "#ffffff", "Page ground."),
        tok("black", "#000000", "Primary text and the mark. 21:1 on `white`."),
        tok("stone", "#afaea7", "Service list text and the small nav chips' ground. 2.2:1 on `white` — the site uses it for secondary text anyway; kept exact. Use only where the same words also appear in `black` (e.g. on hover) or for 18px+."),
        tok("brick", "#c13437", "Spectrum band 1 (Campaign). `white` text 5.5:1."),
        tok("harbour", "#275d82", "Spectrum band 2 (Branding). `white` text 7.1:1."),
        tok("field", "#049435", "Spectrum band 3 (Strategy). `black` text 5.3:1."),
        tok("lime", "#a6f664", "Spectrum band 4 (Design). `black` text 15.2:1."),
        tok("ochre", "#936900", "Spectrum band 5 (Motion). `white` text 4.9:1."),
        tok("lagoon", "#00a4a8", "Spectrum band 6 (Live Action). `black` text 6.9:1."),
        tok("candy", "#f77fb0", "Spectrum band 7 (Experience). `black` text 8.6:1."),
        tok("cobalt", "#0168c9", "Spectrum band 8. `white` text 5.5:1."),
        tok("umber", "#614f43", "Spectrum band 9. `white` text 7.8:1."),
        tok("lilac", "#d1b9f3", "Spectrum band 10. `black` text 11.9:1."),
        tok("aqua", "#75efe2", "Spectrum band 11. `black` text 16.0:1."),
    ],
    "type_groups": [
        {"name": "Condensed", "family": "condensed", "styles": [
            style("body", "14px", "16.8px", 400, "Everything: nav, service list, captions. The site uses a single size.", sample="Campaign  Branding  Strategy  Design  Motion  Live Action  Experience"),
            style("lead", "18px", "21.6px", 400, "The one larger line (\"A Creative Agency\")."),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Nav chip padding."),
        tok("space-2", "16px", "Page margin."),
        tok("space-3", "44px", "Height of a spectrum band."),
        tok("space-4", "172px", "Width of the spectrum column / widest stair band."),
    ],
    "radius": [tok("radius-none", "0px", "Everything is square.")],
    "readme": """
Seventeen is a creative agency of "Odd Minds bringing new angles underpinned with meaning". The homepage is almost empty white space with tiny condensed type, organised around one device: a column of eleven saturated colour bands, one per service, that collapses into a stepped stack as you scroll. Built from the public site seventeenagency.com; the typeface is an open substitute.

## Voice

- Minimal. The page says "A Creative Agency." and lists services as single words: Campaign, Branding, Strategy, Design, Motion, Live Action, Experience.
- Navigation is two words: About, Contact.

## Colour

- `black` on `white` for text. The spectrum (`brick`, `harbour`, `field`, `lime`, `ochre`, `lagoon`, `candy`, `cobalt`, `umber`, `lilac`, `aqua`) is used **only** as solid bands, always in this order, never as text colour.
- When you label a band, use the text colour named in its usage note.
- `stone` is secondary text and the ground of the small nav chips. It is 2.2:1 on white; never rely on it alone.

## Typography

- One condensed face at one size. The site uses **Bagoss Condensed**; this system substitutes **Barlow Condensed**.
- `body` (14px) for everything; `lead` (18px) once per page at most.

## Layout

- Huge white space. Service list in the left margin; the spectrum column centred; nav chips top-right; a small mark top-left.
- The stepped stack: bands narrow by a fixed step as they stack, like an inverted stair.

## Components

`SpectrumColumn`, `ServiceList` and `NavChips` are static previews built on the tokens above. No logo file ships; set "Seventeen" in `lead`.
""",
    "components": {
        "SpectrumColumn": {
            "group": "Content", "height": 300,
            "readme": """
The signature column of colour bands, one per service, in fixed order.

- Provide the services; each band takes the next spectrum token in order (`brick`, `harbour`, `field`, `lime`, `ochre`, `lagoon`, `candy`, `cobalt`, `umber`, `lilac`, `aqua`).
- Bands are `space-3` tall and stack with no gap. Stair variant: each band is narrower than the one above by a fixed step, centred.
- Bands may carry a `body` label in the text colour their token names.
""",
            "css": """
body{background:var(--white);padding:16px;display:flex;gap:48px;justify-content:center}
.col div{width:44px;height:24px}
.stair{display:flex;flex-direction:column;align-items:center}
.stair div{height:44px}
""",
            "html": """
<div class="col"><div style="background:var(--brick)"></div><div style="background:var(--harbour)"></div><div style="background:var(--field)"></div><div style="background:var(--lime)"></div><div style="background:var(--ochre)"></div><div style="background:var(--lagoon)"></div><div style="background:var(--candy)"></div><div style="background:var(--cobalt)"></div><div style="background:var(--umber)"></div><div style="background:var(--lilac)"></div><div style="background:var(--aqua)"></div></div>
<div class="stair"><div style="background:var(--brick);width:172px"></div><div style="background:var(--harbour);width:136px"></div><div style="background:var(--field);width:100px"></div><div style="background:var(--lime);width:64px"></div></div>
""",
        },
        "ServiceList": {
            "group": "Navigation", "height": 160,
            "readme": """
The stacked service words in the left margin.

- Provide the services in spectrum order.
- `body` in `stone`; the hovered or active one turns `black`. No bullets, no gaps beyond the line-height.
""",
            "css": """
body{background:var(--white);padding:16px;font:400 14px/16.8px var(--font-condensed);color:var(--stone)}
a{display:block;color:var(--stone);text-decoration:none}
a.on,a:hover{color:var(--black)}
""",
            "html": """
<a href="#" class="on">Campaign</a><a href="#">Branding</a><a href="#">Strategy</a><a href="#">Design</a><a href="#">Motion</a><a href="#">Live Action</a><a href="#">Experience</a>
""",
        },
        "NavChips": {
            "group": "Navigation", "height": 70,
            "readme": """
Tiny grey chips for the top-right navigation.

- Provide 2–3 labels. `stone` ground, `black` text (9.4:1), `body` style, padding `space-1`, square.
""",
            "css": """
body{background:var(--white);padding:16px;display:flex;gap:4px;justify-content:flex-end}
a{background:var(--stone);color:var(--black);font:400 14px/16.8px var(--font-condensed);padding:2px 4px;text-decoration:none}
""",
            "html": """
<a href="#">About</a><a href="#">Contact</a>
""",
        },
    },
    "cover": {
        "ground": "white", "ink": "black", "muted": "black", "body_font": "condensed",
        "name_font": "condensed", "name_size": 96, "name_lines": ["Seventeen"],
        "tagline": "A creative agency.",
        "css": """
  .r{fill:var(--brick)} .h{fill:var(--harbour)} .f{fill:var(--field)} .l{fill:var(--lime)} .u{fill:var(--umber)}
""",
        "derivation": """
blocks      brick 240x44 · harbour 192x44 · field 144x44 · lime 96x44 · umber 48x44 — the first spectrum bands
arrangement the site's own stepped stack: bands narrowing by a 48px step, centred, flush with no gap
pattern     the stair itself, from the brand's only device ("loud, bold" → stripes at a band pitch); five bands, no extra marks
scales      band height space-3 (44), step 48, radius-none
""",
        "svg": """
<rect class="r" x="120" y="34" width="240" height="44"/>
<rect class="h" x="144" y="78" width="192" height="44"/>
<rect class="f" x="168" y="122" width="144" height="44"/>
<rect class="l" x="192" y="166" width="96" height="44"/>
<rect class="u" x="216" y="210" width="48" height="44"/>
""",
    },
}

SYSTEMS = [surfers, celine, andmade, united, seventeen]
