"""ytauto — the app shell and landing menu.

The menu is home: arrow to a task, Enter to open it. Each task pushes its own
screen and returns here when done.
"""
from pathlib import Path

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, OptionList, Static
from textual.widgets.option_list import Option

from tui.diff_screen import DiffScreen
from tui.predict_screen import PredictScreen
from tui.scrape_screen import ScrapeScreen

STYLES = Path(__file__).with_name("ytauto.tcss")


class MenuScreen(Screen):
    BINDINGS = [("q", "app.quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        yield Static("ytauto", id="brand")
        yield Static("YouTube scraper — pick a task, press Enter", id="tagline")
        menu = OptionList(
            Option("Scrape YouTube", id="scrape"),
            Option("Predict content ideas", id="predict"),
            Option("Compare snapshots", id="diff"),
            Option("Quit", id="quit"),
            id="menu",
        )
        yield menu
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#menu", OptionList).focus()

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        choice = event.option.id
        if choice == "scrape":
            self.app.push_screen(ScrapeScreen())
        elif choice == "predict":
            self.app.push_screen(PredictScreen())
        elif choice == "diff":
            self.app.push_screen(DiffScreen())
        elif choice == "quit":
            self.app.exit()


class YtAutoApp(App):
    CSS_PATH = STYLES
    TITLE = "ytauto"

    def on_mount(self) -> None:
        self.push_screen(MenuScreen())


def main():
    YtAutoApp().run()


if __name__ == "__main__":
    main()
