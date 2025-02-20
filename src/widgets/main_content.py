from textual.containers import Horizontal, Container, Vertical
from textual.widgets import Label

class RightSideContent(Horizontal):
    def compose(self):
        yield Vertical(
            NewsTicker(),
            MainContainer()
        )


class NewsTicker(Label):
    def on_mount(self):
        self.id = "newsTicker"
        self.border_title = "News"

        self.update("")

class MainContainer(Container):
    def on_mount(self):
        self.border_title = "0 stdins"