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

Existing files are skipped unless --force. Downloads `largeImageURL` (1280px wide),
which is what every video in studio/videos/ already uses.
"""
import argparse
import json
import os
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
    with open(out, "wb") as fh:
        fh.write(data)
    return len(data), url


def fetch_one(key, raw_query, out, force, credits):
    if os.path.exists(out) and not force:
        print(f"skip (exists): {out}")
        return
    query, want = split_query(raw_query)
    hit = search(key, query, want)
    if not hit:
        print(f"  ! NO RESULTS for '{query}' -> {out}")
        return
    size, url = download(hit, out)
    print(f"OK {os.path.basename(out):<18} {size:>9,}b  {hit.get('imageWidth')}x{hit.get('imageHeight')}  '{query}'")
    credits.append(f"{os.path.basename(out)}\t{hit.get('pageURL','')}\tby {hit.get('user','?')}\tPixabay Content License")


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

    load_env()
    key = api_key()
    credits = []

    if args.manifest:
        outdir = os.path.dirname(os.path.abspath(args.manifest))
        with open(args.manifest, encoding="utf-8") as fh:
            manifest = json.load(fh)
        for name, query in manifest.items():
            fetch_one(key, query, os.path.join(outdir, name), args.force, credits)
        if credits:
            with open(os.path.join(outdir, "CREDITS.txt"), "a", encoding="utf-8") as fh:
                fh.write("\n".join(credits) + "\n")
            print(f"\ncredits appended -> {os.path.join(outdir, 'CREDITS.txt')}")
    elif args.query and args.out:
        fetch_one(key, args.query, args.out, args.force, credits)
    else:
        sys.exit("ERROR: give --manifest, or both --query and --out.")


def _selftest():
    assert split_query("apartment india#3") == ("apartment india", 2)
    assert split_query("apartment india") == ("apartment india", 0)
    assert split_query("c# tutorial") == ("c# tutorial", 0), split_query("c# tutorial")
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
