A ranked list with a soft bar behind each name: top sources, pages, locations.

- Well and header as `StatCard` (title left, unit right, both `label` `muted-foreground`); inner card `background`, `radius-lg`, `space-1` padding.
- Rows: 32px, `radius-md`, name in `label` `foreground`, value in `label` `muted-foreground` with tabular numerals. The bar is a `data-*-soft` fill sized to the value, drawn behind the row; pick the hue by what is measured (`data-traffic-soft` for visitors).
- Provide rows sorted high to low; widths are value ÷ the top value.
