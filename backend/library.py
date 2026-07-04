#!/usr/bin/env python3
"""
library.py - the central SQLite knowledge base of every video ever scraped.
============================================================================

One row per video (primary key: video_id). Scraping upserts into it: a video
we've seen before has its metrics (views, likes, comments, subscribers, ...)
refreshed instead of duplicated, and first_seen / last_seen / times_seen track
its history in the library. Blank incoming values never overwrite good stored
ones (so a later fast-mode scrape doesn't wipe likes/subs a full scrape found).

Pure stdlib (sqlite3) - no dependency. The DB lives at the project root as
library.db; the TUI's Library screen reads it, and run_scrape() writes it.
"""
import sqlite3
from datetime import date
from pathlib import Path

from youtube_scraper import COLUMNS

PROJECT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT / "library.db"

# Every scraped field except the video_id key is a data column we refresh.
_DATA_COLS = [c for c in COLUMNS if c != "video_id"]


def connect(path=None):
    conn = sqlite3.connect(str(path or DB_PATH))
    conn.row_factory = sqlite3.Row
    _ensure_schema(conn)
    return conn


def _ensure_schema(conn):
    cols = ",\n        ".join(f'"{c}" TEXT' for c in _DATA_COLS)
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS videos (
        "video_id" TEXT PRIMARY KEY,
        {cols},
        first_seen TEXT,
        last_seen  TEXT,
        times_seen INTEGER DEFAULT 1
        )""")
    conn.commit()


def known_ids(conn):
    """Set of every video_id already in the library."""
    return {r[0] for r in conn.execute("SELECT video_id FROM videos")}


def count(conn):
    return conn.execute("SELECT COUNT(*) FROM videos").fetchone()[0]


# Refresh each data column, but keep the stored value when the incoming one is
# blank - a fast-mode rescrape must not blank out likes/subs a full scrape got.
_SET_CLAUSE = ",\n        ".join(
    f'"{c}" = CASE WHEN excluded."{c}" IS NULL OR excluded."{c}" = \'\' '
    f'THEN videos."{c}" ELSE excluded."{c}" END'
    for c in _DATA_COLS
)
_ALL_COLS = ["video_id"] + _DATA_COLS + ["first_seen", "last_seen", "times_seen"]
_UPSERT_SQL = f"""
    INSERT INTO videos ({",".join(f'"{c}"' for c in _ALL_COLS)})
    VALUES ({",".join("?" for _ in _ALL_COLS)})
    ON CONFLICT(video_id) DO UPDATE SET
        {_SET_CLAUSE},
        last_seen  = excluded.last_seen,
        times_seen = videos.times_seen + 1
"""


def upsert_videos(conn, rows, today=None):
    """Insert new videos, refresh existing ones. Returns (new, updated) counts.
    Rows without a video_id are skipped (can't dedup them)."""
    today = today or date.today().isoformat()
    before = known_ids(conn)
    new = updated = 0
    for r in rows:
        vid = (r.get("video_id") or "").strip()
        if not vid:
            continue
        if vid in before:
            updated += 1
        else:
            new += 1
            before.add(vid)   # a video repeated within one batch counts once
        values = ([vid] + [str(r.get(c, "") or "") for c in _DATA_COLS]
                  + [today, today, 1])
        conn.execute(_UPSERT_SQL, values)
    conn.commit()
    return new, updated


# ---------------------------------------------------------------------------
# Read side - for the Library screen
# ---------------------------------------------------------------------------
def all_videos(conn, limit=1000, order="views"):
    """Rows as dicts, biggest first by the given numeric column."""
    col = order if order in _DATA_COLS else "views"
    # DESC already sorts NULLs (blank/non-numeric) last in SQLite.
    q = (f'SELECT * FROM videos ORDER BY CAST(NULLIF("{col}", \'\') AS INTEGER) '
         "DESC LIMIT ?")
    return [dict(r) for r in conn.execute(q, (limit,))]


def search(conn, term, limit=1000):
    """Videos whose title / channel / keyword contains term (case-insensitive)."""
    like = f"%{term}%"
    q = ("SELECT * FROM videos WHERE title LIKE ? OR channel LIKE ? "
         'OR keyword LIKE ? ORDER BY CAST(NULLIF("views", \'\') AS INTEGER) '
         "DESC LIMIT ?")
    return [dict(r) for r in conn.execute(q, (like, like, like, limit))]


def stats(conn):
    """Headline numbers for the Library screen."""
    row = conn.execute(
        "SELECT COUNT(*) AS videos, COUNT(DISTINCT channel) AS channels, "
        "MIN(first_seen) AS since, MAX(last_seen) AS latest FROM videos"
    ).fetchone()
    return dict(row) if row else {"videos": 0, "channels": 0, "since": None, "latest": None}
