#!/usr/bin/env python3
"""
YouTube Search Results Scraper - engine for the ytauto TUI.
===========================================================

Pulls video data for each search (keyword or URL) with yt-dlp and returns clean
row dicts; the TUI's scrape screen drives it via run_scrape(), which upserts the
results into the library and (when given one) tops up brand-new videos. For every
video it collects title, channel, views, likes/comments (full-detail mode),
duration, upload date, subscriber count, tags, and the video/thumbnail links.
"""

import re
import sys
import time
import urllib.parse
from datetime import datetime
from math import ceil

try:
    import yt_dlp
except ImportError:
    sys.exit("yt-dlp is not installed. Run:  pip install -r requirements.txt")


# ----------------------------------------------------------------------------
# SETTINGS  -  run_scrape() overrides these per call from the TUI form.
# ----------------------------------------------------------------------------
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

# --- Top-up (fetch brand-new videos when a search is mostly already-seen) ----
# ponytail: three tunable knobs, no model. If a search's top results are more
# than TOPUP_TRIGGER already in the library, page deeper into the SAME search
# (so results stay relevant) to collect TOPUP_FRACTION x limit brand-new videos,
# but never scrape deeper than TOPUP_MAX_DEPTH x limit. Adjust to taste.
TOPUP_TRIGGER = 0.5       # >50% of the batch already known -> go get new ones
TOPUP_FRACTION = 0.25     # aim to add 25% of the target as brand-new videos
TOPUP_MAX_DEPTH = 4       # ...but stop after paging 4x deep (avoid endless scrape)
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


def scrape_url(url, limit, progress=None, start=1):
    """Use yt-dlp to extract the search results for one URL (no downloading).

    With FETCH_FULL_VIDEO_DETAILS off this is a fast, flat (list-only) pull.
    With it on, each video page is opened so we also get likes, comments,
    exact upload date, subscriber count, tags, category and language.

    start: 1-based rank of the first result to keep (playliststart). Used to page
    DEEPER into the same search when the top results are already in the library.

    progress(str): optional callback fed per-video status during the slow
    full-detail pass (so the UI isn't silent while one search is scraped).
    """
    ydl_opts = _base_opts()
    ydl_opts["playlistend"] = limit           # cap how many results per search
    if start > 1:
        ydl_opts["playliststart"] = start     # skip results already pulled above
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


def _topup_target(batch_size, known_in_batch, limit):
    """How many brand-new videos to still collect for one search (0 = don't).
    Triggered only when the batch is more than TOPUP_TRIGGER already-known."""
    if not batch_size or limit <= 0:
        return 0
    if known_in_batch / batch_size > TOPUP_TRIGGER:
        return ceil(limit * TOPUP_FRACTION)
    return 0


def _topup_deeper(url, limit, need, known_before, have_ids, label, say, should_cancel):
    """Page DEEPER into the same search for brand-new videos (ids not in
    known_before and not already collected). Returns (extra_rows, new_count).
    Stays on-topic by only going deeper into this one query."""
    extra, new_count = [], 0
    step = limit
    start = limit + 1
    max_start = limit * TOPUP_MAX_DEPTH
    while new_count < need:
        if should_cancel and should_cancel():
            break
        if start > max_start:
            say(f'   {label}: {new_count}/{need} new after searching {start - 1} '
                f"deep — no more without going off-topic.")
            break
        say(f"   {label}: {new_count}/{need} new — paging results "
            f"{start}-{start + step - 1} ...")
        try:
            batch = scrape_url(url, start + step - 1, start=start)
        except Exception as exc:
            say(f"   {label}: stopped paging ({exc}).")
            break
        if not batch:
            say(f"   {label}: no more new videos on YouTube to fetch "
                f"({new_count}/{need} found).")
            break
        for r in batch:
            vid = (r.get("video_id") or "").strip()
            if not vid or vid in have_ids:
                continue
            have_ids.add(vid)
            extra.append(r)                 # still refresh known ones in the library
            if vid not in known_before:
                new_count += 1
        start += step
    return extra, new_count


def run_scrape(urls, limit, fast, channel_info, cookies=None, progress=None,
               should_cancel=None, library=None):
    """Callable core of the scraper. Returns row dicts; reports status via
    progress(str). Never prints or exits.

    library: optional library module. When given, every scraped video is
    upserted into it (dedup + refresh on video_id), results are deduped within
    the run, and any search whose top results are mostly already-in-library is
    topped up with brand-new videos paged deeper into the SAME query.

    NOT safe to call concurrently: it mutates module-level globals
    (RESULTS_PER_KEYWORD, COOKIES_FROM_BROWSER, FETCH_*). The TUI runs one
    scrape at a time, so this is safe there.

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

    conn = None
    known_before = set()
    if library is not None:
        conn = library.connect()
        known_before = library.known_ids(conn)

    all_rows = []
    have_ids = set()          # video_ids collected this run (dedup within the run)
    total = len(urls)
    for i, url in enumerate(urls, start=1):
        if should_cancel and should_cancel():
            say("Cancelled — stopping early.")
            break
        kw = keyword_from_url(url)
        label = f'[{i}/{total}] "{kw}"'
        say(f"{label} Searching ...")
        try:
            rows = scrape_url(url, RESULTS_PER_KEYWORD, progress=progress)
        except Exception as exc:
            say(f"{label} ... FAILED ({exc})")
            continue

        fresh = [r for r in rows if not (r.get("video_id") or "").strip() in have_ids]
        for r in fresh:
            vid = (r.get("video_id") or "").strip()
            if vid:
                have_ids.add(vid)
        all_rows.extend(fresh)
        known_in_batch = sum(1 for r in fresh
                             if (r.get("video_id") or "").strip() in known_before)
        note = f" ({known_in_batch} already in library)" if library is not None else ""
        say(f"{label} — {len(fresh)} videos{note}")

        if library is not None and not (should_cancel and should_cancel()):
            need = _topup_target(len(fresh), known_in_batch, RESULTS_PER_KEYWORD)
            if need:
                say(f"   {label}: mostly already known — fetching {need} brand-new ...")
                extra, got = _topup_deeper(url, RESULTS_PER_KEYWORD, need,
                                           known_before, have_ids, label, say,
                                           should_cancel)
                all_rows.extend(extra)
                if got >= need:
                    say(f"   {label}: added {got} brand-new videos.")
                elif got == 0:
                    say(f"   {label}: no new videos on YouTube to fetch.")
                else:
                    say(f"   {label}: only {got}/{need} new videos available on YouTube.")

        if i < total and PAUSE_BETWEEN_URLS:
            time.sleep(PAUSE_BETWEEN_URLS)

    if all_rows and FETCH_CHANNEL_INFO and not (should_cancel and should_cancel()):
        enrich_with_channel_info(all_rows, progress=progress, should_cancel=should_cancel)

    if conn is not None:
        new, updated = library.upsert_videos(conn, all_rows)
        say(f"Library: +{new} new, {updated} refreshed (now {library.count(conn)} total).")
        conn.close()
    return all_rows
