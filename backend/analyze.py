#!/usr/bin/env python3
"""
analyze.py - metric helpers for the scraped YouTube data.
=========================================================

Loads a scraped TSV and scores each video (engagement, views/sub,
velocity, title/length/freshness buckets). The TUI's prediction screen uses
these to build the digest it sends to Claude; nothing here writes files.
"""

import csv
import statistics
from collections import defaultdict
from datetime import date, datetime


# A "breakout" should be a video with real traction that still beat its channel
# size - otherwise a 10-subscriber channel with 200 views tops every list.
MIN_OUTLIER_VIEWS = 10000


# ---------------------------------------------------------------------------
# Loading + numeric helpers
# ---------------------------------------------------------------------------
def _to_int(value):
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return None


def _pct(part, whole):
    if part is None or not whole:
        return None
    return round(100.0 * part / whole, 2)


def _ratio(part, whole, digits=2):
    if part is None or not whole:
        return None
    return round(part / whole, digits)


def _days_since(upload_date, today):
    if not upload_date:
        return None
    try:
        d = datetime.strptime(upload_date, "%Y-%m-%d").date()
    except ValueError:
        return None
    return max((today - d).days, 0)


def load_rows(data_path):
    with open(data_path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def score_rows(rows, today=None):
    """Add computed metric fields to each row (in place) and return the list."""
    today = today or date.today()
    for r in rows:
        views = _to_int(r.get("views"))
        likes = _to_int(r.get("likes"))
        comments = _to_int(r.get("comments"))
        subs = _to_int(r.get("subscribers"))
        dur = _to_int(r.get("duration_sec"))
        days = _days_since(r.get("upload_date"), today)
        title = r.get("title") or ""

        r["_views"] = views or 0
        r["_subs"] = subs or 0
        r["_dur"] = dur or 0
        r["engagement_pct"] = _pct(likes, views)
        r["comment_pct"] = _pct(comments, views)
        r["views_per_sub"] = _ratio(views, subs)
        r["days_since_upload"] = days
        r["views_per_day"] = (round(views / days, 1) if views and days else
                              (views if views and days == 0 else None))
        r["title_length"] = len(title)
        r["title_words"] = len(title.split())
        r["title_has_number"] = "Yes" if any(c.isdigit() for c in title) else "No"
    return rows


# ---------------------------------------------------------------------------
# Aggregations
# ---------------------------------------------------------------------------
def per_keyword_stats(rows):
    by_kw = defaultdict(list)
    for r in rows:
        by_kw[r.get("keyword", "")].append(r)
    out = []
    for kw, items in by_kw.items():
        views = [x["_views"] for x in items]
        top = max(items, key=lambda x: x["_views"])
        out.append({
            "keyword": kw,
            "videos": len(items),
            "total_views": sum(views),
            "avg_views": round(statistics.mean(views)) if views else 0,
            "median_views": round(statistics.median(views)) if views else 0,
            "top_video": top.get("title", ""),
            "top_views": top["_views"],
        })
    out.sort(key=lambda d: d["total_views"], reverse=True)
    return out


def channel_stats(rows):
    by_ch = defaultdict(list)
    for r in rows:
        by_ch[r.get("channel", "")].append(r)
    out = []
    for ch, items in by_ch.items():
        views = [x["_views"] for x in items]
        engs = [x["engagement_pct"] for x in items if x["engagement_pct"] is not None]
        best = max(items, key=lambda x: x["_views"])
        out.append({
            "channel": ch,
            "subscribers": items[0]["_subs"],
            "videos_in_results": len(items),
            "total_views": sum(views),
            "avg_views": round(statistics.mean(views)) if views else 0,
            "avg_engagement_pct": round(statistics.mean(engs), 2) if engs else None,
            "best_views": best["_views"],
            "best_video": best.get("title", ""),
        })
    out.sort(key=lambda d: (d["videos_in_results"], d["total_views"]), reverse=True)
    return out


def _bucketize(rows, key_fn, buckets):
    """buckets: list of (label, predicate). Returns count + avg views per bucket."""
    groups = defaultdict(list)
    for r in rows:
        val = key_fn(r)
        for label, pred in buckets:
            if pred(val):
                groups[label].append(r["_views"])
                break
    out = []
    for label, _ in buckets:
        v = groups.get(label, [])
        out.append({
            "bucket": label,
            "videos": len(v),
            "avg_views": round(statistics.mean(v)) if v else 0,
        })
    return out


def pattern_stats(rows):
    sections = []

    # Title contains a number?
    num = defaultdict(list)
    for r in rows:
        num[r["title_has_number"]].append(r["_views"])
    sections.append(("Number in title", [
        {"bucket": k, "videos": len(v),
         "avg_views": round(statistics.mean(v)) if v else 0}
        for k, v in sorted(num.items())
    ]))

    # Title length buckets
    sections.append(("Title length (characters)", _bucketize(
        rows, lambda r: r["title_length"], [
            ("< 40", lambda x: x < 40),
            ("40-59", lambda x: 40 <= x < 60),
            ("60-79", lambda x: 60 <= x < 80),
            ("80+", lambda x: x >= 80),
        ])))

    # Duration buckets
    sections.append(("Video length", _bucketize(
        rows, lambda r: r["_dur"], [
            ("< 4 min (Shorts-ish)", lambda x: 0 < x < 240),
            ("4-10 min", lambda x: 240 <= x < 600),
            ("10-20 min", lambda x: 600 <= x < 1200),
            ("20-40 min", lambda x: 1200 <= x < 2400),
            ("40+ min", lambda x: x >= 2400),
        ])))

    # Freshness buckets
    sections.append(("Upload recency", _bucketize(
        rows, lambda r: r["days_since_upload"], [
            ("<= 7 days", lambda x: x is not None and x <= 7),
            ("8-30 days", lambda x: x is not None and 8 <= x <= 30),
            ("31-90 days", lambda x: x is not None and 31 <= x <= 90),
            ("91-365 days", lambda x: x is not None and 91 <= x <= 365),
            ("> 365 / unknown", lambda x: x is None or x > 365),
        ])))
    return sections
