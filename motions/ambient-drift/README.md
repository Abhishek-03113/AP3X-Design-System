# Ambient drift

A page-wide, pointer-events-none layer: `position:sticky; height:100vh; margin-bottom:-100vh` so it stays behind content while the page scrolls. Colours and timings were read from the live page's computed styles; fonts are open substitutes (Newsreader for martina). No logos or photography were copied.

| Blob | Size | Position | Fill | Loop |
| --- | --- | --- | --- | --- |
| A | 74vw circle | 38% / 58% | `radial-gradient(circle, rgba(244,201,190,.42), rgba(244,201,190,0) 62%)` | 52s ease-in-out |
| B | 62vw circle | 84% / 72% | `radial-gradient(circle, rgba(221,166,151,.24), rgba(221,166,151,0) 62%)` | 64s ease-in-out |

```css
@keyframes drift-a {
  0%,100% { transform:translate(-50%,-50%) }
  33% { transform:translate(calc(-50% + 9vw), calc(-50% - 7vh)) scale(1.12) }
  66% { transform:translate(calc(-50% - 6vw), calc(-50% + 5vh)) scale(.94) }
}
@keyframes drift-b {
  0%,100% { transform:translate(-50%,-50%) }
  40% { transform:translate(calc(-50% - 10vw), calc(-50% - 8vh)) scale(1.1) }
  75% { transform:translate(calc(-50% + 7vw), calc(-50% + 4vh)) scale(.96) }
}
```

Reduced motion: remove both animations. The coprime durations keep the two blobs from ever syncing.
