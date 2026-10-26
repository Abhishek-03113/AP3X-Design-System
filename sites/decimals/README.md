# Decimals — site design

Landing page of a scout network for hiring designers, captured at 1440×900. Colours and timings were read from the live page's computed styles; fonts are open substitutes (Newsreader for martina). No logos or photography were copied.

Full system: `design-systems/decimals`.

## Page structure
1. **Nav** (`components/decimals-nav-bar`): wordmark, four links, Get started + Log in; blur-fade backdrop (`effects/edge-fade-mask`).
2. **Hero**: centred 56px serif headline "Hire designers who care through scouts that can tell", 18px subline, pill pair (`components/decimals-pill-button`). Content enters via `motions/hero-blur-reveal`. A dotted globe arc (canvas, `.v2-globe`) rises behind the buttons.
3. **Logo ticker** (`motions/logo-ticker`): "From our network, hired by" caption over the marquee.
4. **Proof rows** (`components/decimals-testimonial-row`, stacked by `motions/stacking-sticky-cards`): four alternating rows, each a company mark, serif claim, paragraph and a quote; section background fades in and out with a 340px mask.
5. **Problem section**: "Traditional recruiting stopped working" and three halftone-collage cards.
6. **Closing CTA**: "Let's find your next designer", a single pill, three small tilted portrait cut-outs floating on a blush gradient.
7. **Ambient layer** (`motions/ambient-drift`) behind everything.

## Tokens at a glance
Ground `#ede8e1`, ink `#4d4638`, card `#f3eee6`, blush `#f4c9be`. Headlines Newsreader (martina on the site) -0.04em; text Geist 14px -0.14px.

## Scroll choreography (measured by stepping the page, 1440×900)
| Scroll position | What happens | Asset |
| --- | --- | --- |
| 0 → about 55px | Nav wordmark "DECIMALS" slides letter by letter into the monogram, which pops in with overshoot | `motions/wordmark-collapse` |
| Hero | Dotted canvas globe auto-rotates, leans toward the pointer, pauses off-screen | `effects/dot-globe` |
| About 690 → 2350px | The four proof rows pin at 120px; each recedes (scale 0.965, up 8px, blur 2px) as the next slides over it; the last stays crisp | `motions/stacking-sticky-cards` |
| About 2250px | Problem cards fade up 12px as their top crosses 95% of the viewport | `motions/scroll-fade-up` |
| About 2750px | Closing CTA panel does the same; its five portrait chips are static, tilted −8° to +7° | `motions/scroll-fade-up` |
| End | A giant, low-contrast "DECIMALS" wordmark closes the page | (type only) |
| Always | Blush glows drift behind a sticky layer; section backgrounds use fixed attachment with 220–340px edge masks | `motions/ambient-drift`, `effects/edge-fade-mask` |

No scroll library was detected (no GSAP, ScrollTrigger or Lenis); the page uses CSS sticky, `IntersectionObserver` and plain scroll handlers. Scroll listeners counted: 15 `scroll`, 10 `wheel`, 13 `pointermove`.

## Notes
- The globe's source was not extracted; `effects/dot-globe` is a recreation of the observed behaviour.
- Honour `prefers-reduced-motion`: ticker, drift, blur reveal, sticky recede, fade-ups and the wordmark swap all switch off.
