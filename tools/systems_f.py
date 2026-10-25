from ds_lib import tok, style

CAPTURED = "2026-10-25"
GF = "https://fonts.googleapis.com/css2?"

# ---------------------------------------------------------------- Decimals
decimals = {
    "slug": "decimals",
    "title": "Decimals",
    "note": "Created from the public site https://www.decimals.co/ (found via a1.gallery); styles measured with Playwright on 2026-10-25.",
    "namespace": "Decimals",
    "source": {"url": "https://www.decimals.co/", "captured": CAPTURED},
    "fonts_href": GF + "family=Geist:wght@400;500&family=Newsreader:opsz,wght@6..72,400;6..72,500&family=La+Belle+Aurore&display=swap",
    "families": {
        "serif": "\"Newsreader\", \"martina\", Georgia, serif",
        "sans": "\"Geist\", Arial, Helvetica, system-ui, sans-serif",
        "script": "\"La Belle Aurore\", cursive",
    },
    "colors": [
        tok("cream", "#ede8e1", "Page ground (`--ink-200`)."),
        tok("card", "#f3eee6", "Cards and testimonial panels (`--ink-100`)."),
        tok("paper", "#fffdf8", "Button text on `ink`, glass fills (`--ink-50`). 9.2:1 on `ink`."),
        tok("fog", "#e6e1da", "Hairline fills and quiet panels (`--ink-4`)."),
        tok("ink", "#4d4638", "Headlines, body and the filled button. 7.7:1 on `cream`, 8.1:1 on `card`."),
        tok("ink-deep", "#16130e", "Hover and pressed ink (`--ink-950`)."),
        tok("ink-muted", "#6e685d", "Secondary copy and nav. 4.5:1 on `cream`."),
        tok("ink-soft", "rgba(77, 70, 56, 0.58)", "Inactive nav and logo-strip captions as the site sets them. 2.8:1 on `cream` — keep for decoration; use `ink-muted` for content."),
        tok("blush", "#f4c9be", "Portrait backgrounds and the ambient glow (`--red-200`). `ink` text 6.2:1."),
        tok("rose", "#dda697", "Second ambient blob (sampled; `rgba(221,166,151)`)."),
        tok("pin-red", "#d94f3d", "Pins and error solid (`--red-500`). 3.4:1 on `cream` — graphic use only."),
        tok("success", "#438f31", "Success solid (`--green-500`)."),
    ],
    "type_groups": [
        {"name": "Serif", "family": "serif", "styles": [
            style("display", "56px", "64.4px", 500, "Hero headline.", ls="-2.238px", sample="Hire designers who care through scouts that can tell"),
            style("heading", "28px", "37.8px", 400, "Section and row headings.", ls="-0.84px"),
            style("heading-sm", "23px", "30px", 400, "Card headings.", ls="-0.5px"),
        ]},
        {"name": "Sans", "family": "sans", "styles": [
            style("lead", "18px", "27px", 400, "Hero subline.", ls="-0.14px"),
            style("body", "16px", "24px", 400, "Row paragraphs."),
            style("ui", "14px", "21px", 400, "Nav, buttons (500) and card copy.", ls="-0.14px"),
            style("caption", "13px", "19px", 400, "Quotes and attributions."),
        ]},
        {"name": "Script", "family": "script", "styles": [
            style("annotation", "26px", "1", 400, "The handwritten \"Hiring Manager\" tag on portraits.", sample="Hiring Manager"),
        ]},
    ],
    "spacing": [
        tok("space-1", "8px", "Nav item padding."),
        tok("space-2", "16px", "Button padding; ticker gap unit."),
        tok("space-3", "32px", "Page margin."),
        tok("space-4", "64px", "Between ticker logos."),
        tok("space-5", "96px", "Between sections."),
    ],
    "radius": [
        tok("radius-none", "0px", "Torn-edge cards and rows; the edge is the shape."),
        tok("radius-img", "8px", "Portrait panels."),
        tok("radius-pill", "999px", "Buttons."),
    ],
    "shadow": [
        tok("shadow-pill-ink", "0 0 0 1px rgba(18,18,18,.22), 0 1px 2px rgba(18,18,18,.13), 0 2px 8px rgba(18,18,18,.07), inset 0 0 0 1px rgba(255,255,255,.08), inset 0 1px 0 rgba(255,255,255,.16)", "Filled pill button: hairline ring, two soft drops, inner top light."),
        tok("shadow-pill-glass", "0 1px 2px rgba(18,18,18,.06), 0 2px 6px rgba(18,18,18,.04), inset 0 1px 0 rgba(255,255,255,.75)", "Glass pill button."),
    ],
    "readme": """
Decimals is "a scout network for hiring designers". The site is a warm paper world: cream ground, brown-black ink instead of black, tightly tracked serif headlines, tiny quiet sans, and soft pill buttons with real depth. Torn-paper cards, halftone photography and a handwritten annotation make recruiting feel crafted. A dotted globe arcs behind the hero, a logo ticker drifts under it, and two blush glows wander the page. Built from the public site decimals.co; fonts are open substitutes where the originals are licensed.

## Voice
- Plain, warm and slightly wry: "Hire designers who care through scouts that can tell." "Traditional recruiting stopped working."
- Sentence case everywhere; headings state a claim, not a label.

## Colour
- Everything is ink on cream: `ink` `#4d4638` for text and fills, `cream` for the ground, `card` and `paper` for lifted surfaces.
- `blush` and `rose` appear only as soft glows and portrait grounds; `pin-red` is a graphic accent.
- The site dims secondary text to 58% ink (`ink-soft`, 2.8:1); this system keeps that value but sets content in `ink-muted`.

## Typography
- Headlines use **martina** (licensed); substitute **Newsreader** 400–500 with tight tracking (-0.04em at display size, -0.03em at heading size).
- UI and body are **Geist** 400/500 at 14px with -0.14px tracking; the script tag is **La Belle Aurore**.

## Depth and motion
- Buttons are pills with a layered shadow stack (`shadow-pill-ink`, `shadow-pill-glass`); the glass variant adds `backdrop-filter: blur(10px)`.
- Press feedback is a multiply radial that follows the pointer (see `effects/cta-press-glow`).
- Hero content enters from `blur(12px)` at 30% opacity (`motions/hero-blur-reveal`); the logo strip is a 46s linear ticker under edge masks (`motions/logo-ticker`); two ambient blobs drift over 52s and 64s (`motions/ambient-drift`).
- Scroll (measured by stepping the page): the nav wordmark collapses into a monogram past about 55px (`motions/wordmark-collapse`); the four proof rows pin and recede under each other, scale 0.965, up 8px, blur 2px (`motions/stacking-sticky-cards`); the problem cards and closing CTA fade up 12px as they cross 95% of the viewport (`motions/scroll-fade-up`); the hero globe auto-rotates and leans toward the pointer (`effects/dot-globe`, a recreation). No scroll library is used, only CSS sticky, `IntersectionObserver` and scroll handlers.
- Easing is `cubic-bezier(0.22, 1, 0.36, 1)` for movement and plain `ease` for colour and opacity; durations are 0.15–0.34s. Reduced motion removes the ticker, drift, blur reveal, sticky recede, fade-ups and wordmark swap.

## Imagery
- No logos, portraits or illustrations were copied. Torn edges, halftone and cut-out portraits are described in the README of each component, not reproduced.

## Components
`PillButton`, `NavBar`, `TestimonialRow`, `LogoTicker` and `ProblemCard`.
""",
    "components": {
        "PillButton": {
            "group": "Actions", "height": 110,
            "subtitle": "Ink and glass pills",
            "readme": """
The primary and secondary call-to-action pills.

- Filled: `ink` fill, `paper` text, `shadow-pill-ink`, `radius-pill`, 36px high (48px large, 22px side padding), `ui` at 500.
- Glass: `paper` at 55%, 1px ink-25% border, `shadow-pill-glass`, `backdrop-filter: blur(10px)`, same size.
- Hover/press: `transform`, `box-shadow` and `filter` ease 0.15s on `cubic-bezier(0.22, 1, 0.36, 1)`; opacity 0.2s.
""",
            "css": """
body{background:var(--cream);padding:24px;display:flex;gap:12px;align-items:center;font-family:var(--font-sans)}
.b{height:36px;padding:0 16px;border-radius:var(--radius-pill);font:500 14px/1 var(--font-sans);letter-spacing:-.14px;cursor:pointer;transition:transform .15s cubic-bezier(.22,1,.36,1),box-shadow .15s cubic-bezier(.22,1,.36,1),filter .15s cubic-bezier(.22,1,.36,1)}
.f{background:var(--ink);color:var(--paper);border:1px solid var(--ink);box-shadow:var(--shadow-pill-ink)}
.g{background:rgba(255,253,248,.55) linear-gradient(rgba(255,255,255,.5),rgba(255,255,255,0));color:var(--ink);border:1px solid rgba(77,70,56,.25);box-shadow:var(--shadow-pill-glass);backdrop-filter:blur(10px)}
.lg{height:48px;padding:0 22px}
.b:active{transform:scale(.98);filter:brightness(.96)}
""",
            "html": "<button class=\"b f lg\">Get started</button><button class=\"b g lg\">How it works</button><button class=\"b f\">Get started</button><button class=\"b g\">Log in</button>",
        },
        "NavBar": {
            "group": "Navigation", "height": 90,
            "readme": """
A floating nav that dissolves into the page.

- Three zones: wordmark left, links centre (`ui`, `ink-soft`; hover to `ink` in 0.2s), pills right.
- Behind it a gradient `rgba(237,232,225,.78) → .55 → 0` with `backdrop-filter: blur(12px)`, masked top-to-transparent so no edge shows (`effects/edge-fade-mask`).
""",
            "css": """
body{background:var(--cream);margin:0;font-family:var(--font-sans)}
.n{position:relative;display:flex;align-items:center;justify-content:space-between;padding:20px 32px}
.n::before{content:"";position:absolute;inset:0 0 -36px;z-index:-1;background:linear-gradient(rgba(237,232,225,.78),rgba(237,232,225,.55) 55%,rgba(237,232,225,0));backdrop-filter:blur(12px);-webkit-mask-image:linear-gradient(#000 50%,transparent);mask-image:linear-gradient(#000 50%,transparent)}
.w{font:500 22px/1 var(--font-serif);letter-spacing:.12em;color:var(--ink)}
.l{display:flex;gap:20px;font:400 14px/21px var(--font-sans);letter-spacing:-.14px;color:var(--ink-soft)}
.l a{padding:12px 8px;transition:color .2s}.l a:hover{color:var(--ink)}
.p{display:flex;gap:8px}
.p span{height:36px;padding:0 16px;border-radius:999px;display:inline-flex;align-items:center;font:500 14px var(--font-sans);letter-spacing:-.14px}
.a{background:var(--ink);color:var(--paper);box-shadow:var(--shadow-pill-ink)}
.b{background:rgba(255,253,248,.55);color:var(--ink);border:1px solid rgba(77,70,56,.25);box-shadow:var(--shadow-pill-glass)}
""",
            "html": "<div class=\"n\"><span class=\"w\">DECIMALS</span><nav class=\"l\"><a>How it works</a><a>Placements</a><a>Become a Scout</a><a>Blog</a></nav><div class=\"p\"><span class=\"a\">Get started</span><span class=\"b\">Log in</span></div></div>",
        },
        "TestimonialRow": {
            "group": "Content", "height": 300,
            "readme": """
A two-column proof row: copy on a paper card, a portrait panel beside it. Rows alternate sides.

- Copy: company mark, `heading` title, `body` paragraph in `ink-muted`, then a `caption` quote and attribution pinned to the bottom.
- Card: `card` fill with a hand-torn edge (an irregular `clip-path` polygon); portrait panel `blush` with `radius-img`, black-and-white cut-out figure with a white stroke, `annotation` in the corner, image `mix-blend-mode: multiply`.
- Provide your own portrait; none is shipped.
""",
            "css": """
body{background:var(--cream);padding:24px;font-family:var(--font-sans)}
.r{display:grid;grid-template-columns:1fr 1fr;background:var(--card);min-height:230px}
.c{padding:24px 28px;display:flex;flex-direction:column;justify-content:space-between}
h3{margin:6px 0 8px;font:400 28px/37.8px var(--font-serif);letter-spacing:-.84px;color:var(--ink)}
p{margin:0;font:400 15px/22px var(--font-sans);color:var(--ink-muted);max-width:30ch}
.q{font:400 12px/17px var(--font-sans);color:var(--ink-muted)}
.q b{font-weight:500;color:var(--ink)}
.i{margin:6px;border-radius:var(--radius-img);background:linear-gradient(160deg,#fde3da,var(--blush));position:relative}
.i span{position:absolute;right:14px;bottom:12px;font:400 22px/1 var(--font-script);color:rgba(217,79,61,.55);transform:rotate(-8deg)}
""",
            "html": "<div class=\"r\"><div class=\"c\"><div><h3>Skip straight to the shortlist</h3><p>You'll get a curated handful worth meeting.</p></div><div class=\"q\">“Everyone you get is designer good.” <b>Lead Product Designer</b></div></div><div class=\"i\" role=\"img\" aria-label=\"Portrait panel placeholder\"><span>Hiring Manager</span></div></div>",
        },
        "LogoTicker": {
            "group": "Content", "height": 120,
            "readme": """
An endless strip of client marks.

- Track is `display:flex; width:max-content`, content duplicated once, animated `translateX(0 → -50%)` over 46s linear.
- Wrapper masks both ends: `linear-gradient(90deg, transparent, #000 10%, #000 90%, transparent)`.
- Marks sit at 64px gaps, tinted to `ink` at 92%; hovering the strip pauses it and dims every mark to 40%, the hovered mark returns to full.
- Reduced motion: no animation.
""",
            "css": """
body{background:var(--cream);padding:24px;font-family:var(--font-sans)}
.cap{text-align:center;font:400 14px/21px var(--font-sans);color:var(--ink-muted);margin:0 0 12px}
.t{overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent)}
.k{display:flex;align-items:center;width:max-content;animation:tick 46s linear infinite}
.t:hover .k{animation-play-state:paused}
.k span{margin-right:64px;font:500 22px/1 var(--font-serif);color:var(--ink);opacity:.92;transition:opacity .25s}
.k:hover span{opacity:.4}.k span:hover{opacity:1}
@keyframes tick{to{transform:translateX(-50%)}}
@media (prefers-reduced-motion:reduce){.k{animation:none}}
""",
            "html": "<p class=\"cap\">Hired by teams at</p><div class=\"t\"><div class=\"k\"><span>Northwind</span><span>Fieldnote</span><span>Orbital</span><span>Lumen</span><span>Parcel</span><span>Quill</span><span>Northwind</span><span>Fieldnote</span><span>Orbital</span><span>Lumen</span><span>Parcel</span><span>Quill</span></div></div>",
        },
        "ProblemCard": {
            "group": "Content", "height": 330,
            "readme": """
A three-up card for the problem section: halftone image on top, `heading-sm` title, `ui` copy in `ink-muted`.

- Card `card` fill with the same torn edge as `TestimonialRow`; image area is a sepia halftone collage (supply your own).
- Padding 20px; gap 8px.
""",
            "css": """
body{background:var(--cream);padding:24px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px;font-family:var(--font-sans)}
.c{background:var(--card);padding:6px 6px 20px}
.i{height:120px;background:repeating-radial-gradient(circle at 30% 40%,#6e685d 0 1px,#3a3428 1px 3px);opacity:.85;margin-bottom:14px}
h4{margin:0 14px 6px;font:400 19px/26px var(--font-serif);letter-spacing:-.4px;color:var(--ink)}
p{margin:0 14px;font:400 14px/21px var(--font-sans);color:var(--ink-muted)}
""",
            "html": "<div class=\"c\"><div class=\"i\" role=\"img\" aria-label=\"Halftone placeholder\"></div><h4>Inbound applications overwhelm</h4><p>Up to a thousand applicants per role, maybe five worth talking to.</p></div><div class=\"c\"><div class=\"i\" role=\"img\" aria-label=\"Halftone placeholder\"></div><h4>Hiring becomes a second job</h4><p>Reviewing applications eats the time you should spend on product.</p></div><div class=\"c\"><div class=\"i\" role=\"img\" aria-label=\"Halftone placeholder\"></div><h4>The bar keeps rising</h4><p>The gap between good and great is getting wider.</p></div>",
        },
    },
    "cover": {
        "ground": "cream", "ink": "ink", "muted": "ink-muted", "body_font": "sans",
        "name_font": "serif", "name_size": 64, "name_weight": 500, "name_ls": "-0.04em", "leading": 0.95,
        "name_lines": ["Decimals"],
        "tagline": "A scout network for hiring designers.",
        "css": """
  .ln{fill:none;stroke:var(--ink);stroke-opacity:.28;stroke-width:1}
  .dt{fill:var(--ink)} .gl{fill:var(--blush)}
""",
        "derivation": """
blocks      blush glow disc, dotted globe arc with meridians, ink dots
arrangement half-sphere rising from the bottom edge, as the site's hero globe does
pattern     meridian ellipses + latitude arcs → dots scattered denser on the right limb
scales      hairline 1px at 28% ink; dot radius 1.5
""",
        "svg": """
<circle class="gl" cx="360" cy="300" r="190" opacity=".55"/>
<circle class="ln" cx="360" cy="300" r="170"/>
<ellipse class="ln" cx="360" cy="300" rx="120" ry="170"/>
<ellipse class="ln" cx="360" cy="300" rx="60" ry="170"/>
<path class="ln" d="M190 300 H530"/>
<path class="ln" d="M205 240 Q360 215 515 240"/>
<path class="ln" d="M240 185 Q360 165 480 185"/>
<circle class="dt" cx="262" cy="196" r="1.5"/><circle class="dt" cx="298" cy="168" r="1.5"/><circle class="dt" cx="330" cy="204" r="1.5"/>
<circle class="dt" cx="372" cy="152" r="1.5"/><circle class="dt" cx="410" cy="186" r="1.5"/><circle class="dt" cx="440" cy="158" r="1.5"/>
<circle class="dt" cx="468" cy="190" r="1.5"/><circle class="dt" cx="486" cy="214" r="1.5"/><circle class="dt" cx="452" cy="232" r="1.5"/>
<circle class="dt" cx="318" cy="248" r="1.5"/><circle class="dt" cx="396" cy="244" r="1.5"/><circle class="dt" cx="500" cy="248" r="1.5"/>
""",
    },
}

SYSTEMS = [decimals]
