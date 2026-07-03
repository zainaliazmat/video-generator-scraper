"""Read saved TSV snapshots for the predict + diff screens.

Lists history snapshots and parses a TSV into scraper-style row dicts, with a
breakout-data guard so we never ask Claude to predict from data it cannot use.
Pure — no Textual. Moved here from the deleted web `server/` package.
"""
import csv
import io
import re
from pathlib import Path

import analyze

# Anchor history/ to the project root, not the process cwd.
BACKEND = Path(__file__).resolve().parent.parent
PROJECT = BACKEND.parent
HISTORY_DIR = PROJECT / "history"

_DATE_RE = re.compile(r"_(\d{4}-\d{2}-\d{2})\.tsv$")


def _int(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def _date_key(name):
    m = _DATE_RE.search(name)
    return m.group(1) if m else ""


def list_snapshots():
    """Return [{file, path, date, count, keywords}] for every video-table TSV in
    history/, newest first. Skips diff_* reports and unparseable files."""
    if not HISTORY_DIR.exists():
        return []
    out = []
    for p in sorted(HISTORY_DIR.glob("*.tsv")):
        if p.name.startswith("diff_"):
            continue
        try:
            rows = analyze.load_rows(str(p))
        except Exception:
            continue
        keywords = sorted({r.get("keyword", "") for r in rows if r.get("keyword")})
        out.append({"file": p.name, "path": str(p), "date": _date_key(p.name),
                    "count": len(rows), "keywords": keywords})
    out.sort(key=lambda d: d["date"], reverse=True)
    return out


def parse_tsv(data):
    """Parse TSV bytes or text (BOM-tolerant) into a list of row dicts."""
    if isinstance(data, bytes):
        text = data.decode("utf-8-sig", errors="replace")
    else:
        text = data.lstrip("﻿")
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    return list(reader)


def source_error(rows):
    """Return a reason string if these rows cannot drive a prediction, else None."""
    if not rows:
        return "This file has no rows."
    if "subscribers" not in rows[0].keys():
        return "This file has no 'subscribers' column (was it scraped in fast mode?)."
    if not any(_int(r.get("subscribers")) for r in rows):
        return "No usable subscriber counts, so there is nothing to analyse."
    return None
