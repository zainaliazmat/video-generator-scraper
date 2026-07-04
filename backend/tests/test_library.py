import library
import youtube_scraper as ys


def _row(vid, **kw):
    r = {c: "" for c in ys.COLUMNS}
    r["video_id"] = vid
    r.update(kw)
    return r


def test_upsert_dedups_and_updates(tmp_path):
    conn = library.connect(tmp_path / "lib.db")

    new, updated = library.upsert_videos(
        conn, [_row("a", views="100", title="T"), _row("b", views="200")],
        today="2026-06-01")
    assert (new, updated) == (2, 0)
    assert library.count(conn) == 2

    # Re-scrape: "a" seen again with a fresh view count, "c" is brand new.
    new, updated = library.upsert_videos(
        conn, [_row("a", views="150", title="T"), _row("c", views="50")],
        today="2026-06-08")
    assert (new, updated) == (1, 1)
    assert library.count(conn) == 3          # no duplicate row for "a"

    a = next(r for r in library.all_videos(conn) if r["video_id"] == "a")
    assert a["views"] == "150"               # refreshed
    assert a["first_seen"] == "2026-06-01"   # kept
    assert a["last_seen"] == "2026-06-08"    # advanced
    assert a["times_seen"] == 2


def test_blank_incoming_does_not_wipe_stored(tmp_path):
    conn = library.connect(tmp_path / "lib.db")
    library.upsert_videos(conn, [_row("a", views="100", subscribers="9999")])
    # A later fast-mode scrape has no subscriber count — must NOT blank it out.
    library.upsert_videos(conn, [_row("a", views="120", subscribers="")])
    a = library.all_videos(conn)[0]
    assert a["subscribers"] == "9999"        # preserved
    assert a["views"] == "120"               # still refreshed


def test_rows_without_video_id_are_skipped(tmp_path):
    conn = library.connect(tmp_path / "lib.db")
    new, updated = library.upsert_videos(conn, [_row(""), _row("a")])
    assert (new, updated) == (1, 0)


def test_search_matches_title_channel_keyword(tmp_path):
    conn = library.connect(tmp_path / "lib.db")
    library.upsert_videos(conn, [
        _row("a", title="Best AI tools", channel="TechCo", keyword="ai"),
        _row("b", title="Cooking pasta", channel="FoodCo", keyword="food"),
    ])
    assert {r["video_id"] for r in library.search(conn, "ai")} == {"a"}
    assert {r["video_id"] for r in library.search(conn, "FoodCo")} == {"b"}


# --- top-up decision math ---------------------------------------------------
def test_topup_target_triggers_over_half():
    assert ys._topup_target(100, 60, 100) == 25   # 60% known -> top up 25% of 100
    assert ys._topup_target(100, 50, 100) == 0    # exactly 50% -> not "more than"
    assert ys._topup_target(0, 0, 100) == 0       # nothing fetched
    assert ys._topup_target(100, 90, 40) == 10    # 25% of the target (40), not the batch


# --- top-up integration: pages deeper for brand-new videos ------------------
class _FakeLib:
    """Minimal stand-in for the library module: an in-memory known-id set."""
    def __init__(self, known):
        self.known = set(known)
        self.upserted = []

    def connect(self):
        return self

    def close(self):
        pass

    def known_ids(self, conn):
        return set(self.known)

    def upsert_videos(self, conn, rows):
        ids = [r["video_id"] for r in rows if r.get("video_id")]
        self.upserted = ids
        return len(set(ids) - self.known), len(set(ids) & self.known)

    def count(self, conn):
        return len(self.known | set(self.upserted))


def test_topup_pages_deeper_when_mostly_known(monkeypatch):
    # Page 1 (results 1-4): all already in the library -> must top up.
    # Deeper pages return brand-new videos e1.. so the run can hit its target.
    pages = {
        1: [_row(v) for v in ("a", "b", "c", "d")],          # start=1
        5: [_row(v) for v in ("e1", "e2", "e3", "e4")],      # start=5 (deeper)
    }

    def fake_scrape(url, limit, progress=None, start=1):
        return pages.get(start, [])

    monkeypatch.setattr(ys, "PAUSE_BETWEEN_URLS", 0)
    monkeypatch.setattr(ys, "scrape_url", fake_scrape)
    monkeypatch.setattr(ys, "TOPUP_FRACTION", 0.5)   # want 2 new for limit=4

    seen = []
    lib = _FakeLib(known={"a", "b", "c", "d"})
    rows = ys.run_scrape(["u"], limit=4, fast=True, channel_info=False,
                         progress=seen.append, library=lib)

    ids = [r["video_id"] for r in rows]
    assert "e1" in ids and "e2" in ids            # brand-new videos were fetched
    assert any("brand-new" in line for line in seen)


def test_topup_reports_when_no_new_videos(monkeypatch):
    # Top page is all-known, and paging deeper returns nothing -> say so.
    def fake_scrape(url, limit, progress=None, start=1):
        return [_row(v) for v in ("a", "b", "c", "d")] if start == 1 else []

    monkeypatch.setattr(ys, "PAUSE_BETWEEN_URLS", 0)
    monkeypatch.setattr(ys, "scrape_url", fake_scrape)

    seen = []
    lib = _FakeLib(known={"a", "b", "c", "d"})
    ys.run_scrape(["u"], limit=4, fast=True, channel_info=False,
                  progress=seen.append, library=lib)
    assert any("no new videos on youtube" in line.lower()
               or "no more new videos on youtube" in line.lower() for line in seen)
