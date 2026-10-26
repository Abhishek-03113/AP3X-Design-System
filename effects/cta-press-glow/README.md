# CTA press glow

On press the pill tilts about 0.8° toward the pointer, shrinks to 0.976, loses 2% brightness, and a dark radial blooms under the finger with a light one opposite. Colours and timings were read from the live page's computed styles; fonts are open substitutes (Newsreader for martina). No logos or photography were copied.

## How it works
JS writes four variables on `pointerdown`: `--cta-press-x/y` (percent inside the button) and `--cta-press-dx/dy` (offset from centre, -0.5…0.5). CSS does the rest.

```css
.cta{--press-dur:.15s;--press-ease:cubic-bezier(.22,1,.36,1);position:relative;
  transition:transform var(--press-dur) var(--press-ease), filter var(--press-dur) var(--press-ease)}
.cta.is-pressed{
  transform:translate3d(calc(var(--cta-press-dx)*2.5px),calc(var(--cta-press-dy)*2.5px),-2px)
            rotateX(calc(var(--cta-press-dy)*-4deg)) rotateY(calc(var(--cta-press-dx)*4deg)) scale(.976);
  filter:saturate(1.03) brightness(.98)}
.cta::after{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;opacity:0;mix-blend-mode:multiply;
  background:radial-gradient(circle at var(--cta-press-x) var(--cta-press-y),#12100c47 0%,#12100c29 18%,#12100c00 44%),
             radial-gradient(circle at calc(100% - var(--cta-press-x)) calc(100% - var(--cta-press-y)),#fff3 0%,#ffffff14 22%,#fff0 48%);
  transform:translate3d(calc(var(--cta-press-dx)*-1.5px),calc(var(--cta-press-dy)*-1.5px),0);
  transition:opacity var(--press-dur) ease, transform var(--press-dur) var(--press-ease)}
.cta.is-pressed::after{opacity:.82}
```

Measured on the live button: press at 30%/40% gave `--press-dx:-0.2`, `--press-dy:-0.1`, `::after` opacity 0.82, transform scale 0.976. The rotation and translate multipliers (4deg, 2.5px, 1.5px) were derived from that matrix; they reproduce the measured numbers. Keep `prefers-reduced-motion` users on a plain opacity change.
