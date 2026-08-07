#!/usr/bin/env python3
"""Re-tint a Lottie into the blockframe palette: duotone by luminance.

A stock flat illustration arrives in someone else's colours and lands on top of
a graded film as clip-art. This maps every colour to one ramp
panel -> accent -> ink, keeping the artwork's own light/dark structure.

usage: tint.py <library-name | in.json | jsonUrl> <out.js> [#accent]

    ./tint.py growth-chart-person-coins \
              studio/videos/<slug>-hi/assets/lottie/growth.js "#22c55e"

The first argument is normally a name from the library (`assets/lottie/`, see
tools/lottie/search.py) — the library stores every asset PRISTINE and the tint
happens per scene, because the accent is the scene's role colour, not the
asset's property. A URL still works as an escape hatch but does not populate
the library; `search.py --save` is what grows it.

An output ending in .js is written as `window.L_<basename> = {...};` — which is
the only form the composition may load. A `path:` fetch at render time resolves
after the runtime has inspected the page and the scene renders blank.

ponytail: solid colours + gradient stops only. Effects that carry their own
colour (drop shadow, fill overrides) are left alone — none of the picked
assets use them.
"""
import json, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIB = os.path.join(ROOT, "assets", "lottie")

PANEL = (0x16, 0x1b, 0x25)      # --panel
INK = (0xf5, 0xf3, 0xec)        # --ink


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def ramp(rgb01, accent):
    r, g, b = rgb01[:3]
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b     # 0..1, sRGB-ish
    lo, hi = (PANEL, accent) if lum < 0.5 else (accent, INK)
    t = lum * 2 if lum < 0.5 else (lum - 0.5) * 2
    return [(lo[i] + (hi[i] - lo[i]) * t) / 255.0 for i in range(3)]


def walk(node, accent):
    if isinstance(node, dict):
        for k, v in node.items():
            # solid colour: {"c": {"a":0, "k":[r,g,b,a]}}
            if k == "c" and isinstance(v, dict) and isinstance(v.get("k"), list) \
                    and len(v["k"]) >= 3 and all(isinstance(x, (int, float)) for x in v["k"][:3]):
                v["k"][:3] = ramp(v["k"], accent)
            # gradient: {"g": {"p": n, "k": {"k": [pos,r,g,b, ...]}}}
            elif k == "g" and isinstance(v, dict) and isinstance(v.get("k"), dict):
                stops, p = v["k"].get("k"), v.get("p", 0)
                if isinstance(stops, list) and stops and isinstance(stops[0], (int, float)):
                    for i in range(p):
                        o = i * 4
                        if o + 3 < len(stops):
                            stops[o + 1:o + 4] = ramp(stops[o + 1:o + 4], accent)
            else:
                walk(v, accent)
    elif isinstance(node, list):
        for v in node:
            walk(v, accent)


def load(src):
    if src.startswith("http"):
        req = urllib.request.Request(src, headers={"user-agent": "Mozilla/5.0"})
        return json.load(urllib.request.urlopen(req, timeout=30))
    if not src.endswith(".json"):                 # a library name
        lib = os.path.join(LIB, src + ".json")
        if not os.path.exists(lib):
            sys.exit(f"no such library asset: {src}\n"
                     f"  tools/lottie/search.py \"<phrase>\" --sheet   # find one")
        src = lib
    return json.load(open(src))


def record_use(name, dst):
    """Note which cut used a library asset. Auto-maintained: an agent that has
    to remember to log it, won't — and 'have we used this before?' is the whole
    reason the index exists."""
    idx_path = os.path.join(LIB, "index.json")
    if not os.path.exists(idx_path):
        return
    idx = json.load(open(idx_path))
    if name not in idx:
        return
    m = re.search(r"studio/videos/([^/]+)/", dst.replace(os.sep, "/"))
    if not m:
        return                       # a probe or a one-off — not a shipped cut
    cut = m.group(1)
    if cut not in idx[name].setdefault("used_in", []):
        idx[name]["used_in"].append(cut)
        json.dump(idx, open(idx_path, "w"), indent=1)
        n = len(idx[name]["used_in"])
        if n > 1:
            print(f"  NOTE: {name} has now been used in {n} cuts: "
                  f"{', '.join(idx[name]['used_in'])}")


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    accent = hex2rgb(sys.argv[3] if len(sys.argv) > 3 else "#22c55e")
    j = load(src)
    if any("p" in a for a in j.get("assets", [])):
        sys.exit("refusing: this Lottie embeds a bitmap — it cannot be re-tinted "
                 "and will not scale to 1080p. Pick a pure-vector asset.")
    walk(j, accent)
    # A hyphen in the basename emitted `window.L_phone-notify-credit={…}`, which is a
    # syntax error, so window.L_* stayed undefined and the scene rendered BLANK while
    # every check passed. Every name in assets/lottie/ is hyphenated, so this was the
    # default path, not an edge case (found on passive-income-number, 2026-08-07).
    name = re.sub(r"\W", "_", os.path.splitext(os.path.basename(dst))[0])
    body = json.dumps(j, separators=(",", ":"))
    os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True)
    open(dst, "w").write(f"window.L_{name}={body};" if dst.endswith(".js") else body)
    if not src.startswith("http") and not src.endswith(".json"):
        record_use(src, dst)          # after the write, so a failed run logs nothing
    frames = j["op"] - j["ip"]
    print(f"{dst}  window.L_{name}  {frames:.0f} frames @ {j['fr']}fps "
          f"= {frames / j['fr']:.2f}s  accent #{'%02x%02x%02x' % accent}")
