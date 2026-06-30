#!/usr/bin/env python3
"""
analyze.py - turn youtube_results.csv into a content-research dashboard.
========================================================================

Reads the CSV produced by youtube_scraper.py and writes a multi-sheet Excel
workbook (youtube_results_analysis.xlsx) full of the numbers that actually
help you decide what to make next:

  Dashboard      - headline stats, per-keyword table, top videos & outliers
  All Videos     - every video scored (engagement, views/sub, velocity)
  Outliers       - videos that broke out relative to their channel size
  Trending       - fastest-growing videos (views per day since upload)
  Channels       - per-channel leaderboard (who dominates your niche)
  Cross-Keyword  - videos that rank under several of your searches
  Patterns       - what wins: title style, length, duration, freshness

Run on its own at any time:
    python analyze.py [youtube_results.csv] [output.xlsx]
"""

import csv
import statistics
import sys
from collections import defaultdict
from datetime import date, datetime

try:
    from openpyxl import Workbook
    from openpyxl.chart import BarChart, Reference
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
except ImportError:
    sys.exit("openpyxl is required for analysis. Run:  pip install -r requirements.txt")


# A "breakout" should be a video with real traction that still beat its channel
# size - otherwise a 10-subscriber channel with 200 views tops every list.
MIN_OUTLIER_VIEWS = 10000

HEADER_FILL = PatternFill("solid", fgColor="C00000")
HEADER_FONT = Font(bold=True, color="FFFFFF")
TITLE_FONT = Font(bold=True, size=14)
SECTION_FONT = Font(bold=True, size=11, color="C00000")


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
# Sheet-writing helpers
# ---------------------------------------------------------------------------
NUMERIC_FORMATS = {
    "views": "#,##0", "likes": "#,##0", "comments": "#,##0",
    "subscribers": "#,##0", "views_per_day": "#,##0.0",
    "total_views": "#,##0", "avg_views": "#,##0", "median_views": "#,##0",
    "best_views": "#,##0", "engagement_pct": "0.00", "comment_pct": "0.00",
    "views_per_sub": "0.00", "avg_engagement_pct": "0.00",
}


def _style_header(ws, row_idx, ncols):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row_idx, column=c)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(vertical="center")


def write_table(ws, columns, records, widths=None, start_row=1, autofilter=True):
    """Write a header + rows starting at start_row. records are dicts."""
    widths = widths or {}
    for j, col in enumerate(columns, start=1):
        ws.cell(row=start_row, column=j, value=col)
        ws.column_dimensions[get_column_letter(j)].width = widths.get(col, 16)
    _style_header(ws, start_row, len(columns))

    for i, rec in enumerate(records, start=start_row + 1):
        for j, col in enumerate(columns, start=1):
            val = rec.get(col, "")
            if val is None:
                val = ""
            cell = ws.cell(row=i, column=j, value=val)
            fmt = NUMERIC_FORMATS.get(col)
            if fmt and isinstance(val, (int, float)):
                cell.number_format = fmt

    last_row = start_row + len(records)
    if autofilter and records:
        ws.auto_filter.ref = (f"{get_column_letter(1)}{start_row}:"
                              f"{get_column_letter(len(columns))}{last_row}")
    ws.freeze_panes = ws.cell(row=start_row + 1, column=1)
    return last_row


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


def cross_keyword(rows):
    by_vid = defaultdict(list)
    for r in rows:
        vid = r.get("video_id", "")
        if vid:
            by_vid[vid].append(r)
    out = []
    for vid, items in by_vid.items():
        kws = sorted({x.get("keyword", "") for x in items})
        if len(kws) >= 2:
            out.append({
                "title": items[0].get("title", ""),
                "channel": items[0].get("channel", ""),
                "keywords_count": len(kws),
                "keywords": " | ".join(kws),
                "views": items[0]["_views"],
                "video_url": items[0].get("video_url", ""),
            })
    out.sort(key=lambda d: (d["keywords_count"], d["views"]), reverse=True)
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


# ---------------------------------------------------------------------------
# Workbook
# ---------------------------------------------------------------------------
SCORED_COLS = ["keyword", "title", "channel", "subscribers", "views", "likes",
               "comments", "engagement_pct", "comment_pct", "views_per_sub",
               "views_per_day", "days_since_upload", "duration", "upload_date",
               "video_url"]
SCORED_WIDTHS = {"keyword": 28, "title": 55, "channel": 24, "subscribers": 12,
                 "views": 12, "likes": 10, "comments": 10, "engagement_pct": 14,
                 "comment_pct": 12, "views_per_sub": 13, "views_per_day": 13,
                 "days_since_upload": 16, "duration": 9, "upload_date": 12,
                 "video_url": 44}


def _dashboard(ws, rows, kw_stats):
    ws["A1"] = "YouTube Content Research - Dashboard"
    ws["A1"].font = TITLE_FONT
    views = [r["_views"] for r in rows]
    engs = [r["engagement_pct"] for r in rows if r["engagement_pct"] is not None]
    dates = [r.get("upload_date") for r in rows if r.get("upload_date")]
    overview = [
        ("Generated", date.today().isoformat()),
        ("Total videos", len(rows)),
        ("Unique channels", len({r.get("channel", "") for r in rows})),
        ("Keywords", len(kw_stats)),
        ("Total views", sum(views)),
        ("Median views", round(statistics.median(views)) if views else 0),
        ("Avg engagement %", round(statistics.mean(engs), 2) if engs else "n/a"),
        ("Upload date range", f"{min(dates)} -> {max(dates)}" if dates else "n/a"),
    ]
    row = 3
    for label, val in overview:
        ws.cell(row=row, column=1, value=label).font = Font(bold=True)
        c = ws.cell(row=row, column=2, value=val)
        if isinstance(val, int):
            c.number_format = "#,##0"
        row += 1

    ws.column_dimensions["A"].width = 20
    for col in "BCDEF":
        ws.column_dimensions[col].width = 16

    # Per-keyword table
    row += 1
    ws.cell(row=row, column=1, value="Per-keyword summary").font = SECTION_FONT
    row += 1
    kw_cols = ["keyword", "videos", "total_views", "avg_views", "median_views",
               "top_views", "top_video"]
    kw_start = row
    for j, col in enumerate(kw_cols, start=1):
        ws.cell(row=row, column=j, value=col)
    _style_header(ws, row, len(kw_cols))
    for rec in kw_stats:
        row += 1
        for j, col in enumerate(kw_cols, start=1):
            c = ws.cell(row=row, column=j, value=rec.get(col, ""))
            fmt = NUMERIC_FORMATS.get(col)
            if fmt and isinstance(rec.get(col), (int, float)):
                c.number_format = fmt
    ws.column_dimensions["G"].width = 55

    # Chart: avg views per keyword
    try:
        chart = BarChart()
        chart.title = "Average views per keyword"
        chart.type = "bar"
        chart.height = max(6, 0.4 * len(kw_stats) + 2)
        chart.width = 18
        data = Reference(ws, min_col=4, min_row=kw_start, max_row=row)  # avg_views
        cats = Reference(ws, min_col=1, min_row=kw_start + 1, max_row=row)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        chart.legend = None
        ws.add_chart(chart, f"I{kw_start}")
    except Exception:
        pass

    # Top videos & outliers side tables
    row += 2
    ws.cell(row=row, column=1, value="Top 10 videos by views").font = SECTION_FONT
    row += 1
    top_cols = ["title", "channel", "views"]
    for j, col in enumerate(top_cols, start=1):
        ws.cell(row=row, column=j, value=col)
    _style_header(ws, row, len(top_cols))
    for rec in sorted(rows, key=lambda x: x["_views"], reverse=True)[:10]:
        row += 1
        ws.cell(row=row, column=1, value=rec.get("title", ""))
        ws.cell(row=row, column=2, value=rec.get("channel", ""))
        ws.cell(row=row, column=3, value=rec["_views"]).number_format = "#,##0"

    row += 2
    ws.cell(row=row, column=1,
            value="Top 10 breakout videos (views per subscriber)").font = SECTION_FONT
    row += 1
    out_cols = ["title", "channel", "subscribers", "views", "views_per_sub"]
    for j, col in enumerate(out_cols, start=1):
        ws.cell(row=row, column=j, value=col)
    _style_header(ws, row, len(out_cols))
    outliers = [r for r in rows if r["views_per_sub"] is not None
                and r["_views"] >= MIN_OUTLIER_VIEWS]
    for rec in sorted(outliers, key=lambda x: x["views_per_sub"], reverse=True)[:10]:
        row += 1
        ws.cell(row=row, column=1, value=rec.get("title", ""))
        ws.cell(row=row, column=2, value=rec.get("channel", ""))
        ws.cell(row=row, column=3, value=rec["_subs"]).number_format = "#,##0"
        ws.cell(row=row, column=4, value=rec["_views"]).number_format = "#,##0"
        ws.cell(row=row, column=5, value=rec["views_per_sub"]).number_format = "0.00"


def _patterns_sheet(ws, rows):
    ws["A1"] = "What wins in this niche"
    ws["A1"].font = TITLE_FONT
    ws.column_dimensions["A"].width = 26
    ws.column_dimensions["B"].width = 12
    ws.column_dimensions["C"].width = 14
    row = 3
    for section_title, recs in pattern_stats(rows):
        ws.cell(row=row, column=1, value=section_title).font = SECTION_FONT
        row += 1
        for j, col in enumerate(["bucket", "videos", "avg_views"], start=1):
            ws.cell(row=row, column=j, value=col)
        _style_header(ws, row, 3)
        for rec in recs:
            row += 1
            ws.cell(row=row, column=1, value=rec["bucket"])
            ws.cell(row=row, column=2, value=rec["videos"])
            ws.cell(row=row, column=3, value=rec["avg_views"]).number_format = "#,##0"
        row += 2


def build_workbook(rows, out_path):
    score_rows(rows)
    kw_stats = per_keyword_stats(rows)

    wb = Workbook()
    _dashboard(wb.active, rows, kw_stats)
    wb.active.title = "Dashboard"

    # All videos, scored
    ws = wb.create_sheet("All Videos")
    by_views = sorted(rows, key=lambda x: x["_views"], reverse=True)
    write_table(ws, SCORED_COLS, by_views, SCORED_WIDTHS)

    # Outliers (breakouts with real traction, sorted by views-per-subscriber)
    ws = wb.create_sheet("Outliers")
    outliers = sorted([r for r in rows if r["views_per_sub"] is not None
                       and r["_views"] >= MIN_OUTLIER_VIEWS],
                      key=lambda x: x["views_per_sub"], reverse=True)
    write_table(ws, SCORED_COLS, outliers, SCORED_WIDTHS)

    # Trending (velocity)
    ws = wb.create_sheet("Trending")
    trend = sorted([r for r in rows if r["views_per_day"] is not None],
                   key=lambda x: x["views_per_day"], reverse=True)
    write_table(ws, SCORED_COLS, trend, SCORED_WIDTHS)

    # Channels
    ws = wb.create_sheet("Channels")
    ch_cols = ["channel", "subscribers", "videos_in_results", "total_views",
               "avg_views", "avg_engagement_pct", "best_views", "best_video"]
    write_table(ws, ch_cols, channel_stats(rows),
                {"channel": 26, "subscribers": 12, "videos_in_results": 17,
                 "total_views": 13, "avg_views": 12, "avg_engagement_pct": 18,
                 "best_views": 12, "best_video": 55})

    # Cross-keyword
    ws = wb.create_sheet("Cross-Keyword")
    ck_cols = ["title", "channel", "keywords_count", "keywords", "views", "video_url"]
    write_table(ws, ck_cols, cross_keyword(rows),
                {"title": 50, "channel": 24, "keywords_count": 16,
                 "keywords": 50, "views": 12, "video_url": 44})

    # Patterns
    _patterns_sheet(wb.create_sheet("Patterns"), rows)

    wb.save(out_path)
    return out_path


def run(csv_path="youtube_results.csv", out_path="youtube_results_analysis.xlsx"):
    rows = load_rows(csv_path)
    if not rows:
        print(f"(analysis: '{csv_path}' has no rows)")
        return None
    path = build_workbook(rows, out_path)
    from pathlib import Path
    print(f"Analysis dashboard saved:\n   {Path(path).resolve()}")
    return path


if __name__ == "__main__":
    csv_in = sys.argv[1] if len(sys.argv) > 1 else "youtube_results.csv"
    xlsx_out = sys.argv[2] if len(sys.argv) > 2 else "youtube_results_analysis.xlsx"
    run(csv_in, xlsx_out)
