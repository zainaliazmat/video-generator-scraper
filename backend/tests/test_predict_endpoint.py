import io

from fastapi.testclient import TestClient

import server.app as app_mod
from server import tsv_sources

client = TestClient(app_mod.app)

_FULL = ("keyword\tsubscribers\tviews\tvideo_id\ttitle\n"
         "ai tools\t100\t1000\tv1\tHello\n")
_FAST = "keyword\tsubscribers\tviews\tvideo_id\nai\t\t1000\tv1\n"   # subs blank


def test_history_lists_snapshots(tmp_path, monkeypatch):
    monkeypatch.setattr(tsv_sources, "HISTORY_DIR", tmp_path)
    (tmp_path / "web_youtube_results_2026-07-01.tsv").write_text(_FULL, encoding="utf-8-sig")
    r = client.get("/api/history")
    assert r.status_code == 200
    snaps = r.json()["snapshots"]
    assert snaps[0]["file"] == "web_youtube_results_2026-07-01.tsv"
    assert snaps[0]["count"] == 1
    assert snaps[0]["keywords"] == ["ai tools"]


def test_predict_upload_creates_done_job():
    files = {"file": ("snap.tsv", _FULL, "text/tab-separated-values")}
    r = client.post("/api/predict", files=files)
    assert r.status_code == 200
    jid = r.json()["job_id"]
    job = app_mod.MANAGER.get(jid)
    assert job.status == "done"
    assert job.rows[0]["title"] == "Hello"
    assert job.params["predict"] is True


def test_predict_from_history(tmp_path, monkeypatch):
    monkeypatch.setattr(tsv_sources, "HISTORY_DIR", tmp_path)
    (tmp_path / "web_youtube_results_2026-07-01.tsv").write_text(_FULL, encoding="utf-8-sig")
    r = client.post("/api/predict", data={"history": "web_youtube_results_2026-07-01.tsv"})
    assert r.status_code == 200
    assert app_mod.MANAGER.get(r.json()["job_id"]).rows[0]["title"] == "Hello"


def test_predict_history_traversal_404(tmp_path, monkeypatch):
    monkeypatch.setattr(tsv_sources, "HISTORY_DIR", tmp_path)
    r = client.post("/api/predict", data={"history": "../../etc/passwd"})
    assert r.status_code == 404


def test_predict_fast_mode_tsv_rejected():
    files = {"file": ("fast.tsv", _FAST, "text/tab-separated-values")}
    r = client.post("/api/predict", files=files)
    assert r.status_code == 422
    assert r.json()["detail"] == "no_breakout_data"


def test_predict_empty_file_rejected():
    files = {"file": ("empty.tsv", "", "text/tab-separated-values")}
    r = client.post("/api/predict", files=files)
    assert r.status_code == 422
    assert r.json()["detail"] == "empty"


def test_predict_too_large_rejected():
    big = "keyword\tsubscribers\n" + ("ai\t100\n" * 1_600_000)  # > 10 MB
    files = {"file": ("big.tsv", big, "text/tab-separated-values")}
    r = client.post("/api/predict", files=files)
    assert r.status_code == 413
    assert r.json()["detail"] == "too_large"


def test_predict_requires_a_source():
    assert client.post("/api/predict").status_code == 400
