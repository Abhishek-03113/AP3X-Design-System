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
