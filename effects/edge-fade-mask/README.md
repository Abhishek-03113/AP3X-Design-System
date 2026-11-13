# Edge fade mask

A fixed bar that has no bottom border: content scrolls under a tinted blur that fades out. Colours and timings were read from the live page's computed styles; fonts are open substitutes (Newsreader for martina). No logos or photography were copied.

```css
.nav{position:sticky;top:0}
.nav::before{
  content:"";position:absolute;inset:0 0 -36px;z-index:-1;pointer-events:none;
  background:linear-gradient(rgba(237,232,225,.78) 0%, rgba(237,232,225,.55) 55%, rgba(237,232,225,0) 100%);
  backdrop-filter:blur(12px);
  mask-image:linear-gradient(#000 0%, #000 50%, transparent 100%);
}
```

The overhang (`-36px`) is the fade zone. Match the gradient colour to the page ground.
