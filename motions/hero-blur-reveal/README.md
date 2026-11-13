# Hero blur reveal

Colours and timings were read from the live page's computed styles; fonts are open substitutes (Newsreader for martina). No logos or photography were copied.

Hero children start dimmed and blurred and are released by JS (a transition of `opacity, filter` over 0.25s). If JS never runs, a keyframe fallback reveals them anyway.

```css
html:not(.js-ready) .hero > * {
  opacity:.3; filter:blur(12px);
  animation:reveal .6s ease 2.6s 1 forwards;      /* fallback after 2.6s */
}
@keyframes reveal { 100% { opacity:1; filter:none } }
.hero > * { transition:opacity .25s ease, filter .25s ease }
@media (prefers-reduced-motion:reduce) {
  html:not(.js-ready) .hero > * { opacity:1; filter:none; animation:none }
}
```

The fallback timing (0.6s ease, 2.6s delay) and the 0.3 / 12px start state are measured. The per-child stagger is not documented here; add `transition-delay` in steps of about 60ms for a sequenced entrance.
