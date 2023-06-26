from .widget import Widget


class Tree(Widget):
    def __init__(self, widget_id: str = None):
        self._selected_rows = []
        super().__init__(widget_id)

    def select_rows(self, n_rows: tuple[int, ...]):
        for n in n_rows:
            self.select_row(n)

    def select_row(self, n: int):
        self._selected_rows.append(n)

    @property
    def selected_rows(self) -> tuple[int, ...]:
        return tuple(self._selected_rows)
