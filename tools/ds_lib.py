"""Shared helpers for building Claude Design System folders.

Each system is described by a spec dict (see tools/systems_*.py) and written to
design-systems/<slug>/project/ in the layout the Design System artifact type reads.
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "design-systems")


def tok(name, value, usage):
    return {"name": name, "value": value, "usage": usage}


def style(name, size, lh, weight, usage, ls=None, sample=None, family=None, transform=None):
    s = {"name": name, "fontSize": size, "lineHeight": lh, "fontWeight": weight, "usage": usage}
    if ls is not None:
        s["letterSpacing"] = ls
    if sample:
        s["sample"] = sample
    if family:
        s["family"] = family
    return s


def preview(group, height, fonts_href, css, body, subtitle=None):
    sub = f' subtitle="{subtitle}"' if subtitle else ""
    link = f'<link rel="stylesheet" href="{fonts_href}">\n' if fonts_href else ""
    return (
        f'<!-- @dsCard group="{group}" height={height}{sub} -->\n'
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        f"{link}<style>\n"
        "html,body{margin:0}\n"
        f"{css.strip()}\n</style>\n</head>\n<body>\n{body.strip()}\n</body>\n</html>\n"
    )


def cover(spec):
    c = spec["cover"]
    href = spec["fonts_href"]
    lines = c["name_lines"]
    name_html = "<br>".join(lines)
    return (
        "<!-- @dsCard height=288 -->\n<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        f"<title>{spec['title']}</title>\n"
        + (f'<link rel="stylesheet" href="{href}">\n' if href else "")
        + "<style>\n"
        "  html, body { margin:0; height:100%; }\n"
        f"  body {{ background:var(--{c['ground']}); color:var(--{c['ink']}); font-family:var(--font-{c['body_font']}); overflow:hidden; }}\n"
        "  .cover { position:relative; height:288px; overflow:hidden; }\n"
        "  .art { position:absolute; top:0; left:480px; width:480px; height:288px; overflow:hidden; }\n"
        "  .art svg { display:block; width:480px; height:288px; }\n"
        f"{c['css']}\n"
        "  .words { position:absolute; left:32px; bottom:28px; max-width:440px; }\n"
        f"  .name {{ margin:0; font-family:var(--font-{c['name_font']}); font-size:{c['name_size']}px; line-height:{c.get('leading', .95)}; "
        f"font-weight:{c.get('name_weight', 400)}; letter-spacing:{c.get('name_ls', '0')}; color:var(--{c['ink']}); {c.get('name_extra', '')} }}\n"
        f"  .tag {{ margin:10px 0 0 2px; font-size:14px; line-height:20px; color:var(--{c['muted']}); }}\n"
        "</style>\n</head>\n<body>\n<div class=\"cover\">\n<div class=\"art\" aria-hidden=\"true\">\n"
        "<svg viewBox=\"0 0 480 288\" width=\"480\" height=\"288\">\n"
        f"<!--\n{c['derivation'].strip()}\n-->\n{c['svg'].strip()}\n</svg>\n</div>\n"
        f"<div class=\"words\">\n<h1 class=\"name\">{name_html}</h1>\n<p class=\"tag\">{c['tagline']}</p>\n</div>\n</div>\n</body>\n</html>\n"
    )


def build(spec, when=None):
    when = when or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    base = os.path.join(OUT, spec["slug"], "project")
    os.makedirs(base, exist_ok=True)

    def write(rel, text):
        p = os.path.join(base, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(text)

    tokens = {
        "name": spec["title"],
        "version": 1,
        "meta": {"source": spec["source"]},
        "color": {"themes": spec.get("themes", [{"id": "light", "name": "Light"}]), "tokens": spec["colors"]},
        "type": {"families": spec["families"], "groups": spec["type_groups"]},
        "spacing": {"tokens": spec["spacing"]},
        "radius": {"tokens": spec["radius"]},
    }
    if spec.get("radius_note"):
        tokens["radius"]["note"] = spec["radius_note"]
    if spec.get("shadow"):
        tokens["shadow"] = {"tokens": spec["shadow"]}
    write("tokens.json", json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
    write("README.md", spec["readme"].strip() + "\n")
    for name, comp in spec["components"].items():
        write(f"components/{name}/README.md", comp["readme"].strip() + "\n")
        write(f"components/{name}/preview.html", preview(comp["group"], comp["height"], spec["fonts_href"], comp["css"], comp["html"], comp.get("subtitle")))
    write("components/Cover/preview.html", cover(spec))
    index = {
        "v": 3,
        "layout": "files",
        "createdOnFiles": {"v": 1, "at": when},
        "title": spec["title"],
        "namespace": spec["namespace"],
        "libraries": [],
        "sections": {},
        "groups": [],
        "assetGroups": {},
        "blobs": {},
        "docs": {"readme": "project/README.md", "sections": []},
        "lastChange": {"by": "Abhishek", "via": "Claude Code", "at": when,
                       "note": f"Created from the public site {spec['source']['url']} (featured on siteofsites.co)."},
    }
    write("design-system.json", json.dumps(index, indent=2, ensure_ascii=False) + "\n")
    return base
