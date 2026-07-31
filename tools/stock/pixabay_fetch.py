#!/usr/bin/env python3
"""Stock-photo fetcher — Pixabay + Pexels, stdlib only, no deps.

Reads PIXABAY_API_KEY and PEXELS_API_KEY from the project-root .env (or the env).

TWO WORKFLOWS
-------------
1. Contact-sheet (fast — recommended): fetch N candidates per slot, view ONE
   numbered sheet per slot, then promote the chosen cell at full resolution.

     python3 tools/stock/pixabay_fetch.py --manifest .../img/manifest.json --candidates 6
     # -> writes .../img/_cand/<slot>.jpg (a numbered grid) + <slot>.json per slot
     # agent Reads each _cand/<slot>.jpg (one vision call, N options at once)
     python3 tools/stock/pixabay_fetch.py --manifest .../img/manifest.json --pick "s1=2,s4=5"
     # -> downloads the chosen cell at FULL res into <slot>, writes CREDITS + .src

2. Single-fetch (the original one-image-per-slot path, still supported):
     python3 tools/stock/pixabay_fetch.py --manifest .../img/manifest.json
     python3 tools/stock/pixabay_fetch.py --query "indian man phone city" --out img/s1.jpg

Manifest is {"filename.jpg": "search query", ...}. Two query knobs (compose freely,
either order, e.g. "rupee notes@pexels#3"):
  * "#N"       take the Nth result instead of the first (1-based).
  * "@pexels"  fetch from Pexels instead of the default Pixabay — a separate,
               non-overlapping pool (the fix when a slot keeps failing the
               cross-project md5 dedup). "@pixabay" is also accepted.

Contact sheets use small previews (Pixabay webformatURL / Pexels src.medium);
the promoted pick downloads full res (Pixabay largeImageURL ~1280px / Pexels
src.large2x). Sheets live in the throwaway _cand/ subdir (not in the manifest,
so no check or dedup counts them).

Existing files are skipped only when the query that produced them is unchanged
(recorded in a `<file>.src` sidecar). --force re-downloads. CREDITS.txt is
appended per image as it lands. Set FIN_FAKE_APIS=1 to generate local placeholder
jpgs instead of calling any API (zero-cost dry runs + selftest).
"""
import argparse
import glob as globmod
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request

PIXABAY_API = "https://pixabay.com/api/"
PEXELS_API = "https://api.pexels.com/v1/search"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROVIDERS = ("pixabay", "pexels")
CELL_W, CELL_H, COLS = 512, 288, 3        # 16:9 contact-sheet cells, 3-wide grid


def load_env(path=None):
    """Minimal .env parser: KEY=VALUE lines, ignores # comments and blanks."""
    path = path or os.path.join(ROOT, ".env")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))


def provider_key(provider):
    env = "PIXABAY_API_KEY" if provider == "pixabay" else "PEXELS_API_KEY"
    key = os.environ.get(env, "").strip()
    if not key:
        sys.exit(f"ERROR: {env} is empty. Paste your key into .env then re-run.")
    return key


def split_query(raw):
    """'apartment india#3' -> ('apartment india', 2). Index is 1-based in the manifest."""
    query, sep, idx = raw.rpartition("#")
    if sep and idx.isdigit():
        return query.strip(), max(0, int(idx) - 1)
    return raw.strip(), 0


def parse_query(raw):
    """'rupee notes@pexels#3' -> ('pexels', 'rupee notes', 2). Provider suffix
    (@pixabay/@pexels) and #N may appear in either order; default is pixabay. A
    bare '#' with no digits (e.g. 'c# tutorial') is left untouched."""
    provider = "pixabay"
    m = re.search(r"@(pixabay|pexels)\b", raw)
    if m:
        provider = m.group(1)
        raw = raw[:m.start()] + raw[m.end():]
    query, want = split_query(raw.strip())
    return provider, query, want


# ---------------------------------------------------------------- provider search
# Each returns a LIST of normalized hits (up to `count`):
#   {dl, preview, page, author, license, w, h}

def pixabay_hits(query, count):
    url = PIXABAY_API + "?" + urllib.parse.urlencode({
        "key": provider_key("pixabay"), "q": query, "image_type": "photo",
        "orientation": "horizontal", "safesearch": "true", "min_width": 1280,
        "per_page": max(3, count),
    })
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            hits = json.loads(resp.read()).get("hits", [])
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR {e.code} from Pixabay: {e.read().decode('utf-8', 'replace')}")
    except urllib.error.URLError as e:
        sys.exit(f"ERROR: could not reach Pixabay ({e.reason}).")
    return [{
        "dl": h.get("largeImageURL") or h.get("webformatURL"),
        "preview": h.get("webformatURL") or h.get("largeImageURL"),
        "page": h.get("pageURL", ""), "author": h.get("user", "?"),
        "license": "Pixabay Content License",
        "w": h.get("imageWidth"), "h": h.get("imageHeight"),
    } for h in hits[:count]]


def pexels_hits(query, count):
    url = PEXELS_API + "?" + urllib.parse.urlencode({
        "query": query, "orientation": "landscape", "per_page": min(80, max(3, count)),
    })
    req = urllib.request.Request(url, headers={
        "Authorization": provider_key("pexels"), "User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            photos = json.loads(resp.read()).get("photos", [])
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR {e.code} from Pexels: {e.read().decode('utf-8', 'replace')}")
    except urllib.error.URLError as e:
        sys.exit(f"ERROR: could not reach Pexels ({e.reason}).")
    out = []
    for p in photos[:count]:
        src = p.get("src", {})
        out.append({
            "dl": src.get("large2x") or src.get("large") or src.get("original"),
            "preview": src.get("medium") or src.get("small") or src.get("large"),
            "page": p.get("url", ""), "author": p.get("photographer", "?"),
            "license": "Pexels License", "w": p.get("width"), "h": p.get("height"),
        })
    return out


HITS = {"pixabay": pixabay_hits, "pexels": pexels_hits}


def provider_hits(provider, query, count):
    return HITS[provider](query, count)


# ---------------------------------------------------------------- download / credit

def download(url, out):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    tmp = out + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(data)
    os.replace(tmp, out)
    return len(data), url


def write_credit(out, line):
    """Append attribution immediately — an aborted batch must never leave an
    image on disk without its licence line."""
    path = os.path.join(os.path.dirname(os.path.abspath(out)), "CREDITS.txt")
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


# ---------------------------------------------------------------- contact sheet

def _find_font():
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"):
        if os.path.exists(p):
            return p
    found = globmod.glob("/usr/share/fonts/**/*.ttf", recursive=True)
    return found[0] if found else None


FONT = _find_font()


def _make_cell(preview_path, label, out):
    """Scale+pad a preview to one grid cell and burn its number (if a font exists)."""
    vf = (f"scale={CELL_W}:{CELL_H}:force_original_aspect_ratio=decrease,"
          f"pad={CELL_W}:{CELL_H}:(ow-iw)/2:(oh-ih)/2:color=#111111")
    if FONT:
        vf += (f",drawtext=fontfile='{FONT}':text='{label}':x=14:y=10:fontsize=56:"
               f"fontcolor=white:box=1:boxcolor=black@0.65:boxborderw=12")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", preview_path,
                    "-vf", vf, "-frames:v", "1", out], check=True)


def build_sheet(preview_paths, out):
    """Tile numbered cells (row-major, COLS wide) into one contact-sheet jpg."""
    rows = max(1, math.ceil(len(preview_paths) / COLS))
    td = tempfile.mkdtemp(prefix="sheet-")
    try:
        for i, pv in enumerate(preview_paths, 1):
            _make_cell(pv, str(i), os.path.join(td, f"cell{i:02d}.jpg"))
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-start_number", "1",
                        "-i", os.path.join(td, "cell%02d.jpg"),
                        "-vf", f"tile={COLS}x{rows}:color=#111111",
                        "-frames:v", "1", out], check=True)
    finally:
        shutil.rmtree(td, ignore_errors=True)


def fake_flat(seed, out, w=CELL_W, h=CELL_H):
    """FIN_FAKE_APIS: a flat-colour jpg keyed to `seed` (distinct bytes per seed)."""
    colour = hashlib.md5(seed.encode("utf-8")).hexdigest()[:6]
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
                    "-i", f"color=c=#{colour}:s={w}x{h}", "-frames:v", "1",
                    "-q:v", "2", out], check=True)


# ---------------------------------------------------------------- single fetch (mode 2)

def fake_fetch(raw_query, out):
    fake_flat(raw_query, out, 1280, 720)
    print(f"OK (FAKE) {os.path.basename(out):<18} '{raw_query}'")
    write_credit(out, f"{os.path.basename(out)}\tFIN_FAKE_APIS placeholder\tby nobody\tno licence")


def fetch_one(raw_query, out, force):
    """Returns True if the image is on disk when we're done."""
    src = out + ".src"
    if os.path.exists(out) and not force:
        prev = open(src, encoding="utf-8").read().strip() if os.path.exists(src) else None
        if prev == raw_query:
            print(f"skip (exists): {out}")
            return True
    if os.environ.get("FIN_FAKE_APIS") == "1":
        fake_fetch(raw_query, out)
        open(src, "w", encoding="utf-8").write(raw_query)
        return True
    provider, query, want = parse_query(raw_query)
    hits = provider_hits(provider, query, want + 5)
    if not hits:
        print(f"  ! NO RESULTS ({provider}) for '{query}' -> {out}")
        return False
    if want >= len(hits):
        print(f"  ! only {len(hits)} hits, wanted #{want + 1} — using the last one")
        want = len(hits) - 1
    hit = hits[want]
    size, _ = download(hit["dl"], out)
    open(src, "w", encoding="utf-8").write(raw_query)
    print(f"OK {os.path.basename(out):<18} {size:>9,}b  {hit['w']}x{hit['h']}  [{provider}] '{query}'")
    write_credit(out, f"{os.path.basename(out)}\t{hit['page']}\tby {hit['author']}\t{hit['license']}")
    return True


# ---------------------------------------------------------------- contact-sheet mode (mode 1)

def cand_dir_for(manifest_path):
    return os.path.join(os.path.dirname(os.path.abspath(manifest_path)), "_cand")


def cmd_candidates(manifest_path, n):
    """One API search + N preview downloads per slot → a numbered contact sheet
    (_cand/<slot>.jpg) + candidate metadata (_cand/<slot>.json)."""
    outdir = os.path.dirname(os.path.abspath(manifest_path))
    cdir = cand_dir_for(manifest_path)
    os.makedirs(cdir, exist_ok=True)
    manifest = json.load(open(manifest_path, encoding="utf-8"))
    fake = os.environ.get("FIN_FAKE_APIS") == "1"
    missing = []
    for slot, raw in manifest.items():
        base = os.path.splitext(slot)[0]
        provider, query, want = parse_query(raw)
        hits = ([{"dl": f"FAKE:{query}#{i}", "preview": None, "page": "",
                  "author": "nobody", "license": "no licence", "w": 0, "h": 0}
                 for i in range(1, want + n + 1)] if fake
                else provider_hits(provider, query, want + n))
        # '#N' is a START OFFSET for the sheet, not just for --query. Without
        # this the sheet for 'rupee notes#3' was byte-identical to 'rupee notes'
        # (want was parsed and thrown away), so a deterministic bad top hit — the
        # demonetised ₹500 pile that owns every rupee query — could not be
        # escaped on the path fin-assets actually uses.
        if want:
            hits = hits[want:] if want < len(hits) else []
            if not hits:
                print(f"  ! fewer than {want + 1} hits ({provider}) for '{query}' -> {slot}")
        if not hits:
            print(f"  ! NO RESULTS ({provider}) for '{query}' -> {slot}")
            missing.append(slot)
            continue
        td = tempfile.mkdtemp(prefix="prev-")
        try:
            previews, cands = [], []
            for i, h in enumerate(hits, 1):
                pv = os.path.join(td, f"p{i:02d}.jpg")
                if fake:
                    fake_flat(h["dl"].replace("FAKE:", ""), pv)  # true query#N, post-offset
                else:
                    download(h["preview"] or h["dl"], pv)
                previews.append(pv)
                cands.append({"n": i, "full": h["dl"], "page": h["page"],
                              "author": h["author"], "license": h["license"],
                              "w": h["w"], "h": h["h"]})
            build_sheet(previews, os.path.join(cdir, f"{base}.jpg"))
        finally:
            shutil.rmtree(td, ignore_errors=True)
        json.dump({"slot": slot, "query": raw, "provider": provider, "cands": cands},
                  open(os.path.join(cdir, f"{base}.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        off = f" from #{want + 1}" if want else ""
        print(f"SHEET _cand/{base}.jpg  {len(cands)} candidates  [{provider}] '{query}'{off}")
    if missing:
        sys.exit(f"ERROR: {len(missing)} slot(s) returned no candidates: {', '.join(missing)}")


def parse_picks(spec):
    """'s1=2, s4.jpg=5' -> {'s1.jpg': 2, 's4.jpg': 5} (‘.jpg’ optional per key)."""
    picks = {}
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        slot, _, k = part.partition("=")
        slot = slot.strip()
        if not slot.lower().endswith(".jpg"):
            slot += ".jpg"
        picks[slot] = int(k.strip())
    return picks


def cmd_pick(manifest_path, spec):
    """Promote each chosen cell to its slot at FULL resolution (+ CREDITS + .src)."""
    outdir = os.path.dirname(os.path.abspath(manifest_path))
    cdir = cand_dir_for(manifest_path)
    fake = os.environ.get("FIN_FAKE_APIS") == "1"
    picks = parse_picks(spec)
    missing = []
    for slot, k in picks.items():
        base = os.path.splitext(slot)[0]
        meta_path = os.path.join(cdir, f"{base}.json")
        if not os.path.exists(meta_path):
            print(f"  ! no candidate sheet for {slot} — run --candidates first")
            missing.append(slot)
            continue
        meta = json.load(open(meta_path, encoding="utf-8"))
        cand = next((c for c in meta["cands"] if c["n"] == k), None)
        if not cand:
            print(f"  ! cell {k} does not exist for {slot} (has {len(meta['cands'])})")
            missing.append(slot)
            continue
        out = os.path.join(outdir, slot)
        if fake:
            fake_fetch(f"{meta['query']} cell{k}", out)
        else:
            size, _ = download(cand["full"], out)
            print(f"PICK {slot:<14} <- cell {k}  {size:>9,}b  [{meta['provider']}]")
            write_credit(out, f"{slot}\t{cand['page']}\tby {cand['author']}\t{cand['license']}")
        # .src records the manifest query so a later plain --manifest run SKIPS
        # (won't clobber a pick); re-pick via another --pick overwrites.
        open(out + ".src", "w", encoding="utf-8").write(meta["query"])
    if missing:
        sys.exit(f"ERROR: {len(missing)} pick(s) failed: {', '.join(missing)}")


# ---------------------------------------------------------------- cli

def main(argv=None):
    p = argparse.ArgumentParser(description="Pixabay+Pexels stock fetcher (stdlib only)")
    p.add_argument("--manifest", help="JSON {filename: query} — downloaded next to the manifest")
    p.add_argument("--query", help="single search query (supports @pexels / #N suffixes)")
    p.add_argument("--out", help="output path for --query")
    p.add_argument("--candidates", type=int, metavar="N",
                   help="with --manifest: build an N-candidate contact sheet per slot")
    p.add_argument("--pick", metavar="SPEC",
                   help="with --manifest: promote chosen cells, e.g. 's1=2,s4=5'")
    p.add_argument("--force", action="store_true", help="re-download files that already exist")
    p.add_argument("--selftest", action="store_true", help="offline check (needs ffmpeg)")
    args = p.parse_args(argv)

    if args.selftest:
        _selftest()
        return

    if os.environ.get("FIN_FAKE_APIS") != "1":
        load_env()  # provider keys are read lazily per-provider inside search()

    if args.manifest and args.candidates:
        cmd_candidates(args.manifest, args.candidates)
        return
    if args.manifest and args.pick:
        cmd_pick(args.manifest, args.pick)
        return

    missing = []
    if args.manifest:
        outdir = os.path.dirname(os.path.abspath(args.manifest))
        manifest = json.load(open(args.manifest, encoding="utf-8"))
        for name, query in manifest.items():
            if not fetch_one(query, os.path.join(outdir, name), args.force):
                missing.append(name)
    elif args.query and args.out:
        if not fetch_one(args.query, args.out, args.force):
            missing.append(os.path.basename(args.out))
    else:
        sys.exit("ERROR: give --manifest [--candidates N | --pick SPEC], or --query and --out.")

    if missing:
        sys.exit(f"ERROR: {len(missing)} image(s) missing: {', '.join(missing)}")


def _selftest():
    # query parsing
    assert split_query("apartment india#3") == ("apartment india", 2)
    assert split_query("c# tutorial") == ("c# tutorial", 0)
    assert parse_query("rupee notes") == ("pixabay", "rupee notes", 0)
    assert parse_query("rupee notes@pexels#3") == ("pexels", "rupee notes", 2)
    assert parse_query("rupee notes#3@pexels") == ("pexels", "rupee notes", 2)
    assert parse_picks("s1=2, s4.jpg=5") == {"s1.jpg": 2, "s4.jpg": 5}

    os.environ["FIN_FAKE_APIS"] = "1"
    d = tempfile.mkdtemp(prefix="stock-")
    try:
        # --- single-fetch path: skip-on-same-query, replace-on-change ---
        out = os.path.join(d, "s1.jpg")
        assert fetch_one("empty gym", out, False)
        first = open(out, "rb").read()
        mt = os.path.getmtime(out)
        assert fetch_one("empty gym", out, False) and os.path.getmtime(out) == mt
        assert fetch_one("empty gym@pexels", out, False)
        assert open(out, "rb").read() != first, "provider switch kept old image"

        # --- contact-sheet path: candidates -> sheet+json, pick -> full image ---
        mdir = os.path.join(d, "img")
        os.makedirs(mdir)
        mpath = os.path.join(mdir, "manifest.json")
        json.dump({"a.jpg": "bank statement", "b.jpg": "rupee notes@pexels"},
                  open(mpath, "w"))
        cmd_candidates(mpath, 6)
        assert os.path.getsize(os.path.join(mdir, "_cand", "a.jpg")) > 1000, "sheet A missing"
        meta = json.load(open(os.path.join(mdir, "_cand", "b.json")))
        assert len(meta["cands"]) == 6 and meta["provider"] == "pexels"
        cmd_pick(mpath, "a=3,b=1")
        for slot in ("a.jpg", "b.jpg"):
            assert os.path.getsize(os.path.join(mdir, slot)) > 1000, f"{slot} not promoted"
        credits = open(os.path.join(mdir, "CREDITS.txt"), encoding="utf-8").read()
        assert "a.jpg" in credits and "b.jpg" in credits

        # --- '#N' offsets the SHEET too (it used to be parsed and dropped here,
        #     so 'q#3' and 'q' produced byte-identical candidates) ---
        m2 = os.path.join(mdir, "manifest2.json")
        json.dump({"c.jpg": "bank statement", "d.jpg": "bank statement#3"}, open(m2, "w"))
        cmd_candidates(m2, 4)
        c0 = json.load(open(os.path.join(mdir, "_cand", "c.json")))["cands"]
        d0 = json.load(open(os.path.join(mdir, "_cand", "d.json")))["cands"]
        assert len(d0) == 4, f"offset sheet should still hold 4 cells, got {len(d0)}"
        assert c0[0]["full"] != d0[0]["full"], "'#N' ignored on the contact-sheet path"
        assert d0[0]["full"].endswith("#3"), d0[0]["full"]
        assert c0[0]["full"].endswith("#1"), c0[0]["full"]
        # a later plain --manifest run must SKIP the picked slots (no clobber)
        picked = open(os.path.join(mdir, "a.jpg"), "rb").read()
        for name, q in json.load(open(mpath)).items():
            fetch_one(q, os.path.join(mdir, name), False)
        assert open(os.path.join(mdir, "a.jpg"), "rb").read() == picked, "plain run clobbered a pick"
    finally:
        os.environ.pop("FIN_FAKE_APIS", None)
        shutil.rmtree(d, ignore_errors=True)

    with tempfile.NamedTemporaryFile("w", suffix=".env", delete=False, encoding="utf-8") as fh:
        fh.write('PIXABAY_API_KEY="abc123"\nPEXELS_API_KEY=xyz789\n')
        tmp = fh.name
    for k in ("PIXABAY_API_KEY", "PEXELS_API_KEY"):
        os.environ.pop(k, None)
    load_env(tmp)
    assert provider_key("pixabay") == "abc123" and provider_key("pexels") == "xyz789"
    os.remove(tmp)
    print("selftest OK" + ("" if FONT else "  (no system .ttf — sheet cells unnumbered)"))


if __name__ == "__main__":
    main()
