"""PredictScreen — pick a data source, then stream a Claude prediction.

Source is either the rows from the scrape you just ran (passed in) or a saved
snapshot from history/. The AI text streams live into the RunScreen log.
"""
import ideas
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.screen import Screen
from textual.widgets import Footer, Header, OptionList, Static
from textual.widgets.option_list import Option

from tui import sources
from tui.run_screen import RunScreen


class PredictScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Back")]

    def __init__(self, rows=None):
        super().__init__()
        self._fresh_rows = rows          # rows from a just-finished scrape, or None
        self._snapshots = []

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with VerticalScroll(id="form"):
            yield Static("Predict content ideas", id="form-title")
            yield Static("Choose the data to analyse:", classes="label")
            yield OptionList(id="sources")
            yield Static("", id="predict-error")
        yield Footer()

    def on_mount(self) -> None:
        ol = self.query_one("#sources", OptionList)
        if self._fresh_rows:
            ol.add_option(Option(f"Last scrape — {len(self._fresh_rows)} videos", id="fresh"))
        self._snapshots = sources.list_snapshots()
        for snap in self._snapshots:
            label = f"{snap['date'] or snap['file']} — {snap['count']} videos"
            if snap["keywords"]:
                label += f"  ({', '.join(snap['keywords'][:3])})"
            ol.add_option(Option(label, id=f"snap:{snap['path']}"))
        if not ol.option_count:
            self.query_one("#predict-error", Static).update(
                "[yellow]No data yet — run a scrape first.[/yellow]")
        else:
            ol.focus()

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        oid = event.option.id
        if oid == "fresh":
            self._start(self._fresh_rows)
            return
        if oid and oid.startswith("snap:"):
            path = oid[len("snap:"):]
            try:
                rows = sources.parse_tsv(open(path, "rb").read())
            except Exception as exc:
                self.query_one("#predict-error", Static).update(f"[red]Could not read file: {exc}[/red]")
                return
            self._start(rows)

    def _start(self, rows) -> None:
        reason = sources.source_error(rows)
        if reason:
            self.query_one("#predict-error", Static).update(f"[red]{reason}[/red]")
            return

        def work(log, should_cancel):
            log(f"$ predict --videos {len(rows)}")
            log(f"connecting to Claude ({getattr(ideas, 'MODEL', 'claude')})…\n")
            return ideas.generate_prediction(rows, on_text=log)

        def summarize(result):
            if result and result.get("ok"):
                return f"Prediction: {result.get('topic', '(untitled)')}"
            reason = (result or {}).get("reason", "unknown")
            return f"No prediction ({reason})."

        def followups(result):
            if result and result.get("ok"):
                return [("Show full prediction", lambda: self._dump(result))]
            return []

        self.app.push_screen(RunScreen("Predicting…", work, summarize, followups))

    def _dump(self, p) -> None:
        """Append the structured prediction to the current RunScreen log."""
        screen = self.app.screen
        log = getattr(screen, "_write", None)
        if not log:
            return
        log("")
        log(f"TOPIC:  {p.get('topic','')}")
        log(f"ANGLE:  {p.get('angle','')}")
        log(f"EST. BREAKOUT SCORE: {p.get('est','')}")
        if p.get("rationale"):
            log(f"WHY:    {p['rationale']}")
        for e in p.get("evidence", []):
            log(f"  - {e}")
        if p.get("ideas"):
            log("IDEAS:")
            for it in p["ideas"]:
                log(f"  - {it.get('title','')}  (est {it.get('est','')})")
