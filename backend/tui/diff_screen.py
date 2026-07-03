"""DiffScreen — compare two saved snapshots and show what changed.

Picks an OLD and a NEW snapshot (defaults to the two most recent), runs
history.diff, and streams its report into a RunScreen. history.diff prints its
summary, so we redirect stdout into the log.
"""
import contextlib

import history
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Select, Static

from tui import sources
from tui.run_screen import RunScreen


class _LogWriter:
    """File-like object that forwards each written line to a log callback."""

    def __init__(self, log):
        self._log = log
        self._buf = ""

    def write(self, s):
        self._buf += s
        while "\n" in self._buf:
            line, self._buf = self._buf.split("\n", 1)
            self._log(line)

    def flush(self):
        if self._buf:
            self._log(self._buf)
            self._buf = ""


class DiffScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Back")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with VerticalScroll(id="form"):
            yield Static("Compare snapshots", id="form-title")
            self._snaps = sources.list_snapshots()   # newest first
            if len(self._snaps) < 2:
                yield Static(
                    "[yellow]Need at least two snapshots to compare. "
                    "Run a scrape a couple of times first.[/yellow]",
                    classes="label")
            else:
                opts = [(f"{s['date'] or s['file']} — {s['count']} videos", s["path"])
                        for s in self._snaps]
                yield Static("OLD snapshot:", classes="label")
                yield Select(opts, value=self._snaps[1]["path"], id="old", allow_blank=False)
                yield Static("NEW snapshot:", classes="label")
                yield Select(opts, value=self._snaps[0]["path"], id="new", allow_blank=False)
                yield Button("Compare", id="compare", variant="success")
            yield Static("", id="diff-error")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id != "compare":
            return
        old = self.query_one("#old", Select).value
        new = self.query_one("#new", Select).value
        if old == new:
            self.query_one("#diff-error", Static).update(
                "[red]Pick two different snapshots.[/red]")
            return

        def work(log, should_cancel):
            with contextlib.redirect_stdout(_LogWriter(log)):
                out_path = history.diff(old, new)
            return out_path

        def summarize(out_path):
            return f"Diff written → {out_path}"

        self.app.push_screen(RunScreen("Comparing snapshots…", work, summarize))
