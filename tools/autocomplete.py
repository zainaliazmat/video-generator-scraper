#!/usr/bin/env python3
"""YouTube autocomplete fetcher — stdlib only. Closes the fin-package evidence
gap (both pay-yourself-first packs shipped with 'no fresh autocomplete pull
was possible').

  python3 tools/autocomplete.py --q "pay yourself first" --gl us
  python3 tools/autocomplete.py --q "paise kaise bachaye" --gl in --hl hi

Prints one suggestion per line (tab-separated rank). Empty result exits 0 with
"NO SUGGESTIONS" — an honest empty is evidence too; never invent.
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

URL = "https://suggestqueries.google.com/complete/search"


def fetch(query, gl="us", hl="en"):
    qs = urllib.parse.urlencode(
        {"client": "firefox", "ds": "yt", "gl": gl, "hl": hl, "q": query})
    req = urllib.request.Request(URL + "?" + qs,
                                 headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return parse(resp.read().decode("utf-8", "replace"))


def parse(raw):
    data = json.loads(raw)
    return list(data[1]) if len(data) > 1 and isinstance(data[1], list) else []


def _selftest():
    assert parse('["q",["a","b"]]') == ["a", "b"]
    assert parse('["q",[]]') == []
    assert parse('["q"]') == []
    print("selftest OK")


def main(argv=None):
    p = argparse.ArgumentParser(description="YouTube autocomplete evidence")
    p.add_argument("--q", help="seed query")
    p.add_argument("--gl", default="us", help="country (us, in, ...)")
    p.add_argument("--hl", default="en", help="language (en, hi, ...)")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args(argv)
    if args.selftest:
        _selftest()
        return 0
    if not args.q:
        p.error("give --q")
    try:
        hits = fetch(args.q, args.gl, args.hl)
    except Exception as e:
        print(f"ERROR: fetch failed ({e})", file=sys.stderr)
        return 3  # retryable
    if not hits:
        print("NO SUGGESTIONS")
        return 0
    for i, h in enumerate(hits, 1):
        print(f"{i}\t{h}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
