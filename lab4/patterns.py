from abc import ABC, abstractmethod
from typing import List, Optional


class Drink(ABC):
    @abstractmethod
    def cost(self) -> float:
        ...

    @abstractmethod
    def description(self) -> str:
        ...


class Espresso(Drink):
    def cost(self) -> float:
        return 2.0

    def description(self) -> str:
        return "Эспрессо"


class Latte(Drink):
    def cost(self) -> float:
        return 3.5

    def description(self) -> str:
        return "Латте"


class DrinkFactory(ABC):
    @abstractmethod
    def create_drink(self, drink_type: str) -> Drink:
        ...


class SimpleDrinkFactory(DrinkFactory):
    def create_drink(self, drink_type: str) -> Drink:
        if drink_type == "espresso":
            return Espresso()
        elif drink_type == "latte":
            return Latte()
        else:
            raise ValueError(f"Неизвестный тип напитка: {drink_type}")


class DrinkDecorator(Drink, ABC):
    def __init__(self, base_drink: Drink):
        self._base = base_drink


class Milk(DrinkDecorator):
    def cost(self) -> float:
        return self._base.cost() + 0.5

    def description(self) -> str:
        return self._base.description() + " + молоко"


class Sugar(DrinkDecorator):
    def cost(self) -> float:
        return self._base.cost() + 0.2

    def description(self) -> str:
        return self._base.description() + " + сахар"


factory = SimpleDrinkFactory()
drink = factory.create_drink("espresso")     # Эспрессо за 2.0
drink = Milk(drink)                          # +0.5
drink = Sugar(drink)                         # +0.2
print(drink.description())  # "Эспрессо + молоко + сахар"
print(drink.cost())         # 2.7



class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float:
        ...


class NoDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self._percent = percent

    def apply(self, amount: float) -> float:
        return amount * (1 - self._percent / 100)


class FixedDiscount(DiscountStrategy):
    def __init__(self, value: float):
        self._value = value

    def apply(self, amount: float) -> float:
        # Сумма не может быть отрицательной
        return max(0.0, amount - self._value)


class Order:
    def __init__(self, discount_strategy: Optional[DiscountStrategy] = None):
        self.items: List[Drink] = []
        self.discount_strategy = discount_strategy or NoDiscount()

    def add_drink(self, drink: Drink) -> None:
        self.items.append(drink)

    def total(self) -> float:
        base = sum(d.cost() for d in self.items)
        return self.discount_strategy.apply(base)
