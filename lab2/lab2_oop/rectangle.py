from .geom_figure import GeomFigure
from .color import FigureColor


class Rectangle(GeomFigure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width: float, height: float, color: str):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self) -> float:
        return self.width * self.height

    def __repr__(self) -> str:
        return "Фигура: {0}, цвет: {1}, ширина: {2}, высота: {3}, площадь: {4:.2f}".format(
            self.get_figure_type(),
            self.color.color,
            self.width,
            self.height,
            self.area(),
        )
