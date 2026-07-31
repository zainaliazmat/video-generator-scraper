#!/usr/bin/env python3
"""Find a Lottie: the local library FIRST, LottieFiles' free catalogue second.

The library (`assets/lottie/`, git-tracked, outside studio/) is the point. Every
asset a video fetches is saved back into it pristine, so the next video reuses a
file instead of paying another search — the collection compounds. studio/ is
gitignored and gets deleted per the finished-video rule; nothing durable lives
there.

    ./search.py "piggy bank saving"              # local hits, then remote
    ./search.py "piggy bank saving" --sheet      # + a numbered contact sheet
    ./search.py --save "07=piggy-bank-coins" --tags "piggy,savings,coins"

`--save` takes a cell number off the last sheet and writes the PRISTINE json
(plus its animated preview) into the library. Tinting is per-scene and belongs
to tools/lottie/tint.py — a library asset is never stored pre-coloured.

Licence: searchPublicAnimations returns the FREE catalogue only — Lottie Simple
License: commercial use ok, modification ok, no attribution required, don't
redistribute the raw file. The paid marketplace is out of scope.
"""
import argparse, datetime, json, os, shutil, subprocess, sys, tempfile, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIB = os.path.join(ROOT, "assets", "lottie")
INDEX = os.path.join(LIB, "index.json")
SHEET = "/tmp/lottie-sheet.jpg"          # sidecar records: same path + .json

EP = "https://graphql.lottiefiles.com/2022-08/"
Q = """{ searchPublicAnimations(query:"%s", first:%d) { edges { node {
      id name jsonUrl gifUrl createdBy { username } } } } }"""


def get(url, timeout=30):
    req = urllib.request.Request(url, headers={"user-agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=timeout).read()


def index():
    return json.load(open(INDEX)) if os.path.exists(INDEX) else {}


def local(terms):
    """Score library assets by word overlap with name + tags. Dumb on purpose:
    a librarian who types good tags beats any similarity metric at this size."""
    words = {w for t in terms for w in t.lower().replace(",", " ").split()}
    hits = []
    for name, m in index().items():
        bag = set(name.replace("-", " ").split()) | {t.lower() for t in m.get("tags", [])}
        n = len(words & bag)
        if n:
            hits.append((n, name, m))
    return sorted(hits, reverse=True, key=lambda h: h[0])


def search(term, n=12):
    req = urllib.request.Request(
        EP, json.dumps({"query": Q % (term, n)}).encode(),
        {"content-type": "application/json",
         "user-agent": "Mozilla/5.0"})      # urllib's default UA is 403'd
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    return [e["node"] for e in d["data"]["searchPublicAnimations"]["edges"]]


def midframe(gif):
    """One PNG from the middle of a preview.

    Halfway, per file: a fixed frame index lands mid-entrance on a long preview
    and shows a half-drawn asset as if that were the artwork. Via ffmpeg, not
    ImageMagick, for two reasons found the hard way — `convert x.gif[n]` reads a
    delta frame without its history (ghosted cells), and montage reorders its
    arguments when they are multi-frame GIFs, so the grid stops matching the
    printed table."""
    d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", gif], capture_output=True, text=True).stdout.strip()
    png = os.path.splitext(gif)[0] + ".png"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(float(d or 1) / 2),
                    "-i", gif, "-frames:v", "1", png], check=True)
    return png


def sheet(hits, out):
    """Tile every candidate's preview into ONE numbered contact sheet — one
    vision pass over twelve, the same trade the stock-photo flow makes."""
    tmp, cells = tempfile.mkdtemp(), []
    for i, h in enumerate(hits):
        if not h.get("gifUrl"):
            continue
        p = os.path.join(tmp, f"{i:02d}.gif")
        try:
            open(p, "wb").write(get(h["gifUrl"]))
        except Exception as e:
            print(f"  {i:02d} preview failed: {e}", file=sys.stderr)
            continue
        cells.append(midframe(p))
        h["cell"] = i
    if cells:
        subprocess.run(["montage", "-label", "%t", *cells, "-tile", "6x",
                        "-geometry", "200x200+6+6", "-background", "white",
                        "-fill", "black", "-pointsize", "15", out], check=True)
    shutil.rmtree(tmp, ignore_errors=True)
    json.dump(hits, open(os.path.splitext(out)[0] + ".json", "w"), indent=1)


def save(spec, tags, sheet_path):
    """cell=name — copy a candidate off the last sheet into the library."""
    cell, name = spec.split("=", 1)
    recs = json.load(open(os.path.splitext(sheet_path)[0] + ".json"))
    hit = next(h for h in recs if h.get("cell") == int(cell))
    os.makedirs(LIB, exist_ok=True)
    j = json.loads(get(hit["jsonUrl"]))
    if any("p" in a for a in j.get("assets", [])):
        sys.exit("refusing: embeds a bitmap — it cannot be re-tinted and will "
                 "not scale to 1080p. Pick a pure-vector asset.")
    json.dump(j, open(os.path.join(LIB, name + ".json"), "w"), separators=(",", ":"))
    if hit.get("gifUrl"):
        # A still preview, not the animated gif: this is how the NEXT video sees
        # the asset without rendering it, and it goes in git — 891 KB of gif per
        # asset would outweigh the artwork it previews.
        tmp = tempfile.mkdtemp()
        g = os.path.join(tmp, "p.gif")
        open(g, "wb").write(get(hit["gifUrl"]))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", midframe(g),
                        "-vf", "scale=320:-1", os.path.join(LIB, name + ".png")], check=True)
        shutil.rmtree(tmp, ignore_errors=True)
    idx = index()
    frames = j["op"] - j["ip"]
    idx[name] = {
        "tags": [t.strip() for t in tags.split(",") if t.strip()],
        "source": hit["jsonUrl"], "author": (hit.get("createdBy") or {}).get("username"),
        "license": "Lottie Simple License (LottieFiles free catalogue)",
        "frames": frames, "fps": j["fr"], "seconds": round(frames / j["fr"], 2),
        "w": j["w"], "h": j["h"],
        "added": datetime.date.today().isoformat(), "used_in": [],
    }
    json.dump(dict(sorted(idx.items())), open(INDEX, "w"), indent=1)
    print(f"library += {name}  {frames:.0f}f @ {j['fr']}fps = "
          f"{frames / j['fr']:.2f}s  tags {idx[name]['tags']}")
    print(f"  tools/lottie/tint.py {name} <out.js> \"#<accent>\"")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("terms", nargs="*", help="search phrases")
    p.add_argument("--sheet", nargs="?", const=SHEET, default=None,
                   help=f"build a contact sheet of the remote candidates (default {SHEET})")
    p.add_argument("--save", metavar="CELL=NAME",
                   help="copy a cell off the last sheet into the library")
    p.add_argument("--tags", default="", help="comma-separated tags for --save")
    a = p.parse_args()
    terms, sheet_path = a.terms, a.sheet or SHEET

    if a.save:
        save(a.save, a.tags, sheet_path)
        sys.exit(0)

    hits = local(terms)
    print(f"— library ({len(index())} assets, {len(hits)} match) —")
    for n, name, m in hits:
        used = f"used in {len(m.get('used_in', []))}" if m.get("used_in") else "unused"
        print(f"  {name:34} {m['seconds']:>5.2f}s  {used:9} {','.join(m['tags'])}")
    if not hits:
        print("  (none — nothing local reads this scene)")
    else:
        # a name is not enough to judge an illustration by — show them
        shot = os.path.splitext(sheet_path)[0] + "-library.jpg"
        pngs = [os.path.join(LIB, n + ".png") for _, n, _ in hits
                if os.path.exists(os.path.join(LIB, n + ".png"))]
        if pngs:
            subprocess.run(["montage", "-label", "%t", *pngs, "-tile", "6x",
                            "-geometry", "200x200+6+6", "-background", "white",
                            "-fill", "black", "-pointsize", "15", shot], check=True)
            print(f"  {shot} — LOOK at this before fetching anything")
        print("  reuse: tools/lottie/tint.py <name> <out.js> \"#<accent>\"")

    remote = []
    for t in terms or ["finance"]:
        for h in search(t):
            h["q"] = t
            remote.append(h)
    if a.sheet is not None:
        sheet(remote, sheet_path)
        shown = [h for h in remote if "cell" in h]
        print(f"\n— {sheet_path}: {len(shown)}/{len(remote)} candidates —")
        for h in shown:
            print(f"  {h['cell']:02d}  {(h['name'] or '')[:30]:30} "
                  f"{(h.get('createdBy') or {}).get('username', ''):20} {h['jsonUrl']}")
        print("\n  save the one you picked, then tint it into the cut:\n"
              "  tools/lottie/search.py --save \"<cell>=<name>\" --tags \"a,b,c\"")
    else:
        print(f"\n— remote: {len(remote)} candidates (add --sheet to look at them) —")
