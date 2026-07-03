"""Headless smoke test: boot the TUI and open each screen without a terminal.

Uses Textual's Pilot. No network, no scraping — just proves the screens compose
and navigation works, so a broken import or bad CSS is caught in CI.
"""
import pytest

from tui.app import YtAutoApp
from tui.diff_screen import DiffScreen
from tui.predict_screen import PredictScreen
from tui.scrape_screen import ScrapeScreen


@pytest.mark.asyncio
async def test_menu_boots_and_lists_tasks():
    app = YtAutoApp()
    async with app.run_test() as pilot:
        menu = app.screen.query_one("#menu")
        labels = [str(opt.prompt) for opt in menu._options]
        assert "Scrape YouTube" in labels
        assert "Quit" in labels
        await pilot.pause()


@pytest.mark.asyncio
async def test_open_each_screen():
    app = YtAutoApp()
    async with app.run_test() as pilot:
        app.push_screen(ScrapeScreen())
        await pilot.pause()
        assert isinstance(app.screen, ScrapeScreen)
        app.pop_screen()
        await pilot.pause()

        app.push_screen(PredictScreen())
        await pilot.pause()
        assert isinstance(app.screen, PredictScreen)
        app.pop_screen()
        await pilot.pause()

        app.push_screen(DiffScreen())
        await pilot.pause()
        assert isinstance(app.screen, DiffScreen)


@pytest.mark.asyncio
async def test_scrape_requires_input():
    """Generate with an empty form shows an error, does not start a run."""
    app = YtAutoApp()
    async with app.run_test() as pilot:
        app.push_screen(ScrapeScreen())
        await pilot.pause()
        scrape = app.screen
        scrape._generate()
        await pilot.pause()
        # No run started: still on the scrape form, with an error shown.
        assert app.screen is scrape
        err = scrape.query_one("#scrape-error")
        assert "Add at least one" in str(err.content)
