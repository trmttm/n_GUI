from n_gui.command import Command
from n_gui.property import Property
from .widget import Widget


class Button(Widget):
    push = Command()
    text = Property()

    def __init__(self, widget_id: str):
        super().__init__(widget_id)
