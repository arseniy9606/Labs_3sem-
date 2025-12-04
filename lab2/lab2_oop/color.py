class FigureColor:
    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        self._color = new_color

    def __repr__(self) -> str:
        return "Цвет: {0}".format(self._color)
