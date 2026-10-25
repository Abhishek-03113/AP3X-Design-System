# Float in + ping slow

Two small keyframes the site keeps in its sheet. Colours and timings were read from the live page's computed styles; fonts are open substitutes (Newsreader for martina). No logos or photography were copied.

```css
@keyframes float-in { 0% { opacity:0; transform:translateY(10px) } 100% { opacity:1; transform:translateY(0) } }
@keyframes ping-slow { 0% { opacity:.7; transform:scale(1) } 100% { opacity:0; transform:scale(2.4) } }
```

Durations are not set in the keyframe sheet; the preview uses 0.5s `cubic-bezier(.22,1,.36,1)` for `float-in` (the site's movement easing) and 2s for `ping-slow`. Treat those two as starting values.
