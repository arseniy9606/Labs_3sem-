from abc import ABC, abstractmethod


class GeomFigure(ABC):
    FIGURE_TYPE = "Фигура"

    @classmethod
    def get_figure_type(cls) -> str:
        return cls.FIGURE_TYPE

    @abstractmethod
    def area(self) -> float:
        pass
