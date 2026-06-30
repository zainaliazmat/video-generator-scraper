import ideas


def test_parse_prediction_extracts_embedded_json():
    text = 'sure! {"topic":"X","ideas":[]} done'
    assert ideas.parse_prediction_json(text)["topic"] == "X"


def test_parse_prediction_bad_returns_none():
    assert ideas.parse_prediction_json("no json here") is None


def test_normalize_clamps_and_cleans():
    obj = {"topic": "T", "angle": "A", "est_breakout": "x12",
           "rationale": "R",
           "evidence": ["a", "b", "c", "d", "e"],     # >4 -> clipped
           "ideas": [{"title": "i1", "est": "x11"}, {"title": "i2", "est": "9"},
                     {"title": "i3"}, {"title": "i4"}, {"title": "i5"}]}
    out = ideas.normalize_prediction(obj)
    assert out["est"] == "12"                  # stripped to digits
    assert len(out["evidence"]) == 4
    assert len(out["ideas"]) == 4
    assert out["ideas"][0] == {"title": "i1", "est": "11"}


def test_generate_prediction_reports_cli_missing(monkeypatch):
    from claude_agent_sdk import CLINotFoundError

    async def boom(digest):
        raise CLINotFoundError("claude CLI not found")

    monkeypatch.setattr(ideas, "build_digest", lambda rows: "digest")
    monkeypatch.setattr(ideas, "_prediction_async", boom)
    out = ideas.generate_prediction([{"video_id": "a"}])
    assert out["ok"] is False
    assert out["reason"] == "cli_missing"


def test_generate_prediction_success(monkeypatch):
    async def fake(digest):
        return '{"topic":"Do X","angle":"now","est_breakout":"x9",' \
               '"rationale":"r","evidence":["e1"],"ideas":[{"title":"t","est":"5"}]}'

    monkeypatch.setattr(ideas, "build_digest", lambda rows: "digest")
    monkeypatch.setattr(ideas, "_prediction_async", fake)
    out = ideas.generate_prediction([{"video_id": "a"}])
    assert out["ok"] is True
    assert out["source"] == "ai"
    assert out["topic"] == "Do X"


def test_generate_prediction_parse_failure(monkeypatch):
    async def junk(digest):
        return "the model rambled with no json"

    monkeypatch.setattr(ideas, "build_digest", lambda rows: "digest")
    monkeypatch.setattr(ideas, "_prediction_async", junk)
    out = ideas.generate_prediction([{"video_id": "a"}])
    assert out["ok"] is False
    assert out["reason"] == "parse_failed"
