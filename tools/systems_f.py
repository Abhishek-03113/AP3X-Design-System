"""Systems built from a site's own compiled stylesheet plus a recorded Playwright capture.

Tracwell (tracwell.app) ships Next.js with Turbopack and no public source maps, so the
tokens come from its compiled Tailwind v4 CSS (`:root`, `.dark`, `.landing`) and the
component measurements from computed styles in headless Chromium at 1440px, with a
scroll-through video recording, on 2026-11-06.
"""
from ds_lib import tok, style

GF = "https://fonts.googleapis.com/css2?"

# ---------------------------------------------------------------- Tracwell
tracwell = {
    "slug": "tracwell",
    "title": "Tracwell",
    "namespace": "Tracwell",
    "source": {"url": "https://tracwell.app/", "captured": "2026-11-06",
               "method": "Compiled Tailwind v4 stylesheet (no source maps served) plus a Playwright capture: computed styles, 21 scroll frames and a scroll-through video at 1440px."},
    "note": "Created from the public site https://tracwell.app/ (compiled CSS plus a Playwright capture).",
    "fonts_href": GF + "family=Inter:wght@400;500;600&display=swap",
    "themes": [{"id": "light", "name": "Light"}, {"id": "dark", "name": "Dark"}],
    "contrast_ground": "background",
    "fonts": [
        {"family": "Open Runde", "file": "fonts/OpenRunde-Medium.woff2", "weight": "500", "style": "normal"},
        {"family": "Open Runde", "file": "fonts/OpenRunde-Semibold.woff2", "weight": "600", "style": "normal"},
    ],
    "families": {
        "display": "\"Open Runde\", \"Inter\", ui-sans-serif, system-ui, sans-serif",
        "sans": "\"Inter\", \"Inter Variable\", ui-sans-serif, system-ui, sans-serif",
        "mono": "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, \"Liberation Mono\", monospace",
    },
    "colors": [
        # chrome
        tok("background", {"light": "#ffffff", "dark": "#1c1c1c"}, "Page and panel ground; the inner layer of every card."),
        tok("surface", {"light": "#f7fafc", "dark": "#171717"}, "The landing's cool off-white (`--landing-surface`) behind the hero and agent sections. The marketing site is light only; the dark value is the app's `card`."),
        tok("card", {"light": "#ffffff", "dark": "#171717"}, "Raised cards, popovers and the FAQ items."),
        tok("well", {"light": "rgba(245, 245, 245, 0.7)", "dark": "rgba(38, 38, 38, 0.7)"}, "The grey outer layer of a dashboard card (`muted` at 70%): it holds the label row and frames a `background` card inside."),
        tok("muted", {"light": "#f5f5f5", "dark": "#262626"}, "Segmented-control track, hover fills, sidebar active row."),
        tok("secondary", {"light": "#f4f4f5", "dark": "#27272a"}, "Secondary button fill (\"Explore demo\")."),
        tok("secondary-foreground", {"light": "#18181b", "dark": "#fafafa"}, "Text on `secondary`. 16.1:1 light, 14.3:1 dark."),
        tok("foreground", {"light": "#0a0a0a", "dark": "#fafafa"}, "Headlines, numbers and body text. 19.8:1 on `background` light, 16.3:1 dark."),
        tok("foreground-soft", {"light": "rgba(10, 10, 10, 0.55)", "dark": "rgba(250, 250, 250, 0.55)"}, "The grey second line of two-tone headlines (\"for you and your agent\"). 4.4:1 light: display sizes only (24px+), never body text."),
        tok("muted-foreground", {"light": "#737373", "dark": "#a1a1a1"}, "Body copy, nav, labels, table heads. 4.7:1 on `background`, 4.5:1 on `surface`, 4.46:1 on `well`, just under AA: the site's own pairing for 12px card labels, so keep labels short and medium weight. Dark: 6.6:1 on `background`, 6.1:1 on `well`."),
        tok("border", {"light": "#e5e5e5", "dark": "rgba(255, 255, 255, 0.1)"}, "Hairlines, inputs, the nav bar outline (used at 40–70% strength)."),
        tok("ring", {"light": "rgba(76, 153, 248, 0.55)", "dark": "rgba(128, 186, 255, 0.6)"}, "Focus ring around inputs and buttons."),
        # brand
        tok("primary", "#357dff", "Tracwell blue: primary buttons, the final CTA band, active dots. Same in both themes."),
        tok("primary-foreground", "#ffffff", "Text on `primary`. 3.8:1 — the site's own pairing on 14px semibold buttons; it misses AA, so keep labels short and never put body copy on `primary`."),
        tok("destructive", {"light": "#e40014", "dark": "#ff6568"}, "Negative deltas and errors. 4.9:1 on `background` light, 6.2:1 on `card` dark."),
        tok("success-text", {"light": "#007956", "dark": "#5ee9b5"}, "Text in positive-delta pills (\"+18.4%\"). 5.2:1 on `success-soft` light, 5.1:1 dark."),
        tok("success-soft", {"light": "#ecfdf5", "dark": "#005f46"}, "Positive-delta pill ground. Dark value from the site's own emerald scale."),
        # data
        tok("data-traffic", {"light": "#2885ef", "dark": "#5fa7ff"}, "Traffic series: bars, lines, the \"Indexing\" bot dot."),
        tok("data-traffic-text", {"light": "#0c54a0", "dark": "#9bc7ff"}, "Text in traffic tags and status badges. 6.7:1 on `data-traffic-soft` light, 7.4:1 dark."),
        tok("data-traffic-soft", {"light": "rgba(40, 133, 239, 0.1)", "dark": "rgba(95, 167, 255, 0.16)"}, "Bar-list fills and traffic tag grounds."),
        tok("data-revenue", {"light": "#845de7", "dark": "#a88fff"}, "Revenue series."),
        tok("data-revenue-text", {"light": "#59419b", "dark": "#cbc1ff"}, "Text in revenue tags (\"$290 purchase\"). 7.0:1 on `data-revenue-soft` light, 7.9:1 dark."),
        tok("data-revenue-soft", {"light": "rgba(132, 93, 231, 0.1)", "dark": "rgba(168, 143, 255, 0.16)"}, "Revenue tag grounds and area fills."),
        tok("data-acquisition", {"light": "#e85a48", "dark": "#fb8371"}, "Acquisition series; the \"AI fetch\" bot dot."),
        tok("data-acquisition-text", {"light": "#932c21", "dark": "#ffb5a8"}, "Text in acquisition tags. 7.1:1 on `data-acquisition-soft` light, 7.7:1 dark."),
        tok("data-acquisition-soft", {"light": "rgba(232, 90, 72, 0.1)", "dark": "rgba(251, 131, 113, 0.16)"}, "Acquisition tag grounds."),
        tok("data-engagement", {"light": "#009d96", "dark": "#49c7c0"}, "Engagement series: funnels, the \"Training\" bot dot."),
        tok("data-engagement-text", {"light": "#005451", "dark": "#9be0db"}, "Text in engagement tags. 7.8:1 on `data-engagement-soft` light, 8.4:1 dark."),
        tok("data-engagement-soft", {"light": "rgba(0, 157, 150, 0.1)", "dark": "rgba(73, 199, 192, 0.16)"}, "Engagement tag grounds and funnel bands."),
        tok("data-positive", "#10ce6a", "Up-arrow deltas in charts (\"↗ 12.4%\"). 2.1:1 on white — the site's own value; use it for marks and icons, and `success-text` for any figure someone must read."),
        # landing tints
        tok("tint-blue", {"light": "#e8f0ff", "dark": "rgba(95, 167, 255, 0.16)"}, "\"Install\" step card ground. `foreground` 17.3:1. Dark values reuse the app's dark data fills; the landing itself is light only."),
        tok("tint-lilac", {"light": "#efeafe", "dark": "rgba(168, 143, 255, 0.16)"}, "AI-traffic section band."),
        tok("tint-mint", {"light": "#e6f5ed", "dark": "rgba(73, 199, 192, 0.16)"}, "\"Ask\" step card and revenue band ground. `foreground` 17.6:1."),
        tok("tint-peach", {"light": "#fdf0e6", "dark": "rgba(249, 156, 0, 0.16)"}, "\"Track\" step card ground."),
        tok("tint-rose", {"light": "#fdeaf1", "dark": "rgba(251, 131, 113, 0.16)"}, "Spare landing tint; one per section at most."),
        # terminal
        tok("terminal", "#18181b", "The agent terminal panel. Same in both themes."),
        tok("terminal-raised", "#262626", "The prompt line inside the terminal."),
        tok("terminal-text", "#f5f5f5", "Prompt and answer text. 16.3:1 on `terminal`."),
        tok("terminal-dim", "#d4d4d4", "Tool-call lines (\"● tracwell - analytics_revenue (MCP)\"). 12.0:1 on `terminal`."),
        tok("terminal-muted", "#a1a1a1", "Hints (\"? for shortcuts\"). 6.9:1 on `terminal` (the site uses #737373 at 3.7:1; lifted here)."),
    ],
    "type_groups": [
        {"name": "Display", "family": "display", "styles": [
            style("hero", "60px", "63px", 600, "Hero headline, two lines: first in `foreground`, second in `foreground-soft`. -0.03em.", ls="-1.8px", sample="Product analytics for you and your agent"),
            style("section", "36px", "37.8px", 600, "Section heads, often two-tone. -0.03em.", ls="-1.08px", sample="Everything in one place."),
            style("card-title", "20px", "25px", 500, "Step and feature card titles.", ls="-0.6px", sample="Track what matters"),
            style("panel-title", "18px", "28px", 600, "Dashboard panel titles (\"Overview\").", ls="-0.27px"),
        ]},
        {"name": "Text", "family": "sans", "styles": [
            style("lead", "16px", "28px", 400, "Hero and section intros in `muted-foreground`, max 36rem.", sample="Tracwell follows every visit through signup and payment."),
            style("body", "14px", "24px", 400, "Card copy."),
            style("question", "18px", "28px", 500, "FAQ questions."),
            style("ui", "14px", "20px", 600, "Buttons and \"Log in\".", sample="Start free"),
            style("nav", "14px", "20px", 500, "Nav links, sidebar items, row names."),
            style("label", "12px", "16px", 500, "Card labels, chips, table values."),
            style("eyebrow", "12px", "16px", 600, "Uppercase section labels and table heads. +0.08em.", ls="0.96px", sample="HOW IT WORKS"),
            style("micro", "10px", "15px", 500, "Bot-type tags (\"AI fetch\")."),
            style("stat", "30px", "30px", 500, "Dashboard figures, tabular numerals. -0.04em.", ls="-1.2px", sample="$18,940"),
        ]},
        {"name": "Mono", "family": "mono", "styles": [
            style("terminal", "12px", "22px", 400, "Agent terminal and code snippets; the site uses the system monospace.", sample="❯ What brought paying customers last week?"),
            style("code", "14px", "20px", 400, "Inline URLs such as the MCP endpoint."),
        ]},
    ],
    "spacing": [
        tok("space-1", "4px", "Well padding around the inner card; Tailwind's base step (0.25rem)."),
        tok("space-2", "8px", "Icon gaps; bar-row vertical padding."),
        tok("space-3", "12px", "Bar-row and badge inline padding; gaps between dashboard cards."),
        tok("space-4", "16px", "Card inline padding; nav-button padding."),
        tok("space-5", "20px", "Secondary hero button padding; page gutter on phones."),
        tok("space-6", "24px", "Gaps between feature cards; FAQ row padding."),
        tok("space-8", "32px", "Page gutter on desktop; feature card padding."),
        tok("space-14", "56px", "Padding inside a tinted landing band."),
        tok("space-20", "80px", "CTA band vertical padding; section rhythm."),
    ],
    "radius": [
        tok("radius-sm", "6px", "Text links (focus outline)."),
        tok("radius-md", "10px", "Sidebar items and bar-list rows (`--radius`, 0.625rem)."),
        tok("radius-lg", "14px", "The inner card of a well, inputs, floating chips."),
        tok("radius-xl", "18px", "Cards, wells, the dashboard frame and the terminal."),
        tok("radius-2xl", "22px", "The FAQ well."),
        tok("radius-band", "24px", "Landing bands, the CTA band and the floating nav bar."),
        tok("radius-3xl", "28px", "FAQ items and the AI-traffic panel."),
        tok("radius-pill", "9999px", "Every button, badge and segmented control."),
    ],
    "shadow": [
        tok("shadow-hairline", {"light": "0 0 0 1px rgba(0, 0, 0, 0.05)", "dark": "0 0 0 1px rgba(255, 255, 255, 0.07)"}, "A 1px ring instead of a border: the active sidebar item."),
        tok("shadow-card", {"light": "0 0 0 1px rgba(0, 0, 0, 0.035), 0 1px 2px -1px rgba(0, 0, 0, 0.05), 0 3px 8px -4px rgba(0, 0, 0, 0.08)", "dark": "0 0 0 1px rgba(255, 255, 255, 0.07)"}, "Dashboard wells."),
        tok("shadow-float", {"light": "0 0 0 1px rgba(0, 0, 0, 0.04), 0 8px 24px -16px rgba(0, 0, 0, 0.24)", "dark": "0 0 0 1px rgba(255, 255, 255, 0.07), 0 8px 24px -16px rgba(0, 0, 0, 0.6)"}, "Event chips that float over a visual."),
        tok("shadow-frame", {"light": "0 0 0 1px rgba(0, 0, 0, 0.06), 0 24px 60px -28px rgba(0, 0, 0, 0.28), 0 40px 90px -48px rgba(0, 0, 0, 0.36)", "dark": "0 0 0 1px rgba(255, 255, 255, 0.07), 0 24px 60px -28px rgba(0, 0, 0, 0.7)"}, "The big product frame in the hero and revenue band; once per section."),
        tok("shadow-sm", "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)", "Step-card mockups and the terminal."),
        tok("shadow-button", "inset 0 1px 0 rgba(255, 255, 255, 0.3)", "The top highlight on `primary` buttons."),
    ],
    "readme": """
Tracwell is agent-first product analytics for founders and small teams: it follows every visit through signup and payment, and lets you ask Claude, Cursor or Codex about it over MCP. The site is calm, white and product-led: a floating pill nav, a two-tone headline in a rounded grotesk, then real-looking dashboard panels built from grey wells holding white cards, with four data hues doing all the colour work and one blue for actions. Built from the public site tracwell.app.

## Voice
- Plain, specific and outcome-first: "Find out which traffic pays." "See which visit led to each sale." "Paste one script tag."
- Two-tone headlines put the promise first and the qualifier second, in `foreground-soft`: "Everything in one place. / No paid add-ons."
- Numbers are concrete: "From $9/month for 300K events", "7 days free, no card required".
- Event names are snake_case and set in the UI as secondary text: `page_view`, `signup_completed`.
- Sentence case everywhere; uppercase only for `eyebrow` labels and table heads.

## Colour
- The chrome is neutral: `background`, `surface`, `well`, `muted`, `border`, `foreground`, `muted-foreground`.
- `primary` is for actions only: the Start free button, the CTA band, a live dot. Never for data.
- Data has its own four hues, each in three strengths: the solid hue for marks (`data-traffic`), a `-soft` 10% fill for bars and tag grounds, and a `-text` shade for words on that fill. Traffic is blue, revenue purple, acquisition coral, engagement teal.
- Landing sections take one pastel each (`tint-blue`, `tint-peach`, `tint-mint`, `tint-lilac`), behind a white mockup.
- Deltas: `success-text` on `success-soft` for up, `destructive` for down, always with an arrow.
- The marketing site is light only. The dark theme is the product app's own (`.dark` in the same stylesheet); the landing tints borrow the app's dark data fills.

## Typography
- **Open Runde** (Laurids Kern, SIL OFL 1.1) is the display face, 500 and 600, tracked -0.03em. It is a rounded cut of Inter, and its files ship in `fonts/`.
- **Inter** for all text (the site uses Inter Variable; Google Fonts serves the same family).
- Mono is the system `ui-monospace` stack, used in the terminal and code snippets.
- Numbers in dashboards use `font-variant-numeric: tabular-nums` and the `stat` style.

## Layout
- Content sits in a 72rem (1152px) column; the nav bar is the same width, floating 8px from the top.
- Hero: centred eyebrow chip, two-line headline, a 36rem `lead`, two pill buttons, then a row of three check-marked facts in `label`.
- Sections alternate between centred heads with three-up cards and split layouts (copy left, visual right).
- Product visuals are framed dashboards (`radius-xl`, `shadow-frame`) on a soft lilac-to-mint wash; the wash is a drawn canvas on the site and is not part of this system.

## Surfaces and elevation
- The signature is the two-layer card: a `well` with `radius-xl` and `space-1` padding, its label row on the well, and a `background` card with `radius-lg` inside holding the figure.
- Borders are 1px `border`, often at reduced strength; shadows are rings plus a long, faint drop (`shadow-card`, `shadow-float`, `shadow-frame`).
- Everything clickable is a pill (`radius-pill`).

## Iconography
- Thin 1.5px outline icons (Lucide-style) at 16–20px in `muted-foreground`, inside 36px white rounded squares with a `border` outline for feature lists.
- Visitor avatars are small illustrated busts; they are not copied here.
- The Tracwell mark (a slanted double stroke with a dot, blue gradient) is not reproduced: set the name in `display` 600, or use the official files from tracwell.app/branding.

## Motion
- Sections rise 16px and fade in on scroll; product visuals loop small demos (rolling events, a drawing goal line, a funnel sweep) on a `cubic-bezier(.77, 0, .175, 1)` ease. All of it is disabled under `prefers-reduced-motion`.

## Components
`Button`, `NavBar`, `StatCard`, `BarList`, `Badge` and `AgentTerminal`.
""",
    "components": {
        "Button": {
            "group": "Actions", "height": 120,
            "readme": """
Pill buttons for the one main action and its quiet alternative, plus the arrow text link.

- Primary: `primary` fill and border, `primary-foreground` text in `ui`, `shadow-button` highlight, `radius-pill`. Hero size is 48px tall with 28px padding; the nav size is 36px with `space-4`.
- Secondary: `secondary` fill, `secondary-foreground` text, 48px tall with `space-5` padding.
- Text link: `nav` in `foreground` with a chevron; the quieter one is `muted-foreground` with an underline.
- Focus: a 3px `ring`. One primary per view.
""",
            "css": """
body{background:var(--background);padding:20px;font-family:var(--font-sans)}
.row{display:flex;flex-wrap:wrap;align-items:center;gap:12px}
.row+.row{margin-top:16px}
.b{display:inline-flex;align-items:center;height:48px;border-radius:var(--radius-pill);font:600 14px/20px var(--font-sans);text-decoration:none;border:1px solid transparent}
.b:focus-visible{outline:none;box-shadow:0 0 0 3px var(--ring)}
.p{background:var(--primary);border-color:var(--primary);color:var(--primary-foreground);padding:0 28px;box-shadow:var(--shadow-button)}
.s{background:var(--secondary);color:var(--secondary-foreground);padding:0 20px}
.sm{height:36px;padding:0 16px}
.l{font:500 14px/20px var(--font-sans);color:var(--foreground);text-decoration:none}
.q{font:400 14px/20px var(--font-sans);color:var(--muted-foreground);text-decoration:underline;text-decoration-color:var(--border);text-underline-offset:4px}
""",
            "html": """
<div class="row"><a class="b p" href="#">Start free</a><a class="b s" href="#">Explore demo</a><a class="b p sm" href="#">Start free</a></div>
<div class="row"><a class="l" href="#">Connect your agent ›</a><a class="q" href="#">Read the guide</a></div>
""",
        },
        "NavBar": {
            "group": "Navigation", "height": 96,
            "readme": """
The floating pill nav: wordmark left, links centre, Log in and Start free right.

- 48px tall, `radius-band`, 1px `border`, `background` at 85% with a 24px backdrop blur; sticky 8px from the top, 72rem wide.
- Links in `nav`, `muted-foreground`, 10px padding; Log in in `ui` `foreground`; Start free is the 36px primary `Button`.
- Provide the wordmark: the name in `display` 600 (the mark is not part of this system).
- Under 768px the centre links collapse into a menu button.
""",
            "css": """
body{background:var(--surface);padding:20px;font-family:var(--font-sans)}
nav{display:flex;align-items:center;justify-content:space-between;gap:8px;height:48px;padding:0 6px 0 14px;border:1px solid var(--border);border-radius:var(--radius-band);background:var(--background);max-width:900px}
.w{font:600 18px/1 var(--font-display);letter-spacing:-0.4px;color:var(--foreground)}
.c{display:flex}
.c a{font:500 14px/20px var(--font-sans);color:var(--muted-foreground);padding:0 10px;text-decoration:none}
.r{display:flex;align-items:center;gap:4px}
.li{font:600 14px/20px var(--font-sans);color:var(--foreground);padding:0 16px;text-decoration:none}
.st{display:inline-flex;align-items:center;height:36px;padding:0 16px;border-radius:var(--radius-pill);background:var(--primary);color:var(--primary-foreground);font:600 14px/20px var(--font-sans);text-decoration:none;box-shadow:var(--shadow-button)}
@media (max-width:640px){.c{display:none}}
""",
            "html": """
<nav aria-label="Main navigation"><span class="w">Tracwell</span><div class="c"><a href="#">Features</a><a href="#">Demo</a><a href="#">How it works</a><a href="#">Pricing</a><a href="#">Docs</a></div><div class="r"><a class="li" href="#">Log in</a><a class="st" href="#">Start free</a></div></nav>
""",
        },
        "StatCard": {
            "group": "Data", "height": 170,
            "readme": """
A dashboard figure in the two-layer card: the label on the grey well, the number on a white card inside it.

- Provide label, value and an optional delta. Well: `well`, `radius-xl`, `space-1` padding, `shadow-card`; label row in `label` `muted-foreground`, padded 8px × `space-4`.
- Inner card: `background`, `radius-lg`, padding 12px `space-4` 8px; value in `stat` `foreground` with tabular numerals; delta in `label` with an arrow, `success-text` up, `destructive` down.
- Example figures below are the site's sample report, not real data.
""",
            "css": """
body{background:var(--background);padding:16px;font-family:var(--font-sans)}
.g{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;max-width:820px}
.w{background:var(--well);border-radius:var(--radius-xl);padding:4px;box-shadow:var(--shadow-card)}
.lb{font:500 12px/16px var(--font-sans);color:var(--muted-foreground);padding:6px 12px 6px}
.in{background:var(--background);border-radius:var(--radius-lg);padding:12px 16px 8px}
.v{font:500 30px/30px var(--font-sans);letter-spacing:-1.2px;color:var(--foreground);font-variant-numeric:tabular-nums}
.d{font:500 12px/16px var(--font-sans);margin-top:6px}
.up{color:var(--success-text)}
.dn{color:var(--destructive)}
""",
            "html": """
<div class="g">
<div class="w"><div class="lb">Visitors</div><div class="in"><div class="v">8,420</div><div class="d up">↗ 12.4%</div></div></div>
<div class="w"><div class="lb">Signups</div><div class="in"><div class="v">612</div><div class="d up">↗ 8.1%</div></div></div>
<div class="w"><div class="lb">Revenue</div><div class="in"><div class="v">$18,940</div><div class="d dn">↘ 2.3%</div></div></div>
</div>
""",
        },
        "BarList": {
            "group": "Data", "height": 260,
            "readme": """
A ranked list with a soft bar behind each name: top sources, pages, locations.

- Well and header as `StatCard` (title left, unit right, both `label` `muted-foreground`); inner card `background`, `radius-lg`, `space-1` padding.
- Rows: 32px, `radius-md`, name in `label` `foreground`, value in `label` `muted-foreground` with tabular numerals. The bar is a `data-*-soft` fill sized to the value, drawn behind the row; pick the hue by what is measured (`data-traffic-soft` for visitors).
- Provide rows sorted high to low; widths are value ÷ the top value.
""",
            "css": """
body{background:var(--background);padding:16px;font-family:var(--font-sans)}
.w{background:var(--well);border-radius:var(--radius-xl);padding:4px;box-shadow:var(--shadow-card);max-width:360px}
.h{display:flex;justify-content:space-between;font:500 12px/16px var(--font-sans);color:var(--muted-foreground);padding:6px 12px}
.in{background:var(--background);border-radius:var(--radius-lg);padding:4px;display:grid;gap:4px}
.r{position:relative;display:flex;justify-content:space-between;align-items:center;height:32px;padding:0 12px;font:500 12px/16px var(--font-sans);color:var(--foreground);isolation:isolate}
.r::before{content:"";position:absolute;inset:0 auto 0 0;width:var(--w);background:var(--data-traffic-soft);border-radius:var(--radius-md);z-index:-1}
.n{font-weight:400;color:var(--muted-foreground);font-variant-numeric:tabular-nums}
""",
            "html": """
<div class="w"><div class="h"><span>Top sources</span><span>Visitors</span></div><div class="in">
<div class="r" style="--w:72%"><span>Google</span><span class="n">3,184</span></div>
<div class="r" style="--w:46%"><span>Direct</span><span class="n">1,208</span></div>
<div class="r" style="--w:34%"><span>Newsletter</span><span class="n">842</span></div>
<div class="r" style="--w:26%"><span>Product Hunt</span><span class="n">517</span></div>
<div class="r" style="--w:16%"><span>Reddit</span><span class="n">348</span></div>
</div></div>
""",
        },
        "Badge": {
            "group": "Status", "height": 110,
            "readme": """
Small pills for live status, deltas and data categories.

- Status: `label`, `data-traffic-text` on `data-traffic-soft` with a 1px `border`, a 6px `primary` dot, `radius-pill`, padding 4px 10px. The site sets this text in `primary` (3.6:1); the `-text` shade keeps the look and passes AA.
- Delta: `label`, `success-text` on `success-soft`, padding 4px 8px.
- Category tags: `micro`, a `data-*-text` on its `data-*-soft`, padding 2px 8px. AI fetch is acquisition, Indexing traffic, Training engagement, purchases revenue.
""",
            "css": """
body{background:var(--background);padding:20px;font-family:var(--font-sans)}
.row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.row+.row{margin-top:14px}
.s{display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:var(--radius-pill);border:1px solid var(--border);background:var(--data-traffic-soft);color:var(--data-traffic-text);font:500 12px/16px var(--font-sans)}
.s i{width:6px;height:6px;border-radius:50%;background:var(--primary)}
.d{padding:4px 8px;border-radius:var(--radius-pill);background:var(--success-soft);color:var(--success-text);font:500 12px/16px var(--font-sans)}
.t{padding:2px 8px;border-radius:var(--radius-pill);font:500 10px/15px var(--font-sans)}
.acq{background:var(--data-acquisition-soft);color:var(--data-acquisition-text)}
.trf{background:var(--data-traffic-soft);color:var(--data-traffic-text)}
.eng{background:var(--data-engagement-soft);color:var(--data-engagement-text)}
.rev{background:var(--data-revenue-soft);color:var(--data-revenue-text)}
""",
            "html": """
<div class="row"><span class="s"><i></i>Connected</span><span class="s"><i></i>Receiving</span><span class="d">+18.4%</span></div>
<div class="row"><span class="t acq">AI fetch</span><span class="t trf">Indexing</span><span class="t eng">Training</span><span class="t rev">$290 purchase</span></div>
""",
        },
        "AgentTerminal": {
            "group": "Content", "height": 230,
            "readme": """
A dark terminal showing an agent asking Tracwell a question over MCP; the site's proof that "your agent sees the same numbers".

- Panel: `terminal`, `radius-xl`, 1px `terminal-raised` border, `shadow-sm`; the same in both themes.
- Text in `terminal` style: the prompt on a `terminal-raised` line, tool calls in `terminal-dim` with a `data-positive` dot, the answer in `terminal-text`, hints in `terminal-muted`.
- Provide a real question and an answer drawn from real report fields; mark sample data as an example.
""",
            "css": """
body{background:var(--surface);padding:16px}
.t{background:var(--terminal);border:1px solid var(--terminal-raised);border-radius:var(--radius-xl);box-shadow:var(--shadow-sm);padding:14px 18px;max-width:560px;font:400 12px/22px var(--font-mono);color:var(--terminal-text)}
.p{background:var(--terminal-raised);border-radius:6px;padding:2px 8px;margin-bottom:8px}
.tool{color:var(--terminal-dim)}
.tool b{color:var(--data-positive);font-weight:400}
.a{margin:2px 0 8px}
.a b{font-weight:400;color:var(--terminal-dim)}
.m{color:var(--terminal-muted)}
""",
            "html": """
<div class="t" role="img" aria-label="Example agent session: asking which traffic brought paying customers">
<div class="p">❯ What brought paying customers last week?</div>
<div class="tool"><b>●</b> tracwell - analytics_revenue (MCP)(from: "2026-10-18", to: "2026-10-25")</div>
<div class="a"><b>●</b> ChatGPT brought the most revenue last week: $1,160 of $2,320. Example data.</div>
<div class="m">? for shortcuts</div>
</div>
""",
        },
    },
    "cover": {
        "ground": "background", "ink": "foreground", "muted": "muted-foreground", "body_font": "sans",
        "name_font": "display", "name_size": 88, "name_weight": 600, "name_ls": "-2.6px", "name_lines": ["Tracwell"],
        "tagline": "Agent-first product analytics for founders and builders.",
        "css": """
  .pr{fill:var(--primary)} .rv{fill:var(--data-revenue)} .en{fill:var(--data-engagement)} .fg{fill:var(--foreground)}
  .dot{fill:var(--background)}
""",
        "derivation": """
blocks      primary 264x240 slab (radius-band 24) · data-revenue 152x112 (radius-xl 18) · data-engagement 72x112 (radius-xl 18) · foreground 64x32 pill (radius-pill, half of 32)
arrangement one tall primary slab with three satellites to its right, like the CTA band beside the dashboard's data hues
pattern     the CTA band's own dot field: background discs at a space-6 (24) pitch cut out of the primary slab — the most Tracwell thing on the page
scales      pitch space-6 24, disc r 8, gaps space-4 16, radii radius-band 24, radius-xl 18, radius-pill
""",
        "svg": """
<rect class="pr" x="24" y="24" width="264" height="240" rx="24"/>
<g class="dot">
<circle cx="60" cy="60" r="8"/><circle cx="84" cy="60" r="8"/><circle cx="108" cy="60" r="8"/><circle cx="132" cy="60" r="8"/><circle cx="156" cy="60" r="8"/><circle cx="180" cy="60" r="8"/><circle cx="204" cy="60" r="8"/><circle cx="228" cy="60" r="8"/><circle cx="252" cy="60" r="8"/>
<circle cx="60" cy="84" r="8"/><circle cx="84" cy="84" r="8"/><circle cx="108" cy="84" r="8"/><circle cx="132" cy="84" r="8"/><circle cx="228" cy="84" r="8"/><circle cx="252" cy="84" r="8"/>
<circle cx="60" cy="108" r="8"/><circle cx="84" cy="108" r="8"/><circle cx="108" cy="108" r="8"/><circle cx="252" cy="108" r="8"/>
<circle cx="60" cy="132" r="8"/><circle cx="84" cy="132" r="8"/><circle cx="252" cy="132" r="8"/>
<circle cx="60" cy="156" r="8"/><circle cx="84" cy="156" r="8"/><circle cx="228" cy="156" r="8"/><circle cx="252" cy="156" r="8"/>
<circle cx="60" cy="180" r="8"/><circle cx="84" cy="180" r="8"/><circle cx="108" cy="180" r="8"/><circle cx="204" cy="180" r="8"/><circle cx="228" cy="180" r="8"/><circle cx="252" cy="180" r="8"/>
<circle cx="60" cy="204" r="8"/><circle cx="84" cy="204" r="8"/><circle cx="108" cy="204" r="8"/><circle cx="132" cy="204" r="8"/><circle cx="180" cy="204" r="8"/><circle cx="204" cy="204" r="8"/><circle cx="228" cy="204" r="8"/><circle cx="252" cy="204" r="8"/>
<circle cx="60" cy="228" r="8"/><circle cx="84" cy="228" r="8"/><circle cx="108" cy="228" r="8"/><circle cx="132" cy="228" r="8"/><circle cx="156" cy="228" r="8"/><circle cx="180" cy="228" r="8"/><circle cx="204" cy="228" r="8"/><circle cx="228" cy="228" r="8"/><circle cx="252" cy="228" r="8"/>
</g>
<rect class="rv" x="304" y="24" width="152" height="112" rx="18"/>
<rect class="en" x="304" y="152" width="72" height="112" rx="18"/>
<rect class="fg" x="392" y="232" width="64" height="32" rx="16"/>
""",
    },
}

SYSTEMS = [tracwell]
