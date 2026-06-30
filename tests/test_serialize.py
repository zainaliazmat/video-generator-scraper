from server import serialize


def test_full_row_computes_breakout():
    row = {"video_id": "x1", "title": "T", "channel": "C",
           "subscribers": "57000", "channel_verified": "No",
           "views": "1230000", "likes": "48200", "comments": "3110",
           "duration": "12:40", "duration_sec": "760", "upload_date": "2026-06-14",
           "keyword": "best ai tools", "thumbnail": "http://t", "channel_url": "http://c",
           "video_url": "http://v"}
    out = serialize.row_to_api(row)
    assert out["views"] == 1230000
    assert out["verified"] is False
    assert out["breakout"] == round(1230000 / 57000, 1)


def test_int_typed_inputs_serialize(monkeypatch):
    # run_scrape produces int-typed values, not strings.
    row = {"video_id": "x3", "views": 1000, "subscribers": 100,
           "likes": 50, "comments": 5, "duration_sec": 600, "channel_verified": "Yes"}
    out = serialize.row_to_api(row)
    assert out["views"] == 1000
    assert out["breakout"] == 10.0
    assert out["verified"] is True


def test_fast_mode_blanks_become_none_and_breakout_none():
    row = {"video_id": "x2", "title": "T", "channel": "C",
           "subscribers": "", "channel_verified": "", "views": "5000",
           "likes": "", "comments": "", "duration": "", "duration_sec": "",
           "upload_date": "", "keyword": "k", "thumbnail": "", "channel_url": "",
           "video_url": ""}
    out = serialize.row_to_api(row)
    assert out["subscribers"] is None
    assert out["verified"] is None
    assert out["breakout"] is None


def test_zero_subscribers_does_not_divide_by_zero():
    row = {"video_id": "x4", "views": "5000", "subscribers": "0"}
    assert serialize.row_to_api(row)["breakout"] is None
