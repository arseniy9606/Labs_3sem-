from .rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side: float, color: str):
        super().__init__(side, side, color)

    def __repr__(self) -> str:
        return "Фигура: {0}, цвет: {1}, сторона: {2}, площадь: {3:.2f}".format(
            self.get_figure_type(),
            self.color.color,
            self.width,
            self.area(),
        )
