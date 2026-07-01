from server import tsv_sources as ts


def _write(dirpath, name, rows, header="keyword\tsubscribers\tviews\n"):
    p = dirpath / name
    body = header + "".join(rows)
    p.write_text(body, encoding="utf-8-sig")   # BOM, like history.save_snapshot
    return p


def test_parse_tsv_is_bom_tolerant():
    data = "﻿keyword\tsubscribers\tviews\nai\t100\t1000\n".encode("utf-8")
    rows = ts.parse_tsv(data)
    assert rows[0]["keyword"] == "ai"          # not "﻿keyword"
    assert rows[0]["subscribers"] == "100"


def test_source_error_codes():
    assert ts.source_error([]) == "empty"
    assert ts.source_error([{"title": "t"}]) == "bad_columns"          # no subscribers col
    assert ts.source_error([{"subscribers": ""}]) == "no_breakout_data"
    assert ts.source_error([{"subscribers": "0"}]) == "no_breakout_data"
    assert ts.source_error([{"subscribers": "100"}]) is None


def test_list_snapshots_excludes_diffs_and_sorts_newest_first(tmp_path, monkeypatch):
    monkeypatch.setattr(ts, "HISTORY_DIR", tmp_path)
    _write(tmp_path, "web_youtube_results_2026-06-01.tsv", ["ai\t10\t100\n"])
    _write(tmp_path, "youtube_results_2026-07-01.tsv", ["ml\t20\t200\n", "ml\t5\t50\n"])
    _write(tmp_path, "diff_a__b.tsv", ["x\ty\tz\n"])   # must be skipped
    snaps = ts.list_snapshots()
    names = [s["file"] for s in snaps]
    assert "diff_a__b.tsv" not in names
    assert names[0] == "youtube_results_2026-07-01.tsv"    # newest by trailing date
    assert snaps[0]["count"] == 2
    assert snaps[0]["keywords"] == ["ml"]


def test_resolve_history_path_blocks_traversal(tmp_path, monkeypatch):
    monkeypatch.setattr(ts, "HISTORY_DIR", tmp_path)
    real = _write(tmp_path, "web_youtube_results_2026-07-01.tsv", ["ai\t10\t100\n"])
    assert ts.resolve_history_path("web_youtube_results_2026-07-01.tsv") == real.resolve()
    assert ts.resolve_history_path("../../etc/passwd") is None
    assert ts.resolve_history_path("nope.tsv") is None          # missing
    assert ts.resolve_history_path("web_youtube_results_2026-07-01.csv") is None  # not .tsv
