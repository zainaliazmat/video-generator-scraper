"""Turn the scrape form's pasted text + choices into scraper inputs.

Pure functions (no Textual, no I/O): a line is either a YouTube URL (passed
through) or a plain keyword (turned into a search URL with the chosen
upload-date filter). Moved here from the deleted web `server/` package.
"""
import youtube_scraper as ys

# Menu labels -> youtube_scraper.SP_FILTERS period keys. Only periods with a
# real YouTube `sp` code are offered.
DATE_FILTERS = {
    "Any time": "none",
    "This year": "year",
    "This month": "month",
    "This week": "week",
}

# Choices shown for "videos per link"; the label's leading number is the limit.
PER_LINK_CHOICES = ["30 videos", "60 videos", "120 videos"]


def _looks_like_url(line):
    return line.startswith("http://") or line.startswith("https://")


def parse_inputs(text, date_filter_label):
    """Return a list of YouTube search URLs from the pasted text.

    Blank lines, `# comments`, and a leading `*` bullet are ignored so pasting
    a rough list still works.
    """
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
