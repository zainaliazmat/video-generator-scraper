"""LibraryScreen — browse and search the central video library (library.db).

Shows headline stats and a table of every video ever scraped, newest-value
first by views. Type in the search box to filter by title / channel / keyword.
Read-only: the library is written by scraping, this just looks at it.
"""
import library
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.screen import Screen
from textual.widgets import DataTable, Footer, Header, Input, Static

COLS = [("Title", 60), ("Channel", 24), ("Views", 12), ("Subs", 11),
        ("Seen", 5), ("Last seen", 11)]


def _int(v):
    try:
        return f"{int(float(v)):,}"
    except (TypeError, ValueError):
        return v or ""


class LibraryScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Back")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with VerticalScroll(id="form"):
            yield Static("Library", id="form-title")
            yield Static("", id="lib-stats", classes="label")
            yield Input(placeholder="Search title / channel / keyword…", id="lib-search")
            yield DataTable(id="lib-table", zebra_stripes=True, cursor_type="row")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one("#lib-table", DataTable)
        for name, width in COLS:
            table.add_column(name, width=width)
        try:
            with library.connect() as conn:
                st = library.stats(conn)
                self.query_one("#lib-stats", Static).update(
                    f"{st['videos']} videos · {st['channels']} channels · "
                    f"first seen {st['since'] or '—'} · latest {st['latest'] or '—'}")
        except Exception as exc:
            self.query_one("#lib-stats", Static).update(f"[red]Could not open library: {exc}[/red]")
        self._load("")
        self.query_one("#lib-search", Input).focus()

    def on_input_changed(self, event: Input.Changed) -> None:
        self._load(event.value.strip())

    def _load(self, term) -> None:
        table = self.query_one("#lib-table", DataTable)
        table.clear()
        try:
            with library.connect() as conn:
                rows = (library.search(conn, term) if term
                        else library.all_videos(conn))
        except Exception:
            rows = []
        if not rows:
            table.add_row("(no matching videos)" if term else "(library is empty — run a scrape)",
                          "", "", "", "", "")
            return
        for r in rows:
            table.add_row(
                (r.get("title") or "")[:60],
                (r.get("channel") or "")[:24],
                _int(r.get("views")),
                _int(r.get("subscribers")),
                str(r.get("times_seen") or ""),
                r.get("last_seen") or "",
            )
