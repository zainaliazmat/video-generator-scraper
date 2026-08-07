import study


def _row(vid, views, dur=600):
    return {"video_id": vid, "views": str(views), "duration_sec": str(dur)}


def test_pick_three_top_mid_low():
    rows = [_row("a", 1_000_000), _row("b", 500_000), _row("c", 90_000),
            _row("d", 5_000), _row("e", 300)]
    picks = dict(study.pick_three(rows))
    assert picks["top"]["video_id"] == "a"
    assert picks["low"]["video_id"] == "e"
    assert picks["mid"]["video_id"] in ("b", "c")   # closest to median, not top/low


def test_pick_three_filters_shorts_and_junk():
    rows = [_row("short", 9_999_999, dur=60),        # a Short - not comparable
            _row("tiny", 50),                        # below MIN_VIEWS
            {"video_id": "", "views": "100000", "duration_sec": "600"},
            _row("ok", 10_000)]
    picks = study.pick_three(rows)
    assert [r["video_id"] for _, r in picks] == ["ok"]


def test_vtt_to_transcript_dedupes_rolling_captions():
    vtt = """WEBVTT
Kind: captions
Language: en

00:00:01.000 --> 00:00:03.000
so today we're testing

00:00:03.000 --> 00:00:05.000
so today we're testing
<c>eleven</c> AI tools

00:00:05.000 --> 00:00:07.000
eleven AI tools
and only one survived
"""
    out = study.vtt_to_transcript(vtt)
    lines = out.splitlines()
    assert lines[0] == "[0:01] so today we're testing"
    assert "[0:03] eleven AI tools" in lines        # tag stripped, kept once
    assert sum("so today we're testing" in l for l in lines) == 1
    assert lines[-1] == "[0:05] and only one survived"


def test_cookie_opts(monkeypatch):
    monkeypatch.delenv("YTAUTO_COOKIES", raising=False)
    monkeypatch.delenv("YTAUTO_COOKIES_BROWSER", raising=False)
    assert study.cookie_opts() == {}                       # opt-in: no jar by default

    monkeypatch.setenv("YTAUTO_COOKIES_BROWSER", "chrome")
    assert study.cookie_opts() == {"cookiesfrombrowser": ("chrome",)}

    monkeypatch.setenv("YTAUTO_COOKIES", "/tmp/c.txt")     # file wins over browser
    assert study.cookie_opts() == {"cookiefile": "/tmp/c.txt"}
