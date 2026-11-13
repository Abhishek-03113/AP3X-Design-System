# Logo ticker

Colours and timings were read from the live page's computed styles; fonts are open substitutes (Newsreader for martina). No logos or photography were copied.

| Property | Value |
| --- | --- |
| Track | `display:flex; width:max-content`, content duplicated once |
| Keyframe | `to { transform: translateX(-50%) }` |
| Duration / easing | 46s linear, infinite |
| Gap | 64px between items |
| Edge mask | `linear-gradient(90deg, transparent 0%, #000 10%, #000 90%, transparent 100%)` |
| Hover | strip pauses (`animation-play-state`), marks drop to 0.4 opacity, hovered mark returns to 1 (0.25s) |
| Reduced motion | animation removed |

Duplicate the item list exactly once so `-50%` lands on a seamless loop.
