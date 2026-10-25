"""Individual assets distilled from decimals.co (captured 2026-10-25)."""

SRC = {"name": "decimals.co", "url": "https://www.decimals.co/", "captured": "2026-10-25", "designSystem": "design-systems/decimals"}
FONTS = "https://fonts.googleapis.com/css2?family=Geist:wght@400;500&family=Newsreader:opsz,wght@6..72,400;6..72,500&family=La+Belle+Aurore&display=swap"
VARS = (
    "--cream:#ede8e1;--card:#f3eee6;--paper:#fffdf8;--ink:#4d4638;--ink-deep:#16130e;--ink-muted:#6e685d;--blush:#f4c9be;--rose:#dda697;"
    "--font-sans:'Geist',Arial,system-ui,sans-serif;--font-serif:'Newsreader',Georgia,serif;--font-script:'La Belle Aurore',cursive;"
    "--ease-out:cubic-bezier(.22,1,.36,1)"
)
NOTE = "Colours and timings were read from the live page's computed styles; fonts are open substitutes (Newsreader for martina). No logos or photography were copied."


def meta(kind, slug, title, summary, tags, tech):
    return {"slug": slug, "kind": kind, "title": title, "summary": summary, "source": SRC, "tags": tags, "tech": tech}


def asset(m, readme, css, html, script=None):
    return {"meta": m, "fonts": FONTS, "vars": VARS, "readme": readme, "css": css, "html": html, "script": script}


ASSETS = []

# ------------------------------------------------------------------ effects
ASSETS.append(asset(
    meta("effect", "glass-pill-depth", "Glass pill depth", "Layered shadow stack that gives pill buttons a pressed-paper, lit-from-above depth, in ink and glass variants.",
         ["shadow", "button", "glass", "light"], ["css box-shadow", "backdrop-filter"]),
    f"""
# Glass pill depth

Two shadow recipes that make flat pills feel physical. {NOTE}

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
""",
    """
.row{display:flex;gap:16px;padding:48px;background:linear-gradient(120deg,var(--cream),var(--blush));border-radius:12px}
.b{height:48px;padding:0 22px;border-radius:999px;font:500 14px/1 var(--font-sans);letter-spacing:-.14px;cursor:pointer}
.ink{background:var(--ink);color:var(--paper);border:1px solid var(--ink);box-shadow:0 0 0 1px rgba(18,18,18,.22),0 1px 2px rgba(18,18,18,.13),0 2px 8px rgba(18,18,18,.07),inset 0 0 0 1px rgba(255,255,255,.08),inset 0 1px 0 rgba(255,255,255,.16)}
.glass{background:rgba(255,253,248,.55) linear-gradient(rgba(255,255,255,.5),rgba(255,255,255,0));color:var(--ink);border:1px solid rgba(77,70,56,.25);box-shadow:0 1px 2px rgba(18,18,18,.06),0 2px 6px rgba(18,18,18,.04),inset 0 1px 0 rgba(255,255,255,.75);backdrop-filter:blur(10px)}
""",
    '<div class="row"><button class="b ink">Get started</button><button class="b glass">How it works</button></div>'))

ASSETS.append(asset(
    meta("effect", "edge-fade-mask", "Edge fade mask", "Blur-and-tint gradient masked to transparent so a sticky bar dissolves into the page with no visible edge.",
         ["mask", "blur", "nav", "gradient"], ["css mask-image", "backdrop-filter"]),
    f"""
# Edge fade mask

A fixed bar that has no bottom border: content scrolls under a tinted blur that fades out. {NOTE}

```css
.nav{{position:sticky;top:0}}
.nav::before{{
  content:"";position:absolute;inset:0 0 -36px;z-index:-1;pointer-events:none;
  background:linear-gradient(rgba(237,232,225,.78) 0%, rgba(237,232,225,.55) 55%, rgba(237,232,225,0) 100%);
  backdrop-filter:blur(12px);
  mask-image:linear-gradient(#000 0%, #000 50%, transparent 100%);
}}
```

The overhang (`-36px`) is the fade zone. Match the gradient colour to the page ground.
""",
    """
.stage{height:260px;overflow:auto;border-radius:12px;background:var(--cream);position:relative}
.nav{position:sticky;top:0;padding:18px 24px;font:500 14px var(--font-sans);display:flex;gap:20px}
.nav::before{content:"";position:absolute;inset:0 0 -36px;z-index:-1;pointer-events:none;background:linear-gradient(rgba(237,232,225,.78) 0%,rgba(237,232,225,.55) 55%,rgba(237,232,225,0) 100%);backdrop-filter:blur(12px);-webkit-mask-image:linear-gradient(#000 0%,#000 50%,transparent 100%);mask-image:linear-gradient(#000 0%,#000 50%,transparent 100%)}
.blk{height:90px;margin:16px 24px;border-radius:8px;background:var(--blush)}
.blk:nth-child(even){background:var(--rose)}
""",
    '<div class="stage"><div class="nav"><span>How it works</span><span>Placements</span><span>Blog</span></div><div class="blk"></div><div class="blk"></div><div class="blk"></div><div class="blk"></div></div><p>Scroll inside the frame.</p>'))

ASSETS.append(asset(
    meta("effect", "cta-press-glow", "CTA press glow", "Button that tilts toward the pointer on press while a multiply glow follows the touch point.",
         ["interaction", "button", "3d", "pointer"], ["css custom properties", "pointer events", "mix-blend-mode"]),
    f"""
# CTA press glow

On press the pill tilts about 0.8° toward the pointer, shrinks to 0.976, loses 2% brightness, and a dark radial blooms under the finger with a light one opposite. {NOTE}

## How it works
JS writes four variables on `pointerdown`: `--cta-press-x/y` (percent inside the button) and `--cta-press-dx/dy` (offset from centre, -0.5…0.5). CSS does the rest.

```css
.cta{{--press-dur:.15s;--press-ease:cubic-bezier(.22,1,.36,1);position:relative;
  transition:transform var(--press-dur) var(--press-ease), filter var(--press-dur) var(--press-ease)}}
.cta.is-pressed{{
  transform:translate3d(calc(var(--cta-press-dx)*2.5px),calc(var(--cta-press-dy)*2.5px),-2px)
            rotateX(calc(var(--cta-press-dy)*-4deg)) rotateY(calc(var(--cta-press-dx)*4deg)) scale(.976);
  filter:saturate(1.03) brightness(.98)}}
.cta::after{{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;opacity:0;mix-blend-mode:multiply;
  background:radial-gradient(circle at var(--cta-press-x) var(--cta-press-y),#12100c47 0%,#12100c29 18%,#12100c00 44%),
             radial-gradient(circle at calc(100% - var(--cta-press-x)) calc(100% - var(--cta-press-y)),#fff3 0%,#ffffff14 22%,#fff0 48%);
  transform:translate3d(calc(var(--cta-press-dx)*-1.5px),calc(var(--cta-press-dy)*-1.5px),0);
  transition:opacity var(--press-dur) ease, transform var(--press-dur) var(--press-ease)}}
.cta.is-pressed::after{{opacity:.82}}
```

Measured on the live button: press at 30%/40% gave `--press-dx:-0.2`, `--press-dy:-0.1`, `::after` opacity 0.82, transform scale 0.976. The rotation and translate multipliers (4deg, 2.5px, 1.5px) were derived from that matrix; they reproduce the measured numbers. Keep `prefers-reduced-motion` users on a plain opacity change.
""",
    """
.cta{--press-dur:.15s;--press-ease:cubic-bezier(.22,1,.36,1);--cta-press-x:50%;--cta-press-y:50%;--cta-press-dx:0;--cta-press-dy:0;position:relative;height:56px;padding:0 32px;border-radius:999px;border:1px solid var(--ink);background:var(--ink);color:var(--paper);font:500 15px/1 var(--font-sans);cursor:pointer;box-shadow:0 0 0 1px rgba(18,18,18,.22),0 1px 2px rgba(18,18,18,.13),0 2px 8px rgba(18,18,18,.07),inset 0 1px 0 rgba(255,255,255,.16);transition:transform var(--press-dur) var(--press-ease),filter var(--press-dur) var(--press-ease);touch-action:manipulation}
.cta.is-pressed{transform:perspective(600px) translate3d(calc(var(--cta-press-dx)*2.5px),calc(var(--cta-press-dy)*2.5px),-2px) rotateX(calc(var(--cta-press-dy)*-4deg)) rotateY(calc(var(--cta-press-dx)*4deg)) scale(.976);filter:saturate(1.03) brightness(.98)}
.cta::after{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;opacity:0;mix-blend-mode:multiply;background:radial-gradient(circle at var(--cta-press-x) var(--cta-press-y),#12100c47 0%,#12100c29 18%,#12100c00 44%),radial-gradient(circle at calc(100% - var(--cta-press-x)) calc(100% - var(--cta-press-y)),#fff3 0%,#ffffff14 22%,#fff0 48%);transform:translate3d(calc(var(--cta-press-dx)*-1.5px),calc(var(--cta-press-dy)*-1.5px),0);transition:opacity var(--press-dur) ease,transform var(--press-dur) var(--press-ease)}
.cta.is-pressed::after{opacity:.82}
@media (prefers-reduced-motion:reduce){.cta.is-pressed{transform:none}}
""",
    '<button class="cta">Press anywhere on me</button>',
    """
const b = document.querySelector('.cta');
const release = () => b.classList.remove('is-pressed');
b.addEventListener('pointerdown', e => {
  const r = b.getBoundingClientRect();
  const x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
  b.style.setProperty('--cta-press-x', x * 100 + '%');
  b.style.setProperty('--cta-press-y', y * 100 + '%');
  b.style.setProperty('--cta-press-dx', (x - .5).toFixed(3));
  b.style.setProperty('--cta-press-dy', (y - .5).toFixed(3));
  b.classList.add('is-pressed');
});
['pointerup', 'pointerleave', 'pointercancel'].forEach(t => b.addEventListener(t, release));
"""))

# ------------------------------------------------------------------ motions
ASSETS.append(asset(
    meta("motion", "logo-ticker", "Logo ticker", "Endless 46s linear marquee under edge masks that pauses on hover and dims everything except the hovered mark.",
         ["marquee", "loop", "hover", "mask"], ["css animation", "mask-image"]),
    f"""
# Logo ticker

{NOTE}

| Property | Value |
| --- | --- |
| Track | `display:flex; width:max-content`, content duplicated once |
| Keyframe | `to {{ transform: translateX(-50%) }}` |
| Duration / easing | 46s linear, infinite |
| Gap | 64px between items |
| Edge mask | `linear-gradient(90deg, transparent 0%, #000 10%, #000 90%, transparent 100%)` |
| Hover | strip pauses (`animation-play-state`), marks drop to 0.4 opacity, hovered mark returns to 1 (0.25s) |
| Reduced motion | animation removed |

Duplicate the item list exactly once so `-50%` lands on a seamless loop.
""",
    """
.cap{text-align:center;color:var(--ink-muted);margin:0 0 12px}
.t{overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent 0%,#000 10%,#000 90%,transparent 100%);mask-image:linear-gradient(90deg,transparent 0%,#000 10%,#000 90%,transparent 100%)}
.k{display:flex;align-items:center;width:max-content;animation:tick 46s linear infinite}
.t:hover .k{animation-play-state:paused}
.k span{margin-right:64px;font:500 24px/1 var(--font-serif);color:var(--ink);opacity:.92;transition:opacity .25s,filter .25s}
.k:hover span{opacity:.4}.k span:hover{opacity:1}
@keyframes tick{to{transform:translateX(-50%)}}
@media (prefers-reduced-motion:reduce){.k{animation:none}}
""",
    '<p class="cap">Hired by teams at</p><div class="t"><div class="k"><span>Northwind</span><span>Fieldnote</span><span>Orbital</span><span>Lumen</span><span>Parcel</span><span>Quill</span><span>Northwind</span><span>Fieldnote</span><span>Orbital</span><span>Lumen</span><span>Parcel</span><span>Quill</span></div></div>'))

ASSETS.append(asset(
    meta("motion", "hero-blur-reveal", "Hero blur reveal", "Hero content enters from 30% opacity and a 12px blur, with a CSS-only fallback that reveals it after 2.6s.",
         ["entrance", "blur", "hero", "progressive-enhancement"], ["css animation", "css transition"]),
    f"""
# Hero blur reveal

{NOTE}

Hero children start dimmed and blurred and are released by JS (a transition of `opacity, filter` over 0.25s). If JS never runs, a keyframe fallback reveals them anyway.

```css
html:not(.js-ready) .hero > * {{
  opacity:.3; filter:blur(12px);
  animation:reveal .6s ease 2.6s 1 forwards;      /* fallback after 2.6s */
}}
@keyframes reveal {{ 100% {{ opacity:1; filter:none }} }}
.hero > * {{ transition:opacity .25s ease, filter .25s ease }}
@media (prefers-reduced-motion:reduce) {{
  html:not(.js-ready) .hero > * {{ opacity:1; filter:none; animation:none }}
}}
```

The fallback timing (0.6s ease, 2.6s delay) and the 0.3 / 12px start state are measured. The per-child stagger is not documented here; add `transition-delay` in steps of about 60ms for a sequenced entrance.
""",
    """
.hero{text-align:center;padding:48px 0}
.hero>*{opacity:.3;filter:blur(12px);transition:opacity .25s ease,filter .25s ease}
.hero.in>*{opacity:1;filter:none}
.hero.in>*:nth-child(2){transition-delay:.06s}.hero.in>*:nth-child(3){transition-delay:.12s}
h1{font:500 48px/1.15 var(--font-serif);letter-spacing:-.04em;margin:0 0 12px}
p{font-size:18px;color:var(--ink-muted);margin:0 0 20px}
.btn{height:44px;padding:0 20px;border-radius:999px;background:var(--ink);color:var(--paper);border:0;font:500 14px var(--font-sans)}
.replay{margin:0 auto;display:block;background:none;border:1px solid var(--ink-muted);border-radius:999px;padding:6px 14px;color:var(--ink);font:500 13px var(--font-sans);cursor:pointer}
@media (prefers-reduced-motion:reduce){.hero>*{opacity:1;filter:none;transition:none}}
""",
    '<section class="hero" id="h"><h1>Hire designers who care</h1><p>A scout network for hiring designers</p><button class="btn">Get started</button></section><button class="replay" id="r">Replay</button>',
    """
const h = document.getElementById('h');
const play = () => { h.classList.remove('in'); void h.offsetWidth; requestAnimationFrame(() => h.classList.add('in')); };
document.getElementById('r').addEventListener('click', play);
setTimeout(play, 300);
"""))

ASSETS.append(asset(
    meta("motion", "ambient-drift", "Ambient drift", "Two huge blush radial blobs drifting on 52s and 64s ease-in-out loops behind sticky page content.",
         ["background", "loop", "ambient", "gradient"], ["css animation", "radial-gradient"]),
    f"""
# Ambient drift

A page-wide, pointer-events-none layer: `position:sticky; height:100vh; margin-bottom:-100vh` so it stays behind content while the page scrolls. {NOTE}

| Blob | Size | Position | Fill | Loop |
| --- | --- | --- | --- | --- |
| A | 74vw circle | 38% / 58% | `radial-gradient(circle, rgba(244,201,190,.42), rgba(244,201,190,0) 62%)` | 52s ease-in-out |
| B | 62vw circle | 84% / 72% | `radial-gradient(circle, rgba(221,166,151,.24), rgba(221,166,151,0) 62%)` | 64s ease-in-out |

```css
@keyframes drift-a {{
  0%,100% {{ transform:translate(-50%,-50%) }}
  33% {{ transform:translate(calc(-50% + 9vw), calc(-50% - 7vh)) scale(1.12) }}
  66% {{ transform:translate(calc(-50% - 6vw), calc(-50% + 5vh)) scale(.94) }}
}}
@keyframes drift-b {{
  0%,100% {{ transform:translate(-50%,-50%) }}
  40% {{ transform:translate(calc(-50% - 10vw), calc(-50% - 8vh)) scale(1.1) }}
  75% {{ transform:translate(calc(-50% + 7vw), calc(-50% + 4vh)) scale(.96) }}
}}
```

Reduced motion: remove both animations. The coprime durations keep the two blobs from ever syncing.
""",
    """
.amb{position:relative;height:300px;overflow:hidden;border-radius:12px;background:var(--cream)}
.blob{position:absolute;border-radius:50%;pointer-events:none}
.a{width:74%;aspect-ratio:1;top:58%;left:38%;background:radial-gradient(circle,rgba(244,201,190,.42) 0%,rgba(244,201,190,0) 62%);animation:da 52s ease-in-out infinite}
.b{width:62%;aspect-ratio:1;top:72%;left:84%;background:radial-gradient(circle,rgba(221,166,151,.24) 0%,rgba(221,166,151,0) 62%);animation:db 64s ease-in-out infinite}
.txt{position:relative;padding:32px;font:500 28px/1.2 var(--font-serif);letter-spacing:-.03em}
@keyframes da{0%,100%{transform:translate(-50%,-50%)}33%{transform:translate(calc(-50% + 9vw),calc(-50% - 7vh)) scale(1.12)}66%{transform:translate(calc(-50% - 6vw),calc(-50% + 5vh)) scale(.94)}}
@keyframes db{0%,100%{transform:translate(-50%,-50%)}40%{transform:translate(calc(-50% - 10vw),calc(-50% - 8vh)) scale(1.1)}75%{transform:translate(calc(-50% + 7vw),calc(-50% + 4vh)) scale(.96)}}
@media (prefers-reduced-motion:reduce){.blob{animation:none}}
""",
    '<div class="amb"><div class="blob a"></div><div class="blob b"></div><div class="txt">Traditional recruiting stopped working</div></div>'))

ASSETS.append(asset(
    meta("motion", "float-in", "Float in", "Ten-pixel rise with fade, plus a slow ping-ring for live indicators.",
         ["entrance", "fade", "indicator"], ["css animation"]),
    f"""
# Float in + ping slow

Two small keyframes the site keeps in its sheet. {NOTE}

```css
@keyframes float-in {{ 0% {{ opacity:0; transform:translateY(10px) }} 100% {{ opacity:1; transform:translateY(0) }} }}
@keyframes ping-slow {{ 0% {{ opacity:.7; transform:scale(1) }} 100% {{ opacity:0; transform:scale(2.4) }} }}
```

Durations are not set in the keyframe sheet; the preview uses 0.5s `cubic-bezier(.22,1,.36,1)` for `float-in` (the site's movement easing) and 2s for `ping-slow`. Treat those two as starting values.
""",
    """
.card{width:260px;padding:20px;border-radius:8px;background:var(--card);animation:float-in .5s var(--ease-out) both}
.card:nth-child(2){animation-delay:.1s}.card:nth-child(3){animation-delay:.2s}
.wrap{display:flex;gap:16px}
.live{position:relative;display:inline-block;width:10px;height:10px;border-radius:50%;background:#438f31;margin-right:10px}
.live::after{content:"";position:absolute;inset:0;border-radius:50%;background:#438f31;animation:ping-slow 2s ease-out infinite}
@keyframes float-in{0%{opacity:0;transform:translateY(10px)}100%{opacity:1;transform:translateY(0)}}
@keyframes ping-slow{0%{opacity:.7;transform:scale(1)}100%{opacity:0;transform:scale(2.4)}}
@media (prefers-reduced-motion:reduce){.card,.live::after{animation:none}}
""",
    '<div class="wrap"><div class="card"><span class="live"></span>Scouts online</div><div class="card">Curated shortlist</div><div class="card">Offer support</div></div>'))

# ------------------------------------------------------------------ components
ASSETS.append(asset(
    meta("component", "decimals-pill-button", "Pill button pair", "Filled ink and glass call-to-action pills, 36px and 48px, with the layered shadow stack.",
         ["button", "cta", "pill"], ["css"]),
    f"""
# Pill button pair

Primary (`ink` fill) and secondary (glass) pills. {NOTE}

| Size | Height | Side padding | Text |
| --- | --- | --- | --- |
| default | 36px | 16px | Geist 500 14px, -0.14px tracking |
| large | 48px | 22px | same |

Shadows and glass fill: see `effects/glass-pill-depth`. Press behaviour: `effects/cta-press-glow`. Hover opacity 0.2s.
""",
    """
.row{display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.b{height:36px;padding:0 16px;border-radius:999px;font:500 14px/1 var(--font-sans);letter-spacing:-.14px;cursor:pointer;transition:opacity .2s,transform .15s var(--ease-out)}
.b:hover{opacity:.92}.b:active{transform:scale(.976)}
.lg{height:48px;padding:0 22px}
.ink{background:var(--ink);color:var(--paper);border:1px solid var(--ink);box-shadow:0 0 0 1px rgba(18,18,18,.22),0 1px 2px rgba(18,18,18,.13),0 2px 8px rgba(18,18,18,.07),inset 0 0 0 1px rgba(255,255,255,.08),inset 0 1px 0 rgba(255,255,255,.16)}
.glass{background:rgba(255,253,248,.55) linear-gradient(rgba(255,255,255,.5),rgba(255,255,255,0));color:var(--ink);border:1px solid rgba(77,70,56,.25);box-shadow:0 1px 2px rgba(18,18,18,.06),0 2px 6px rgba(18,18,18,.04),inset 0 1px 0 rgba(255,255,255,.75);backdrop-filter:blur(10px)}
""",
    '<div class="row"><button class="b ink lg">Get started</button><button class="b glass lg">How it works</button><button class="b ink">Get started</button><button class="b glass">Log in</button></div>'))

ASSETS.append(asset(
    meta("component", "decimals-nav-bar", "Nav bar", "Three-zone floating nav (wordmark, links, pills) over a blur-fade gradient.",
         ["navigation", "header", "sticky"], ["css"]),
    f"""
# Nav bar

Wordmark left, links centred (Geist 14px, 55% ink, hover to full ink in 0.2s, 12px × 8px padding), pill pair right. The background uses `effects/edge-fade-mask`. {NOTE}
""",
    """
.n{position:relative;display:flex;align-items:center;justify-content:space-between;padding:12px 8px}
.n::before{content:"";position:absolute;inset:0 0 -36px;z-index:-1;background:linear-gradient(rgba(237,232,225,.78),rgba(237,232,225,.55) 55%,rgba(237,232,225,0));backdrop-filter:blur(12px);-webkit-mask-image:linear-gradient(#000 50%,transparent);mask-image:linear-gradient(#000 50%,transparent)}
.w{font:500 22px/1 var(--font-serif);letter-spacing:.12em}
.l{display:flex;gap:20px;letter-spacing:-.14px}
.l a{padding:12px 8px;color:rgba(77,70,56,.55);transition:color .2s;cursor:pointer}.l a:hover{color:var(--ink)}
.p{display:flex;gap:8px}
.p span{height:36px;padding:0 16px;border-radius:999px;display:inline-flex;align-items:center;font-weight:500;letter-spacing:-.14px}
.a{background:var(--ink);color:var(--paper);box-shadow:0 0 0 1px rgba(18,18,18,.22),0 1px 2px rgba(18,18,18,.13),inset 0 1px 0 rgba(255,255,255,.16)}
.g{background:rgba(255,253,248,.55);border:1px solid rgba(77,70,56,.25);box-shadow:inset 0 1px 0 rgba(255,255,255,.75)}
""",
    '<div class="n"><span class="w">STUDIO</span><nav class="l"><a>How it works</a><a>Placements</a><a>Become a Scout</a><a>Blog</a></nav><div class="p"><span class="a">Get started</span><span class="g">Log in</span></div></div>'))

ASSETS.append(asset(
    meta("component", "decimals-testimonial-row", "Testimonial row", "Two-column proof row: copy and pinned quote beside a blush portrait panel with a handwritten tag.",
         ["card", "testimonial", "content"], ["css"]),
    f"""
# Testimonial row

Copy on a `card` surface (torn-edge `clip-path` in the original; the preview uses a simple polygon), portrait panel beside it, alternating sides. Quote and attribution are pinned to the bottom. Portrait is a black-and-white cut-out with white stroke on a blush ground, image blended with `multiply`; supply your own. {NOTE}

Copy: `heading` 28px/37.8px -0.03em serif; paragraph 16px/24px at 80% ink; quote 13px.
""",
    """
.r{display:grid;grid-template-columns:1fr 1fr;background:var(--card);min-height:260px;clip-path:polygon(0 1%,3% 0,12% 1%,25% 0,40% 1%,58% 0,75% 1%,90% 0,100% 1%,100% 99%,92% 100%,70% 99%,50% 100%,30% 99%,10% 100%,0 99%)}
.c{padding:28px;display:flex;flex-direction:column;justify-content:space-between}
h3{margin:0 0 10px;font:400 28px/37.8px var(--font-serif);letter-spacing:-.84px}
p{margin:0;max-width:32ch;font-size:16px;line-height:24px;color:rgba(77,70,56,.8)}
.q{font-size:13px;line-height:19px;color:var(--ink-muted)}.q b{font-weight:500;color:var(--ink)}
.i{margin:8px;border-radius:8px;background:linear-gradient(160deg,#fde3da,var(--blush));position:relative}
.i span{position:absolute;right:16px;bottom:14px;font:400 26px/1 var(--font-script);color:rgba(217,79,61,.55);transform:rotate(-8deg)}
""",
    '<div class="r"><div class="c"><div><h3>Skip straight to the shortlist</h3><p>You\'ll get a curated handful worth meeting, with your feedback refining each round.</p></div><div class="q">“Everyone you get is designer good, not just recruiter good.” <b>Lead Product Designer</b></div></div><div class="i" role="img" aria-label="Portrait placeholder"><span>Hiring Manager</span></div></div>'))

# ------------------------------------------------------------------ sites
ASSETS.append(asset(
    meta("site", "decimals", "Decimals site", "Warm-paper recruiting site: dotted-globe hero, logo ticker, alternating proof rows, torn-paper problem cards, ambient glow.",
         ["site", "landing", "recruiting", "warm", "serif"], ["next.js", "css", "canvas"]),
    f"""
# Decimals — site design

Landing page of a scout network for hiring designers, captured at 1440×900. {NOTE}

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
""",
    """
.frame{border-radius:12px;overflow:hidden;background:var(--cream);box-shadow:0 0 0 1px rgba(77,70,56,.2)}
.nav{display:flex;justify-content:space-between;align-items:center;padding:14px 24px}
.w{font:500 20px var(--font-serif);letter-spacing:.12em}
.pill{height:32px;padding:0 14px;border-radius:999px;background:var(--ink);color:var(--paper);display:inline-flex;align-items:center;font-weight:500}
.hero{text-align:center;padding:48px 24px 0;position:relative;overflow:hidden;height:340px}
h1{margin:0 auto 10px;max-width:15ch;font:500 44px/1.15 var(--font-serif);letter-spacing:-.04em}
.hero p{color:var(--ink-muted);margin:0 0 18px}
.globe{position:absolute;left:50%;bottom:-210px;width:560px;height:560px;margin-left:-280px;border-radius:50%;border:1px solid rgba(77,70,56,.25);background:radial-gradient(circle at 50% 30%,rgba(244,201,190,.5),transparent 60%),repeating-radial-gradient(circle at 50% 50%,rgba(77,70,56,.28) 0 1px,transparent 1px 7px);-webkit-mask-image:linear-gradient(#000 40%,transparent 80%);mask-image:linear-gradient(#000 40%,transparent 80%);z-index:0}
.hero>*:not(.globe){position:relative;z-index:1}
.sec{padding:20px 24px 28px;background:var(--card)}
.sec h2{margin:0 0 6px;font:400 24px/1.3 var(--font-serif);letter-spacing:-.03em}
""",
    '<div class="frame"><div class="nav"><span class="w">STUDIO</span><span class="pill">Get started</span></div><div class="hero"><div class="globe"></div><h1>Hire designers who care</h1><p>A scout network for hiring designers</p><span class="pill">Get started</span></div><div class="sec"><h2>Traditional recruiting stopped working</h2><p>Layout sketch only: see the README for the full page structure.</p></div></div>'))
