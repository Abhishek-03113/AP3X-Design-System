from ds_lib import tok, style

CAPTURED = "2026-10-25"
GF = "https://fonts.googleapis.com/css2?"

# Provenance: resurf.so sits behind a bot challenge (CSS, JS, fonts and images return 429 to automated browsers), so there is
# no computed-style capture. This system is read from five full-width screenshots of the live site taken in the owner's own
# browser on 2026-10-25 (2000px wide). Colours are pixel-sampled; sizes are measured from cap heights and gaps, anchored to the
# 56rem container class seen in the page HTML (the card grid is 832px = 896px - 2x32px, so those shots are about 1:1).
# The App Store listing art is a secondary source for the earlier chip assets in effects/ and components/.
resurf = {
    "slug": "resurf",
    "title": "Resurf",
    "namespace": "Resurf",
    "note": "Read from owner-supplied screenshots of resurf.so (2026-10-25) with sampled colours and measured sizes; the site blocks automated browsers, so no computed styles were captured.",
    "source": {
        "url": "https://resurf.so/",
        "captured": CAPTURED,
        "method": "five full-width browser screenshots supplied by the owner; pixel sampling and cap-height measurement; page HTML for the 56rem container class",
    },
    "fonts_href": GF + "family=EB+Garamond:wght@400;500&family=Inter:wght@400;500;600&display=swap",
    "families": {
        "serif": "\"EB Garamond\", Garamond, \"Times New Roman\", serif",
        "sans": "\"Inter\", -apple-system, \"SF Pro Text\", system-ui, sans-serif",
    },
    "colors": [
        tok("ground", "#f8f8f8", "Page ground (sampled everywhere outside cards)."),
        tok("card", "#efefef", "Feature cards and the hero panel (sampled #efefef)."),
        tok("tile", "#f3f3f3", "Format tiles, the tour tab track and thumbnail wells (sampled #f3f3f3 / #f2f2f2)."),
        tok("paper", "#fffffd", "Active tab, floating mini-UI, round carousel buttons (sampled #fffffd)."),
        tok("ink", "#0f100d", "Headlines, first line of two-tone heads (sampled). 18.0:1 on `ground`."),
        tok("ink-button", "#181614", "Primary buttons: warm near-black (sampled #181614). `paper` text 18.0:1."),
        tok("ink-title", "#2b2b29", "Card titles and button labels on grey (sampled). 12.3:1 on `card`."),
        tok("ink-body", "#6c6d6a", "Hero paragraph and section subtext (sampled). 4.9:1 on `ground`, 4.5:1 on `card`."),
        tok("ink-nav", "#5a5a5a", "Nav links (sampled). 6.5:1 on `ground`."),
        tok("ink-muted", "#767676", "Card descriptions, microcopy and tagline (sampled). 4.3:1 on `ground`, 4.0:1 on `card`: below AA at 12px, the site's own pairing."),
        tok("ink-quiet", "#7f7f7f", "Footer links (sampled). 3.8:1 on `ground`: below AA, the site's own pairing; keep to non-essential links."),
        tok("ink-faint", "#939393", "Second line of two-tone headlines (sampled #939393). 2.9:1 on `ground`: just under 3:1 even at headline size; keep for the decorative second line."),
        tok("line", "#e5e6e3", "Hairlines (footer rule, segmented control edge; sampled #e5e6e3 / #ebebeb)."),
        tok("chip", "#dcdcdc", "Small tag chips and the Opt-in pill (sampled #dcdcdc). Pill text needs `ink-nav` or darker: #929292 on it is only 2.3:1."),
        tok("grey-button", "#eeeeee", "Secondary button fill (sampled #eeeeee)."),
        tok("blue", "#4078e8", "Selection ring on thumbnails and the send button in mini-UI (sampled #4078e8 / #4878d0). 4.1:1 on `paper`."),
        tok("orange", "#f07018", "Folder glyph in the Research chip (sampled). Graphic only."),
        tok("pink", "#d85090", "Feather glyph in the Writing chip (sampled). Graphic only."),
        tok("ph-red", "#f87068", "Product Hunt mark in the badge (sampled from a 24px glyph, so approximate)."),
    ],
    "type_groups": [
        {"name": "Serif", "family": "serif", "styles": [
            style("display", "40px", "44px", 500, "Hero and section headlines; cap height measured 25px.", ls="-0.02em", sample="A Personal Context Library"),
            style("display-soft", "40px", "44px", 500, "Second line of a two-tone headline, in `ink-faint`.", ls="-0.02em", sample="in files you own."),
        ]},
        {"name": "Sans", "family": "sans", "styles": [
            style("body", "14px", "21px", 400, "Hero paragraph and section subtext; lines measured 21px apart.", sample="Save notes, bookmarks, screenshots and PDFs in one local library."),
            style("ui", "13px", "20px", 500, "Nav links, buttons, tab labels."),
            style("card-title", "14px", "20px", 500, "Feature card titles."),
            style("small", "12px", "19px", 400, "Card descriptions, footer links, microcopy."),
            style("tiny", "11px", "14px", 500, "Pills and chips."),
        ]},
    ],
    "spacing": [
        tok("space-1", "8px", "Gap between cards (measured 7–8px) and button pair."),
        tok("space-2", "14px", "Card inner padding."),
        tok("space-3", "24px", "Nav link gap; footer link rhythm (24px line pitch)."),
        tok("space-4", "32px", "Page side padding inside the container."),
        tok("space-5", "896px", "Container max width (56rem, from the page HTML)."),
    ],
    "radius": [
        tok("radius-card", "14px", "Feature cards (read from corners, estimated)."),
        tok("radius-button", "8px", "Primary and secondary buttons (estimated)."),
        tok("radius-small", "6px", "Nav Get Resurf button (estimated)."),
        tok("radius-image", "12px", "Product screenshots (estimated)."),
        tok("radius-pill", "999px", "Tabs, pills, chips, carousel buttons."),
    ],
    "radius_note": "Radii are read by eye from corners at about 1:1; treat them as ±2px.",
    "shadow": [
        tok("shadow-float", "0 1px 2px rgba(0,0,0,.06), 0 6px 18px rgba(0,0,0,.07)", "Floating mini-UI inside feature cards. Estimated from soft shadows in the art."),
        tok("shadow-image", "0 24px 48px -12px rgba(0,0,0,.18)", "Under the large product screenshot; the sampled column fades from #cccfd9 to #f2f2f2 over about 50px."),
        tok("shadow-tab", "0 1px 2px rgba(0,0,0,.08)", "Active segmented tab. Estimated."),
    ],
    "readme": """
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
""",
    "components": {
        "NavBar": {
            "group": "Navigation", "height": 90,
            "readme": """
The top bar: logo mark left, links centred, one dark button right.

- Links `ui` style in `ink-nav`, 24px apart; Resources carries a small chevron.
- "Get Resurf" button: `ink-button` fill, `paper` text, `radius-small`, 12px type, chevron after the label (about 24px high).
- Behind the bar sits a white-to-`ground` fade (`effects/nav-soft-fade`); content scrolls under it without a hard edge.
- The mark is a small hexagonal cube glyph; this preview uses a neutral placeholder, not the real mark.
""",
            "css": """
body{background:var(--ground);margin:0;font-family:var(--font-sans)}
.n{position:relative;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:14px 20px}
.n::before{content:"";position:absolute;inset:0 0 -24px;z-index:-1;background:linear-gradient(#fff,rgba(248,248,248,0));pointer-events:none}
.m{width:18px;height:18px;border-radius:5px;background:var(--ink-button);display:block}
.l{display:flex;gap:24px;font:500 13px/20px var(--font-sans);color:var(--ink-nav)}
.b{justify-self:end;display:inline-flex;align-items:center;gap:4px;height:24px;padding:0 10px;border-radius:var(--radius-small);background:var(--ink-button);color:var(--paper);font:500 12px/1 var(--font-sans)}
""",
            "html": "<div class=\"n\"><i class=\"m\"></i><nav class=\"l\"><span>Story</span><span>Roadmap</span><span>Updates</span><span>Pricing</span><span>Resources ⌄</span></nav><span class=\"b\">Get Resurf ⌄</span></div>",
        },
        "HeroHeadline": {
            "group": "Content", "height": 300,
            "readme": """
The hero text block: a small badge, the two-tone serif headline, a two-line paragraph, then the button pair and a meta line.

- Badge: `paper` pill with a hairline, `tiny` type, a round `ph-red` mark, label "#1 Product of the Day" and an arrow.
- Headline: `display`, centred; second line `display-soft` in `ink-faint`.
- Paragraph: `body` in `ink-body`, two lines, max about 50ch.
- Meta line under the buttons: `small` in `ink-muted`, items separated by a centre dot.
""",
            "css": """
body{background:var(--ground);padding:24px 16px;text-align:center;font-family:var(--font-sans)}
.bd{display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px 0 5px;border-radius:var(--radius-pill);background:var(--paper);box-shadow:0 0 0 1px var(--line);font:500 11px/1 var(--font-sans);color:var(--ink-title)}
.bd i{width:14px;height:14px;border-radius:50%;background:var(--ph-red);display:inline-block}
h1{margin:20px 0 14px;font:500 40px/44px var(--font-serif);letter-spacing:-.02em;color:var(--ink)}
h1 span{color:var(--ink-faint)}
p{margin:0 auto 18px;max-width:46ch;font:400 14px/21px var(--font-sans);color:var(--ink-body)}
.r{display:flex;gap:8px;justify-content:center}
.a,.g{height:36px;padding:0 16px;border-radius:var(--radius-button);font:500 13px/36px var(--font-sans)}
.a{background:var(--ink-button);color:var(--paper)}.g{background:var(--grey-button);color:var(--ink-title)}
.mt{margin-top:14px;font:400 12px/19px var(--font-sans);color:var(--ink-muted)}
""",
            "html": "<span class=\"bd\"><i></i>#1 Product of the Day ↗</span><h1>A Personal Context Library<br><span>in files you own.</span></h1><p>Save notes, bookmarks, screenshots and PDFs in one local library. Find anything, then hand that context to your agents.</p><div class=\"r\"><span class=\"a\">Download for Mac</span><span class=\"g\">Buy a license · $39</span></div><div class=\"mt\">Mac, iPhone &amp; iPad · Chrome extension · MCP &amp; CLI for agents</div>",
        },
        "ButtonPair": {
            "group": "Actions", "height": 100,
            "readme": """
Primary and secondary buttons.

- Primary: `ink-button` fill, `paper` label, an Apple glyph before "Download for Mac", `radius-button`, 36px high, `ui` type.
- Secondary: `grey-button` fill, `ink-title` label, same size.
- Gap `space-1` (8px). No border, no shadow.
""",
            "css": """
body{background:var(--ground);padding:24px;display:flex;gap:8px;align-items:center;font-family:var(--font-sans)}
.a,.g{display:inline-flex;align-items:center;gap:7px;height:36px;padding:0 16px;border-radius:var(--radius-button);font:500 13px/1 var(--font-sans);cursor:pointer}
.a{background:var(--ink-button);color:var(--paper)}.g{background:var(--grey-button);color:var(--ink-title)}
""",
            "html": "<span class=\"a\">⌘ Download for Mac</span><span class=\"g\">Buy a license · $39</span>",
        },
        "FeatureCard": {
            "group": "Content", "height": 300,
            "readme": """
A flat grey card: an illustration well on top holding one small floating mini-UI, then title and description.

- Card: `card` fill, `radius-card`, 14px padding, about 270 × 260 in a three-column grid with `space-1` gaps. No border or shadow.
- Illustration well: about 170px tall, content centred, mini-UI in `paper` with `shadow-float`.
- Title `card-title` in `ink-title`; description `small` in `ink-muted` (4.0:1 on `card`: the site's own pairing).
- Optional "Opt-in" pill beside the title: `chip` fill, `tiny` type, `radius-pill`; use `ink-nav` text, not the site's lighter grey.
""",
            "css": """
body{background:var(--ground);padding:16px;display:grid;grid-template-columns:repeat(3,1fr);gap:8px;font-family:var(--font-sans)}
.c{background:var(--card);border-radius:var(--radius-card);padding:14px;display:flex;flex-direction:column;min-height:240px}
.w{height:150px;display:grid;place-items:center}
.k{display:flex;gap:6px}.k i{width:36px;height:36px;border-radius:9px;background:var(--paper);box-shadow:var(--shadow-float);display:grid;place-items:center;font:500 14px var(--font-sans);font-style:normal;color:var(--ink-title)}
.t{display:flex;align-items:center;gap:8px;margin-top:12px;font:500 14px/20px var(--font-sans);color:var(--ink-title)}
.o{height:18px;padding:0 7px;border-radius:var(--radius-pill);background:var(--chip);font:500 11px/18px var(--font-sans);color:var(--ink-nav)}
.d{margin:4px 0 0;font:400 12px/19px var(--font-sans);color:var(--ink-muted)}
.s{background:var(--paper);box-shadow:var(--shadow-float);border-radius:10px;padding:10px 12px;font:500 11px/16px var(--font-sans);color:var(--ink-title)}
.tg{display:flex;flex-wrap:wrap;gap:5px;justify-content:center;max-width:150px}.tg span{background:var(--chip);border-radius:var(--radius-pill);padding:2px 8px;font:500 11px/16px var(--font-sans);color:var(--ink-nav)}
""",
            "html": "<div class=\"c\"><div class=\"w\"><div class=\"k\"><i>⌘</i><i>⇧</i><i>C</i></div></div><div class=\"t\">Quick Capture</div><p class=\"d\">Save notes, links, and screenshots with a global shortcut on Mac.</p></div><div class=\"c\"><div class=\"w\"><div class=\"s\">Designing for AI agents in 2026</div></div><div class=\"t\">Inbox First</div><p class=\"d\">Save now, organize later.</p></div><div class=\"c\"><div class=\"w\"><div class=\"tg\"><span>Research</span><span>Writing</span><span>#ml</span><span>#ideas</span></div></div><div class=\"t\">Bring Your Own AI <span class=\"o\">Opt-in</span></div><p class=\"d\">Use your own AI key, or hand off saved context to agents.</p></div>",
        },
        "TourTabs": {
            "group": "Navigation", "height": 150,
            "readme": """
The product-tour switcher and its caption.

- Track: `tile` fill, hairline `line`, `radius-pill`, about 36px high, tabs padded 14px.
- Active tab: `paper` fill, `shadow-tab`, `ink` label; inactive labels `ink-body`-ish grey (`#6b6b6b`, 4.8:1 on the track). `ui` type.
- Caption under the screenshot: `body`, first word in `ink-title` medium weight, rest in `ink-body`.
- Related controls on the screenshot (not previewed): 52px round `paper` arrow buttons at the vertical middle of each side, and a white "Pause" pill bottom right. The thumbnail strip below uses 8px-radius thumbs with a 2px `blue` ring on the active one.
""",
            "css": """
body{background:var(--ground);padding:24px;text-align:center;font-family:var(--font-sans)}
.t{display:inline-flex;padding:4px;border-radius:var(--radius-pill);background:var(--tile);box-shadow:0 0 0 1px var(--line)}
.t span{height:28px;padding:0 14px;border-radius:var(--radius-pill);font:500 13px/28px var(--font-sans);color:#6b6b6b}
.t .a{background:var(--paper);box-shadow:var(--shadow-tab);color:var(--ink)}
.cap{margin-top:18px;font:400 14px/21px var(--font-sans);color:var(--ink-body)}.cap b{font-weight:500;color:var(--ink-title)}
""",
            "html": "<div class=\"t\"><span class=\"a\">Library</span><span>Inbox</span><span>View</span><span>Notes</span><span>Assistant</span></div><div class=\"cap\"><b>Library</b> Select an image and discover similar references across your library.</div>",
        },
        "FormatTiles": {
            "group": "Content", "height": 250,
            "readme": """
Two offset rows of small format tiles that fade out at both ends.

- Tile: `tile` fill, about 128 × 84, `radius-card` minus 4px, icon top-left in a mid grey, label bottom-left in `ui` / `ink-title`.
- Rows are offset horizontally by about half a tile and both are masked at the edges (`linear-gradient(90deg, transparent, #000 12%, #000 88%, transparent)`), so they read as a marquee. No speed was captured.
- Labels from the site: Images, Video, Tweets, GitHub, Articles, PDFs, Audio, YouTube, Code, Notes.
""",
            "css": """
body{background:var(--ground);padding:16px 0;font-family:var(--font-sans)}
.m{overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent)}
.r{display:flex;gap:8px;margin-bottom:8px;width:max-content}.r.o{margin-left:-64px}
.r div{width:128px;height:84px;border-radius:10px;background:var(--tile);padding:12px;display:flex;flex-direction:column;justify-content:space-between;font:500 12px/16px var(--font-sans);color:var(--ink-title)}
.r i{width:14px;height:14px;border-radius:4px;background:#8a8a88;display:block}
""",
            "html": "<div class=\"m\"><div class=\"r\"><div><i></i>Video</div><div><i></i>Tweets</div><div><i></i>GitHub</div><div><i></i>Articles</div><div><i></i>Images</div><div><i></i>PDFs</div><div><i></i>Audio</div></div><div class=\"r o\"><div><i></i>PDFs</div><div><i></i>Audio</div><div><i></i>YouTube</div><div><i></i>Code</div><div><i></i>Notes</div><div><i></i>Images</div><div><i></i>Video</div></div></div>",
        },
        "Footer": {
            "group": "Navigation", "height": 220,
            "readme": """
The page footer: hairline, brand block left, four link columns.

- Rule: 1px `line`. Brand: small mark plus "Resurf" in `card-title`, tagline `small` in `ink-muted`, max 28ch.
- Columns: Product, Compare, Learn, Company. Headings `small` at 500 in `ink-title`; links `small` in `ink-quiet` (3.8:1, the site's own pairing), 24px line pitch.
""",
            "css": """
body{background:var(--ground);padding:0 24px;font-family:var(--font-sans)}
.f{border-top:1px solid var(--line);padding-top:24px;display:grid;grid-template-columns:1.4fr repeat(4,1fr);gap:16px}
.b{font:500 14px/20px var(--font-sans);color:var(--ink-title)}.b p{margin:6px 0 0;max-width:28ch;font:400 12px/19px var(--font-sans);color:var(--ink-muted)}
h4{margin:0 0 8px;font:500 12px/19px var(--font-sans);color:var(--ink-title)}
a{display:block;font:400 12px/24px var(--font-sans);color:var(--ink-quiet)}
""",
            "html": "<div class=\"f\"><div class=\"b\">Resurf<p>A Personal Context Library. Local-first, on Mac, iPhone and iPad.</p></div><div><h4>Product</h4><a>Download for Mac</a><a>iPhone and iPad</a><a>Pricing</a></div><div><h4>Compare</h4><a>vs mymind</a><a>vs Raindrop.io</a><a>vs Eagle</a></div><div><h4>Learn</h4><a>Guides</a><a>FAQ</a><a>Blog</a></div><div><h4>Company</h4><a>Story</a><a>Support</a><a>Press kit</a></div></div>",
        },
    },
    "cover": {
        "ground": "ground", "ink": "ink", "muted": "ink-muted", "body_font": "sans",
        "name_font": "serif", "name_size": 64, "name_weight": 500, "name_ls": "-0.02em", "leading": 0.95,
        "name_lines": ["Resurf"],
        "tagline": "A personal context library.",
        "css": """
  .cd{fill:var(--card)} .tl{fill:var(--tile)} .pp{fill:var(--paper)} .bt{fill:var(--ink-button)} .ln{fill:var(--chip)}
""",
        "derivation": """
blocks      one grey feature card with a floating paper mini-UI, a dark button, two tag chips
arrangement card centred on the right, button and chips overlapping its lower edge
pattern     flat card (#efefef) + paper tile with soft shadow, as in the site's feature grid
scales      radius-card 14, radius-button 8, pill chips
""",
        "svg": """
<rect class="cd" x="96" y="40" width="288" height="208" rx="14"/>
<rect class="pp" x="148" y="76" width="184" height="64" rx="10"/>
<rect class="ln" x="164" y="92" width="112" height="8" rx="4"/><rect class="ln" x="164" y="110" width="76" height="8" rx="4"/>
<rect class="tl" x="130" y="168" width="64" height="22" rx="11"/><rect class="tl" x="202" y="168" width="52" height="22" rx="11"/>
<rect class="bt" x="262" y="204" width="104" height="28" rx="8"/>
""",
    },
}

SYSTEMS = [resurf]
