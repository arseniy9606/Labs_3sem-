import math

from .geom_figure import GeomFigure
from .color import FigureColor


class Circle(GeomFigure):
    FIGURE_TYPE = "Круг"

    def __init__(self, radius: float, color: str):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def __repr__(self) -> str:
        return "Фигура: {0}, цвет: {1}, радиус: {2}, площадь: {3:.2f}".format(
            self.get_figure_type(),
            self.color.color,
            self.radius,
            self.area(),
        )
