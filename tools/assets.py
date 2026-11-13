"""Build the individual asset library (effects/, motions/, components/, sites/) and its index.

Each asset lives alone in <kind>/<slug>/ with meta.json, README.md and a standalone preview.html.
Assets are declared in tools/assets_*.py as dicts; this script writes them and regenerates
assets/INDEX.md plus the asset table in README.md.

Usage: python3 tools/assets.py          # write every asset, validate, rebuild the index
       python3 tools/assets.py --check  # validate existing meta.json files only
"""
import json
import os
import sys

import assets_decimals
import assets_resurf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KINDS = {"effect": "effects", "motion": "motions", "component": "components", "site": "sites"}
REQUIRED = ["slug", "kind", "title", "summary", "source", "tags"]

ASSETS = assets_decimals.ASSETS + assets_resurf.ASSETS

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
{link}<style>
:root{{{vars}}}
*{{box-sizing:border-box}}
html,body{{margin:0}}
body{{background:var(--cream);color:var(--ink);font:400 14px/21px var(--font-sans);padding:32px}}
{css}
</style>
</head>
<body>
{body}
{script}</body>
</html>
"""


def validate(meta):
    missing = [k for k in REQUIRED if k not in meta]
    if missing:
        raise SystemExit(f"{meta.get('slug', '?')}: missing {missing}")
    if meta["kind"] not in KINDS:
        raise SystemExit(f"{meta['slug']}: bad kind {meta['kind']}")


def write_asset(a):
    meta = a["meta"]
    validate(meta)
    d = os.path.join(ROOT, KINDS[meta["kind"]], meta["slug"])
    os.makedirs(d, exist_ok=True)
    base = ["meta.json", "README.md", "preview.html"]
    meta = dict(meta, files=base + sorted(f for f in os.listdir(d) if f not in base))
    link = f'<link rel="stylesheet" href="{a["fonts"]}">\n' if a.get("fonts") else ""
    script = f"<script>\n{a['script'].strip()}\n</script>\n" if a.get("script") else ""
    html = PAGE.format(title=meta["title"], link=link, vars=a["vars"], css=a["css"].strip(), body=a["html"].strip(), script=script)
    for name, text in (("meta.json", json.dumps(meta, indent=2, ensure_ascii=False) + "\n"),
                       ("README.md", a["readme"].strip() + "\n"), ("preview.html", html)):
        with open(os.path.join(d, name), "w", encoding="utf-8") as f:
            f.write(text)
    return meta


def collect():
    out = []
    for kind, folder in KINDS.items():
        base = os.path.join(ROOT, folder)
        if not os.path.isdir(base):
            continue
        for slug in sorted(os.listdir(base)):
            p = os.path.join(base, slug, "meta.json")
            if os.path.isfile(p):
                meta = json.load(open(p, encoding="utf-8"))
                validate(meta)
                out.append(meta)
    return out


def table(metas):
    rows = ["| Asset | Kind | What it is | Source | Tags |", "| --- | --- | --- | --- | --- |"]
    for m in sorted(metas, key=lambda m: (m["kind"], m["slug"])):
        src = m["source"]
        link = f"[{src['name']}]({src['url']})"
        rows.append(f"| [{m['title']}]({KINDS[m['kind']]}/{m['slug']}) | {m['kind']} | {m['summary']} | {link} | {', '.join(m['tags'])} |")
    return "\n".join(rows)


def update_readme(metas):
    p = os.path.join(ROOT, "README.md")
    text = open(p, encoding="utf-8").read()
    a, b = "<!-- assets:start -->", "<!-- assets:end -->"
    block = f"{a}\n{table(metas)}\n{b}"
    if a in text:
        text = text[:text.index(a)] + block + text[text.index(b) + len(b):]
    else:
        text = text.rstrip() + f"\n\n## Individual assets\n\nEffects, motions, components and site designs are stored one per folder, with a standalone `preview.html` (open it directly in a browser), a `README.md` and a `meta.json`. Regenerate with `python3 tools/assets.py`.\n\n{block}\n"
    open(p, "w", encoding="utf-8").write(text)


if __name__ == "__main__":
    if "--check" not in sys.argv:
        for a in ASSETS:
            write_asset(a)
    metas = collect()
    update_readme(metas)
    print(f"{len(metas)} assets: " + ", ".join(f"{k} {sum(m['kind'] == k for m in metas)}" for k in KINDS))
