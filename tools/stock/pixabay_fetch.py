#!/usr/bin/env python3
"""Pixabay stock-photo fetcher — stdlib only, no deps.

Reads PIXABAY_API_KEY from the project-root .env (or the environment).

  # download every image named in a manifest:
  python3 tools/stock/pixabay_fetch.py --manifest .../assets/img/manifest.json

  # one-off:
  python3 tools/stock/pixabay_fetch.py --query "indian man phone city" --out assets/img/s1.jpg

Manifest is {"filename.jpg": "search query", ...}. Append "#N" to a query to take
the Nth result instead of the first — that's the retry knob when hit 0 is wrong:

  {"s4.jpg": "apartment building india#3"}

Existing files are skipped only when the query that produced them is unchanged
(recorded in a `<file>.src` sidecar) — a retried query with a new `#N` re-fetches
instead of silently keeping the rejected image. --force re-downloads everything.
Downloads `largeImageURL` (1280px wide), which is what every video in
studio/videos/ already uses.

CREDITS.txt is appended per image as it lands, so an aborted batch never leaves
downloaded images without attribution. Exits non-zero if any requested image is
missing at the end. Set FIN_FAKE_APIS=1 to generate local placeholder jpgs
instead of calling the API (zero-cost pipeline dry runs).
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://pixabay.com/api/"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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


def api_key():
    key = os.environ.get("PIXABAY_API_KEY", "").strip()
    if not key:
        sys.exit("ERROR: PIXABAY_API_KEY is empty. Paste your key into .env then re-run.")
    return key


def split_query(raw):
    """'apartment india#3' -> ('apartment india', 2). Index is 1-based in the manifest."""
    query, sep, idx = raw.rpartition("#")
    if sep and idx.isdigit():
        return query.strip(), max(0, int(idx) - 1)
    return raw.strip(), 0


def search(key, query, want):
    url = API + "?" + urllib.parse.urlencode({
        "key": key, "q": query, "image_type": "photo", "orientation": "horizontal",
        "safesearch": "true", "min_width": 1280, "per_page": max(3, want + 5),
    })
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            hits = json.loads(resp.read()).get("hits", [])
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR {e.code} from Pixabay: {e.read().decode('utf-8', 'replace')}")
    except urllib.error.URLError as e:
        sys.exit(f"ERROR: could not reach Pixabay ({e.reason}).")
    if not hits:
        return None
    if want >= len(hits):
        print(f"  ! only {len(hits)} hits, wanted #{want + 1} — using the last one")
        want = len(hits) - 1
    return hits[want]


def download(hit, out):
    url = hit.get("largeImageURL") or hit.get("webformatURL")
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


def fake_fetch(raw_query, out):
    """FIN_FAKE_APIS=1: a flat-colour 1280x720 jpg, colour keyed to the query so
    different queries yield different bytes (keeps md5-dedup checks meaningful)."""
    colour = hashlib.md5(raw_query.encode("utf-8")).hexdigest()[:6]
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
         "-i", f"color=c=#{colour}:s=1280x720", "-frames:v", "1",
         "-q:v", "2", out], check=True)
    print(f"OK (FAKE) {os.path.basename(out):<18} '{raw_query}'")
    write_credit(out, f"{os.path.basename(out)}\tFIN_FAKE_APIS placeholder\tby nobody\tno licence")


def fetch_one(key, raw_query, out, force):
    """Returns True if the image is on disk when we're done."""
    src = out + ".src"
    if os.path.exists(out) and not force:
        # skip only if the SAME query produced this file — a changed query
        # means the old image was rejected and must be replaced (spec E-8)
        prev = open(src, encoding="utf-8").read().strip() if os.path.exists(src) else None
        if prev == raw_query:
            print(f"skip (exists): {out}")
            return True
    if os.environ.get("FIN_FAKE_APIS") == "1":
        fake_fetch(raw_query, out)
        with open(src, "w", encoding="utf-8") as fh:
            fh.write(raw_query)
        return True
    query, want = split_query(raw_query)
    hit = search(key, query, want)
    if not hit:
        print(f"  ! NO RESULTS for '{query}' -> {out}")
        return False
    size, url = download(hit, out)
    with open(src, "w", encoding="utf-8") as fh:
        fh.write(raw_query)
    print(f"OK {os.path.basename(out):<18} {size:>9,}b  {hit.get('imageWidth')}x{hit.get('imageHeight')}  '{query}'")
    write_credit(out, f"{os.path.basename(out)}\t{hit.get('pageURL','')}\tby {hit.get('user','?')}\tPixabay Content License")
    return True


def main(argv=None):
    p = argparse.ArgumentParser(description="Pixabay stock fetcher (stdlib only)")
    p.add_argument("--manifest", help="JSON {filename: query} — downloaded next to the manifest")
    p.add_argument("--query", help="single search query")
    p.add_argument("--out", help="output path for --query")
    p.add_argument("--force", action="store_true", help="re-download files that already exist")
    p.add_argument("--selftest", action="store_true", help="offline check of parsing helpers")
    args = p.parse_args(argv)

    if args.selftest:
        _selftest()
        return

    fake = os.environ.get("FIN_FAKE_APIS") == "1"
    key = ""
    if not fake:
        load_env()
        key = api_key()

    missing = []
    if args.manifest:
        outdir = os.path.dirname(os.path.abspath(args.manifest))
        with open(args.manifest, encoding="utf-8") as fh:
            manifest = json.load(fh)
        for name, query in manifest.items():
            if not fetch_one(key, query, os.path.join(outdir, name), args.force):
                missing.append(name)
    elif args.query and args.out:
        if not fetch_one(key, args.query, args.out, args.force):
            missing.append(os.path.basename(args.out))
    else:
        sys.exit("ERROR: give --manifest, or both --query and --out.")

    if missing:
        sys.exit(f"ERROR: {len(missing)} image(s) missing: {', '.join(missing)}")


def _selftest():
    assert split_query("apartment india#3") == ("apartment india", 2)
    assert split_query("apartment india") == ("apartment india", 0)
    assert split_query("c# tutorial") == ("c# tutorial", 0), split_query("c# tutorial")
    import shutil, tempfile
    # fake-mode fetch + query-keyed skip (offline, needs ffmpeg)
    os.environ["FIN_FAKE_APIS"] = "1"
    d = tempfile.mkdtemp(prefix="pixabay-")
    try:
        out = os.path.join(d, "s1.jpg")
        assert fetch_one("", "empty gym", out, False)
        first = open(out, "rb").read()
        mtime = os.path.getmtime(out)
        assert fetch_one("", "empty gym", out, False)          # same query → skip
        assert os.path.getmtime(out) == mtime, "unchanged query was re-fetched"
        assert fetch_one("", "empty gym#3", out, False)        # new query → replace
        assert open(out, "rb").read() != first, "changed query kept the rejected image"
        credits = open(os.path.join(d, "CREDITS.txt"), encoding="utf-8").read()
        assert credits.count("s1.jpg") == 2, credits
    finally:
        os.environ.pop("FIN_FAKE_APIS", None)
        shutil.rmtree(d, ignore_errors=True)
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".env", delete=False, encoding="utf-8") as fh:
        fh.write('# c\n\nPIXABAY_API_KEY = "abc123"\n')
        tmp = fh.name
    os.environ.pop("PIXABAY_API_KEY", None)
    load_env(tmp)
    assert os.environ["PIXABAY_API_KEY"] == "abc123"
    os.remove(tmp)
    print("selftest OK")


if __name__ == "__main__":
    main()
