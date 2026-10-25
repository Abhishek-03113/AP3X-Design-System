"""Individual assets for Resurf. Source: public App Store listing art (pixel-sampled) plus the text of resurf.so's HTML.
resurf.so serves its CSS, JS, fonts and images behind a bot challenge, so nothing here is a computed style from the site
and no motion was captured."""

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

ASSETS.append(asset(
    meta("site", "resurf", "Resurf site and store art", "Personal context library for Mac, iPhone and iPad: airy white ground, two-tone headlines, tilted colour-coded chips, fading devices.",
         ["site", "app", "productivity", "light", "apple"], ["next.js"]),
    f"""
# Resurf: site structure and store art

{NOTE}

Full system: `design-systems/resurf`. Effects and components: `effects/fade-to-ground-mask`, `effects/tilted-chip-lift`, `components/resurf-tag-chip`, `components/resurf-status-pill`.

## What was reachable
resurf.so sends its stylesheets, scripts, fonts and press images through a bot challenge (HTTP 429, `x-vercel-mitigated: challenge`), including on the first request. Only the HTML text loads. The press kit's own images were challenged too, and Resurf's `robots.txt` disallows `/api/`, `/checkout/` and `/gift`. Nothing was fetched from those paths after the first pass (two `/checkout` loads from an early crawler bug are the exception, noted in the PR).

## Page structure (from the HTML text)
- **Nav:** Story, Roadmap, Updates, Pricing, Resources, Get Resurf.
- **Hero:** "A Personal Context Library open to your agents. that remembers. in files you own. that works offline." Primary actions "Download for Mac" and "Buy a license · $39", then "Mac, iPhone & iPad · Chrome extension · MCP & CLI for agents".
- **Product tour tabs:** Library (similar images), Image details, Reader, Notes (Markdown), Inbox, Search, Spaces, PDFs, Assistant (opt-in, your own AI key).
- **Section:** "Save, organize, and search your notes, bookmarks, and files."
- **Comparison pages:** vs MyMind, Raindrop, Anybox, Eagle.
- **Resources:** guides (start guide, import, sync, backup and export, keyboard shortcuts, capture on Mac, inbox, layouts, search, AI providers, vault, connect agents, license key, free and Pro), blog, changelogs, roadmap, FAQ, support, press kit, affiliates.
- **Page size:** the home document measured 88,510px tall because the stylesheet failed to load; that is not the real layout.

## Store art language (sampled)
Ground `#f3f3f3` to `#ffffff`; headline two-tone (`#727272` then `#000000`); chip glyph colours amber `#d89024`, ember `#fc480c`, violet `#b46cd8`, azure `#0c78fc`, leaf `#30a818`.

## Not captured
CSS tokens, real font files, spacing scale, shadows, easing, any scroll or hover motion, and the website's actual layout and imagery. Treat this as a starting point to verify against the site's own CSS.
""",
    """
.frame{border-radius:12px;background:linear-gradient(var(--ground),var(--paper));padding:28px;text-align:center}
.nav{display:flex;justify-content:center;gap:22px;font:500 13px var(--font-sans);color:var(--ink-soft);margin-bottom:26px}
h1{margin:0;font:600 32px/34px var(--font-sans);letter-spacing:-.02em}h1 span{color:var(--ink-soft)}
.cta{margin-top:18px;display:flex;gap:10px;justify-content:center}
.b{height:38px;padding:0 18px;border-radius:999px;font:600 14px/38px var(--font-sans)}
.k{background:#111;color:#fff}.o{background:#fff;box-shadow:0 0 0 1px rgba(0,0,0,.12)}
.tabs{margin-top:22px;display:flex;gap:8px;justify-content:center;flex-wrap:wrap}
.tabs span{height:30px;padding:0 12px;border-radius:999px;background:#fff;box-shadow:0 0 0 1px rgba(0,0,0,.1);font:500 13px/30px var(--font-sans)}
""",
    '<div class="frame"><div class="nav"><span>Story</span><span>Roadmap</span><span>Updates</span><span>Pricing</span><span>Resources</span></div><h1><span>A Personal Context Library</span><br>open to your agents.</h1><div class="cta"><span class="b k">Download for Mac</span><span class="b o">Buy a license · $39</span></div><div class="tabs"><span>Library</span><span>Reader</span><span>Notes</span><span>Inbox</span><span>Search</span><span>Spaces</span><span>PDFs</span></div></div>'))
