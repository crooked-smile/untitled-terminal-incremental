from textual.containers import Container, Vertical
from textual.widgets import Label

class RightSideContent(Vertical):
    def compose(self):
        yield NewsTicker()
        yield MainContainer()


class NewsTicker(Label):
    def on_mount(self):
        self.id = "newsTicker"
        self.border_title = "News"

        self.update("")

class MainContainer(Container):
    def on_mount(self):
        self.border_title = "0 Processes"