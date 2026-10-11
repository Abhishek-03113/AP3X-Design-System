The Surfer's Journal Archives is the digital library of every issue of *The Surfer's Journal*. Each page takes the colourway of the issue on show: a flat pastel ground, black serif type at the corners, and the cover photograph as the only image. Built from the public site archives.surfersjournal.com; the typeface is an open substitute.

## Voice

- Librarian-quiet. Nav words are single nouns: Issues, Collections, Search, Library.
- Numbers carry the content: the year (2026), the issue (35.5), the count ("All (188)").

## Colour

- Pick ONE colourway per page from `sea-glass`, `tangerine`, `blush`, `olive`, `butter`, `harbour`, `sand`, and fill the whole viewport with it. Never place two colourways side by side except in the issue index.
- Everything else is `ink`. `paper` appears only on photography.
- `deep-water` is a placeholder for a cover still loading.

## Typography

- One serif family. The site uses **Practice**; this system substitutes **EB Garamond**.
- Corners carry `display` numerals; nav is `body` (20px); the masthead is the only uppercase line.
- Underline the current nav item (1px, offset `space-1`).

## Layout

- A fixed three-part top bar (nav left, masthead centre, Library right) and a three-part bottom bar (year left, "All (188)" centre, issue number right).
- The cover is centred on the stage at roughly 30% of the viewport width with a flat edge; no shadow, no radius.

## Imagery

- Only the issue's own cover art. No logo file ships; set the masthead in type.

## Components

`TopBar`, `IssueStage` and `ColourwayIndex` are static previews built on the tokens above.
