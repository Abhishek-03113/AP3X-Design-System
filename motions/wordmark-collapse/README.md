# Wordmark collapse

Measured on 2026-10-25 by stepping the live page down at 1440×900 and sampling computed transform, opacity and filter (tools/capture-scroll.js, plus 10–60px fine scans). Values marked *derived* are fitted to those samples.

At the top the nav shows the full wordmark. Between 50px and 59px of scroll (threshold *derived* from the two samples that bracket it) a class flips and the letters slide left into the monogram, then reverse on return.

## Letters (DECIMALS)
| Letter | translateX when collapsed | delay |
| --- | --- | --- |
| D | none (fades in place) | 0.06s |
| E | −11.96px | 0.11s |
| C | −23.92px | 0.132s |
| I, M, A, L, S | −35.88 … −83.72px (−11.96px × index) | 0.154s … 0.242s (+0.022s each) |

Each letter: `transition: opacity .24s ease, transform .34s cubic-bezier(.22,1,.36,1)`; collapsed `opacity:0`.

## Monogram
Hidden: `opacity:0; transform:translateY(-10px) scale(.82)`. Shown: `opacity:1; scale(1)`. `transition: opacity .22s ease, transform .3s cubic-bezier(.34,1.36,.64,1)`: the 1.36 control point gives the overshoot (scale reached 1.0045 before settling).

Reduced motion: swap without transitions.
