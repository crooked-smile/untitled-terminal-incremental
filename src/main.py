from textual.app import App
from textual.containers import Container, Horizontal
from textual.widgets import Button, Label

from widgets.main_content import RightSideContent
from widgets.sidebar import Sidebar

class MainApp(App):
    TITLE = "Untitled Terminal Incremental"
    ENABLE_COMMAND_PALETTE = False
    CSS_PATH = "index.tcss"

    def compose(self):
        yield Label(self.TITLE, id="mainHeader")
        yield Horizontal(
            Sidebar(),
            RightSideContent()
        )

    def on_mount(self):
        self.notify(message="test", title="title")

if __name__ == "__main__":
    MainApp().run()
