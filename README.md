# AP3X Design System

Ten Claude Design Systems, each distilled from a site featured on [Site of Sites](https://www.siteofsites.co/?p=1). Every folder under `design-systems/<slug>/project/` is the exact file tree of a Claude Design System artifact: `design-system.json` (index), `tokens.json`, a `README.md` brand book, three component previews and a cover.

The existing **Apple HIG** system (https://claude.ai/artifact/TiFCULRVtSBGMNiXwdaHtM) lives only as an artifact and is not touched by anything here.

| System | Source site | Artifact | Look |
| --- | --- | --- | --- |
| Odyssée | [odysseeclinic.com.au](https://www.odysseeclinic.com.au/) | [open](https://claude.ai/artifact/XNppTtkxdTkXgZCUCdmxAm) | Navy on cream, light serif, uppercase sans |
| L'Étude | [letude.group](https://letude.group/) | [open](https://claude.ai/artifact/P9yhCeV1yFYQ5mSfHifaBe) | Cobalt on periwinkle haze, signal-red field |
| Brik | [brik.space](https://brik.space/home) | [open](https://claude.ai/artifact/7a2eXmbYYUropwzVWex9f9) | Square grey tool chrome, one electric-blue action |
| Aino | [aino.agency](https://aino.agency/) | [open](https://claude.ai/artifact/Sw3geFUhXLadAcs1gkyPko) | One ink on paper, ASCII art |
| The Design Society | [thedesignsociety.fr](https://www.thedesignsociety.fr/) | [open](https://claude.ai/artifact/APSBmg5f2JfnUtNJ9W2ciU) | Electric blue, acid lime, pixel type |
| Surfer's Journal Archives | [archives.surfersjournal.com](https://archives.surfersjournal.com/) | [open](https://claude.ai/artifact/P3pLjTF6jeXwJDDBxR3WWH) | One pastel colourway per issue, black serif |
| Celine Ka Wing Lau | [celinelkw.com](https://celinelkw.com/) | [open](https://claude.ai/artifact/K8BU2yGntiRW5JpryEmaad) | Highlighter yellow, outlined drawn objects |
| ANDMADE | [andmade.jp](https://andmade.jp/) | [open](https://claude.ai/artifact/CkLZm2Z8WodZtvFxmJVd3e) | Quiet index on warm paper, typewriter dates |
| United Carriers | [unitedcarriers.com](https://unitedcarriers.com/) | [open](https://claude.ai/artifact/DLPoqZ8sF29ykcmLikiGu3) | Light + dark themes, wide uppercase, pills |
| Seventeen | [seventeenagency.com](https://www.seventeenagency.com/) | [open](https://claude.ai/artifact/6QHX6Az7bjnKaruu9mhb6B) | White space, condensed type, 11-band spectrum |

## How these were made

- Colours, type sizes, line heights, letter-spacing and radii were measured from each live site's computed styles (headless Chromium, 1440px viewport) on 2026-10-11, plus pixel sampling for illustration colours.
- The sites' typefaces are licensed, so each system names the original and substitutes the closest Google Font. Swap the `type.families` entries if you hold the originals.
- No logos or illustrations were copied; each README says so and sets the name in type.
- Every text/ground pair named in a token note was contrast-checked. Where the source's own pair misses WCAG AA (e.g. L'Étude cobalt on haze 4.4:1, Seventeen stone on white 2.2:1, ANDMADE 50% ink 3.9:1), the value is kept exact and the note flags it.

## Regenerating

The systems are generated from `tools/systems_a.py` and `tools/systems_b.py`:

```sh
python3 tools/build.py   # rewrites design-systems/*/project and prints contrast ratios
```

To push a change to an artifact, republish the changed `project/` files to that system's URL (index last).
