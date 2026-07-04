#!/usr/bin/env python3
"""
history.py - keep dated snapshots and compare runs over time.
=============================================================

Every scrape drops a timestamped copy into history/, so you build up a record
of how your niche changes week to week. The TUI's Compare screen calls diff()
on two snapshots to highlight what changed:
  - NEW videos that entered the results
  - GONE videos that dropped out
  - CLIMBERS - biggest view gains since last run (your trend signal)

A diff report is written to history/diff_<old>__<new>.tsv (and printed).
"""

import csv
from datetime import date
from pathlib import Path

HISTORY_DIR = "history"


def _to_int(value):
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return 0


def save_snapshot(rows, columns, basename="youtube_results", when=None):
    """Write history/<basename>_<YYYY-MM-DD>.tsv. Returns the path."""
    when = when or date.today().isoformat()
    Path(HISTORY_DIR).mkdir(exist_ok=True)
    path = Path(HISTORY_DIR) / f"{basename}_{when}.tsv"
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nSnapshot saved:\n   {path.resolve()}")
    return str(path)


def _load(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        return {r["video_id"]: r for r in reader if r.get("video_id")}


def diff(old_path, new_path, out_path=None):
    old = _load(old_path)
    new = _load(new_path)

    new_ids = [vid for vid in new if vid not in old]
    gone_ids = [vid for vid in old if vid not in new]

    climbers = []
    for vid, r in new.items():
        if vid in old:
            gain = _to_int(r.get("views")) - _to_int(old[vid].get("views"))
            climbers.append((gain, r))
    climbers.sort(key=lambda t: t[0], reverse=True)

    report = []
    for vid in new_ids:
        r = new[vid]
        report.append({"change": "NEW", "view_gain": "",
                       "views": r.get("views", ""), "keyword": r.get("keyword", ""),
                       "channel": r.get("channel", ""), "title": r.get("title", ""),
                       "video_url": r.get("video_url", "")})
    for gain, r in climbers:
        if gain <= 0:
            continue
        report.append({"change": "CLIMBER", "view_gain": gain,
                       "views": r.get("views", ""), "keyword": r.get("keyword", ""),
                       "channel": r.get("channel", ""), "title": r.get("title", ""),
                       "video_url": r.get("video_url", "")})
    for vid in gone_ids:
        r = old[vid]
        report.append({"change": "GONE", "view_gain": "",
                       "views": r.get("views", ""), "keyword": r.get("keyword", ""),
                       "channel": r.get("channel", ""), "title": r.get("title", ""),
                       "video_url": r.get("video_url", "")})

    if out_path is None:
        o = Path(old_path).stem
        n = Path(new_path).stem
        out_path = str(Path(HISTORY_DIR) / f"diff_{o}__{n}.tsv")
    cols = ["change", "view_gain", "views", "keyword", "channel", "title", "video_url"]
    with open(out_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(report)

    print(f"Comparing:\n   OLD {old_path}\n   NEW {new_path}\n")
    print(f"  New videos:   {len(new_ids)}")
    print(f"  Dropped out:  {len(gone_ids)}")
    print(f"  Climbers:     {sum(1 for g, _ in climbers if g > 0)}")
    top = [c for c in climbers if c[0] > 0][:5]
    if top:
        print("\n  Top climbers (view gain since last run):")
        for gain, r in top:
            print(f"    +{gain:>10,}  {r.get('title','')[:60]}")
    print(f"\nFull diff written:\n   {Path(out_path).resolve()}")
    return out_path
