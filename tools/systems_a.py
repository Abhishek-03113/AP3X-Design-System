from ds_lib import tok, style

CAPTURED = "2026-10-11"

# ---------------------------------------------------------------- 1. Odyssée
odyssee = {
    "slug": "odyssee",
    "title": "Odyssée",
    "namespace": "Odyssee",
    "source": {"url": "https://www.odysseeclinic.com.au/", "captured": CAPTURED},
    "fonts_href": "https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300;6..72,400&family=Albert+Sans:wght@400;500&display=swap",
    "families": {
        "serif": "\"Newsreader\", \"Times New Roman\", Times, serif",
        "sans": "\"Albert Sans\", \"Helvetica Neue\", Arial, sans-serif",
    },
    "colors": [
        tok("cream", "#fffcf8", "Page ground for every screen. Warm off-white; never swap for pure white."),
        tok("navy", "#1e305e", "All text, the wordmark, rules and filled buttons. Reads 12.5:1 on `cream` and 10.5:1 on `stone`."),
        tok("navy-muted", "#56607e", "Secondary copy: captions, card metadata, the (1). numerals. 6.1:1 on `cream`."),
        tok("white", "#ffffff", "Text and the wordmark when they sit on `navy`, `charcoal` or full-bleed photography. 12.8:1 on `navy` and 14.6:1 on `charcoal`."),
        tok("charcoal", "#28292a", "The one dark section (footer and booking band). Pair with `white` text."),
        tok("stone", "#e8e9ea", "Studio-wall grey from the photography backdrops. Image placeholders and quiet panels; never a text colour."),
        tok("clay", "#b89480", "Skin-tone warmth sampled from the campaign photography. Decorative fills and image placeholders only; 2.7:1 on `cream`, so never text."),
        tok("hairline", "#d9dbe2", "1px dividers between treatment rows and around inputs on `cream`."),
    ],
    "type_groups": [
        {"name": "Display", "family": "serif", "styles": [
            style("display-xl", "48px", "48px", 300, "Hero statements over photography and section openers.", sample="Medical aesthetics for timeless results."),
            style("display-lg", "32px", "33.6px", 300, "Section headlines and the long intro paragraph.", sample="Clarity precedes creation."),
            style("title", "18px", "19.8px", 400, "Card and treatment titles.", sample="An experience like no other"),
        ]},
        {"name": "Text", "family": "sans", "styles": [
            style("body", "14px", "18.2px", 400, "Running copy. Keep to 60–70 characters a line.", sample="More than a treatment, Odyssée is a restoration."),
            style("body-sm", "13px", "16.9px", 400, "Captions, footnotes, form help."),
            style("label", "12px", "12px", 400, "Uppercase nav, buttons and eyebrows. Always `text-transform: uppercase`.", ls="0.36px", sample="BOOK CONSULTATION"),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Icon-to-label gaps."),
        tok("space-2", "8px", "Between a title and its body line."),
        tok("space-3", "16px", "Inner padding of buttons (vertical ×0.75) and nav gutters."),
        tok("space-4", "24px", "Page side margin on mobile; gap between cards."),
        tok("space-5", "48px", "Page side margin on desktop; space between stacked sections."),
        tok("space-6", "96px", "Top and bottom padding of full sections."),
    ],
    "radius": [tok("radius-none", "0px", "Every surface, image and button. The site uses no rounded corners.")],
    "readme": """
Odyssée is a medical-aesthetics clinic in Hunters Hill, Sydney. The brand reads like a quiet gallery: large close-crop skin photography, a light serif for everything that is said, and a small uppercase sans for everything that is done. Built from the public site odysseeclinic.com.au; fonts are open substitutes (see Typography).

## Voice

- Calm, clinical, unhurried. Short declarative sentences: "Clarity precedes creation." "No two faces are the same."
- Speak as "we" to "you"; Australian spelling (*personalised*, *prioritise*).
- Never use exclamation marks, emoji or sales language. Treatments are "tailored" and "bespoke", results are "timeless".
- Enumerate reasons with parenthesised numerals: `(1).`, `(2).`, `(3).`.

## Colour

- Set every page on `cream`; text, rules and filled buttons are `navy`. The brand is essentially two colours, so keep it that way.
- Use `navy-muted` for metadata and the `(1).` numerals, never for body copy you need people to read in full.
- `charcoal` is reserved for the closing booking band and footer; put `white` text on it.
- `stone` and `clay` come from the photography. Use them only as image placeholders or quiet fills, never as text.
- Dividers are 1px `hairline`; no shadows anywhere.

## Typography

- Say things in the serif (`display-xl`, `display-lg`, `title`) at weight 300–400; do things in the sans (`label` uppercase for nav and buttons, `body` for reading).
- The site uses psTimes (a light Times cut) and Basel Grotesk. These are licensed faces, so this system substitutes **Newsreader** (Google Fonts) for the serif and **Albert Sans** for the sans. Swap the `serif` and `sans` families if you hold the originals.
- Headlines sit tight: line-height 1.0–1.05. Never bold the serif.

## Layout

- Full-bleed photography first, then generous `space-6` sections on `cream`.
- Side margins `space-5` on desktop, `space-4` on mobile. Align copy to a left column; the intro paragraph can run wide in `display-lg`.
- Square corners everywhere (`radius-none`).

## Imagery

- Close, warm, softly lit skin and hands on a pale grey backdrop. No before/after grids, no product shots on white.
- No logo file ships with this system: set the wordmark ODYSSÉE in the serif, uppercase, tracked +0.04em.

## Components

`Button`, `FeatureList` and `Header` are static previews built on the tokens above.
""",
    "components": {
        "Button": {
            "group": "Actions", "height": 120,
            "readme": """
Uppercase text buttons in navy: filled for the one booking action on a screen, outlined for everything else.

- Label text in `label` style, uppercase, tracked 0.36px.
- Filled: `navy` ground, `white` text. Outline: 1px `navy` border, `navy` text on `cream`. On photography or `charcoal` use the outline in `white` (never on light photo areas or `clay`, where white falls to 2.7:1).
- Square corners, padding `space-2` × `space-3`. One filled button per view: "BOOK CONSULTATION".
- Focus: 2px `navy` outline offset 3px.
""",
            "css": """
body{background:var(--cream);font-family:var(--font-sans);padding:24px}
.row{display:flex;gap:16px;flex-wrap:wrap;align-items:center}
.btn{font:400 12px/12px var(--font-sans);letter-spacing:.36px;text-transform:uppercase;padding:12px 20px;border:1px solid var(--navy);border-radius:var(--radius-none);background:transparent;color:var(--navy);cursor:pointer}
.btn.fill{background:var(--navy);color:var(--white)}
.btn:focus-visible{outline:2px solid var(--navy);outline-offset:3px}
.photo{background:var(--charcoal);padding:16px;display:flex}
.btn.inv{border-color:var(--white);color:var(--white)}
""",
            "html": """
<div class="row">
  <button class="btn fill">Book consultation</button>
  <button class="btn">Treatments</button>
  <div class="photo"><button class="btn inv">Concerns</button></div>
</div>
""",
        },
        "FeatureList": {
            "group": "Content", "height": 280,
            "readme": """
The numbered reasons block ("Why Odyssée?"): parenthesised numerals over a serif title and a short sans paragraph.

- Provide 2–4 items, each `{numeral, title, body}`. Numerals are written `(1).`.
- Numeral in `label` style, `navy-muted`; title in `title`; body in `body`, max 32ch.
- Items sit in a row with `space-4` gaps and stack below 640px. Separate with a 1px `hairline` top rule.
""",
            "css": """
body{background:var(--cream);color:var(--navy);padding:24px;font-family:var(--font-sans)}
.eyebrow{font:400 12px/12px var(--font-sans);letter-spacing:.36px;text-transform:uppercase;margin:0 0 24px}
.list{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:24px}
.item{border-top:1px solid var(--hairline);padding-top:16px}
.num{font:400 12px/12px var(--font-sans);color:var(--navy-muted)}
h3{font:400 18px/19.8px var(--font-serif);margin:16px 0 8px}
p{font:400 14px/18.2px var(--font-sans);margin:0;max-width:32ch}
""",
            "html": """
<p class="eyebrow">Why Odyssée?</p>
<div class="list">
  <div class="item"><span class="num">(1).</span><h3>An experience like no other</h3><p>More than a treatment, Odyssée is a restoration. Each visit offers a moment to relax.</p></div>
  <div class="item"><span class="num">(2).</span><h3>Bespoke treatment</h3><p>No two faces are the same. Every treatment is tailored to your skin and your time.</p></div>
  <div class="item"><span class="num">(3).</span><h3>Multi-modality efficiency</h3><p>Innovation delivers synergy. We combine complementary treatments for more effect.</p></div>
</div>
""",
        },
        "Header": {
            "group": "Navigation", "height": 150,
            "readme": """
The top bar: serif wordmark, a one-line serif tagline, uppercase nav links and the booking link at the far right.

- Provide the wordmark text, tagline and 3–4 nav links.
- Sits over photography in `white`, or on `cream` in `navy`. Links use `label`; the tagline uses the serif at 13px.
- Collapse links into a "MENU" label below 768px.
""",
            "css": """
body{background:var(--charcoal);padding:0}
.bar{display:flex;align-items:center;gap:48px;padding:24px;color:var(--white);flex-wrap:wrap}
.mark{font:400 22px/1 var(--font-serif);letter-spacing:.04em;text-transform:uppercase}
.tag{font:300 13px/1.2 var(--font-serif);flex:1;min-width:160px}
nav{display:flex;gap:24px}
nav a{font:400 12px/12px var(--font-sans);letter-spacing:.36px;text-transform:uppercase;color:var(--white);text-decoration:none}
""",
            "html": """
<div class="bar">
  <span class="mark">Odyssée</span>
  <span class="tag">Medical aesthetics for timeless results.</span>
  <nav><a href="#">Treatments</a><a href="#">Concerns</a><a href="#">About</a><a href="#">Book consultation</a></nav>
</div>
""",
        },
    },
    "cover": {
        "ground": "cream", "ink": "navy", "muted": "navy-muted", "body_font": "sans",
        "name_font": "serif", "name_size": 112, "name_weight": 300, "name_lines": ["Odyssée"],
        "tagline": "Medical aesthetics for timeless results.",
        "css": """
  .navy{fill:var(--navy)} .clay{fill:var(--clay)} .char{fill:var(--charcoal)} .stone{fill:var(--stone)}
  .rule{stroke:var(--navy);stroke-width:1;fill:none}
""",
        "derivation": """
blocks      navy 144x288 full-height slab · clay 96x192 · stone 120x144 · charcoal 48x48 — about 30% of 960x288
arrangement one tall navy slab with satellites, bottoms on one line, square corners (radius-none)
pattern     editorial hairlines: "borders not shadows", serif-led, so four 1px navy rules cross the blocks
scales      gutters space-3 (16), sides in space-5 (48) multiples, radius-none
""",
        "svg": """
<rect class="stone" x="16" y="96" width="120" height="144"/>
<rect class="clay" x="152" y="48" width="96" height="192"/>
<rect class="navy" x="264" y="0" width="144" height="288"/>
<rect class="char" x="424" y="192" width="48" height="48"/>
<line class="rule" x1="0" y1="240.5" x2="480" y2="240.5"/>
<line class="rule" x1="0" y1="48.5" x2="248" y2="48.5"/>
<line class="rule" x1="136.5" y1="0" x2="136.5" y2="288"/>
<line class="rule" x1="424" y1="96.5" x2="480" y2="96.5"/>
""",
    },
}

# ---------------------------------------------------------------- 2. L'Étude
letude = {
    "slug": "letude",
    "title": "L'Étude",
    "namespace": "Letude",
    "source": {"url": "https://letude.group/", "captured": CAPTURED},
    "fonts_href": "https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&display=swap",
    "families": {"sans": "\"Manrope\", Helvetica, Arial, sans-serif"},
    "colors": [
        tok("haze", "#9597a7", "Default page ground: a cool periwinkle grey."),
        tok("cobalt", "#012094", "Primary text, headlines, the menu glyphs and icon badges. 4.4:1 on `haze`: the source's own pairing, just under the 4.5:1 floor for small text, so keep cobalt text at 24px+ (or 19px+ bold) and set small labels in `ink`."),
        tok("signal", "#ee382b", "The alternate ground (hero, case-study openers) and the one hot accent. Cobalt text on it is 3.2:1, so only use cobalt at 24px+ or bold 19px+ there; use `ink` for smaller text."),
        tok("ink", "#151515", "Small labels and captions. 6.3:1 on `haze`, 4.6:1 on `signal`."),
        tok("paper", "#ffffff", "Text on photography and on `cobalt` fills. 13.6:1 on `cobalt`."),
    ],
    "type_groups": [
        {"name": "Display", "family": "sans", "styles": [
            style("display-xxl", "100.8px", "90.72px", 600, "The studio name and one-word heroes.", ls="-2.16px", sample="L'ÉTUDE"),
            style("display-xl", "72px", "64.8px", 600, "Section headers.", ls="-2.16px"),
            style("display-lg", "56px", "50.4px", 600, "Case-study titles.", ls="-1.12px"),
            style("headline", "32px", "33.6px", 700, "The manifesto paragraphs (\"We've always believed…\").", ls="-1.12px", sample="We are an international boutique studio."),
            style("title", "24px", "25.2px", 600, "Sub-heads inside a case study.", ls="-0.32px"),
        ]},
        {"name": "Text", "family": "sans", "styles": [
            style("body", "16px", "19.2px", 500, "Paragraph copy.", ls="-0.32px"),
            style("label", "13.008px", "13.008px", 550, "Uppercase project codes, captions and the definition block.", sample="LET.27 — THE DEEP END"),
            style("label-strong", "13.008px", "15.6096px", 650, "Uppercase nav and emphasised captions."),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Gap between an icon badge and its label."),
        tok("space-2", "8px", "Caption-to-image gap."),
        tok("space-3", "16px", "Gutters between modules."),
        tok("space-4", "24px", "Page side margin."),
        tok("space-5", "48px", "Between modules in a row."),
        tok("space-6", "96px", "Between page sections."),
    ],
    "radius": [
        tok("radius-sm", "4px", "Image tiles and project cards."),
        tok("radius-pill", "900px", "Circular icon badges (INFO, @, globe) and pills."),
    ],
    "readme": """
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
""",
    "components": {
        "ProjectCard": {
            "group": "Content", "height": 280,
            "readme": """
An image tile with a vertical project code and an arrow caption.

- Provide `code` (e.g. `LET.27`), `title`, and an image (16:10).
- Image corners `radius-sm`. Code rotated 90° in `label`, `ink`; caption `↗ TITLE` in `label` uppercase, `ink` (cobalt at 13px is 4.4:1 on `haze`, under the floor).
- Never put the caption on the image.
""",
            "css": """
body{background:var(--haze);color:var(--cobalt);font-family:var(--font-sans);padding:24px}
.grid{display:flex;gap:48px;flex-wrap:wrap}
.card{display:flex;gap:8px}
.code{writing-mode:vertical-rl;transform:rotate(180deg);font:550 13.008px/13.008px var(--font-sans);color:var(--ink);text-transform:uppercase}
.img{width:220px;height:140px;border-radius:var(--radius-sm);background:var(--cobalt)}
.img.red{background:var(--signal)}
.cap{font:550 13.008px/13.008px var(--font-sans);text-transform:uppercase;margin-top:8px;color:var(--ink)}
""",
            "html": """
<div class="grid">
  <div class="card"><span class="code">LET.27</span><div><div class="img"></div><div class="cap">↗ The deep end</div></div></div>
  <div class="card"><span class="code">LET.16</span><div><div class="img red"></div><div class="cap">↗ Bugatti Tourbillon campaign</div></div></div>
</div>
""",
        },
        "IconBadge": {
            "group": "Navigation", "height": 100,
            "readme": """
Circular outline badges used as the fixed right-edge rail (INFO, contact, language).

- Provide a single glyph (i, @, a globe letter, ↗) and an accessible name; the glyph is an icon, so 3:1 is its floor and `cobalt` on `haze` passes.
- 40px circle, 2px `cobalt` border, `radius-pill`. Glyph `label-strong` at 13px+, `cobalt`. Put any word label (INFO) in `aria-label`, not inside the circle.
- Filled variant: `cobalt` ground with `paper` glyph for the current item.
""",
            "css": """
body{background:var(--haze);padding:24px}
.row{display:flex;gap:16px;align-items:center}
.b{width:40px;height:40px;border:2px solid var(--cobalt);border-radius:var(--radius-pill);display:grid;place-items:center;font:650 16px/1 var(--font-sans);color:var(--cobalt);text-decoration:none;box-sizing:border-box}
.b.on{background:var(--cobalt);color:var(--paper)}
""",
            "html": """
<div class="row"><a class="b" href="#" aria-label="Info">i</a><a class="b" href="#" aria-label="Contact">@</a><a class="b on" href="#" aria-label="Work">W</a><a class="b" href="#" aria-label="Open project">↗</a></div>
""",
        },
        "Definition": {
            "group": "Content", "height": 150,
            "readme": """
The dictionary-entry block that introduces the studio name.

- Provide `term`, `class` (noun), `pronunciation` and a one-sentence definition.
- Term, class and pronunciation separated by `•` on one line in `label-strong`; definition in `label`, max 30ch.
- Sits top-right of the hero, on `signal` (text `ink`) or `haze` (text `cobalt`).
""",
            "css": """
body{background:var(--signal);color:var(--ink);padding:24px;font-family:var(--font-sans)}
.def{max-width:30ch}
.h{font:650 13.008px/15.6px var(--font-sans);margin:0 0 4px}
.d{font:550 13.008px/14.96px var(--font-sans);margin:0}
""",
            "html": """
<div class="def"><p class="h">Étude • noun • \\e.tyd\\</p><p class="d">From French "study". A methodical application of the mind in pursuit of learning and understanding.</p></div>
""",
        },
    },
    "cover": {
        "ground": "haze", "ink": "cobalt", "muted": "ink", "body_font": "sans",
        "name_font": "sans", "name_size": 104, "name_weight": 700, "name_ls": "-2.16px", "name_lines": ["L'Étude"],
        "tagline": "Modular creative studio.",
        "css": """
  .sig{fill:var(--signal)} .cob{fill:var(--cobalt)} .ink{fill:var(--ink)} .pap{fill:var(--paper)}
  .tile{rx:var(--radius-sm)}
  .ring{fill:none;stroke:var(--cobalt);stroke-width:3}
""",
        "derivation": """
blocks      signal 240x288 bleeding off top and right · cobalt 144x112 · ink 64x64 — about 40% of the cover
arrangement modules floating on haze, as the site floats image tiles; one big red field
pattern     icon-badge rings (radius-pill) — the site's literal motif — six 40px circles in cobalt over haze and red
scales      tiles radius-sm (4px), gaps space-3 (16), badge 40px circle
""",
        "svg": """
<rect class="sig" x="240" y="-8" width="248" height="304"/>
<rect class="cob tile" x="40" y="128" width="144" height="112" rx="4"/>
<rect class="ink tile" x="160" y="40" width="64" height="64" rx="4"/>
<circle class="ring" cx="64" cy="64" r="20"/>
<circle class="ring" cx="208" cy="168" r="20"/>
<circle class="ring" cx="300" cy="64" r="20"/>
<circle class="ring" cx="300" cy="112" r="20"/>
<circle class="cob" cx="420" cy="232" r="20"/>
<circle class="ring" cx="420" cy="184" r="20"/>
""",
    },
}

# ---------------------------------------------------------------- 3. Brik
brik = {
    "slug": "brik",
    "title": "Brik",
    "namespace": "Brik",
    "source": {"url": "https://brik.space/home", "captured": CAPTURED},
    "fonts_href": "https://fonts.googleapis.com/css2?family=Geist:wght@400;500&family=Geist+Mono:wght@500&display=swap",
    "families": {
        "sans": "\"Geist\", \"Neue Haas Grotesk Display Pro\", system-ui, sans-serif",
        "mono": "\"Geist Mono\", ui-monospace, SFMono-Regular, monospace",
    },
    "colors": [
        tok("canvas", "#fafafa", "Page ground."),
        tok("surface", "#ffffff", "Panels, cards and the prompt box interior."),
        tok("panel", "#ededed", "Input wells, slider tracks and the prompt textarea."),
        tok("ink", "#262626", "Primary text. 14.5:1 on `canvas`."),
        tok("ink-2", "#595959", "Secondary text and control labels. 6.7:1 on `canvas`, 6.0:1 on `panel`."),
        tok("ink-3", "#b2b2b2", "The faded second half of a headline (\"Other *design tools stop at export*\") and placeholders. 2.0:1 on `canvas` — decorative only; the meaning must also be in `ink` text."),
        tok("dark", "#1f1f1f", "The dark primary button (Build a Tool) and inverse panels. `surface` text on it is 16.5:1."),
        tok("electric", "#193ef9", "The send arrow, links and active slider fill. `surface` text on it is 6.8:1."),
        tok("go", "#36d972", "Live / success dot. Pair with `ink` text (8.2:1), not white."),
        tok("tag-orange", "#ff9060", "Use-case chip: Image Effect. `dark` text on it."),
        tok("tag-blue", "#608dff", "Use-case chip: Logo Motion. `dark` text on it (5.3:1)."),
        tok("tag-green", "#0aff89", "Use-case chip: Kinetic Typography. `dark` text on it."),
        tok("tag-coral", "#ff6063", "Use-case chip: 3D Scene. `dark` text on it."),
        tok("tag-pink", "#ff3366", "Use-case chip: Animated Gallery. `dark` text on it (4.6:1; `ink` would only reach 4.3:1)."),
    ],
    "type_groups": [
        {"name": "Display", "family": "sans", "styles": [
            style("display", "117px", "99.918px", 400, "Hero headline.", ls="-2.5px", sample="Build the design tool you wish existed"),
            style("headline", "50px", "53px", 400, "Section headlines; the two-tone ink / ink-3 statements.", ls="-0.96px"),
            style("title", "24px", "26px", 400, "Card titles and panel headers.", ls="-0.3px"),
        ]},
        {"name": "Text", "family": "sans", "styles": [
            style("body", "15px", "17px", 400, "UI text, nav and descriptions.", ls="-0.45px"),
            style("body-loose", "13px", "27px", 400, "Lists of controls in tool panels."),
            style("caption", "12px", "15.6px", 400, "Chip text and footnotes."),
        ]},
        {"name": "Mono", "family": "mono", "styles": [
            style("mono-label", "14px", "19px", 500, "Uppercase section eyebrows and step markers.", sample="[ 01 ] YOURS TO KEEP"),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Chip inner padding (vertical)."),
        tok("space-2", "8px", "Gap between chips; slider label to track."),
        tok("space-3", "12px", "Panel inner padding."),
        tok("space-4", "24px", "Gap between panels."),
        tok("space-5", "48px", "Section gutters."),
        tok("space-6", "96px", "Between page sections."),
    ],
    "radius": [tok("radius-none", "0px", "Everything. Brik draws square boxes, buttons and chips.")],
    "readme": """
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
""",
    "components": {
        "PromptBox": {
            "group": "Inputs", "height": 220,
            "readme": """
The hero brief input: a grey textarea, a large square `electric` send button and a row of use-case chips.

- Provide a placeholder ("Describe an image effect…") and the chips.
- Textarea on `panel`, text `body`, placeholder `ink-2`. Send button is a 96px square `electric` block with a `surface` arrow.
- Chips: `caption` text in `dark` on a `tag-*` fill, `space-1` × `space-2` padding, square.
""",
            "css": """
body{background:var(--canvas);padding:24px;font-family:var(--font-sans);color:var(--ink)}
.box{display:flex;max-width:560px}
textarea{flex:1;height:96px;border:0;background:var(--panel);padding:12px;font:400 15px/17px var(--font-sans);letter-spacing:-.45px;color:var(--ink);resize:none;border-radius:var(--radius-none)}
textarea::placeholder{color:var(--ink-2)}
.send{width:96px;height:120px;background:var(--electric);color:var(--surface);border:0;font:400 48px/1 var(--font-sans);cursor:pointer}
.chips{display:flex;gap:4px;margin-top:8px;flex-wrap:wrap}
.chip{font:400 12px/15.6px var(--font-sans);padding:2px 6px;color:var(--dark)}
.o{background:var(--tag-orange)}.b{background:var(--tag-blue)}.g{background:var(--tag-green)}.c{background:var(--tag-coral)}.p{background:var(--tag-pink)}
""",
            "html": """
<div class="box"><textarea id="brief" placeholder="Describe an image effect…"></textarea><button class="send" aria-label="Build">↑</button></div>
<div class="chips"><span class="chip o">Image Effect</span><span class="chip b">Logo Motion</span><span class="chip g">Kinetic Typography</span><span class="chip c">3D Scene</span><span class="chip p">Animated Gallery</span></div>
""",
        },
        "SliderControl": {
            "group": "Inputs", "height": 170,
            "readme": """
A labelled range row from a generated tool's control panel.

- Provide a label, min, max and value; the value prints at the right in `caption`.
- Label `caption` in `ink-2`; track 2px `panel`, filled part `ink`, thumb a 4×12 `ink` bar.
- Group rows in a `surface` panel with a `title`-style header and 1px `panel` border.
""",
            "css": """
body{background:var(--canvas);padding:24px;font-family:var(--font-sans)}
.panel{background:var(--surface);border:1px solid var(--panel);width:260px}
.hd{font:400 15px/17px var(--font-sans);letter-spacing:-.45px;color:var(--ink);padding:12px;border-bottom:1px solid var(--panel)}
.r{display:grid;grid-template-columns:1fr 90px 28px;gap:8px;align-items:center;padding:6px 12px;font:400 12px/15.6px var(--font-sans);color:var(--ink-2)}
.t{height:2px;background:var(--panel);position:relative}
.t i{position:absolute;left:0;top:0;bottom:0;background:var(--ink)}
.t b{position:absolute;top:-5px;width:4px;height:12px;background:var(--ink)}
.v{text-align:right}
""",
            "html": """
<div class="panel"><div class="hd">Chroma Block Ascii</div>
<div class="r"><span>Grid Resolution (Base)</span><span class="t"><i style="width:92%"></i><b style="left:92%"></b></span><span class="v">400</span></div>
<div class="r"><span>Model Spacing</span><span class="t"><i style="width:30%"></i><b style="left:30%"></b></span><span class="v">2</span></div>
<div class="r"><span>Contrast</span><span class="t"><i style="width:45%"></i><b style="left:45%"></b></span><span class="v">11</span></div>
</div>
""",
        },
        "Button": {
            "group": "Actions", "height": 90,
            "readme": """
Square buttons: `dark` for the primary action, plain text for secondary.

- Primary: `dark` ground, `surface` text, `body` style, padding `space-2` × `space-3`.
- Secondary: text only in `ink`; hover underlines.
- Focus: 2px `electric` outline, offset 2px.
""",
            "css": """
body{background:var(--canvas);padding:24px;font-family:var(--font-sans)}
.row{display:flex;gap:16px;align-items:center}
.btn{font:400 15px/17px var(--font-sans);letter-spacing:-.45px;padding:8px 12px;border:0;border-radius:var(--radius-none);cursor:pointer}
.pri{background:var(--dark);color:var(--surface)}
.sec{background:transparent;color:var(--ink)}
.btn:focus-visible{outline:2px solid var(--electric);outline-offset:2px}
""",
            "html": """
<div class="row"><button class="btn pri">Build a Tool</button><button class="btn sec">Sign in</button><button class="btn sec">Explore community</button></div>
""",
        },
    },
    "cover": {
        "ground": "canvas", "ink": "ink", "muted": "ink-2", "body_font": "sans",
        "name_font": "sans", "name_size": 120, "name_ls": "-2.5px", "name_lines": ["Brik"],
        "tagline": "Brief it. Control it. Use it.",
        "css": """
  .el{fill:var(--electric)} .dk{fill:var(--dark)} .pn{fill:var(--panel)}
  .o{fill:var(--tag-orange)} .g{fill:var(--tag-green)} .p{fill:var(--tag-pink)}
  .dot{fill:var(--ink-2)}
""",
        "derivation": """
blocks      electric 144x144 (the send button) · dark 96x48 (Build a Tool) · panel 192x96 (the prompt well) · three tag chips 48x16
arrangement a flush modular grid like the hero prompt: well + send block, chips under it
pattern     dot grid, from "precise, technical, mono": 36 dots at a space-4 (24px) pitch in ink-2
scales      gutters space-2 (8), pitch space-4 (24), radius-none
""",
        "svg": """
<rect class="pn" x="88" y="72" width="192" height="144"/>
<rect class="el" x="288" y="72" width="144" height="144"/>
<rect class="dk" x="336" y="16" width="96" height="48"/>
<rect class="o" x="88" y="224" width="48" height="16"/>
<rect class="g" x="144" y="224" width="64" height="16"/>
<rect class="p" x="216" y="224" width="40" height="16"/>
<g class="dot">
<circle cx="16" cy="24" r="1.5"/><circle cx="40" cy="24" r="1.5"/><circle cx="64" cy="24" r="1.5"/><circle cx="88" cy="24" r="1.5"/><circle cx="112" cy="24" r="1.5"/><circle cx="136" cy="24" r="1.5"/>
<circle cx="16" cy="48" r="1.5"/><circle cx="40" cy="48" r="1.5"/><circle cx="64" cy="48" r="1.5"/><circle cx="88" cy="48" r="1.5"/><circle cx="112" cy="48" r="1.5"/><circle cx="136" cy="48" r="1.5"/>
<circle cx="16" cy="72" r="1.5"/><circle cx="40" cy="72" r="1.5"/><circle cx="64" cy="72" r="1.5"/>
<circle cx="16" cy="96" r="1.5"/><circle cx="40" cy="96" r="1.5"/><circle cx="64" cy="96" r="1.5"/>
<circle cx="16" cy="120" r="1.5"/><circle cx="40" cy="120" r="1.5"/><circle cx="64" cy="120" r="1.5"/>
<circle cx="16" cy="144" r="1.5"/><circle cx="40" cy="144" r="1.5"/><circle cx="64" cy="144" r="1.5"/>
<circle cx="16" cy="168" r="1.5"/><circle cx="40" cy="168" r="1.5"/><circle cx="64" cy="168" r="1.5"/>
<circle cx="16" cy="264" r="1.5"/><circle cx="40" cy="264" r="1.5"/><circle cx="64" cy="264" r="1.5"/><circle cx="88" cy="264" r="1.5"/><circle cx="112" cy="264" r="1.5"/><circle cx="136" cy="264" r="1.5"/>
</g>
""",
    },
}

# ---------------------------------------------------------------- 4. Aino
aino = {
    "slug": "aino",
    "title": "Aino",
    "namespace": "Aino",
    "source": {"url": "https://aino.agency/", "captured": CAPTURED},
    "fonts_href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400&family=Schibsted+Grotesk:wght@400;500;700;800&display=swap",
    "families": {
        "mono": "\"IBM Plex Mono\", ui-monospace, monospace",
        "sans": "\"Schibsted Grotesk\", Helvetica, sans-serif",
    },
    "colors": [
        tok("paper", "#f5f5f0", "The only ground. A faintly warm off-white."),
        tok("ink", "#181818", "All text, ASCII art, rules and filled buttons. 16.2:1 on `paper`."),
        tok("ink-10", "rgba(24, 24, 24, 0.1)", "Hover wash behind nav items and button outlines' resting fill. Never text."),
        tok("ink-60", "#6e6e6b", "Secondary captions (dates, roles). 4.7:1 on `paper`. An addition: the site itself uses ink only."),
    ],
    "type_groups": [
        {"name": "Mono", "family": "mono", "styles": [
            style("ascii", "12.5831px", "16.1798px", 400, "ASCII artwork and terminal-like rule lines. Tracked 0.54px so glyphs sit on a square cell.", ls="0.54px", sample="AINO=====WORK=====SERVICES====="),
        ]},
        {"name": "Sans", "family": "sans", "styles": [
            style("headline", "37.7494px", "38.8315px", 720, "Page and case headlines.", ls="-1.13248px", sample="Design & technology"),
            style("title", "22.6497px", "25.8876px", 500, "Sub-heads and lead paragraphs.", ls="-0.452993px"),
            style("nav", "12.5831px", "17.4742px", 500, "Uppercase nav and buttons.", ls="0.02px", sample="WORK  SERVICES  ABOUT  PLAY"),
            style("body", "12.5831px", "16.1798px", 400, "Body copy and lists."),
        ]},
    ],
    "spacing": [
        tok("cell", "8px", "One ASCII cell width; the base unit for nudges."),
        tok("space-2", "16px", "Gaps inside components."),
        tok("space-3", "24px", "Page margin."),
        tok("space-4", "48px", "Between blocks."),
        tok("space-5", "96px", "Between sections."),
    ],
    "radius": [tok("radius-sm", "4px", "Buttons and the settings panel; the only rounding on the site.")],
    "readme": """
Aino is a Scandinavian design and technology agency (e-commerce, product design, visual identity, agentic engineering). Its site is a single ink colour on paper: navigation drawn as an ASCII rule line, hero images rendered as animated ASCII art, and a compact grotesk for the words. Built from the public site aino.agency; fonts are open substitutes.

## Voice

- Plain, confident, Nordic understatement. Nav words are single uppercase nouns: WORK, SERVICES, ABOUT, PLAY, SETTINGS, CONTACT.
- No exclamation marks. Let the ASCII do the showing.

## Colour

- One ink on one paper: `ink` on `paper`. Nothing else is required.
- `ink-10` is the only tint: hover washes and quiet fills.
- `ink-60` is an addition for metadata; use sparingly.

## Typography

- The site uses ABC Plus (a grotesk) and a custom mono. Substitutes here: **Schibsted Grotesk** and **IBM Plex Mono**.
- The mono is the brand's picture-making tool: ASCII art and `=` rule lines in `ascii`. Words are set in the sans.
- Sizes are fluid on the site; the values here are the 1440px-wide renders, kept exactly.

## Layout

- The header is one line of mono: name and nav joined by `=` runs that fill the width.
- Content centres on ASCII figures; text blocks sit in narrow columns.

## Imagery

- Convert photography to ASCII (density ramp ` .:-=+*#%@` or the site's own ` ·:;=+!?><7I2496A8`). Never show raw photos in the hero.
- No logo file ships; the name AINO is set in the mono.

## Components

`AsciiNav`, `AsciiFigure` and `Button` are static previews built on the tokens above.
""",
    "components": {
        "AsciiNav": {
            "group": "Navigation", "height": 80,
            "readme": """
The header: the agency name and nav items joined by runs of `=` in the mono, spanning the full width.

- Provide the brand name and 4–6 nav labels.
- One line of `ascii` style in `ink`; the `=` runs flex to fill the space. Hover a label: `ink-10` wash.
- Below 640px, keep name + CONTACT and collapse the rest into MENU.
""",
            "css": """
body{background:var(--paper);color:var(--ink);padding:24px;font:400 12.5831px/16.1798px var(--font-mono);letter-spacing:.54px}
nav{display:flex;align-items:center;white-space:nowrap;overflow:hidden}
nav a{color:var(--ink);text-decoration:none;padding:0 2px}
nav a:hover{background:var(--ink-10)}
.fill{flex:1;overflow:hidden;color:var(--ink)}
.fill::before{content:"=================================================================================================="}
""",
            "html": """
<nav><a href="#">AINO</a><span class="fill"></span><a href="#">WORK</a><span class="fill"></span><a href="#">SERVICES</a><span class="fill"></span><a href="#">ABOUT</a><span class="fill"></span><a href="#">PLAY</a><span class="fill"></span><a href="#">SETTINGS</a><span class="fill"></span><a href="#">CONTACT</a></nav>
""",
        },
        "AsciiFigure": {
            "group": "Media", "height": 220,
            "readme": """
A hero image rendered as ASCII text.

- Provide the pre-rendered ASCII string (or render it from an image with the density ramp in the README).
- `ascii` style, `ink`, `white-space: pre`, centred. Give it `role="img"` and an `aria-label` describing the picture.
""",
            "css": """
body{background:var(--paper);color:var(--ink);padding:16px;margin:0}
pre{font:400 12.5831px/16.1798px var(--font-mono);letter-spacing:.54px;margin:0;text-align:center;overflow:hidden}
""",
            "html": """
<pre role="img" aria-label="ASCII rendering of a diamond shape">
                 ·
                !A>
              -:=+!?>-
           ?:-=!?>&lt;7I2=:·
        :=+!?>&lt;7I249968A?!=
     ·-=!?>&lt;7I24996888AAAA8?!:
        :=+!?>&lt;7I249968A?!=
           ?:-=!?>&lt;7I2=:·
              -:=+!?>-
                !A>
                 ·
</pre>
""",
        },
        "Button": {
            "group": "Actions", "height": 90,
            "readme": """
Small uppercase buttons with a 4px corner.

- Filled: `ink` ground, `paper` text. Quiet: `ink-10` ground, `ink` text.
- Text `nav` style. Padding `cell` × `space-2`. Corners `radius-sm`.
- Focus: 2px `ink` outline, offset 2px.
""",
            "css": """
body{background:var(--paper);padding:24px}
.row{display:flex;gap:8px}
.btn{font:500 12.5831px/17.4742px var(--font-sans);text-transform:uppercase;padding:8px 16px;border:0;border-radius:var(--radius-sm);cursor:pointer}
.f{background:var(--ink);color:var(--paper)}
.q{background:var(--ink-10);color:var(--ink)}
.btn:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
""",
            "html": """
<div class="row"><button class="btn f">Contact</button><button class="btn q">Settings</button></div>
""",
        },
    },
    "cover": {
        "ground": "paper", "ink": "ink", "muted": "ink-60", "body_font": "sans",
        "name_font": "mono", "name_size": 120, "name_lines": ["Aino"],
        "tagline": "Design and technology, drawn in one ink.",
        "css": """
  .ink{fill:var(--ink)} .t10{fill:var(--ink-10)}
  .blk{rx:var(--radius-sm)}
  .eq{stroke:var(--ink);stroke-width:2}
""",
        "derivation": """
blocks      ink 192x192 slab bleeding off the right edge · ink-10 tint 144x240 behind it — one-ink brand, so two blocks
arrangement tint and slab overlapped, offset by space-4 (48)
pattern     the "=" rule line from the header: paired 2px strokes at a cell pitch, six runs, from "precise, technical, mono"
scales      cell 8px, space-4 48px, radius-sm 4px
""",
        "svg": """
<rect class="t10 blk" x="144" y="24" width="192" height="240" rx="4"/>
<rect class="ink blk" x="288" y="72" width="200" height="168" rx="4"/>
<g class="eq">
<line x1="16" y1="40" x2="128" y2="40"/><line x1="16" y1="48" x2="128" y2="48"/>
<line x1="16" y1="104" x2="96" y2="104"/><line x1="16" y1="112" x2="96" y2="112"/>
<line x1="16" y1="168" x2="128" y2="168"/><line x1="16" y1="176" x2="128" y2="176"/>
<line x1="352" y1="24" x2="472" y2="24"/><line x1="352" y1="32" x2="472" y2="32"/>
</g>
""",
    },
}

# ---------------------------------------------------------------- 5. The Design Society
designsociety = {
    "slug": "the-design-society",
    "title": "The Design Society",
    "namespace": "DesignSociety",
    "source": {"url": "https://www.thedesignsociety.fr/", "captured": CAPTURED},
    "fonts_href": "https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400&family=DM+Sans:opsz,wght@9..40,400&family=Space+Mono:wght@400;700&display=swap",
    "families": {
        "pixel": "\"Pixelify Sans\", \"Courier New\", monospace",
        "sans": "\"DM Sans\", Arial, sans-serif",
        "mono": "\"Space Mono\", \"Courier New\", monospace",
    },
    "colors": [
        tok("electric", "#350aff", "Signature ground: the full-bleed blue sections and the pixel emblems. `white` text on it is 7.9:1; `lime` is 5.9:1."),
        tok("lime", "#bcf015", "Acid accent: event tiles, stickers, the hover state of links. `ink` text on it is 12.4:1."),
        tok("mist", "#ebedf5", "Light ground for the hero and event pages."),
        tok("ink", "#1e1e1e", "Text on `mist`, `lime` and `white`. 14.3:1 on `mist`."),
        tok("smoke", "#efeeec", "Body text on `electric` (6.9:1) and `night` (16.0:1)."),
        tok("night", "#131313", "Dark sections (footer, photo strips)."),
        tok("white", "#fefeff", "Cards and the floating menu bar; text on `electric`."),
    ],
    "type_groups": [
        {"name": "Pixel display", "family": "pixel", "styles": [
            style("display-xl", "132px", "140px", 400, "The society name on the hero.", sample="The Design Society"),
            style("display-lg", "79.8px", "95.76px", 400, "Event titles."),
            style("display-sm", "28.8px", "33.12px", 400, "Card headlines and the floating menu name."),
        ]},
        {"name": "Sans", "family": "sans", "styles": [
            style("headline", "54px", "54px", 400, "Statements in the sans: talk titles, section openers.", ls="-1.19px"),
            style("body", "14px", "20px", 400, "Paragraphs.", sample="Entre les talks pour partager le savoir et les apéros pour l'oublier."),
        ]},
        {"name": "Mono", "family": "mono", "styles": [
            style("mono-lg", "29.75px", "29.75px", 400, "Large numerals (TALK #1)."),
            style("mono", "14px", "14px", 400, "Bracketed tags and nav, uppercase.", sample="[ CRITÈRE D'ACCÈS : SAVOIR RESPIRER ]"),
            style("mono-sm", "11px", "11px", 400, "Footnotes, credits and small uppercase meta."),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Inside tags."),
        tok("space-2", "8px", "Menu bar inner padding."),
        tok("space-3", "16px", "Card padding."),
        tok("space-4", "32px", "Gaps between cards."),
        tok("space-5", "64px", "Section padding."),
        tok("space-6", "128px", "Hero top padding."),
    ],
    "radius": [
        tok("radius-xs", "2px", "Inline image chips set between headline words."),
        tok("radius-sm", "4px", "Buttons and tags."),
        tok("radius-md", "6px", "The floating menu bar and cards."),
        tok("radius-pill", "999px", "Round stickers and pill links."),
    ],
    "readme": """
The Design Society is a Lyon association that gathers designers for talks and apéros: "la société secrète la moins gardée de Lyon". The site mixes an electric-blue ground, an acid-lime accent, a pixel serif headline face and bracketed monospace stage directions. Built from the public site thedesignsociety.fr; fonts are open substitutes.

## Voice

- French first, playful and self-mocking: "Une société secrète si mal gardée qu'on a fait un site."
- Stage directions in brackets and caps: `[ CRITÈRE D'ACCÈS : SAVOIR RESPIRER ]`, `[ FORMATION SUR PLACE POSSIBLE ]`.
- Events are numbered: `TALK #1`, then "AVEC HUGO DOUCHET".

## Colour

- Two loud colours, used whole: `electric` as a full section ground, `lime` as tiles and stickers. Keep them in big areas, not thin accents.
- Light pages sit on `mist` with `ink` text; dark strips use `night` with `smoke` text.
- Never put `lime` text on `mist` (1.2:1); lime is a fill.

## Typography

- The site uses FK Raster Roman (pixel serif), KH Teka (sans) and KH Interference (mono). Substitutes here: **Pixelify Sans**, **DM Sans** and **Space Mono**.
- Pixel face for names and titles only; sans for statements and paragraphs; mono, uppercase and bracketed, for meta.
- Headlines can carry small inline images or emblems between words (`radius-xs` chips at cap height).

## Layout

- A floating `white` menu bar (`radius-md`) centred at the top, with the society name and a burger.
- Sections alternate `mist` and `electric`. Event tiles in `lime` sit bottom-right of blue sections.

## Iconography

- Pixel-art emblems (eye, star, flame) in `electric` or `ink`. None ship here; draw on a pixel grid, single colour.

## Components

`BracketTag`, `EventCard` and `MenuBar` are static previews built on the tokens above.
""",
    "components": {
        "BracketTag": {
            "group": "Content", "height": 110,
            "readme": """
A bracketed uppercase stage direction set in the mono.

- Provide one short phrase. Render as `[ PHRASE ]` in `mono`, uppercase.
- On `mist`: `ink`. On `electric`: `lime` or `smoke`.
""",
            "css": """
body{margin:0;font:400 14px/14px var(--font-mono);text-transform:uppercase}
.a{background:var(--mist);color:var(--ink);padding:24px}
.b{background:var(--electric);color:var(--lime);padding:24px}
""",
            "html": """
<div class="a">[ Critère d'accès : savoir respirer ]</div>
<div class="b">[ Formation sur place possible ]</div>
""",
        },
        "EventCard": {
            "group": "Content", "height": 260,
            "readme": """
A lime event tile: talk number in the mono, speaker line, title in the pixel face, a one-line summary.

- Provide `number`, `speaker`, `title`, `summary`.
- `lime` ground, `ink` text, `radius-md`, padding `space-3`. Number `mono-lg`; speaker `mono` uppercase; title `display-sm`; summary `body`.
- Place on `electric` or `night` sections.
""",
            "css": """
body{background:var(--electric);padding:24px}
.card{background:var(--lime);color:var(--ink);border-radius:var(--radius-md);padding:16px;max-width:300px}
.n{font:400 29.75px/29.75px var(--font-mono)}
.s{font:400 11px/11px var(--font-mono);text-transform:uppercase;margin:8px 0 16px}
h3{font:400 28.8px/33.12px var(--font-pixel);margin:0 0 8px}
p{font:400 14px/20px var(--font-sans);margin:0}
""",
            "html": """
<div class="card"><div class="n">TALK #1</div><div class="s">Avec Hugo Douchet</div><h3>L'histoire du Design</h3><p>Talk sur l'influence des outils sur nos démarches créatives.</p></div>
""",
        },
        "MenuBar": {
            "group": "Navigation", "height": 110,
            "readme": """
The floating top menu: emblem, society name in the pixel face, burger at the right.

- Provide the name and an emblem (single-colour SVG or glyph).
- `white` ground, `radius-md`, padding `space-2` × `space-3`, width 360–420px, centred.
- Name `display-sm` at 16px in `ink`; emblem in `electric`.
""",
            "css": """
body{background:var(--electric);padding:24px;display:flex;justify-content:center}
.bar{background:var(--white);border-radius:var(--radius-md);display:flex;align-items:center;gap:8px;padding:8px 16px;width:360px;box-sizing:border-box}
.e{color:var(--electric);font:700 16px/1 var(--font-mono)}
.nm{font:400 16px/1 var(--font-pixel);color:var(--ink);flex:1}
.bg{width:16px;height:8px;border-top:2px solid var(--ink);border-bottom:2px solid var(--ink)}
""",
            "html": """
<div class="bar"><span class="e">✲</span><span class="nm">The Design Society</span><span class="bg" aria-label="Menu"></span></div>
""",
        },
    },
    "cover": {
        "ground": "mist", "ink": "ink", "muted": "ink", "body_font": "sans",
        "name_font": "pixel", "name_size": 72, "name_lines": ["The Design", "Society"],
        "tagline": "La société secrète la moins gardée de Lyon.",
        "css": """
  .el{fill:var(--electric)} .li{fill:var(--lime)} .ni{fill:var(--night)}
  .card{rx:var(--radius-md)}
""",
        "derivation": """
blocks      electric 336x288 full-bleed right field · lime 112x112 event tile · night 64x64 photo tile — about 45% of the cover
arrangement one big blue section with the lime tile bottom-right, as on the site
pattern     pixel checker: 16px squares in lime over the blue, from "loud, bold, poster type" and the pixel face — 20 cells
scales      tiles radius-md (6), pitch 16 (space-3), gaps space-3
""",
        "svg": """
<rect class="el" x="144" y="0" width="336" height="288"/>
<rect class="li card" x="344" y="152" width="112" height="112" rx="6"/>
<rect class="ni card" x="264" y="200" width="64" height="64" rx="6"/>
<g class="li">
<rect x="176" y="32" width="16" height="16"/><rect x="208" y="32" width="16" height="16"/><rect x="240" y="32" width="16" height="16"/><rect x="272" y="32" width="16" height="16"/>
<rect x="192" y="48" width="16" height="16"/><rect x="224" y="48" width="16" height="16"/><rect x="256" y="48" width="16" height="16"/>
<rect x="176" y="64" width="16" height="16"/><rect x="208" y="64" width="16" height="16"/><rect x="240" y="64" width="16" height="16"/>
<rect x="192" y="80" width="16" height="16"/><rect x="224" y="80" width="16" height="16"/>
<rect x="176" y="96" width="16" height="16"/><rect x="208" y="96" width="16" height="16"/>
<rect x="192" y="112" width="16" height="16"/>
<rect x="176" y="128" width="16" height="16"/>
</g>
<rect class="ni" x="64" y="32" width="48" height="48"/>
""",
    },
}

SYSTEMS = [odyssee, letude, brik, aino, designsociety]
