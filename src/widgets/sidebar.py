from textual.containers import Vertical, VerticalScroll
from textual.widgets import Label, Button

class Sidebar(Vertical):
    def compose(self):
        yield SidebarCurrencyTracker()
        yield SidebarMenu()

class SidebarCurrencyTracker(Vertical):
    def compose(self):
        yield Label("0", id="sidebarCurrencyAmount")
        yield Label("stdins", id="sidebarCurrencyName")

class SidebarMenu(VerticalScroll):
    def compose(self):
        yield Button("stdin", disabled=True)
        yield Button("Achievements")
        yield Button("Statistics")
        yield Button("Settings")

    def on_mount(self):
        self.border_title = "Menu"
        self.query("Button").set_styles("width: 100%;")