from .command import Command


class Widget:
    mouse_in = Command()
    mouse_out = Command()

    def __init__(self, widget_id: str = None):
        self._id = widget_id
        self.name = f'{self.__class__.__name__}_{self._id}'
