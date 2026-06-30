import youtube_scraper as ys


def test_run_scrape_calls_progress_and_returns_rows(monkeypatch):
    # Stub the network layer so no YouTube call happens.
    fake_rows = {
        "https://yt/?search_query=a": [{"video_id": "x1", "keyword": "a", "views": 10}],
        "https://yt/?search_query=b": [{"video_id": "x2", "keyword": "b", "views": 20}],
    }
    monkeypatch.setattr(ys, "scrape_url", lambda url, limit: fake_rows[url])
    # In fast mode channel enrichment must NOT run.
    monkeypatch.setattr(ys, "enrich_with_channel_info",
                        lambda rows: (_ for _ in ()).throw(AssertionError("should not enrich")))
    monkeypatch.setattr(ys, "PAUSE_BETWEEN_URLS", 0)

    seen = []
    rows = ys.run_scrape(list(fake_rows), limit=5, fast=True, channel_info=False,
                         progress=seen.append)

    assert [r["video_id"] for r in rows] == ["x1", "x2"]
    assert any("[1/2]" in line for line in seen)
    assert any("[2/2]" in line for line in seen)


def test_run_scrape_honours_should_cancel(monkeypatch):
    calls = []

    def fake_scrape(url, limit):
        calls.append(url)
        return [{"video_id": "v", "keyword": "k"}]

    monkeypatch.setattr(ys, "scrape_url", fake_scrape)
    monkeypatch.setattr(ys, "PAUSE_BETWEEN_URLS", 0)

    # Cancel before the second URL is processed.
    urls = ["u1", "u2", "u3"]
    rows = ys.run_scrape(urls, limit=5, fast=True, channel_info=False,
                         should_cancel=lambda: len(calls) >= 1)

    # Only the first URL was scraped; the rest were skipped on cancel.
    assert calls == ["u1"]
    assert len(rows) == 1
