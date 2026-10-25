# Resurf: site design

Provenance: read from five screenshots of resurf.so taken in the owner's browser on 2026-10-25 (the site blocks automated browsers). Colours are pixel-sampled; sizes are measured at about 1:1 (anchored to the 56rem container), good to ±1–2px; radii and shadows are *estimated*. Typefaces could not be confirmed (Garamond-like serif, Inter-like sans). No motion timings exist: motion is inferred from UI states only.

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
