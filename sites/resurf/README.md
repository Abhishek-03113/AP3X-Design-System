# Resurf: site structure and store art

Provenance: read from the public App Store art, not from resurf.so's CSS (blocked by a bot challenge). Colours are pixel-sampled (about ±6 per channel); sizes, angles and shadows are estimated by eye and marked *estimated*. No timings exist because no motion was captured.

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
