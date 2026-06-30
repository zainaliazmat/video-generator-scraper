"""Parse the web UI's textarea + controls into scraper inputs.

Pure functions: a line is either a YouTube URL (passed through) or a plain
keyword (turned into a search URL with the chosen upload-date filter).
"""
import youtube_scraper as ys

# UI date-filter labels -> youtube_scraper.SP_FILTERS period keys.
# Only periods that map to a real YouTube `sp` code are offered (the
# prototype's "Last 6 months" has no real code, so "This week" replaces it).
DATE_FILTERS = {
    "Any time": "none",
    "This year": "year",
    "This month": "month",
    "This week": "week",
}


def _looks_like_url(line):
    return line.startswith("http://") or line.startswith("https://")


def parse_inputs(text, date_filter_label):
    """Return a list of YouTube search URLs from the textarea text."""
    period = DATE_FILTERS.get(date_filter_label, "none")
    urls = []
    for raw in (text or "").splitlines():
        line = raw.strip().lstrip("*").strip()
        if not line or line.startswith("#"):
            continue
        urls.append(line if _looks_like_url(line) else ys.build_search_url(line, period))
    return urls


def per_link_to_int(label):
    """'60 videos' -> 60; anything unparseable -> 60."""
    try:
        return int(str(label).split()[0])
    except (ValueError, IndexError):
        return 60
