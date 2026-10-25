# Decimals — site design

Landing page of a scout network for hiring designers, captured at 1440×900. Colours and timings were read from the live page's computed styles; fonts are open substitutes (Newsreader for martina). No logos or photography were copied.

Full system: `design-systems/decimals`.

## Page structure
1. **Nav** (`components/decimals-nav-bar`): wordmark, four links, Get started + Log in; blur-fade backdrop (`effects/edge-fade-mask`).
2. **Hero**: centred 56px serif headline "Hire designers who care through scouts that can tell", 18px subline, pill pair (`components/decimals-pill-button`). Content enters via `motions/hero-blur-reveal`. A dotted globe arc (canvas, `.v2-globe`) rises behind the buttons.
3. **Logo ticker** (`motions/logo-ticker`): "From our network, hired by" caption over the marquee.
4. **Proof rows** (`components/decimals-testimonial-row`): four alternating rows, each a company mark, serif claim, paragraph and a quote; section background fades in and out with a 340px mask.
5. **Problem section**: "Traditional recruiting stopped working" and three halftone-collage cards.
6. **Closing CTA**: "Let's find your next designer", a single pill, three small tilted portrait cut-outs floating on a blush gradient.
7. **Ambient layer** (`motions/ambient-drift`) behind everything.

## Tokens at a glance
Ground `#ede8e1`, ink `#4d4638`, card `#f3eee6`, blush `#f4c9be`. Headlines Newsreader (martina on the site) -0.04em; text Geist 14px -0.14px.

## Notes
- Hero globe is a canvas dot sphere with faint meridians; denser dots on the right limb. Not reproduced here beyond the cover sketch.
- Honour `prefers-reduced-motion`: ticker, drift and blur reveal all switch off.
