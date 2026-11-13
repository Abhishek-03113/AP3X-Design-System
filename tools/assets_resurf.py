"""Individual assets for Resurf. Two sources: (1) five owner-supplied screenshots of resurf.so (site assets, SRC_SITE) and
(2) the public App Store listing art (store-art assets, SRC). resurf.so serves its CSS, JS, fonts and images behind a bot
challenge, so nothing is a computed style and no motion timings were captured."""

SRC = {"name": "Resurf (App Store art)", "url": "https://apps.apple.com/us/app/resurf-save-organize/id6782162097", "captured": "2026-10-25",
       "designSystem": "design-systems/resurf",
       "method": "pixel sampling and visual reading of public App Store images; resurf.so was blocked by a bot challenge"}
FONTS = "https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700&display=swap"
VARS = ("--cream:#f3f3f3;--ground:#f3f3f3;--paper:#ffffff;--ink:#000000;--ink-soft:#727272;--amber:#d89024;--ember:#fc480c;--azure:#0c78fc;--violet:#b46cd8;--leaf:#30a818;"
        "--amber-text:#a86a00;--ember-text:#d63a05;--violet-text:#8f3fc0;--leaf-text:#1f7d0e;"
        "--font-sans:'Inter',-apple-system,'SF Pro Text',system-ui,sans-serif;--shadow-chip:0 1px 2px rgba(0,0,0,.10),0 6px 18px rgba(0,0,0,.10)")
NOTE = ("Provenance: read from the public App Store art, not from resurf.so's CSS (blocked by a bot challenge). Colours are pixel-sampled "
        "(about ±6 per channel); sizes, angles and shadows are estimated by eye and marked *estimated*. No timings exist because no motion was captured.")


def meta(kind, slug, title, summary, tags, tech):
    return {"slug": slug, "kind": kind, "title": title, "summary": summary, "source": SRC, "tags": tags, "tech": tech}


def asset(m, readme, css, html, script=None):
    return {"meta": m, "fonts": FONTS, "vars": VARS, "readme": readme, "css": css, "html": html, "script": script}


ASSETS = []

ASSETS.append(asset(
    meta("effect", "fade-to-ground-mask", "Fade to ground mask", "Device mockups dissolve into the page along their lower edge instead of sitting in a frame.",
         ["mask", "gradient", "device", "hero"], ["css mask-image"]),
    f"""
# Fade to ground mask

{NOTE}

In the store art every phone, tablet and laptop mockup is cut off by the artboard and fades into the background, so the product feels like it floats up out of the page.

```css
.device {{
  -webkit-mask-image: linear-gradient(#000 45%, transparent 92%);
          mask-image: linear-gradient(#000 45%, transparent 92%);
}}
```

The 45% / 92% stops are *estimated*. Match the page ground behind it (`#f3f3f3` to `#ffffff`); if the ground is a gradient, use a mask, not an overlay, so shadows and blur fade too.
""",
    """
.stage{height:300px;border-radius:12px;background:linear-gradient(var(--ground),var(--paper));display:flex;justify-content:center;padding-top:24px;overflow:hidden}
.d{width:260px;height:300px;border:6px solid #1c1c1e;border-bottom:0;border-radius:28px 28px 0 0;background:var(--paper);-webkit-mask-image:linear-gradient(#000 45%,transparent 92%);mask-image:linear-gradient(#000 45%,transparent 92%);display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:16px}
.d i{border-radius:8px;background:#e4e4e8;height:62px;display:block}
.d i:nth-child(3n){background:#f0d9c4}.d i:nth-child(4n){background:#d6e4f5}
""",
    '<div class="stage"><div class="d" role="img" aria-label="Device mockup placeholder"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>'))

ASSETS.append(asset(
    meta("effect", "tilted-chip-lift", "Tilted chip lift", "White pill chips rotated by different small angles with a soft diffuse shadow, scattered around a device.",
         ["chips", "shadow", "rotation", "scatter"], ["css transform", "css box-shadow"]),
    f"""
# Tilted chip lift

{NOTE}

The scattered-chip look: each chip is a white pill with a glyph and label, rotated a different amount (about -8° to +6°, *estimated*), lifted by a soft shadow and placed so it overlaps a device edge.

```css
.chip {{
  display:inline-flex; align-items:center; gap:6px; height:44px; padding:0 18px;
  border-radius:999px; background:#fff;
  box-shadow:0 1px 2px rgba(0,0,0,.10), 0 6px 18px rgba(0,0,0,.10);   /* estimated */
  font:600 20px/1 Inter, system-ui; letter-spacing:-.01em;
}}
.chip:nth-child(1) {{ transform:rotate(-6deg) }}
.chip:nth-child(2) {{ transform:rotate(4deg) }}
```

Never rotate a row by the same angle; vary both sign and size. No motion was observed, so the preview is static.
""",
    """
.stage{position:relative;height:300px;border-radius:12px;background:linear-gradient(var(--ground),var(--paper));overflow:hidden}
.d{position:absolute;left:50%;bottom:-40px;width:220px;height:250px;margin-left:-110px;border:6px solid #1c1c1e;border-radius:28px;background:#fff;opacity:.8}
.c{position:absolute;display:inline-flex;align-items:center;gap:6px;height:44px;padding:0 18px;border-radius:999px;background:#fff;box-shadow:var(--shadow-chip);font:600 20px/1 var(--font-sans);letter-spacing:-.01em}
.g{width:20px;height:20px;border-radius:6px;display:inline-block}
""",
    '<div class="stage"><div class="d"></div><span class="c" style="left:8%;top:18%;transform:rotate(-6deg)"><i class="g" style="background:var(--amber)"></i>Inspirations</span><span class="c" style="right:8%;top:10%;transform:rotate(5deg);color:var(--ember-text)"><i class="g" style="background:var(--ember)"></i>Research</span><span class="c" style="right:12%;top:52%;transform:rotate(-3deg);color:var(--violet-text)"><i class="g" style="background:var(--violet)"></i>Ideas</span><span class="c" style="left:10%;top:66%;transform:rotate(4deg);color:var(--leaf-text)"><i class="g" style="background:var(--leaf)"></i>Projects</span></div>'))

ASSETS.append(asset(
    meta("component", "resurf-tag-chip", "Tag chip", "Colour-coded content-type chip (Notes, Voice notes, Links, Screenshots, Videos) with glyph and label.",
         ["chip", "tag", "pill", "content-type"], ["css"]),
    f"""
# Tag chip

{NOTE}

| Type | Glyph colour (sampled) | Label colour (accessible, derived) |
| --- | --- | --- |
| Notes, PDFs | `#d89024` | `#a86a00` |
| Voice notes | `#fc480c` | `#d63a05` |
| Links | `#b46cd8` | `#8f3fc0` |
| Screenshots | `#0c78fc` | `#0c78fc` (4.1:1) |
| Videos | `#30a818` | `#1f7d0e` |
| Images, Meetings, Memos, Lectures | `#000000` | `#000000` |

Sampled accents are 2.6–4.1:1 on white, so they work for glyphs but not label text; use the derived column for labels. Height about 2× label size, side padding 18px (*estimated*).
""",
    """
.row{display:flex;flex-wrap:wrap;gap:14px 16px;padding:24px;border-radius:12px;background:linear-gradient(var(--ground),var(--paper))}
.c{display:inline-flex;align-items:center;gap:6px;height:44px;padding:0 18px;border-radius:999px;background:#fff;box-shadow:var(--shadow-chip);font:600 20px/1 var(--font-sans);letter-spacing:-.01em;color:var(--ink)}
.g{width:20px;height:20px;border-radius:6px;display:inline-block}
""",
    '<div class="row"><span class="c" style="color:var(--amber-text)"><i class="g" style="background:var(--amber)"></i>Notes</span><span class="c" style="color:var(--ember-text)"><i class="g" style="background:var(--ember)"></i>Voice notes</span><span class="c" style="color:var(--violet-text)"><i class="g" style="background:var(--violet)"></i>Links</span><span class="c" style="color:var(--azure)"><i class="g" style="background:var(--azure)"></i>Screenshots</span><span class="c"><i class="g" style="background:var(--ink)"></i>Images</span><span class="c" style="color:var(--leaf-text)"><i class="g" style="background:var(--leaf)"></i>Videos</span></div>'))

ASSETS.append(asset(
    meta("component", "resurf-status-pill", "Status pill", "Small reassurance pills: Local first, No account needed, Synced with iCloud, or your own AI key.",
         ["pill", "badge", "trust"], ["css"]),
    f"""
# Status pill

{NOTE}

Outline-free white pills (hairline ring at 12% ink) for plain facts, and filled pills for the two emphasised ones: `#fc480c` "Synced with iCloud" and `#0c78fc` "or your own AI key" (white label; 4.1:1, keep at 15px semibold or larger). Height 34px, padding 14px, 15px/600 (*estimated*).
""",
    """
.row{display:flex;gap:10px;flex-wrap:wrap;padding:24px;border-radius:12px;background:var(--ground)}
.p{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 14px;border-radius:999px;font:600 15px/1 var(--font-sans);letter-spacing:-.01em}
.l{background:#fff;color:var(--ink);box-shadow:0 0 0 1px rgba(0,0,0,.12)}.e{background:var(--ember);color:#fff}.a{background:var(--azure);color:#fff}
.d{width:14px;height:14px;border-radius:50%;background:currentColor;display:inline-block}
""",
    '<div class="row"><span class="p l"><i class="d"></i>Local first</span><span class="p l"><i class="d"></i>No account needed</span><span class="p e"><i class="d"></i>Synced with iCloud</span><span class="p a">or your own AI key</span></div>'))


# ------------------------------------------------------------------ assets from the owner-supplied resurf.so screenshots
SRC_SITE = {"name": "resurf.so (screenshots)", "url": "https://resurf.so/", "captured": "2026-10-25", "designSystem": "design-systems/resurf",
            "method": "five full-width browser screenshots supplied by the owner; pixel sampling and cap-height measurement at about 1:1 scale"}
VARS_SITE = ("--cream:#f8f8f8;--ground:#f8f8f8;--card:#efefef;--tile:#f3f3f3;--paper:#fffffd;--ink:#0f100d;--ink-button:#181614;--ink-title:#2b2b29;--ink-body:#6c6d6a;"
             "--ink-nav:#5a5a5a;--ink-muted:#767676;--ink-quiet:#7f7f7f;--ink-faint:#939393;--line:#e5e6e3;--chip:#dcdcdc;--grey-button:#eeeeee;--blue:#4078e8;"
             "--font-serif:'EB Garamond',Garamond,serif;--font-sans:'Inter',-apple-system,system-ui,sans-serif;"
             "--shadow-float:0 1px 2px rgba(0,0,0,.06),0 6px 18px rgba(0,0,0,.07);--shadow-tab:0 1px 2px rgba(0,0,0,.08)")
FONTS_SITE = "https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500&family=Inter:wght@400;500;600&display=swap"
NOTE_SITE = ("Provenance: read from five screenshots of resurf.so taken in the owner's browser on 2026-10-25 (the site blocks automated browsers). "
             "Colours are pixel-sampled; sizes are measured at about 1:1 (anchored to the 56rem container), good to ±1–2px; radii and shadows are *estimated*. "
             "Typefaces could not be confirmed (Garamond-like serif, Inter-like sans). No motion timings exist: motion is inferred from UI states only.")


def meta_site(kind, slug, title, summary, tags, tech):
    return {"slug": slug, "kind": kind, "title": title, "summary": summary, "source": SRC_SITE, "tags": tags, "tech": tech}


def asset_site(m, readme, css, html, script=None):
    return {"meta": m, "fonts": FONTS_SITE, "vars": VARS_SITE, "readme": readme, "css": css, "html": html, "script": script}


ASSETS.append(asset_site(
    meta_site("effect", "nav-soft-fade", "Nav soft fade", "A white-to-ground gradient under the sticky nav so scrolled content slides beneath it with no hard edge.",
              ["nav", "gradient", "sticky", "fade"], ["css gradient"]),
    f"""
# Nav soft fade

{NOTE_SITE}

When content scrolls under the nav it dissolves into a soft white band instead of meeting a border. In the screenshots the column under the nav steps `#fdfdfd` → `#fcfbfc` → `#fafafa` → `#f9f9f9` → ground (`#f8f8f8`) over about 50px.

```css
.nav::before {{
  content:""; position:absolute; inset:0 0 -24px; z-index:-1; pointer-events:none;
  background:linear-gradient(#fff, rgba(248,248,248,0));   /* fade length estimated from the sampled column */
}}
```

Whether the site also blurs what is underneath could not be determined from stills; add `backdrop-filter` only if you want it.
""",
    """
.stage{height:280px;overflow:auto;border-radius:12px;background:var(--ground);position:relative}
.nav{position:sticky;top:0;z-index:2;display:flex;gap:24px;padding:14px 24px;font:500 13px var(--font-sans);color:var(--ink-nav)}
.nav::before{content:"";position:absolute;inset:0 0 -24px;z-index:-1;pointer-events:none;background:linear-gradient(#fff,rgba(248,248,248,0))}
.blk{height:88px;margin:14px 24px;border-radius:14px;background:var(--card)}
""",
    '<div class="stage"><div class="nav"><span>Story</span><span>Roadmap</span><span>Updates</span><span>Pricing</span></div><div class="blk"></div><div class="blk"></div><div class="blk"></div><div class="blk"></div></div><p>Scroll inside the frame.</p>'))

ASSETS.append(asset_site(
    meta_site("component", "resurf-feature-card", "Feature card", "Flat grey card with a centred floating mini-UI above a medium title and one-line description; optional Opt-in pill.",
              ["card", "feature", "grid", "grey"], ["css"]),
    f"""
# Feature card

{NOTE_SITE}

| Part | Value |
| --- | --- |
| Card | `#efefef`, about 272 × 262, radius about 14px, padding 14px; grid of three with 8px gaps inside a 896px container |
| Illustration well | about 170px tall, content centred; mini-UI in `#fffffd` with a soft shadow |
| Title | 14px/20px, weight 500, `#2b2b29` |
| Description | 12px/19px, `#767676` (4.0:1 on the card, the site's own pairing) |
| Opt-in pill | `#dcdcdc` fill, 11px/500, fully round; use `#5a5a5a` text (the site's lighter grey is 2.3:1) |

Titles seen: Quick Capture, Inbox First, Spaces & Tags, Visual bookmark library, From Any App, Search your saved content, Voice Memos, Highlight & Annotate, AI Summaries (Opt-in), Bring Your Own AI (Opt-in), Ask Your Library (Opt-in), Fully local.
""",
    """
.g{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;max-width:896px}
.c{background:var(--card);border-radius:14px;padding:14px;min-height:240px}
.w{height:150px;display:grid;place-items:center}
.k{display:flex;gap:6px}.k i{width:36px;height:36px;border-radius:9px;background:var(--paper);box-shadow:var(--shadow-float);display:grid;place-items:center;font:500 14px var(--font-sans);font-style:normal;color:var(--ink-title)}
.s{background:var(--paper);box-shadow:var(--shadow-float);border-radius:10px;padding:10px 12px;font:500 11px/16px var(--font-sans);color:var(--ink-title)}
.tg{display:flex;flex-wrap:wrap;gap:5px;justify-content:center;max-width:150px}.tg span{background:var(--chip);border-radius:999px;padding:2px 8px;font:500 11px/16px var(--font-sans);color:var(--ink-nav)}
.t{display:flex;align-items:center;gap:8px;margin-top:12px;font:500 14px/20px var(--font-sans);color:var(--ink-title)}
.o{height:18px;padding:0 7px;border-radius:999px;background:var(--chip);font:500 11px/18px var(--font-sans);color:var(--ink-nav)}
.d{margin:4px 0 0;font:400 12px/19px var(--font-sans);color:var(--ink-muted)}
""",
    '<div class="g"><div class="c"><div class="w"><div class="k"><i>⌘</i><i>⇧</i><i>C</i></div></div><div class="t">Quick Capture</div><p class="d">Save notes, links, and screenshots with a global shortcut on Mac.</p></div><div class="c"><div class="w"><div class="s">Designing for AI agents in 2026</div></div><div class="t">Inbox First</div><p class="d">Save now, organize later.</p></div><div class="c"><div class="w"><div class="tg"><span>Research</span><span>Writing</span><span>#ml</span><span>#ideas</span></div></div><div class="t">Bring Your Own AI <span class="o">Opt-in</span></div><p class="d">Use your own AI key, or hand off saved context to agents.</p></div></div>'))

ASSETS.append(asset_site(
    meta_site("component", "resurf-tour-tabs", "Tour tabs", "Pill segmented control that switches the product tour, with caption and thumbnail strip.",
              ["tabs", "segmented", "carousel", "tour"], ["css", "js"]),
    f"""
# Tour tabs

{NOTE_SITE}

Five tabs (Library, Inbox, View, Notes, Assistant) in a track of `#f3f3f3` with a hairline, fully round, 36px high. The active tab is `#fffffd` with a faint shadow and `#0f100d` label; inactive labels are about `#6b6b6b`. The caption below has a medium-weight first word (`#2b2b29`) then `#6c6d6a`.

Around the large screenshot (not previewed, supply your own image): two 52px round white arrow buttons at mid-height on each side, a white "Pause" pill bottom right (the tour auto-advances), and a thumbnail strip of six thumbs (radius about 8px) where the active one carries a 2px `#4878d0` ring. Auto-advance timing was not captured.
""",
    """
.t{display:inline-flex;padding:4px;border-radius:999px;background:var(--tile);box-shadow:0 0 0 1px var(--line)}
.t button{height:28px;padding:0 14px;border:0;border-radius:999px;background:none;font:500 13px/28px var(--font-sans);color:#6b6b6b;cursor:pointer}
.t button.on{background:var(--paper);box-shadow:var(--shadow-tab);color:var(--ink)}
.cap{margin-top:18px;font:400 14px/21px var(--font-sans);color:var(--ink-body)}.cap b{font-weight:500;color:var(--ink-title)}
.th{display:flex;gap:8px;margin-top:18px}.th i{width:96px;height:58px;border-radius:8px;background:var(--card);display:block}.th i.on{box-shadow:0 0 0 2px var(--blue)}
""",
    '<div class="t" id="t"><button class="on">Library</button><button>Inbox</button><button>View</button><button>Notes</button><button>Assistant</button></div><div class="cap" id="c"><b>Library</b> Select an image and discover similar references across your library.</div><div class="th" id="h"><i class="on"></i><i></i><i></i><i></i><i></i><i></i></div>',
    """
const caps = { Library: 'Select an image and discover similar references across your library.', Inbox: 'Save now, sort later.', View: 'Read saved articles and PDFs in place.', Notes: 'A real editor, saved as Markdown.', Assistant: 'Ask about anything you have saved.' };
const tabs = [...document.querySelectorAll('#t button')], c = document.getElementById('c'), th = [...document.querySelectorAll('#h i')];
tabs.forEach((b, i) => b.addEventListener('click', () => {
  tabs.forEach(x => x.classList.toggle('on', x === b));
  th.forEach((x, j) => x.classList.toggle('on', j === i));
  c.innerHTML = '<b>' + b.textContent + '</b> ' + caps[b.textContent];
}));
"""))

ASSETS.append(asset_site(
    meta_site("component", "resurf-format-tiles", "Format tiles", "Two offset rows of small grey format tiles (icon top-left, label bottom-left) fading out at both edges.",
              ["tiles", "marquee", "mask", "formats"], ["css mask-image"]),
    f"""
# Format tiles

{NOTE_SITE}

Ten labelled tiles (Images, Video, Tweets, GitHub, Articles, PDFs, Audio, YouTube, Code, Notes) in two rows. Tile `#f3f3f3`, about 128 × 84, radius about 10px, 8px gaps; icon top-left in a mid grey, label bottom-left 12px/500 `#2b2b29`. The second row is offset about half a tile and both rows are masked: `linear-gradient(90deg, transparent, #000 12%, #000 88%, transparent)`. The stills show tiles caught mid-way across the edge fade, which suggests horizontal motion, but no speed or direction was captured.
""",
    """
.m{overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent)}
.r{display:flex;gap:8px;margin-bottom:8px;width:max-content}.r.o{margin-left:-64px}
.r div{width:128px;height:84px;border-radius:10px;background:var(--tile);padding:12px;display:flex;flex-direction:column;justify-content:space-between;font:500 12px/16px var(--font-sans);color:var(--ink-title)}
.r i{width:14px;height:14px;border-radius:4px;background:#8a8a88;display:block}
""",
    '<div class="m"><div class="r"><div><i></i>Video</div><div><i></i>Tweets</div><div><i></i>GitHub</div><div><i></i>Articles</div><div><i></i>Images</div><div><i></i>PDFs</div><div><i></i>Audio</div></div><div class="r o"><div><i></i>PDFs</div><div><i></i>Audio</div><div><i></i>YouTube</div><div><i></i>Code</div><div><i></i>Notes</div><div><i></i>Images</div><div><i></i>Video</div></div></div>'))

ASSETS.append(asset_site(
    meta_site("site", "resurf", "Resurf site", "Calm editorial landing page: off-white ground, two-tone Garamond-like headlines, flat grey feature cards, one big product screenshot on a gradient wallpaper.",
              ["site", "app", "productivity", "light", "editorial"], ["next.js", "tailwind"]),
    f"""
# Resurf: site design

{NOTE_SITE}

Full system: `design-systems/resurf`. Assets: `components/resurf-feature-card`, `components/resurf-tour-tabs`, `components/resurf-format-tiles`, `effects/nav-soft-fade`. The earlier App Store chip assets (`components/resurf-tag-chip`, `components/resurf-status-pill`, `effects/tilted-chip-lift`, `effects/fade-to-ground-mask`) come from the store listing, a different surface with its own look.

## Why screenshots
resurf.so serves CSS, scripts, fonts and images behind a bot challenge (HTTP 429), so automated capture was not possible. Its `robots.txt` also disallows `/api/`, `/checkout/` and `/gift`. The owner supplied five browser screenshots of the home page, which is what this entry is read from.

## Page structure (top to bottom, as seen)
1. **Nav:** logo mark left, centred links Story, Roadmap, Updates, Pricing, Resources (chevron), "Get Resurf" dark button with chevron right. White-to-ground fade underneath.
2. **Hero:** Product Hunt badge "#1 Product of the Day"; two-tone serif H1 "A Personal Context Library / in files you own."; paragraph "Save notes, bookmarks, screenshots and PDFs in one local library. Find anything, then hand that context to your agents."; buttons "Download for Mac" (dark, Apple glyph) and "Buy a license · $39" (grey); meta "Mac, iPhone & iPad · Chrome extension · MCP & CLI for agents".
3. **Hero screenshot:** a large product screenshot on a holographic gradient wallpaper, rounded, soft shadow; round arrow buttons left and right, a "Pause" pill bottom right; caption "Library Select an image and discover similar references across your library."; thumbnail strip of six slides, the active one ringed in blue.
4. **Section "Save, organize, and search your notes, bookmarks, and files.":** subtext, then a 3 × 4 grid of feature cards (Quick Capture, Inbox First, Spaces & Tags, Visual bookmark library, From Any App, Search your saved content, Voice Memos, Highlight & Annotate, AI Summaries, Bring Your Own AI, Ask Your Library, Fully local), three of them marked Opt-in.
5. **Section "Five surfaces, one library.":** subtext, pill tabs (Library, Inbox, View, Notes, Assistant), a screenshot, a caption, then "Articles, PDFs, images, audio, video, code, and more. Every format renders natively." over two offset, edge-faded rows of format tiles.
6. **Section "Your library on Mac, iPhone, and iPad.":** a soft grey panel that fades into the ground, paragraph about the iPhone share sheet and optional private iCloud sync, three pills ("100% native Swift", "Fully local", "Optional iCloud sync"), and a device montage.
7. **CTA:** "Start building your personal context library." serif H2, a dark "Download for Mac" button, microcopy "7-day free trial · macOS 14.3+ (Apple Silicon & Intel) · Free on iPhone & iPad".
8. **Footer:** hairline, logo and tagline, four columns (Product, Compare, Learn, Company).

## Measured values
Container 896px (56rem) with 32px side padding; card grid 3 columns, 8px gap; headline cap height 25px (about 40px Garamond-like); body 14px/21px; nav 13px; card title 14px; card description 12px/19px. Colours: see `design-systems/resurf/project/tokens.json`.

## Not captured
CSS tokens, real font files, the hover and press states, any timing or easing, the Resources dropdown, and the mobile layout.
""",
    """
.frame{border-radius:12px;background:var(--ground);padding:18px;text-align:center;box-shadow:0 0 0 1px var(--line)}
.nav{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;font:500 13px var(--font-sans);color:var(--ink-nav);margin-bottom:20px}
.m{width:18px;height:18px;border-radius:5px;background:var(--ink-button);display:block}
.nav nav{display:flex;gap:20px}.b{justify-self:end;height:24px;padding:0 10px;border-radius:6px;background:var(--ink-button);color:var(--paper);font:500 12px/24px var(--font-sans)}
h1{margin:0;font:500 34px/38px var(--font-serif);letter-spacing:-.02em;color:var(--ink)}h1 span{color:var(--ink-faint)}
p{margin:12px auto 16px;max-width:44ch;font:400 14px/21px var(--font-sans);color:var(--ink-body)}
.r{display:flex;gap:8px;justify-content:center}.r span{height:34px;padding:0 16px;border-radius:8px;font:500 13px/34px var(--font-sans)}
.k{background:var(--ink-button);color:var(--paper)}.g{background:var(--grey-button);color:var(--ink-title)}
.shot{margin-top:18px;height:70px;border-radius:12px;background:linear-gradient(100deg,#8aa0f0,#4fbf7a,#f09078,#7a8cf0)}
""",
    '<div class="frame"><div class="nav"><i class="m"></i><nav><span>Story</span><span>Roadmap</span><span>Updates</span><span>Pricing</span></nav><span class="b">Get Resurf</span></div><h1>A Personal Context Library<br><span>in files you own.</span></h1><p>Save notes, bookmarks, screenshots and PDFs in one local library.</p><div class="r"><span class="k">Download for Mac</span><span class="g">Buy a license · $39</span></div><div class="shot"></div></div>'))
