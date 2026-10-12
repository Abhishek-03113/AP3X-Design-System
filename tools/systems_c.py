from ds_lib import tok, style

CAPTURED = "2026-10-11"
GF = "https://fonts.googleapis.com/css2?"

# ---------------------------------------------------------------- The Lookback (BetterOff)
lookback = {
    "slug": "the-lookback",
    "title": "The Lookback",
    "namespace": "Lookback",
    "source": {"url": "https://tlb.betteroff.studio/surf", "captured": CAPTURED},
    "fonts_href": GF + "family=Archivo:wght@500;700&family=DM+Mono:wght@500&display=swap",
    "families": {
        "sans": "\"Archivo\", \"Helvetica Neue\", Arial, sans-serif",
        "mono": "\"DM Mono\", ui-monospace, monospace",
    },
    "colors": [
        tok("white", "#ffffff", "Page ground and text over photography."),
        tok("black", "#000000", "Index text, the title lockup and button labels. 21:1 on `white`."),
        tok("fog", "#bdbdbd", "Unloaded image tiles in the surf grid. `white` text on it is 1.9:1, the site's own pairing over images; keep such labels decorative and repeat them in `black` elsewhere."),
        tok("grey", "#838383", "Faded index entries that are not yet published. 3.8:1 on `white`: large text or secondary only."),
        tok("tan", "#c39777", "Photo tint: sand and skin in the surf archive. Placeholder fill only."),
        tok("rust", "#bf7048", "Photo tint: late-light rock. Placeholder fill only."),
        tok("swell", "#7c9dc3", "Photo tint: water. Placeholder fill only."),
        tok("white-30", "rgba(255, 255, 255, 0.3)", "Disabled labels over images."),
    ],
    "type_groups": [
        {"name": "Display", "family": "sans", "styles": [
            style("title", "101.088px", "85.9248px", 700, "The lockup \"(BO®S) TLB/2026\".", ls="-1.01088px", sample="(BO®S) TLB/2026"),
            style("label", "19.2px", "24.96px", 500, "Section labels and the four nav words.", sample="Timeline, Surf, Index, About"),
        ]},
        {"name": "Mono", "family": "mono", "styles": [
            style("index", "13.44px", "17.472px", 500, "The month index and everything else small. Always uppercase.", sample="JANUARY  ARTICLES (3)  PODCAST EPISODES (2)"),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Index line gaps."),
        tok("space-2", "12px", "Button padding (horizontal)."),
        tok("space-3", "24px", "Page margin."),
        tok("space-4", "48px", "Between index columns."),
    ],
    "radius": [
        tok("radius-xs", "2.88px", "Tiny tags."),
        tok("radius-sm", "3.84px", "Image tiles."),
        tok("radius-md", "4.8px", "The \"Enter with sound\" button."),
    ],
    "readme": """
The Lookback is BetterOff studio's yearly scrapbook: "a digital reflection of our pulse, taste, and personality. Moments, music, and work that keep us moving." It opens on a white page with a heavy black lockup and a two-column month index in small uppercase mono, then drops into a grid of surf photography. Built from the public site tlb.betteroff.studio; fonts are open substitutes.

## Voice
- Diary-like and list-driven. Content is counted: `ARTICLES (3)`, `PODCAST EPISODES (2)`, `MUSIC PLAYLIST (12)`.
- Nav words end in commas: "Timeline, Surf, Index, About". The marquee repeats the current track: "Redman - Looka Here ft. KRS-One /".
- Status words in caps: `LOADED`.

## Colour
- `black` on `white` for every word. The rest of the colour comes from photography; `tan`, `rust` and `swell` are only placeholders for it.
- `fog` is the empty tile. Text on tiles is `white` like the site, which is decorative at 1.9:1.

## Typography
- The site uses two custom faces called simply "sans" and "mono". Substitutes: **Archivo** (700 for the lockup, 500 for labels) and **DM Mono** 500.
- `index` is uppercase everywhere. The lockup tracks −1px and sets the ® and parentheses at full size.

## Layout
- Lockup centred left of the middle; the index runs in two columns beside it, January–July and August–December.
- One small bordered button under the lockup ("Enter with sound →"), with "…or without" beneath in `grey`.

## Components
`TitleLockup`, `MonthIndex` and `EnterButton`. No logo file ships; the lockup is set in type.
""",
    "components": {
        "TitleLockup": {
            "group": "Content", "height": 200,
            "readme": """
The year lockup: studio code in parentheses over the title and year.

- Provide two lines, e.g. `(BO®S)` and `TLB/2026`.
- `title` style, `black`, centred, line-height under 1.
""",
            "css": """
body{background:var(--white);color:var(--black);padding:24px;text-align:center}
h1{font:700 64px/0.85 var(--font-sans);letter-spacing:-.64px;margin:0}
""",
            "html": "<h1>(BO®S)<br>TLB/2026</h1>",
        },
        "MonthIndex": {
            "group": "Navigation", "height": 220,
            "readme": """
The archive index: months in caps, each followed by indented content counts.

- Provide months and their entries with counts.
- `index` style, uppercase, `black`; entries indented one `space-2`. Unpublished entries in `grey`.
- Two columns, gap `space-4`.
""",
            "css": """
body{background:var(--white);color:var(--black);padding:24px;font:500 13.44px/17.472px var(--font-mono);text-transform:uppercase}
.cols{display:flex;gap:48px}
.e{padding-left:12px}
.g{color:var(--grey)}
""",
            "html": """
<div class="cols">
<div>January<div class="e">Articles (3)</div><div class="e">Podcast episodes (2)</div><div class="e">Inspiration (4)</div><div class="e">Music playlist (12)</div>February<div class="e">Articles (3)</div><div class="e">Podcast episodes (2)</div></div>
<div>August<div class="e">Articles (3)</div><div class="e">Podcast episodes (2)</div>September<div class="e">Articles (3)</div><div class="e g">Cases (1)</div></div>
</div>
""",
        },
        "EnterButton": {
            "group": "Actions", "height": 110,
            "readme": """
The small bordered entry button with a quiet alternative underneath.

- Provide the label and the alternative ("…or without").
- 1px `black` border, `radius-md`, `label` at 13px, padding `space-1` × `space-2`. Alternative 10px in `grey`.
""",
            "css": """
body{background:var(--white);padding:24px;text-align:center;font-family:var(--font-sans)}
button{font:500 13px/1 var(--font-sans);border:1px solid var(--black);border-radius:var(--radius-md);background:var(--white);color:var(--black);padding:6px 12px;cursor:pointer}
p{font:500 10px/1 var(--font-sans);color:var(--grey);margin:8px 0 0}
""",
            "html": "<button>Enter with sound →</button><p>…or without</p>",
        },
    },
    "cover": {
        "ground": "white", "ink": "black", "muted": "black", "body_font": "sans",
        "name_font": "sans", "name_size": 72, "name_weight": 700, "name_ls": "-1px", "name_lines": ["The", "Lookback"],
        "tagline": "Moments, music, and work that keep us moving.",
        "css": """
  .fog{fill:var(--fog)} .tan{fill:var(--tan)} .rust{fill:var(--rust)} .sw{fill:var(--swell)}
  .tile{rx:var(--radius-sm)}
""",
        "derivation": """
blocks      fog, tan, rust, swell as image tiles in the surf grid, 96x128 each (photo tints, the brand's only colour)
arrangement a flush modular grid of tiles, one row offset, like the photo wall
pattern     tiles at radius-sm corners, from "geometric, modular" — eight tiles, two merged wide
scales      gaps space-2 (12), radius-sm 3.84
""",
        "svg": """
<rect class="fog tile" x="24" y="24" width="96" height="128" rx="3.84"/>
<rect class="tan tile" x="132" y="24" width="96" height="128" rx="3.84"/>
<rect class="sw tile" x="240" y="24" width="204" height="128" rx="3.84"/>
<rect class="rust tile" x="78" y="164" width="96" height="100" rx="3.84"/>
<rect class="fog tile" x="186" y="164" width="96" height="100" rx="3.84"/>
<rect class="tan tile" x="294" y="164" width="150" height="100" rx="3.84"/>
""",
    },
}

# ---------------------------------------------------------------- Brittany Taylor
btay = {
    "slug": "brittany-taylor",
    "title": "Brittany Taylor",
    "namespace": "BrittanyTaylor",
    "source": {"url": "https://btay.ca/", "captured": CAPTURED},
    "fonts_href": GF + "family=Inter:wght@400;500;600;700&family=Averia+Serif+Libre:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&family=Homemade+Apple&display=swap",
    "families": {
        "sans": "\"Inter Display\", \"Inter\", sans-serif",
        "serif": "\"Averia Serif Libre\", Georgia, serif",
        "hand": "\"Homemade Apple\", cursive",
    },
    "colors": [
        tok("linen", "#f7f4ed", "Page ground."),
        tok("ink", "#0f0f0f", "Headlines and body. 17.5:1 on `linen`."),
        tok("olive", "#42423a", "Secondary copy and testimonials. 9.2:1 on `linen`."),
        tok("cobalt", "#2978f3", "Project card ground and the hero illustration's blue. `white` text on it is 4.0:1 — large or bold text only."),
        tok("jade", "#0e9c6c", "Project card ground; the green underline under \"web designer\". `white` text on it is 3.4:1 — large or bold text only."),
        tok("sky", "#69afeb", "Illustration blue and link hover."),
        tok("brick", "#bd573c", "Illustration red; the underline under \"Selected projects\"."),
        tok("white", "#fcfcfc", "Card text on `cobalt`/`jade`, and input fields."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("display", "72px", "64.8px", 700, "Hero sentence, mixed with italic serif words.", ls="-1.44px", sample="I'm an independent web designer"),
            style("display-alt", "70px", "63px", 700, "Section heads.", ls="-1.44px"),
            style("lead", "24px", "33.6px", 500, "Intro paragraphs."),
            style("body", "18px", "21.6px", 400, "Body copy.", ls="0.2px"),
            style("small", "16px", "20.8px", 400, "Captions and footer."),
        ]},
        {"name": "Serif", "family": "serif", "styles": [
            style("serif-display", "72px", "72px", 400, "Italic words inside the hero (\"web designer\", \"10+ years\").", sample="web designer"),
            style("serif-title", "36px", "32.4px", 700, "Card titles."),
            style("serif-body", "24px", "28.8px", 400, "Testimonials, italic.", sample="\"Brittany impressed us…\""),
        ]},
        {"name": "Hand", "family": "hand", "styles": [
            style("signature", "24px", "32px", 400, "One handwritten note per page."),
        ]},
    ],
    "spacing": [
        tok("space-1", "8px", "Inline gaps."),
        tok("space-2", "16px", "Card padding."),
        tok("space-3", "32px", "Gap between cards."),
        tok("space-4", "64px", "Section padding."),
        tok("space-5", "120px", "Hero padding."),
    ],
    "radius": [
        tok("radius-card", "16px", "Project cards and images."),
        tok("radius-lg", "40px", "Large feature panels."),
        tok("radius-pill", "1000px", "Buttons and tags."),
    ],
    "readme": """
Brittany Taylor is an independent web designer and marketing strategist in Vancouver. The site is warm and playful: a centred bold sans headline with italic serif words dropped in, cut-paper illustrations in cobalt, jade and brick, and rounded project cards. Built from the public site btay.ca; Inter, Averia Serif Libre and Homemade Apple are the site's own Google faces.

## Voice
- Friendly first person: "Hello! I'm an independent web designer and marketing strategist with 10+ years of experience."
- Underline key phrases with a hand-drawn stroke ("web designer", "Selected projects").
- Testimonials quoted in full with name and role ("Naomi + Jessica").

## Colour
- `ink` on `linen` for reading; `olive` for secondary text.
- `cobalt` and `jade` are card grounds; their white-text contrast is under 4.5:1, so set card text 24px+ or bold.
- `sky` and `brick` belong to the illustrations and underlines.

## Typography
- **Inter Display** bold for statements, **Averia Serif Libre** italic for the emphasised words inside them, **Homemade Apple** for one signature-style note.
- Track display sizes −1.44px.

## Layout
- Everything centred in the hero; cards in a 2–3 column grid below with `radius-card` corners.

## Components
`HeroStatement`, `ProjectCard` and `Testimonial`. No logo or illustration files ship.
""",
    "components": {
        "HeroStatement": {
            "group": "Content", "height": 240,
            "readme": """
The centred hero sentence that mixes bold sans with italic serif emphasis.

- Provide the sentence and mark 1–2 phrases for emphasis.
- Sans in `display`; emphasis in `serif-display` italic with a 2px `jade` underline. Centred, max 14 words.
""",
            "css": """
body{background:var(--linen);color:var(--ink);padding:24px;text-align:center}
.hi{font:italic 400 18px/1 var(--font-serif);margin:0 0 8px}
h1{font:700 40px/36px var(--font-sans);letter-spacing:-.8px;margin:0 auto;max-width:14ch}
em{font:italic 400 40px/36px var(--font-serif);text-decoration:underline;text-decoration-color:var(--jade);text-decoration-thickness:2px;text-underline-offset:4px}
""",
            "html": "<p class=\"hi\">Hello !</p><h1>I'm an independent <em>web designer</em> and marketing strategist with <em>10+ years</em> of experience.</h1>",
        },
        "ProjectCard": {
            "group": "Content", "height": 220,
            "readme": """
A rounded project card with a solid colour ground and the client name.

- Provide the project name and a ground token (`cobalt` or `jade`).
- `radius-card`, padding `space-2`, title `serif-title` in `white` (bold, so large-text contrast applies).
""",
            "css": """
body{background:var(--linen);padding:24px;display:flex;gap:24px;flex-wrap:wrap}
.c{width:200px;height:150px;border-radius:var(--radius-card);padding:16px;box-sizing:border-box;display:flex;align-items:flex-end;color:var(--white);font:700 28px/1 var(--font-serif)}
""",
            "html": "<div class=\"c\" style=\"background:var(--cobalt)\">DSGN Dept.</div><div class=\"c\" style=\"background:var(--jade)\">Panobi</div>",
        },
        "Testimonial": {
            "group": "Content", "height": 200,
            "readme": """
A client quote in italic serif with the name under it.

- Provide quote text and attribution.
- Quote `serif-body` italic in `olive`, max 48ch; attribution `small` in `ink`.
""",
            "css": """
body{background:var(--linen);padding:24px}
q{display:block;font:italic 400 22px/1.3 var(--font-serif);color:var(--olive);max-width:48ch}
p{font:500 16px/20.8px var(--font-sans);color:var(--ink);margin:12px 0 0}
""",
            "html": "<q>Brittany impressed us with how thoughtfully she took the time to understand our work, our goals, and our vision.</q><p>Naomi + Jessica</p>",
        },
    },
    "cover": {
        "ground": "linen", "ink": "ink", "muted": "olive", "body_font": "sans",
        "name_font": "sans", "name_size": 72, "name_weight": 700, "name_ls": "-1.44px", "name_lines": ["Brittany", "Taylor"],
        "tagline": "Independent web designer and marketing strategist.",
        "css": """
  .co{fill:var(--cobalt)} .ja{fill:var(--jade)} .br{fill:var(--brick)} .sk{fill:var(--sky)}
  .card{rx:var(--radius-card)}
""",
        "derivation": """
blocks      cobalt 176x200 card · jade 128x128 card · brick 64x64 · sky 96x40 pill — the illustration palette
arrangement staggered stack of rounded cards, like the project grid
pattern     discs and pills from radius-pill and "warm, playful": three sky discs, one pill
scales      radius-card 16, gaps space-2 (16), pill radius half of 40
""",
        "svg": """
<rect class="co card" x="40" y="32" width="176" height="200" rx="16"/>
<rect class="ja card" x="232" y="104" width="128" height="128" rx="16"/>
<rect class="br card" x="376" y="168" width="64" height="64" rx="16"/>
<rect class="sk" x="232" y="48" width="96" height="40" rx="20"/>
<circle class="sk" cx="400" cy="72" r="24"/>
<circle class="br" cx="408" cy="128" r="10"/>
<circle class="ja" cx="128" cy="260" r="12"/>
""",
    },
}

# ---------------------------------------------------------------- Arc'teryx System_0
system0 = {
    "slug": "arcteryx-system-0",
    "title": "System Ø",
    "namespace": "SystemZero",
    "source": {"url": "https://arcteryx.com/us/en/explore/system0/", "captured": CAPTURED},
    "fonts_href": GF + "family=Gelasio:wght@400&display=swap",
    "families": {
        "serif": "\"Gelasio\", Georgia, serif",
        "sans": "\"Helvetica Now Display\", \"Helvetica Neue\", Helvetica, Arial, sans-serif",
    },
    "colors": [
        tok("night", "#0c0c0c", "Page ground."),
        tok("paper", "#fdfdfd", "Primary text and the wordmark. 19.2:1 on `night`."),
        tok("ash", "#959595", "Secondary nav items and captions. 6.5:1 on `night`."),
        tok("charcoal", "#333333", "Panels and the cookie bar."),
        tok("veil", "rgba(253, 253, 253, 0.05)", "Section wash over black; hover fill."),
        tok("cloth", "#6c4538", "Fabric tone from the hero film (waxed brown ripstop). Image placeholder only."),
        tok("cloth-light", "#9a6956", "Highlight tone of the same fabric. Image placeholder only."),
    ],
    "type_groups": [
        {"name": "Serif", "family": "serif", "styles": [
            style("statement", "40px", "40px", 400, "Chapter statements.", sample="The revolution is circular"),
            style("body", "22px", "24px", 400, "Editorial body copy.", sample="Our journey toward circularity."),
        ]},
        {"name": "Sans", "family": "sans", "styles": [
            style("nav", "14px", "17px", 400, "Uppercase nav and hero overlay text.", ls="0.4px", sample="PROCESS  MISSION  SPERRO SV  REBIRD"),
            style("label-bold", "14px", "16.8px", 700, "Emphasised labels."),
            style("caption", "11.2px", "16.8px", 200, "Credits and legal lines."),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Nav line gap."),
        tok("space-2", "16px", "Page margin."),
        tok("space-3", "40px", "Between text blocks."),
        tok("space-4", "120px", "Between chapters."),
    ],
    "radius": [
        tok("radius-xs", "2px", "Small controls."),
        tok("radius-sm", "4px", "Buttons."),
        tok("radius-circle", "50%", "Carousel dots and round icon buttons."),
    ],
    "readme": """
System_Ø is Arc'teryx's editorial microsite on circular design ("Our journey toward circularity"). It runs on a black ground with full-bleed close-up film of fabric and water, a serif for what is said and a small tracked uppercase sans for navigation. Built from the public page arcteryx.com/us/en/explore/system0; the serif is an open substitute. The Arc'teryx bird logo and System Ø wordmark are not reproduced.

## Voice
- Short manifesto lines in caps over film: "THE REVOLUTION IS CIRCULAR".
- Chapters named by product or principle: PROCESS, MISSION, SPERRO SV, REBIRD.

## Colour
- `paper` on `night`; `ash` for secondary nav. That is the whole UI.
- `cloth` and `cloth-light` stand in for the film while it loads.

## Typography
- The site uses **Elan ITC Pro** (serif) and **Helvetica Now Display**. Substitutes: **Gelasio** and the Helvetica Neue stack.
- Uppercase sans tracked 0.4px for nav and overlays; serif sentence case for reading.

## Layout
- Wordmark top-left, a two-line subtitle beside it, chapter nav top-right as a dotted list, the bird mark far right.
- Full-bleed film; one centred line of caps over it.

## Components
`Header`, `Statement` and `ChapterNav`.
""",
    "components": {
        "Header": {
            "group": "Navigation", "height": 90,
            "readme": """
The top bar: wordmark, a two-line subtitle, then chapter nav on the right.

- Provide the wordmark text, subtitle and chapters.
- Wordmark sans 22px uppercase in `paper`; subtitle `caption` uppercase; nav per `ChapterNav`.
""",
            "css": """
body{background:var(--night);color:var(--paper);padding:16px;font-family:var(--font-sans)}
.b{display:flex;gap:16px;align-items:flex-start}
.w{font:400 22px/1 var(--font-sans);text-transform:uppercase}
.s{font:400 9px/1.2 var(--font-sans);text-transform:uppercase;letter-spacing:.3px;flex:1}
""",
            "html": "<div class=\"b\"><span class=\"w\">System Ø</span><span class=\"s\">Our journey toward<br>circularity</span></div>",
        },
        "Statement": {
            "group": "Content", "height": 160,
            "readme": """
One centred line of uppercase over film.

- Provide one short line (≤6 words).
- `nav` style scaled to 22px, uppercase, `paper`, centred on a `cloth` placeholder until the film loads.
""",
            "css": """
body{margin:0}
.f{background:var(--cloth);height:160px;display:grid;place-items:center}
p{margin:0;font:400 22px/1 var(--font-sans);letter-spacing:.4px;text-transform:uppercase;color:var(--paper)}
""",
            "html": "<div class=\"f\"><p>The revolution is circular</p></div>",
        },
        "ChapterNav": {
            "group": "Navigation", "height": 120,
            "readme": """
The dotted chapter list at top-right.

- Provide chapters and the current one.
- `nav` style, uppercase. Current item `paper` with a 4px `paper` dot before it; others `ash`.
""",
            "css": """
body{background:var(--night);padding:16px;font:400 11px/1.5 var(--font-sans);letter-spacing:.4px;text-transform:uppercase}
a{display:block;color:var(--ash);text-decoration:none;padding-left:12px;position:relative}
a.on{color:var(--paper)}
a.on::before{content:"";position:absolute;left:0;top:6px;width:4px;height:4px;border-radius:var(--radius-circle);background:var(--paper)}
""",
            "html": "<a class=\"on\" href=\"#\">Process</a><a href=\"#\">Mission</a><a href=\"#\">Sperro SV</a><a href=\"#\">Arc'teryx</a><a href=\"#\">ReBird</a>",
        },
    },
    "cover": {
        "ground": "night", "ink": "paper", "muted": "ash", "body_font": "sans",
        "name_font": "sans", "name_size": 96, "name_lines": ["System Ø"],
        "tagline": "Our journey toward circularity.",
        "css": """
  .cl{fill:var(--cloth)} .cll{fill:var(--cloth-light)} .ch{fill:var(--charcoal)}
  .ring{fill:none;stroke:var(--paper);stroke-width:1}
""",
        "derivation": """
blocks      cloth 240x288 film field bleeding off top/bottom/right · cloth-light 96x96 · charcoal 80x48 (the cookie bar)
arrangement one tall film slab with a lighter fold, as the hero crops fabric
pattern     a literal motif: the water bead — three concentric circles, from "the revolution is circular"
scales      radius-circle, spacing space-2 (16)/space-3 (40)
""",
        "svg": """
<rect class="cl" x="240" y="0" width="240" height="288"/>
<rect class="cll" x="288" y="144" width="96" height="96"/>
<rect class="ch" x="40" y="216" width="80" height="48"/>
<circle class="ring" cx="160" cy="112" r="64"/>
<circle class="ring" cx="160" cy="112" r="44"/>
<circle class="ring" cx="160" cy="112" r="24"/>
""",
    },
}

# ---------------------------------------------------------------- Flowlife
flowlife = {
    "slug": "flowlife",
    "title": "Flowlife",
    "namespace": "Flowlife",
    "source": {"url": "https://www.flowlife.com/en-BG", "captured": CAPTURED},
    "fonts_href": GF + "family=IBM+Plex+Sans:wght@400&display=swap",
    "families": {"sans": "\"IBM Plex Sans\", Inter, Arial, sans-serif"},
    "colors": [
        tok("ink", "#111110", "Text, the announcement bar and filled buttons. 18.1:1 on `snow`."),
        tok("white", "#ffffff", "Text over photography and on `ink`."),
        tok("snow", "#fafafa", "Page ground."),
        tok("mist", "#f6f6f6", "Product tile ground."),
        tok("smoke", "rgba(48, 48, 48, 0.75)", "Translucent button ground over photos (\"Read more\") and the cookie card. `white` text on it over light photos is about 6:1."),
        tok("scrim", "rgba(60, 60, 60, 0.6)", "Photo overlays behind captions."),
        tok("sale", "#d82b00", "Price reductions and \"New\" flags. 4.7:1 on `snow`."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("headline", "19px", "24.7px", 400, "Product names and section heads.", sample="Pre-order. Flowlymph Roller Go"),
            style("body", "13px", "18.2px", 400, "Captions over photos and paragraphs.", ls="0.19px"),
            style("small", "12px", "16.8px", 400, "Category nav and footer."),
            style("label", "10px", "14px", 400, "Uppercase buttons, badges and the cookie heading.", ls="0.4px", sample="THIS WEBSITE USES COOKIES"),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Badge padding."),
        tok("space-2", "8px", "Button vertical padding."),
        tok("space-3", "16px", "Button horizontal padding; gutters."),
        tok("space-4", "32px", "Section padding."),
    ],
    "radius": [
        tok("radius-sm", "3px", "Inputs."),
        tok("radius-md", "4px", "Buttons, tiles and cards."),
        tok("radius-pill", "9999px", "Round icon buttons."),
    ],
    "readme": """
Flowlife makes recovery and performance products from Scandinavia: massage guns, vibration plates, rollers. The site is a black-and-white catalogue: monochrome athlete photography, tiny IBM Plex captions, translucent grey buttons and one red for prices. Built from the public site flowlife.com; IBM Plex Sans is the site's own face.

## Voice
- Product-first and plain: "Coming soon. Flowplate Vibe Pro", "Pre-order. Flowlymph Roller Go".
- Status word, full stop, product name.

## Colour
- Greyscale: `ink`, `white`, `snow`, `mist`, plus translucent `smoke` and `scrim` over photos.
- `sale` red only for prices and flags.

## Typography
- **IBM Plex Sans** 400 only. Labels uppercase, tracked 0.4px, at 10px; everything else sentence case.

## Layout
- Announcement bar in `ink` across the top ("CLICK HERE TO GET 15% OFF YOUR FIRST ORDER"), a centred wordmark with icon buttons, then split-screen product photography with a caption and a small button centred on each half.

## Components
`AnnouncementBar`, `PhotoCaption` and `Button`. No logo file ships; set FLOWLIFE in `headline` tracked wide.
""",
    "components": {
        "AnnouncementBar": {
            "group": "Navigation", "height": 60,
            "readme": """
The thin `ink` promo strip across the top of every page.

- Provide one offer line with a link.
- `label` style uppercase, `white` on `ink`, centred, underlined. Height 24px.
""",
            "css": """
body{margin:0;background:var(--snow)}
.a{background:var(--ink);color:var(--white);font:400 10px/24px var(--font-sans);letter-spacing:.4px;text-transform:uppercase;text-align:center}
.a a{color:var(--white)}
""",
            "html": "<div class=\"a\"><a href=\"#\">Click here to get 15% off your first order</a></div>",
        },
        "PhotoCaption": {
            "group": "Content", "height": 180,
            "readme": """
The caption + button pair centred over a product photo.

- Provide status, product name and a button label.
- Caption `body` in `white`; button `label` on `smoke`, `radius-md`. Sits on photography (shown on `scrim`).
""",
            "css": """
body{margin:0}
.p{background:var(--ink);height:180px;display:grid;place-content:center;text-align:center;gap:10px}
.c{color:var(--white);font:400 13px/18.2px var(--font-sans)}
.b{background:var(--smoke);color:var(--white);font:400 10px/14px var(--font-sans);letter-spacing:.4px;padding:6px 12px;border-radius:var(--radius-md);border:0;justify-self:center}
""",
            "html": "<div class=\"p\"><span class=\"c\">Coming soon. Flowplate Vibe Pro</span><button class=\"b\">Read more</button></div>",
        },
        "Button": {
            "group": "Actions", "height": 90,
            "readme": """
Small square-cornered buttons.

- Primary `ink` with `white` text; secondary 1px `ink` outline. `label` style, padding `space-2` × `space-3`, `radius-md`.
""",
            "css": """
body{background:var(--snow);padding:24px;display:flex;gap:8px}
.b{font:400 10px/14px var(--font-sans);letter-spacing:.4px;text-transform:uppercase;padding:8px 16px;border-radius:var(--radius-md);border:1px solid var(--ink);cursor:pointer}
.p{background:var(--ink);color:var(--white)}
.s{background:transparent;color:var(--ink)}
""",
            "html": "<button class=\"b p\">Allow all</button><button class=\"b s\">Customize</button>",
        },
    },
    "cover": {
        "ground": "snow", "ink": "ink", "muted": "ink", "body_font": "sans",
        "name_font": "sans", "name_size": 96, "name_ls": "4px", "name_lines": ["Flowlife"],
        "tagline": "Recovery and performance systems from Scandinavia.",
        "css": """
  .ink{fill:var(--ink)} .mi{fill:var(--mist)} .sm{fill:var(--smoke)} .sa{fill:var(--sale)}
  .t{rx:var(--radius-md)}
""",
        "derivation": """
blocks      ink 200x288 (left photo half) · mist 200x288 (right half) · smoke 80x24 button · sale 32x12 flag
arrangement split-screen halves, as the homepage pairs two product photos
pattern     tiles cut by radius-md: two small smoke buttons centred on each half
scales      gutters space-3 (16), radius-md 4
""",
        "svg": """
<rect class="ink" x="40" y="0" width="200" height="288"/>
<rect class="mi" x="240" y="0" width="240" height="288"/>
<rect class="sm t" x="100" y="160" width="80" height="24" rx="4"/>
<rect class="sm t" x="320" y="160" width="80" height="24" rx="4"/>
<rect class="sa t" x="432" y="24" width="32" height="12" rx="4"/>
""",
    },
}

# ---------------------------------------------------------------- bleibtgleich
bleibt = {
    "slug": "bleibtgleich",
    "title": "bleibtgleich",
    "namespace": "Bleibtgleich",
    "source": {"url": "https://bleibtgleich.dev/", "captured": CAPTURED},
    "fonts_href": GF + "family=Hanken+Grotesk:wght@500&display=swap",
    "families": {"sans": "\"Hanken Grotesk\", \"Akzidenz Grotesk Pro\", Arial, sans-serif"},
    "colors": [
        tok("white", "#ffffff", "Page ground."),
        tok("black", "#000000", "All text, the vertical rule and the Menu pill. 21:1 on `white`."),
        tok("mist", "#f2f2f2", "Project tiles and the faded \"bleibt / gleich\" corner words (decorative, 1.1:1)."),
        tok("wash", "rgba(0, 0, 0, 0.05)", "Hover fill and tile borders."),
        tok("signal", "#e04a3a", "Ring icons in the tile row. An addition sampled from the hero rings; decorative."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("display", "90px", "79.2px", 500, "Split hero words.", ls="-4.45507px", sample="the best ideas deserve execution."),
            style("body", "14px", "14.98px", 500, "Everything small: captions, menu, notes.", ls="-0.378px"),
        ]},
    ],
    "spacing": [
        tok("space-1", "8px", "Caption gaps."),
        tok("space-2", "16px", "Page margin."),
        tok("space-3", "32px", "Gap between tiles."),
        tok("space-4", "96px", "Between hero lines."),
    ],
    "radius": [
        tok("radius-sm", "8px", "Small tiles."),
        tok("radius-md", "16px", "Cards."),
        tok("radius-lg", "32px", "The Menu pill."),
        tok("radius-circle", "50%", "Ring icons and the avatar."),
    ],
    "readme": """
bleibtgleich is the portfolio of Maksym Bleibtgleich, a designer and developer in Kyiv ("Designs and builds websites, products, and digital systems with a focus on clarity, performance, and usability"). The hero splits a sentence across a vertical hairline: "the / best / ideas deserve / execution." Two words only, size and weight. Built from the public site bleibtgleich.dev; the typeface is an open substitute.

## Voice
- Lowercase, aphoristic: "the best ideas deserve execution."
- The name is a pun on German *bleibt gleich* ("stays the same"); the two halves sit in opposite corners.

## Colour
- `black` on `white`. `mist` for tiles and the giant corner words.

## Typography
- The site uses **Akzidenz Grotesk Pro** 500; this system substitutes **Hanken Grotesk** 500.
- Two sizes only: `display` (90px, tracked −0.05em) and `body` (14px).

## Layout
- A single 1px `black` vertical rule runs down the page centre-left; words sit on either side of it at different heights.
- A black `Menu` pill top-right.

## Components
`SplitHeadline`, `MenuPill` and `TileRow`.
""",
    "components": {
        "SplitHeadline": {
            "group": "Content", "height": 260,
            "readme": """
A sentence split around a vertical hairline.

- Provide the words and which side each sits.
- `display` (scaled for width), `black`; 1px `black` vertical rule.
""",
            "css": """
body{background:var(--white);color:var(--black);padding:16px}
.g{display:grid;grid-template-columns:1fr 1px 1.4fr;gap:16px;font:500 48px/42px var(--font-sans);letter-spacing:-2.4px}
.r{background:var(--black)}
.l{align-self:end;text-align:right}
""",
            "html": "<div class=\"g\"><div class=\"l\">the</div><div class=\"r\"></div><div>best<br>ideas deserve<br>execution.</div></div>",
        },
        "MenuPill": {
            "group": "Navigation", "height": 80,
            "readme": """
The small black Menu pill.

- `black` ground, `white` `body` text, `radius-lg`, padding 4px × 10px.
""",
            "css": """
body{background:var(--white);padding:24px}
button{background:var(--black);color:var(--white);font:500 12px/1 var(--font-sans);letter-spacing:-.3px;border:0;border-radius:var(--radius-lg);padding:5px 10px}
""",
            "html": "<button>Menu</button>",
        },
        "TileRow": {
            "group": "Content", "height": 140,
            "readme": """
Square `mist` tiles each holding a small ring icon.

- Provide 3–6 tiles. 72px squares, no radius, a 14px ring (1.5px stroke) centred; ring colour `black` or `signal`.
""",
            "css": """
body{background:var(--white);padding:24px;display:flex;gap:8px}
.t{width:72px;height:72px;background:var(--mist);display:grid;place-items:center}
.t i{width:14px;height:14px;border-radius:var(--radius-circle);border:1.5px solid var(--black)}
""",
            "html": "<div class=\"t\"><i></i></div><div class=\"t\"><i style=\"border-color:var(--signal)\"></i></div><div class=\"t\"><i></i></div><div class=\"t\"><i style=\"border-color:var(--signal)\"></i></div>",
        },
    },
    "cover": {
        "ground": "white", "ink": "black", "muted": "black", "body_font": "sans",
        "name_font": "sans", "name_size": 72, "name_weight": 500, "name_ls": "-3.6px", "name_lines": ["bleibtgleich"],
        "tagline": "the best ideas deserve execution.",
        "css": """
  .mi{fill:var(--mist)} .bk{fill:var(--black)}
  .ring{fill:none;stroke-width:2} .r1{stroke:var(--black)} .r2{stroke:var(--signal)}
""",
        "derivation": """
blocks      mist tiles 72x72 ×4 (the project row) · black 1px vertical rule full height
arrangement one hairline divides the box; tiles sit either side at different heights, like the split hero
pattern     ring icons (radius-circle) inside the tiles, two black, two signal
scales      gap space-1 (8), tile 72, rule 1px
""",
        "svg": """
<rect class="bk" x="160" y="0" width="1" height="288"/>
<rect class="mi" x="40" y="40" width="72" height="72"/>
<rect class="mi" x="200" y="120" width="72" height="72"/>
<rect class="mi" x="280" y="120" width="72" height="72"/>
<rect class="mi" x="360" y="200" width="72" height="72"/>
<circle class="ring r1" cx="76" cy="76" r="8"/>
<circle class="ring r2" cx="236" cy="156" r="8"/>
<circle class="ring r1" cx="316" cy="156" r="8"/>
<circle class="ring r2" cx="396" cy="236" r="8"/>
""",
    },
}

# ---------------------------------------------------------------- a-lign studio
align = {
    "slug": "a-lign-studio",
    "title": "a-lign studio",
    "namespace": "Align",
    "source": {"url": "https://www.a-lign.studio/", "captured": CAPTURED},
    "fonts_href": GF + "family=Geist:wght@400;500;600&display=swap",
    "families": {"sans": "\"Geist\", Arial, sans-serif"},
    "colors": [
        tok("paper", "#f7f7f7", "Page ground."),
        tok("graphite", "#4f4f4f", "All text. 7.6:1 on `paper`."),
        tok("night", "#1f1f1f", "Dark sections and the toolbar. `paper` text 15.4:1."),
        tok("coral", "#de7356", "The single accent: GET ALIGNED, CONTACT, the opening quote mark. `paper` text on it is 2.9:1 — the site's own pairing; set button labels 19px+ bold or use `night` text (5.3:1)."),
        tok("silver", "#d5d5d5", "Faded headline words and placeholder bars (decorative)."),
        tok("graphite-5", "rgba(79, 79, 79, 0.05)", "Panel fills."),
        tok("graphite-10", "rgba(79, 79, 79, 0.1)", "Hover fills."),
        tok("graphite-30", "rgba(79, 79, 79, 0.3)", "Dashed frame lines around images."),
    ],
    "type_groups": [
        {"name": "Sans", "family": "sans", "styles": [
            style("display-xl", "154.341px", "138.907px", 500, "Oversized words.", ls="-0.258571px"),
            style("display-lg", "95.6525px", "86.0872px", 500, "Section heads."),
            style("display", "63.7538px", "63.7538px", 500, "Hero headline and quotes.", sample="Websites that make sense"),
            style("display-strong", "63.7538px", "63.7538px", 600, "Emphasised words in the quote."),
            style("body", "15.971px", "20.7624px", 400, "Paragraphs."),
            style("ui", "15.971px", "19.1652px", 500, "Nav and UI text.", ls="-0.19428px"),
            style("label", "12px", "14.4px", 500, "Uppercase buttons and taglines.", sample="WE TAKE YOU FROM STRATEGY TO SUCCESS"),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Inside dashed frames."),
        tok("space-2", "8px", "Toolbar gaps."),
        tok("space-3", "16px", "Button padding."),
        tok("space-4", "48px", "Between frames."),
        tok("space-5", "120px", "Section padding."),
    ],
    "radius": [
        tok("radius-xs", "2px", "Buttons and toolbar keys."),
        tok("radius-sm", "4px", "Images."),
        tok("radius-md", "7.97104px", "Panels."),
        tok("radius-pill", "1440px", "Pill toggles."),
    ],
    "readme": """
a-lign studio designs and builds websites: "Websites that make sense." The site looks like a layout tool left on screen: images sit inside dashed selection frames, faded headline words step in like a staircase, and a little toolbar of keys (MENU, +, `<a>`, CONTACT) floats at the bottom. Built from the public site a-lign.studio; Geist is the site's own face.

## Voice
- Pragmatic and process-led: "People deserve better process. Better collaboration. Better results."
- Taglines in caps: "WE TAKE YOU FROM STRATEGY TO SUCCESS WITH EVERY STEP EARNING ITS PLACE".

## Colour
- `graphite` on `paper` (not black). `night` for dark sections. `coral` once per view.
- Dashed frames in `graphite-30`.

## Typography
- **Geist** 500 for display and UI, 400 for paragraphs, 600 for emphasis inside quotes.
- Display sizes are fluid; values here are the 1440px renders.

## Layout
- Content framed by dashed 1px boxes like selected layers. Small grey bars step down the margins as decoration.

## Components
`AlignButton`, `DashedFrame` and `Toolbar`.
""",
    "components": {
        "AlignButton": {
            "group": "Actions", "height": 110,
            "readme": """
The coral call-to-action inside a dashed selection frame.

- Provide the label. `coral` ground, `label` text in `night` (5.3:1), `radius-xs`, wrapped in a 1px dashed `graphite-30` frame with `space-1` padding.
""",
            "css": """
body{background:var(--paper);padding:24px}
.f{display:inline-block;border:1px dashed var(--graphite-30);padding:4px}
button{background:var(--coral);color:var(--night);font:500 12px/14.4px var(--font-sans);text-transform:uppercase;border:0;border-radius:var(--radius-xs);padding:8px 12px}
""",
            "html": "<span class=\"f\"><button>Get aligned</button></span>",
        },
        "DashedFrame": {
            "group": "Media", "height": 220,
            "readme": """
An image inside a dashed selection frame.

- Provide an image. 1px dashed `graphite-30` frame, `space-2` inset, image corners `radius-sm`.
""",
            "css": """
body{background:var(--paper);padding:24px}
.f{display:inline-block;border:1px dashed var(--graphite-30);padding:8px}
.i{width:180px;height:140px;background:var(--silver);border-radius:var(--radius-sm)}
""",
            "html": "<div class=\"f\"><div class=\"i\" role=\"img\" aria-label=\"Studio portrait\"></div></div>",
        },
        "Toolbar": {
            "group": "Navigation", "height": 90,
            "readme": """
The floating toolbar of keys.

- Provide 3–4 keys; the last is CONTACT in `coral`.
- Keys: `paper` ground, 1px `graphite-30` border, `radius-xs`, `label` text in `graphite`. Bar: `graphite-5` fill, `radius-md`.
""",
            "css": """
body{background:var(--paper);padding:24px}
.t{display:inline-flex;gap:8px;padding:8px;background:var(--graphite-5);border-radius:var(--radius-md)}
.k{font:500 12px/14.4px var(--font-sans);text-transform:uppercase;padding:6px 10px;background:var(--paper);color:var(--graphite);border:1px solid var(--graphite-30);border-radius:var(--radius-xs)}
.c{background:var(--coral);color:var(--night);border-color:var(--coral)}
""",
            "html": "<div class=\"t\"><span class=\"k\">Menu</span><span class=\"k\">+</span><span class=\"k\">&lt;a&gt;</span><span class=\"k c\">Contact</span></div>",
        },
    },
    "cover": {
        "ground": "paper", "ink": "graphite", "muted": "graphite", "body_font": "sans",
        "name_font": "sans", "name_size": 72, "name_weight": 500, "name_lines": ["a-lign", "studio"],
        "tagline": "Websites that make sense.",
        "css": """
  .ni{fill:var(--night)} .co{fill:var(--coral)} .si{fill:var(--silver)}
  .dash{fill:none;stroke:var(--graphite-30);stroke-dasharray:4 3}
  .k{rx:var(--radius-xs)}
""",
        "derivation": """
blocks      night 160x200 · silver 120x96 image · coral 72x24 button — graphite-led with one coral
arrangement images inside dashed selection frames, offset like layers on a canvas
pattern     stepped silver bars (the staircase of faded words), six bars at an 8px pitch, plus dashed frames
scales      frame inset space-1 (4)/space-2 (8), radius-xs 2
""",
        "svg": """
<rect class="ni" x="264" y="32" width="160" height="200"/>
<rect class="dash" x="256.5" y="24.5" width="175" height="215"/>
<rect class="si" x="72" y="120" width="120" height="96"/>
<rect class="dash" x="64.5" y="112.5" width="135" height="111"/>
<rect class="co k" x="96" y="248" width="72" height="24" rx="2"/>
<rect class="si" x="24" y="24" width="64" height="8"/><rect class="si" x="40" y="40" width="64" height="8"/><rect class="si" x="56" y="56" width="64" height="8"/>
<rect class="si" x="72" y="72" width="64" height="8"/><rect class="si" x="88" y="88" width="48" height="8"/>
""",
    },
}

# ---------------------------------------------------------------- Plnty
plnty = {
    "slug": "plnty",
    "title": "Plnty",
    "namespace": "Plnty",
    "source": {"url": "https://plnty.app/", "captured": CAPTURED},
    "fonts_href": GF + "family=Host+Grotesk:wght@500&family=Instrument+Sans:wght@400;500&display=swap",
    "families": {
        "display": "\"Host Grotesk\", \"Suisse Intl\", system-ui, sans-serif",
        "sans": "\"Instrument Sans\", \"Suisse Intl\", -apple-system, system-ui, sans-serif",
    },
    "colors": [
        tok("canvas", "#f8f8f8", "Page ground."),
        tok("stone", "#e6e5e1", "Cards and tool panels."),
        tok("sand", "#e6e3dc", "Secondary panels."),
        tok("ink", "#1a1a19", "Headlines and filled buttons. 16.4:1 on `canvas`."),
        tok("taupe", "#6c6962", "Body copy and nav. 5.2:1 on `canvas`, 4.3:1 on `stone` — keep body text off `stone` or move it to `ink`."),
        tok("pebble", "#cac7bf", "Logo strip greys and disabled text (decorative)."),
        tok("carbon", "#0d0d0d", "Dark showcase panels."),
        tok("lavender", "#a68aff", "Request Access pill and selection highlights. `ink` text 6.4:1."),
        tok("hot", "#de0001", "Showcase colour from generated art; one accent per section."),
    ],
    "type_groups": [
        {"name": "Display", "family": "display", "styles": [
            style("hero", "105px", "105px", 500, "Hero headline.", ls="-2px", sample="The agentic creative canvas"),
            style("display", "72px", "80px", 500, "Section heads."),
            style("display-sm", "65px", "71px", 500, "Sub-section heads."),
            style("title", "32px", "32px", 500, "Card titles."),
            style("tag", "12px", "16px", 500, "Display-face tags."),
        ]},
        {"name": "Text", "family": "sans", "styles": [
            style("body", "16px", "24px", 450, "Paragraphs.", ls="-0.16px"),
            style("ui", "11.3466px", "20px", 500, "Nav, buttons, tool names.", ls="-0.113466px", sample="Request Access ↗"),
            style("micro", "10px", "14px", 500, "Ticker and footnotes."),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Icon gaps."),
        tok("space-2", "8px", "Button padding."),
        tok("space-3", "16px", "Card padding."),
        tok("space-4", "40px", "Between sections inside a page."),
        tok("space-5", "120px", "Section padding."),
    ],
    "radius": [
        tok("radius-md", "16px", "Panels and media."),
        tok("radius-tool", "22.4638px", "Tool chips (video-restyler)."),
        tok("radius-lg", "24px", "Cards."),
        tok("radius-xl", "35px", "Large showcase panels."),
    ],
    "readme": """
Plnty is "the agentic creative canvas for professional creators": a suite of design tools spanning image, video, vector, 3D and audio. The site is a warm-grey canvas with large centred grotesk headlines, small UI text, rounded tool chips with thick outlines, and loud generated artwork in red and purple. Built from the public site plnty.app; fonts are open substitutes.

## Voice
- Product-confident: "A new class of creative tools." "Each one gives you a precise new way to find, develop or finish an idea."
- Tool names are lowercase-hyphenated: `video-restyler`, `time-machine`.

## Colour
- Greyscale warm chrome: `canvas`, `stone`, `sand`, `ink`, `taupe`.
- `lavender` marks the access pill; `hot` belongs to generated artwork.

## Typography
- The site uses **KMR Apparat** for display and **Suisse Intl** for text. Substitutes: **Host Grotesk** 500 and **Instrument Sans**.
- UI text is tiny (11.35px) and medium weight.

## Layout
- Centred hero, logo strip of client marks in `pebble`, then wide rounded panels (`radius-lg`, `radius-xl`).

## Components
`ButtonPair`, `ToolChip` and `FeatureCard`.
""",
    "components": {
        "ButtonPair": {
            "group": "Actions", "height": 90,
            "readme": """
Primary and secondary hero buttons.

- Primary: `ink` fill, `canvas` text with ↗. Secondary: 1px `ink` outline. `ui` style, `radius-tool`, padding `space-2` × 12px.
- Request Access in the nav uses `lavender` with `ink` text.
""",
            "css": """
body{background:var(--canvas);padding:24px;display:flex;gap:8px}
.b{font:500 11.35px/20px var(--font-sans);padding:4px 12px;border-radius:6px;border:1px solid var(--ink);cursor:pointer}
.p{background:var(--ink);color:var(--canvas)}
.s{background:var(--canvas);color:var(--ink)}
.l{background:var(--lavender);color:var(--ink);border-color:var(--lavender)}
""",
            "html": "<button class=\"b p\">Request Access ↗</button><button class=\"b s\">Book a Demo</button><button class=\"b l\">Request Access</button>",
        },
        "ToolChip": {
            "group": "Content", "height": 130,
            "readme": """
A chunky outlined chip naming a tool.

- Provide the tool name (lowercase-hyphenated).
- 3px `ink` border, `stone` fill, `radius-tool`, `title` style scaled to 20px.
""",
            "css": """
body{background:var(--canvas);padding:24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start}
.c{border:3px solid var(--ink);background:var(--stone);border-radius:12px;font:500 20px/1 var(--font-display);color:var(--ink);padding:8px 14px}
""",
            "html": "<span class=\"c\">video-restyler</span><span class=\"c\">time-machine</span>",
        },
        "FeatureCard": {
            "group": "Content", "height": 230,
            "readme": """
A rounded panel with headline, one line of copy and an explore link.

- `stone` ground, `radius-lg`, padding `space-3`; headline `title`, copy `body` in `ink`, link `ui`.
""",
            "css": """
body{background:var(--canvas);padding:24px}
.c{background:var(--stone);border-radius:var(--radius-lg);padding:20px;max-width:420px}
h3{font:500 28px/1 var(--font-display);color:var(--ink);margin:0 0 8px}
p{font:450 14px/20px var(--font-sans);color:var(--ink);margin:0 0 12px}
a{font:500 11.35px/20px var(--font-sans);color:var(--ink)}
""",
            "html": "<div class=\"c\"><h3>A new class of creative tools</h3><p>Plnty turns frontier models into purpose-built tools with creative intent built in.</p><a href=\"#\">Explore all tools ↗</a></div>",
        },
    },
    "cover": {
        "ground": "canvas", "ink": "ink", "muted": "taupe", "body_font": "sans",
        "name_font": "display", "name_size": 120, "name_weight": 500, "name_ls": "-2px", "name_lines": ["Plnty"],
        "tagline": "The agentic creative canvas for professional creators.",
        "css": """
  .st{fill:var(--stone)} .ca{fill:var(--carbon)} .ho{fill:var(--hot)} .la{fill:var(--lavender)}
  .chip{fill:var(--stone);stroke:var(--ink);stroke-width:3}
""",
        "derivation": """
blocks      stone 240x184 panel (radius-lg) · carbon 112x112 · hot 96x96 artwork tile · lavender 96x28 pill
arrangement one large rounded panel with a showcase tile breaking its corner, as the hero art sits on the canvas
pattern     outlined tool chips (radius-tool) — three, from the chunky video-restyler chips
scales      radius-lg 24, radius-tool ~22, gaps space-3 (16)
""",
        "svg": """
<rect class="st" x="32" y="48" width="280" height="200" rx="24"/>
<rect class="ca" x="296" y="24" width="152" height="152" rx="16"/>
<rect class="ho" x="336" y="120" width="104" height="104" rx="16"/>
<rect class="la" x="352" y="248" width="96" height="28" rx="14"/>
<rect class="chip" x="56" y="80" width="144" height="40" rx="20"/>
<rect class="chip" x="56" y="136" width="120" height="40" rx="20"/>
<rect class="chip" x="56" y="192" width="168" height="40" rx="20"/>
""",
    },
}

# ---------------------------------------------------------------- Child Appetite
childappetite = {
    "slug": "child-appetite",
    "title": "Child Appetite",
    "namespace": "ChildAppetite",
    "source": {"url": "https://childappetite.com/", "captured": CAPTURED},
    "fonts_href": GF + "family=Bayon&display=swap",
    "families": {
        "serif": "\"Times New Roman\", Times, serif",
        "display": "\"Bayon\", \"Arial Narrow\", sans-serif",
    },
    "colors": [
        tok("midnight", "#1f2840", "Page ground behind the contour lines."),
        tok("red", "#f73426", "Contour line colour and the menu card ground. `black` text on it is 5.5:1."),
        tok("yolk", "#f8f048", "Contour line colour. `black` text on it is 17.5:1."),
        tok("sky", "#60b8f8", "Contour line colour. `black` text on it is 9.7:1."),
        tok("white", "#ffffff", "Contour line colour and the SCROLL cue. 14.6:1 on `midnight`."),
        tok("black", "#000000", "Body text on the red card."),
    ],
    "type_groups": [
        {"name": "Serif", "family": "serif", "styles": [
            style("title", "32px", "38px", 700, "Page titles on the menu card.", sample="Child Appetite"),
            style("body", "16px", "20px", 400, "Body text."),
        ]},
        {"name": "Display", "family": "display", "styles": [
            style("cue", "14px", "16px", 400, "Spaced uppercase cues.", ls="2px", sample="SCROLL"),
        ]},
    ],
    "spacing": [
        tok("dash", "6px", "Dash length and gap of contour lines."),
        tok("space-2", "12px", "Line pitch between contours."),
        tok("space-3", "24px", "Margins."),
        tok("space-4", "48px", "Cue offset from the bottom."),
    ],
    "radius": [tok("radius-pill", "999px", "The scroll capsule and toggles.")],
    "readme": """
Child Appetite by Iris opens on a deep midnight field drawn with concentric dashed contour lines in red, yolk, sky and white, swirling into a four-lobed knot, with a tiny spaced SCROLL cue and a capsule toggle at the bottom. Built from the public site childappetite.com; Bayon is the site's own Google face and the serif is system Times.

## Colour
- `midnight` is the ground; contours cycle `red`, `yolk`, `sky`, `white` in that order.
- The red section uses `black` serif text.

## Typography
- System **Times New Roman** for words, **Bayon** spaced 2px for uppercase cues. Nothing else.

## Pattern
- Concentric dashed outlines of one shape, 6px dashes at a 12px pitch. Draw them, don't photograph them.

## Components
`ScrollCue`, `ContourField` and `MenuCard`.
""",
    "components": {
        "ScrollCue": {
            "group": "Navigation", "height": 140,
            "readme": """
The spaced SCROLL label over a white capsule with a dark knob.

- `cue` style in `white`; capsule 22×36 `white`, `radius-pill`, an 8px `midnight` knob.
""",
            "css": """
body{background:var(--midnight);padding:24px;display:grid;justify-items:center;gap:10px}
p{margin:0;font:400 14px/16px var(--font-display);letter-spacing:2px;color:var(--white)}
.c{width:22px;height:36px;background:var(--white);border-radius:var(--radius-pill);display:grid;justify-items:center;padding-top:7px;box-sizing:border-box}
.c i{width:8px;height:8px;border-radius:var(--radius-pill);background:var(--midnight)}
""",
            "html": "<p>SCROLL</p><div class=\"c\" aria-hidden=\"true\"><i></i></div>",
        },
        "ContourField": {
            "group": "Media", "height": 220,
            "readme": """
Concentric dashed outlines in the four line colours.

- Provide a base shape; repeat it outward at a `space-2` pitch, cycling `red`, `yolk`, `sky`, `white`, dashes `dash` long.
""",
            "css": """
body{background:var(--midnight);margin:0}
svg{display:block;width:100%;height:220px}
.l{fill:none;stroke-width:2;stroke-dasharray:6 6}
""",
            "html": "<svg viewBox=\"0 0 400 220\" aria-hidden=\"true\"><rect class=\"l\" style=\"stroke:var(--white)\" x=\"170\" y=\"80\" width=\"60\" height=\"60\" rx=\"30\"/><rect class=\"l\" style=\"stroke:var(--sky)\" x=\"158\" y=\"68\" width=\"84\" height=\"84\" rx=\"42\"/><rect class=\"l\" style=\"stroke:var(--yolk)\" x=\"146\" y=\"56\" width=\"108\" height=\"108\" rx=\"54\"/><rect class=\"l\" style=\"stroke:var(--red)\" x=\"134\" y=\"44\" width=\"132\" height=\"132\" rx=\"66\"/><rect class=\"l\" style=\"stroke:var(--white)\" x=\"122\" y=\"32\" width=\"156\" height=\"156\" rx=\"78\"/><rect class=\"l\" style=\"stroke:var(--sky)\" x=\"110\" y=\"20\" width=\"180\" height=\"180\" rx=\"90\"/></svg>",
        },
        "MenuCard": {
            "group": "Content", "height": 160,
            "readme": """
The red content card with serif text.

- `red` ground, `black` serif: `title` then `body`. Padding `space-3`.
""",
            "css": """
body{background:var(--red);color:var(--black);padding:24px}
h2{font:700 32px/38px var(--font-serif);margin:0 0 8px}
p{font:400 16px/20px var(--font-serif);margin:0}
""",
            "html": "<h2>Child Appetite</h2><p>by Iris</p>",
        },
    },
    "cover": {
        "ground": "midnight", "ink": "white", "muted": "white", "body_font": "serif",
        "name_font": "serif", "name_size": 80, "name_weight": 700, "name_lines": ["Child", "Appetite"],
        "tagline": "by Iris",
        "css": """
  .l{fill:none;stroke-width:2;stroke-dasharray:6 6}
  .r{stroke:var(--red)} .y{stroke:var(--yolk)} .s{stroke:var(--sky)} .w{stroke:var(--white)}
  .rf{fill:var(--red)}
""",
        "derivation": """
blocks      red 96x288 band bleeding off the right (the menu card) — the field is midnight, colour comes from the lines
arrangement concentric contours centred in the box, the red card cutting the right edge
pattern     the site's own contour lines: five dashed rounded squares at a space-2 (12) pitch cycling red/yolk/sky/white
scales      dash 6, pitch 12, radius-pill rounding
""",
        "svg": """
<rect class="rf" x="400" y="0" width="80" height="288"/>
<rect class="l w" x="164" y="108" width="72" height="72" rx="36"/>
<rect class="l s" x="140" y="84" width="120" height="120" rx="60"/>
<rect class="l y" x="116" y="60" width="168" height="168" rx="84"/>
<rect class="l r" x="92" y="36" width="216" height="216" rx="108"/>
<rect class="l w" x="68" y="12" width="264" height="264" rx="132"/>
""",
    },
}

SYSTEMS = [lookback, btay, system0, flowlife, bleibt, align, plnty, childappetite]
