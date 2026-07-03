"""RunScreen — the shared "watch it work" view.

Runs a blocking backend call (scrape, predict, diff) in a background thread so
the UI stays responsive, streams its progress lines into a log, and — when it
finishes — shows a summary plus follow-up buttons. Cancel with Esc.
"""
import threading

from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, LoadingIndicator, RichLog, Static


class RunScreen(Screen):
    """Generic runner.

    work(log, should_cancel) -> result   runs in a thread; `log(str)` is
        thread-safe, `should_cancel()` reflects the Esc/Cancel button.
    summarize(result) -> str             one-line result headline.
    followups(result) -> [(label, fn)]   buttons shown when done; fn() runs on
        the UI thread (e.g. push the next screen).
    """

    BINDINGS = [("escape", "cancel", "Cancel")]

    def __init__(self, title, work, summarize=None, followups=None):
        super().__init__()
        self._title = title
        self._work = work
        self._summarize = summarize or (lambda r: "Done.")
        self._followups = followups or (lambda r: [])
        self._cancel = threading.Event()
        self._done = False

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        yield Static(self._title, id="run-title")
        yield LoadingIndicator(id="run-spinner")
        yield RichLog(id="run-log", wrap=True, markup=False, highlight=False)
        yield Static("", id="run-summary")
        yield Horizontal(id="run-actions")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#run-log", RichLog).focus()
        self._run()

    # --- background work ---------------------------------------------------- #
    def _log(self, msg) -> None:
        """Thread-safe: append a line to the log from the worker thread."""
        text = msg if isinstance(msg, str) else str(msg)
        self.app.call_from_thread(self._write, text.rstrip("\n"))

    def _write(self, text) -> None:
        self.query_one("#run-log", RichLog).write(text)

    @work(thread=True)
    def _run(self) -> None:
        try:
            result = self._work(self._log, self._cancel.is_set)
            self.app.call_from_thread(self._finish, result, None)
        except Exception as exc:  # surface, never crash the app
            self.app.call_from_thread(self._finish, None, exc)

    def _finish(self, result, error) -> None:
        self._done = True
        self.query_one("#run-spinner").display = False
        summary = self.query_one("#run-summary", Static)
        if error is not None:
            summary.update(f"[b red]Failed:[/b red] {error}")
            actions = []
        elif self._cancel.is_set():
            summary.update("[yellow]Cancelled.[/yellow]")
            actions = self._followups(result)
        else:
            summary.update(f"[b green]{self._summarize(result)}[/b green]")
            actions = self._followups(result)

        bar = self.query_one("#run-actions", Horizontal)
        self._handlers = {}
        for i, (label, fn) in enumerate(actions):
            bid = f"fu-{i}"
            self._handlers[bid] = fn
            bar.mount(Button(label, id=bid, variant="primary"))
        bar.mount(Button("Back to menu", id="fu-menu"))
        bar.children[0].focus() if bar.children else None

    # --- interaction -------------------------------------------------------- #
    def action_cancel(self) -> None:
        if self._done:
            self.app.pop_screen()
        elif not self._cancel.is_set():
            self._cancel.set()
            self.query_one("#run-summary", Static).update("[yellow]Cancelling…[/yellow]")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "fu-menu":
            self.app.pop_screen()
        else:
            handler = getattr(self, "_handlers", {}).get(event.button.id)
            if handler:
                handler()
