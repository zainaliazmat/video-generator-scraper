#!/usr/bin/env python3
"""
YouTube Search Results Scraper
==============================

Replaces the manual "Instant Data Scraper" workflow.

Instead of opening each YouTube search URL by hand, scrolling, and clicking
"Export" over and over, this script reads ALL your search URLs from urls.txt,
pulls the video data for each one automatically, and saves everything into a
single tab-separated file (youtube_results.tsv).

For every video it collects:
    keyword        - which search the video came from
    title          - video title
    channel        - channel name
    channel_url    - link to the channel
    views          - view count (number)
    duration       - length, e.g. 12:34
    duration_sec   - length in seconds (handy for sorting/filtering)
    upload_date    - when uploaded (if YouTube provides it)
    video_url      - link to the video
    video_id       - the YouTube video id
    thumbnail      - thumbnail image link

HOW TO RUN (see README.txt for full setup):
    1. pip install -r requirements.txt
    2. put your search URLs in urls.txt (one per line)
    3. python youtube_scraper.py
"""

import argparse
import csv
import re
import sys
import time
import urllib.parse
from datetime import datetime
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    sys.exit("yt-dlp is not installed. Run:  pip install -r requirements.txt")


# ----------------------------------------------------------------------------
# SETTINGS  -  edit these if you want
# ----------------------------------------------------------------------------
URLS_FILE = "urls.txt"            # file containing your search URLs (one per line)
OUTPUT_BASENAME = "youtube_results"  # output file: youtube_results.tsv
RESULTS_PER_KEYWORD = 60          # how many videos to grab per search URL
PAUSE_BETWEEN_URLS = 2            # seconds to wait between searches (be polite)
COOKIES_FROM_BROWSER = None       # e.g. "chrome" if YouTube asks you to sign in /
                                  # shows a bot check. None = no cookies.

# --- Extra detail (slower, but richer) --------------------------------------
FETCH_FULL_VIDEO_DETAILS = True   # True = open each video for likes, comments,
                                  # exact upload date, subscriber count, tags,
                                  # category, language. MUCH slower (loads every
                                  # video page). False = fast list-only mode.
FETCH_CHANNEL_INFO = True         # True = one extra lookup per channel for the
                                  # channel description + channel topics/tags.
PAUSE_BETWEEN_CHANNELS = 1        # seconds to wait between channel lookups
# ----------------------------------------------------------------------------


COLUMNS = [
    "keyword", "title",
    "channel", "channel_url", "channel_id", "subscribers", "channel_verified",
    "views", "likes", "comments",
    "duration", "duration_sec", "upload_date",
    "tags", "categories", "language",
    "channel_description", "channel_tags",
    "video_url", "video_id", "thumbnail",
]


def read_urls(path):
    """Read URLs from the file, ignoring blank lines and # comments."""
    p = Path(path)
    if not p.exists():
        sys.exit(f"Could not find '{path}'. Create it and put one search URL per line.")
    urls = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip().lstrip("*").strip()   # tolerate "* https://..." bullet lines
        if not line or line.startswith("#"):
            continue
        urls.append(line)
    if not urls:
        sys.exit(f"'{path}' has no URLs in it.")
    return urls


def keyword_from_url(url):
    """Pull the human-readable search term out of a YouTube results URL."""
    try:
        q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        if "search_query" in q:
            return q["search_query"][0]
    except Exception:
        pass
    return url  # fall back to the raw URL if we can't parse it


# YouTube "Upload date" filter codes (the &sp=... part of a search URL).
SP_FILTERS = {
    "hour":  "EgIIAQ%3D%3D",
    "today": "EgIIAg%3D%3D",
    "week":  "EgIIAw%3D%3D",
    "month": "EgIIBA%3D%3D",
    "year":  "EgIIBQ%3D%3D",
    "none":  "",
}


def build_search_url(keyword, period="year"):
    """Turn a plain search term into a YouTube results URL with an upload-date
    filter, so you can keep a simple keywords.txt instead of pasting URLs."""
    q = urllib.parse.quote_plus(keyword.strip())
    url = f"https://www.youtube.com/results?search_query={q}"
    sp = SP_FILTERS.get(period, "")
    if sp:
        url += f"&sp={sp}"
    return url


def read_keywords(path, period="year"):
    """Read plain search terms (one per line) and build search URLs from them."""
    p = Path(path)
    if not p.exists():
        sys.exit(f"Could not find '{path}'. Create it and put one search term per line.")
    urls = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip().lstrip("*").strip()
        if not line or line.startswith("#"):
            continue
        urls.append(build_search_url(line, period))
    if not urls:
        sys.exit(f"'{path}' has no keywords in it.")
    return urls


def seconds_to_hms(seconds):
    """120 -> '2:00', 3725 -> '1:02:05'."""
    if seconds is None:
        return ""
    try:
        seconds = int(seconds)
    except (TypeError, ValueError):
        return ""
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def format_upload_date(value):
    """yt-dlp gives upload_date as YYYYMMDD; turn it into YYYY-MM-DD."""
    if not value:
        return ""
    value = str(value)
    if len(value) == 8 and value.isdigit():
        try:
            return datetime.strptime(value, "%Y%m%d").strftime("%Y-%m-%d")
        except ValueError:
            return value
    return value


def best_thumbnail(entry):
    """Pick the highest-resolution thumbnail, or build one from the video id."""
    thumbs = entry.get("thumbnails")
    if isinstance(thumbs, list) and thumbs:
        # last item is usually the largest
        url = thumbs[-1].get("url")
        if url:
            return url
    vid = entry.get("id")
    if vid:
        return f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
    return ""


def _num(value):
    """Return a number as-is, or '' when yt-dlp didn't provide it."""
    return value if value is not None else ""


def entry_to_row(entry, keyword):
    """Turn one yt-dlp video entry into a clean dictionary row.

    Many fields (likes, comments, exact upload_date, subscribers, tags,
    category, language) are only present when FETCH_FULL_VIDEO_DETAILS is on;
    they come back as '' in fast list-only mode, which is fine.
    """
    vid = entry.get("id", "")
    duration = entry.get("duration")
    verified = entry.get("channel_is_verified")
    tags = entry.get("tags") or []
    categories = entry.get("categories") or []
    return {
        "keyword": keyword,
        "title": entry.get("title", ""),
        "channel": entry.get("channel") or entry.get("uploader") or "",
        "channel_url": entry.get("channel_url") or entry.get("uploader_url") or "",
        "channel_id": entry.get("channel_id") or "",
        "subscribers": _num(entry.get("channel_follower_count")),
        "channel_verified": "Yes" if verified else ("No" if verified is False else ""),
        "views": _num(entry.get("view_count")),
        "likes": _num(entry.get("like_count")),
        "comments": _num(entry.get("comment_count")),
        "duration": seconds_to_hms(duration),
        "duration_sec": _num(duration),
        "upload_date": format_upload_date(entry.get("upload_date")),
        "tags": ", ".join(tags),
        "categories": ", ".join(categories),
        "language": entry.get("language") or "",
        "channel_description": "",   # filled later by the channel-info pass
        "channel_tags": "",          # filled later by the channel-info pass
        "video_url": f"https://www.youtube.com/watch?v={vid}" if vid else entry.get("url", ""),
        "video_id": vid,
        "thumbnail": best_thumbnail(entry),
    }


def _base_opts():
    opts = {
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,     # skip a bad video instead of crashing
        "skip_download": True,
    }
    if COOKIES_FROM_BROWSER:
        opts["cookiesfrombrowser"] = (COOKIES_FROM_BROWSER,)
    return opts


_ITEM_RE = re.compile(r"Downloading item (\d+) of (\d+)")


class _ScrapeLogger:
    """Forwards yt-dlp's per-video progress to a progress(str) callback so the
    UI can show live activity while the (slow) full-detail pass runs.

    yt-dlp's own "item N of M" counter resets per internal page, so we keep a
    monotonic count of our own to avoid a confusing restart in the log."""
    def __init__(self, progress):
        self.progress = progress
        self.count = 0

    def _maybe(self, msg):
        if _ITEM_RE.search(msg):
            self.count += 1
            self.progress(f"   video {self.count} — fetching views, likes, tags ...")

    def debug(self, msg):
        self._maybe(msg)

    def info(self, msg):
        self._maybe(msg)

    def warning(self, msg):
        pass

    def error(self, msg):
        pass


def scrape_url(url, limit, progress=None):
    """Use yt-dlp to extract the search results for one URL (no downloading).

    With FETCH_FULL_VIDEO_DETAILS off this is a fast, flat (list-only) pull.
    With it on, each video page is opened so we also get likes, comments,
    exact upload date, subscriber count, tags, category and language.

    progress(str): optional callback fed per-video status during the slow
    full-detail pass (so the UI isn't silent while one search is scraped).
    """
    ydl_opts = _base_opts()
    ydl_opts["playlistend"] = limit           # cap how many results per search
    if not FETCH_FULL_VIDEO_DETAILS:
        ydl_opts["extract_flat"] = True       # list metadata only - fast
    elif progress:
        ydl_opts["logger"] = _ScrapeLogger(progress)   # live per-video lines

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    if not info:
        return []
    entries = info.get("entries") or []
    # keep only real videos (skip channels/playlists that sometimes appear)
    rows = []
    keyword = keyword_from_url(url)
    for e in entries:
        if not e:
            continue
        if e.get("_type") in ("playlist", "url") and not e.get("id", "").strip():
            continue
        rows.append(entry_to_row(e, keyword))
    return rows


def fetch_channel_info(channel_url):
    """Look up one channel's description + topics/tags (and subscribers as a
    backup). Returns a dict; values are '' when YouTube doesn't provide them."""
    ydl_opts = _base_opts()
    ydl_opts["extract_flat"] = True
    ydl_opts["playlist_items"] = "0"          # header only - don't list videos
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(channel_url, download=False)
    except Exception:
        info = None
    if not info:
        return {"channel_description": "", "channel_tags": "", "subscribers": ""}
    tags = info.get("tags") or []
    return {
        "channel_description": (info.get("description") or "").strip(),
        "channel_tags": ", ".join(tags),
        "subscribers": _num(info.get("channel_follower_count")),
    }


def enrich_with_channel_info(rows, progress=None, should_cancel=None):
    """Fill channel_description / channel_tags for every row, one lookup per
    unique channel (cached). Also backfills subscribers if a video page hid it.

    progress(str): optional callback for live status (one line per channel).
    should_cancel(): optional callable -> bool to stop the lookups early.
    """
    def say(msg):
        if progress:
            progress(msg)
        else:
            print(msg)

    cache = {}
    # unique channels, keyed by channel_url (fall back to channel_id)
    channels = []
    seen = set()
    for r in rows:
        key = r.get("channel_url") or r.get("channel_id")
        if key and key not in seen:
            seen.add(key)
            channels.append(key)

    total = len(channels)
    say(f"Looking up {total} channels for subscriber counts + topics ...")
    for i, key in enumerate(channels, start=1):
        if should_cancel and should_cancel():
            say("Cancelled — stopping channel lookups.")
            break
        cache[key] = fetch_channel_info(key)
        # Show the channel name where we have it (nicer than the raw URL).
        name = next((r.get("channel") for r in rows
                     if (r.get("channel_url") or r.get("channel_id")) == key and r.get("channel")), key)
        say(f"[{i}/{total}] {name} ... ok")
        if i < total and PAUSE_BETWEEN_CHANNELS:
            time.sleep(PAUSE_BETWEEN_CHANNELS)

    for r in rows:
        key = r.get("channel_url") or r.get("channel_id")
        info = cache.get(key)
        if not info:
            continue
        r["channel_description"] = info["channel_description"]
        r["channel_tags"] = info["channel_tags"]
        if r.get("subscribers") in ("", None) and info["subscribers"] != "":
            r["subscribers"] = info["subscribers"]


def write_tsv(rows, path):
    # Tab-separated so values that contain commas stay in one column.
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def run_scrape(urls, limit, fast, channel_info, cookies=None, progress=None,
               should_cancel=None):
    """Callable core of the scraper. Returns row dicts; reports status via
    progress(str). Behaviour matches main()'s loop but never prints or exits.

    NOT safe to call concurrently: it mutates module-level globals
    (RESULTS_PER_KEYWORD, COOKIES_FROM_BROWSER, FETCH_*). The web layer
    serializes calls (one scrape at a time) so this is safe there.

    should_cancel: optional callable -> bool, checked before each URL; when it
    returns True the scrape stops early and returns whatever was collected.
    """
    global RESULTS_PER_KEYWORD, COOKIES_FROM_BROWSER
    global FETCH_FULL_VIDEO_DETAILS, FETCH_CHANNEL_INFO
    RESULTS_PER_KEYWORD = limit
    COOKIES_FROM_BROWSER = cookies or None
    FETCH_FULL_VIDEO_DETAILS = not fast
    FETCH_CHANNEL_INFO = channel_info and not fast

    def say(msg):
        if progress:
            progress(msg)

    all_rows = []
    total = len(urls)
    for i, url in enumerate(urls, start=1):
        if should_cancel and should_cancel():
            say("Cancelled — stopping early.")
            break
        kw = keyword_from_url(url)
        # Emit immediately so the UI isn't silent while this search is scraped.
        say(f"[{i}/{total}] Searching \"{kw}\" ...")
        try:
            rows = scrape_url(url, RESULTS_PER_KEYWORD, progress=progress)
            all_rows.extend(rows)
            say(f"[{i}/{total}] {kw} — {len(rows)} videos")
        except Exception as exc:
            say(f"[{i}/{total}] {kw} ... FAILED ({exc})")
        if i < total and PAUSE_BETWEEN_URLS:
            time.sleep(PAUSE_BETWEEN_URLS)

    if all_rows and FETCH_CHANNEL_INFO and not (should_cancel and should_cancel()):
        enrich_with_channel_info(all_rows, progress=progress, should_cancel=should_cancel)
    return all_rows


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description="Scrape YouTube search results into a spreadsheet, then build "
                    "an analysis dashboard.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  python youtube_scraper.py                 # use urls.txt\n"
               "  python youtube_scraper.py --keywords keywords.txt\n"
               "  python youtube_scraper.py --limit 30 --fast\n"
               "  python youtube_scraper.py --cookies chrome\n",
    )
    p.add_argument("urls_file", nargs="?", default=None,
                   help="search-URLs file (default: urls.txt)")
    p.add_argument("--urls", dest="urls_file_opt", default=None,
                   help="search-URLs file (one YouTube results URL per line)")
    p.add_argument("--keywords", default=None,
                   help="plain search terms file (one per line); URLs are built for you")
    p.add_argument("--filter", default="year",
                   choices=list(SP_FILTERS.keys()),
                   help="upload-date filter when using --keywords (default: year)")
    p.add_argument("--limit", type=int, default=RESULTS_PER_KEYWORD,
                   help=f"videos per keyword (default: {RESULTS_PER_KEYWORD})")
    p.add_argument("--output", default=OUTPUT_BASENAME,
                   help=f"output basename (default: {OUTPUT_BASENAME})")
    p.add_argument("--cookies", default=COOKIES_FROM_BROWSER,
                   help="browser to read cookies from if YouTube shows a bot check "
                        "(e.g. chrome, firefox, edge, brave)")
    p.add_argument("--fast", action="store_true",
                   help="fast list-only mode (skip per-video likes/comments/subs/tags)")
    p.add_argument("--no-channel-info", action="store_true",
                   help="skip the per-channel description/topics lookup")
    p.add_argument("--no-history", action="store_true",
                   help="don't save a timestamped snapshot to history/")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    # CLI flags override the SETTINGS constants at the top of the file.
    global RESULTS_PER_KEYWORD, COOKIES_FROM_BROWSER
    global FETCH_FULL_VIDEO_DETAILS, FETCH_CHANNEL_INFO, OUTPUT_BASENAME
    RESULTS_PER_KEYWORD = args.limit
    OUTPUT_BASENAME = args.output
    if args.cookies:
        COOKIES_FROM_BROWSER = args.cookies
    if args.fast:
        FETCH_FULL_VIDEO_DETAILS = False
        FETCH_CHANNEL_INFO = False   # "fast" means skip the per-channel lookups too
    if args.no_channel_info:
        FETCH_CHANNEL_INFO = False

    # Decide where the search URLs come from.
    if args.keywords:
        urls = read_keywords(args.keywords, args.filter)
        source = f"{args.keywords} (built {len(urls)} URL(s), filter={args.filter})"
    else:
        urls_file = args.urls_file_opt or args.urls_file or URLS_FILE
        urls = read_urls(urls_file)
        source = urls_file

    print(f"Found {len(urls)} search(es) from '{source}'.")
    print(f"Grabbing up to {RESULTS_PER_KEYWORD} videos each. This runs without a browser.")
    if FETCH_FULL_VIDEO_DETAILS:
        print("Full-detail mode ON (likes, comments, subscribers, tags, upload date) "
              "- this is much slower; each video page is opened.")
    print()

    all_rows = run_scrape(
        urls,
        limit=RESULTS_PER_KEYWORD,
        fast=args.fast,
        channel_info=not args.no_channel_info,
        cookies=COOKIES_FROM_BROWSER,
        progress=print,
    )

    if not all_rows:
        sys.exit("\nNo data was collected. See README.txt -> Troubleshooting.")

    # Per-keyword counts for the summary table (initialise zeros so keywords
    # that returned nothing still show up).
    per_keyword_counts = {keyword_from_url(u): 0 for u in urls}
    for r in all_rows:
        kw = r.get("keyword", "")
        per_keyword_counts[kw] = per_keyword_counts.get(kw, 0) + 1

    tsv_path = f"{OUTPUT_BASENAME}.tsv"
    write_tsv(all_rows, tsv_path)
    outputs = [tsv_path]

    print("\n" + "=" * 50)
    print("DONE")
    print("=" * 50)
    print(f"Total videos collected: {len(all_rows)}")
    for kw, n in per_keyword_counts.items():
        print(f"   {n:>4}  {kw}")
    print("\nSaved:")
    for o in outputs:
        print(f"   {Path(o).resolve()}")

    # --- Snapshot (best-effort; never break the scrape) ----------------------
    if not args.no_history:
        try:
            import history
            history.save_snapshot(all_rows, COLUMNS, OUTPUT_BASENAME)
        except Exception as exc:
            print(f"(history snapshot skipped: {exc})")


if __name__ == "__main__":
    main()
