# Glass pill depth

Two shadow recipes that make flat pills feel physical. Colours and timings were read from the live page's computed styles; fonts are open substitutes (Newsreader for martina). No logos or photography were copied.

## Ink pill (filled)
```css
box-shadow:
  0 0 0 1px rgba(18,18,18,.22),          /* hairline ring */
  0 1px 2px rgba(18,18,18,.13),          /* contact shadow */
  0 2px 8px rgba(18,18,18,.07),          /* soft drop */
  inset 0 0 0 1px rgba(255,255,255,.08), /* inner rim */
  inset 0 1px 0 rgba(255,255,255,.16);   /* top light */
background:#4d4638; border:1px solid #4d4638; border-radius:999px;
```

## Glass pill
```css
background:rgba(255,253,248,.55) linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,0));
border:1px solid rgba(77,70,56,.25);
box-shadow:0 1px 2px rgba(18,18,18,.06), 0 2px 6px rgba(18,18,18,.04), inset 0 1px 0 rgba(255,255,255,.75);
backdrop-filter:blur(10px);
```

Use on a textured or tinted ground; on flat white the glass variant disappears.
