"""Build every design system folder under design-systems/ and report text contrast.

Usage: python3 tools/build.py
"""
import re
import sys

import systems_a
import systems_b
from ds_lib import build

SYSTEMS = systems_a.SYSTEMS + systems_b.SYSTEMS


def rgb(v, ground=(255, 255, 255)):
    v = v.strip()
    if v.startswith("#"):
        h = v[1:]
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.match(r"rgba?\(([^)]*)\)", v)
    parts = [float(x) for x in m.group(1).replace("/", ",").split(",")]
    a = parts[3] if len(parts) > 3 else 1
    return tuple(round(parts[i] * a + ground[i] * (1 - a)) for i in range(3))


def lum(c):
    def ch(x):
        x /= 255
        return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(x) for x in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    a, b = lum(fg), lum(bg)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def colors(spec, theme):
    out = {}
    for t in spec["colors"]:
        v = t["value"]
        out[t["name"]] = v if isinstance(v, str) else v.get(theme, next(iter(v.values())))
    return out


# (text, ground) pairs whose ratios the usage notes quote
PAIRS = {
    "odyssee": [("navy", "cream"), ("navy", "stone"), ("navy-muted", "cream"), ("white", "navy"), ("white", "charcoal"), ("clay", "cream")],
    "letude": [("cobalt", "haze"), ("cobalt", "signal"), ("ink", "haze"), ("ink", "signal"), ("paper", "cobalt")],
    "brik": [("ink", "canvas"), ("ink-2", "canvas"), ("ink-2", "panel"), ("ink-3", "canvas"), ("surface", "dark"), ("surface", "electric"), ("ink", "go"), ("ink", "tag-orange"), ("ink", "tag-blue"), ("ink", "tag-green"), ("ink", "tag-coral"), ("ink", "tag-pink")],
    "aino": [("ink", "paper"), ("ink-60", "paper")],
    "the-design-society": [("white", "electric"), ("lime", "electric"), ("ink", "lime"), ("ink", "mist"), ("smoke", "night"), ("smoke", "electric"), ("lime", "mist"), ("ink", "white")],
    "surfers-journal-archives": [("ink", g) for g in ["sea-glass", "tangerine", "blush", "olive", "butter", "harbour", "sand"]] + [("paper", "deep-water")],
    "celine-ka-wing-lau": [("ink", "highlighter")] + [("line", g) for g in ["lilac", "sky", "tomato", "tangerine", "frog", "bubblegum", "paper"]],
    "andmade": [("ink", "paper"), ("ink-50", "paper"), ("link-blue", "paper"), ("white", "ink")],
    "united-carriers": [("fg", "bg"), ("fg-muted", "bg"), ("fg-subtle", "bg"), ("fg", "bg-raised"), ("bg", "fg")],
    "seventeen": [("black", "white"), ("stone", "white"), ("black", "stone"), ("white", "brick"), ("white", "harbour"), ("black", "field"), ("black", "lime"), ("white", "ochre"), ("black", "lagoon"), ("black", "candy"), ("white", "cobalt"), ("white", "umber"), ("black", "lilac"), ("black", "aqua")],
}

if __name__ == "__main__":
    for spec in SYSTEMS:
        path = build(spec)
        print(f"built {spec['slug']}")
        for theme in [t["id"] for t in spec.get("themes", [{"id": "light"}])]:
            c = colors(spec, theme)
            row = []
            for fg, bg in PAIRS.get(spec["slug"], []):
                g = rgb(c[bg])
                row.append(f"{fg}/{bg} {ratio(rgb(c[fg], g), g):.1f}")
            print(f"  [{theme}] " + " | ".join(row))
