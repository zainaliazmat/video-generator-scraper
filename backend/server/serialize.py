"""Turn a scraper row dict into the JSON shape the frontend table consumes.

Handles both string-typed rows (reloaded from a TSV) and int-typed rows
(fresh from run_scrape). Blank fields become None; breakout = views/subs.
"""


def _int(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def _verified(v):
    if v == "Yes":
        return True
    if v == "No":
        return False
    return None


def row_to_api(row):
    views = _int(row.get("views"))
    subs = _int(row.get("subscribers"))
    breakout = round(views / subs, 1) if (views and subs and subs > 0) else None
    return {
        "video_id": row.get("video_id", ""),
        "title": row.get("title", ""),
        "video_url": row.get("video_url", ""),
        "thumbnail": row.get("thumbnail", ""),
        "upload_date": row.get("upload_date", ""),
        "duration": row.get("duration", ""),
        "duration_sec": _int(row.get("duration_sec")),
        "keyword": row.get("keyword", ""),
        "channel": row.get("channel", ""),
        "channel_url": row.get("channel_url", ""),
        "subscribers": subs,
        "verified": _verified(row.get("channel_verified", "")),
        "views": views,
        "likes": _int(row.get("likes")),
        "comments": _int(row.get("comments")),
        "breakout": breakout,
    }
