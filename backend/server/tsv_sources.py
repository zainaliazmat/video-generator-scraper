"""TSV sources for the standalone AI-prediction tool.

Lists history snapshots and parses a TSV (uploaded or picked from history) into
scraper-style row dicts, with a breakout-data guard so we never ask Claude to
predict from data it cannot use. Pure — no HTTP, no Job knowledge.
"""
import csv
import io
import re
from pathlib import Path

import analyze

# Anchor history/ to the project root, NOT the process cwd. history.HISTORY_DIR
# is the relative string "history"; resolving it here makes the endpoints
# independent of where uvicorn was launched from.
BACKEND = Path(__file__).resolve().parent.parent
PROJECT = BACKEND.parent
HISTORY_DIR = PROJECT / "history"

MAX_UPLOAD_BYTES = 10 * 1024 * 1024   # 10 MB

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
    """Return [{file, date, count, keywords}] for every video-table TSV in
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
        out.append({"file": p.name, "date": _date_key(p.name),
                    "count": len(rows), "keywords": keywords})
    out.sort(key=lambda d: d["date"], reverse=True)
    return out


def resolve_history_path(name):
    """Map a client-supplied history filename to a real file inside HISTORY_DIR.
    Returns a resolved Path, or None on traversal / non-.tsv / missing."""
    if not name or not name.endswith(".tsv"):
        return None
    candidate = (HISTORY_DIR / Path(name).name).resolve()
    try:
        candidate.relative_to(HISTORY_DIR.resolve())
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def parse_tsv(data):
    """Parse TSV bytes or text (BOM-tolerant) into a list of row dicts."""
    if isinstance(data, bytes):
        text = data.decode("utf-8-sig", errors="replace")
    else:
        text = data.lstrip("﻿")
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    return list(reader)


def source_error(rows):
    """Return a reason code if these rows cannot drive a prediction, else None.

    Mirrors serialize.row_to_api breakout math (views/subs, subs>0): without a
    usable subscriber count there is nothing to analyse. A comma-separated
    (CSV-as-TSV) file yields one giant column and trips 'bad_columns'.
    """
    if not rows:
        return "empty"
    if "subscribers" not in rows[0].keys():
        return "bad_columns"
    if not any(_int(r.get("subscribers")) for r in rows):
        return "no_breakout_data"
    return None
