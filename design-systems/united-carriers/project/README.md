United Carriers does freight forwarding, land transport and customs brokerage across APAC "under one accountable team". The site opens on a black hero with a glowing planet horizon and enormous wide uppercase type, then moves into clean white sections set in Helvetica, with tiny monospace labels everywhere. Built from the public site unitedcarriers.com; display and mono fonts are open substitutes, Helvetica Neue is the site's own stack.

## Voice

- Plainspoken operator: "One operator. Every leg of the journey." "No finger-pointing between vendors."
- Headlines are uppercase and short; paragraphs are full sentences addressed to "your supply chain".
- Mono labels are uppercase and dotted: `NEWS · UC COURTSIDE IS HERE`, `CARBON CALCULATOR · LIVE TRACKING PORTAL`.

## Colour

- Two themes. `dark` is the hero and brand moments (pure black, the planet); `light` carries the services and copy. Use the semantic `bg` / `fg` tokens so components work in both.
- Muted levels are alpha on `fg` (`fg-muted` 72%/70%, `fg-subtle` 60%), exactly as the site does.
- `horizon`, `sky` and `indigo` belong to the planet artwork; don't use them for UI states.

## Typography

- Display is **BT Steinhart** on the site (wide, bold); this system substitutes **Unbounded**. Mono is **BT Steinhart Mono**, substituted by **Martian Mono**. Body is **Helvetica Neue** as on the site.
- All display text uppercase. Body sentence case. Mono uppercase, 10px.

## Shape

- Buttons are pills (`radius-pill`), white-filled on dark or outlined with `hairline`.
- Everything else is square.

## Components

`Button`, `Ticker` and `HeroStatement` are static previews built on the tokens above. No logo file ships; set UNITEDCARRIERS in `display-xs`.
