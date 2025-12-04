from patterns import SimpleDrinkFactory, Milk, Sugar, Order
from patterns import PercentageDiscount, FixedDiscount

# 1. Демонстрация фабрики

factory = SimpleDrinkFactory()

espresso = factory.create_drink("espresso")
latte = factory.create_drink("latte")

print("=== Фабрика ===")
print(espresso.description(), espresso.cost())
print(latte.description(), latte.cost())
print()

# 2. Демонстрация декораторов

decorated = Milk(Sugar(espresso))  # вместо espresso можно latte

print("=== Декораторы ===")
print(decorated.description(), decorated.cost())
print()

# 3. Демонстрация стратегий

order1 = Order(discount_strategy=PercentageDiscount(10))
order1.add_drink(factory.create_drink("espresso"))
order1.add_drink(factory.create_drink("latte"))

print("=== Стратегия: процентная скидка (10%) ===")
print("Сумма:", order1.total())
print()

order2 = Order(discount_strategy=FixedDiscount(2.0))
order2.add_drink(factory.create_drink("espresso"))
order2.add_drink(factory.create_drink("latte"))

print("=== Стратегия: фиксированная скидка (2.0) ===")
print("Сумма:", order2.total())
print()
