"""ScrapeScreen — paste URLs/keywords, pick options, hit Generate.

Replaces editing urls.txt and remembering flags. On Generate it hands a scrape
closure to a RunScreen and (when done) offers to predict on the fresh data.
"""
import youtube_scraper as ys
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Select, Static, Switch, TextArea

import history
from tui import inputs as inp
from tui.run_screen import RunScreen


class ScrapeScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Back")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with VerticalScroll(id="form"):
            yield Static("Scrape YouTube", id="form-title")
            yield Static("Paste search URLs or plain keywords — one per line:", classes="label")
            yield TextArea(id="urls", language=None)
            yield Static("Time range:", classes="label")
            yield Select(
                [(k, k) for k in inp.DATE_FILTERS],
                value="Any time", id="date", allow_blank=False,
            )
            yield Static("Videos per link:", classes="label")
            yield Select(
                [(c, c) for c in inp.PER_LINK_CHOICES],
                value="60 videos", id="perlink", allow_blank=False,
            )
            with Horizontal(id="fast-row"):
                yield Static("Fast mode (skip per-video likes/comments/subs — much faster):",
                             classes="label")
                yield Switch(value=True, id="fast")
            with Horizontal(id="scrape-actions"):
                yield Button("Generate", id="generate", variant="success")
                yield Button("Back", id="back")
            yield Static("", id="scrape-error")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#urls", TextArea).focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id == "generate":
            self._generate()

    def _generate(self) -> None:
        text = self.query_one("#urls", TextArea).text
        date_label = self.query_one("#date", Select).value
        urls = inp.parse_inputs(text, date_label)
        err = self.query_one("#scrape-error", Static)
        if not urls:
            err.update("[red]Add at least one keyword or URL first.[/red]")
            return
        err.update("")
        limit = inp.per_link_to_int(self.query_one("#perlink", Select).value)
        fast = self.query_one("#fast", Switch).value

        def work(log, should_cancel):
            log(f"Starting scrape of {len(urls)} search(es), up to {limit} videos each…")
            rows = ys.run_scrape(urls, limit=limit, fast=fast, channel_info=not fast,
                                 cookies=None, progress=log, should_cancel=should_cancel)
            if rows:
                ys.write_tsv(rows, "youtube_results.tsv")
                log("Saved youtube_results.tsv")
                try:
                    path = history.save_snapshot(rows, ys.COLUMNS)
                    log(f"Saved snapshot {path}")
                except Exception as exc:
                    log(f"(snapshot skipped: {exc})")
            return rows

        def summarize(rows):
            return f"Collected {len(rows)} videos → youtube_results.tsv"

        def followups(rows):
            if not rows:
                return []
            from tui.predict_screen import PredictScreen
            return [("Predict on this data", lambda: self.app.push_screen(PredictScreen(rows=rows)))]

        self.app.push_screen(RunScreen("Scraping YouTube…", work, summarize, followups))
