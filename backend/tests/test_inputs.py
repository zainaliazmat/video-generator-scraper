from tui import inputs


def test_parse_inputs_mixes_urls_and_keywords():
    text = ("https://www.youtube.com/results?search_query=best+ai+tools\n"
            "how to make money with ai\n"
            "\n"  # blank ignored
            "  # a comment\n")
    out = inputs.parse_inputs(text, "This year")
    assert out[0] == "https://www.youtube.com/results?search_query=best+ai+tools"
    assert out[1].startswith("https://www.youtube.com/results?search_query=how")
    assert "sp=" in out[1]            # keyword got the year filter
    assert len(out) == 2             # blank + comment dropped


def test_parse_inputs_any_time_has_no_sp():
    out = inputs.parse_inputs("ai agents", "Any time")
    assert "sp=" not in out[0]


def test_parse_inputs_this_week_maps_to_real_period():
    out = inputs.parse_inputs("ai agents", "This week")
    assert "sp=" in out[0]            # week is a real YouTube sp code


def test_per_link_to_int():
    assert inputs.per_link_to_int("90 videos") == 90
    assert inputs.per_link_to_int("garbage") == 60


def test_date_filter_keys_match_sp_filters():
    import youtube_scraper as ys
    for period in inputs.DATE_FILTERS.values():
        assert period in ys.SP_FILTERS
