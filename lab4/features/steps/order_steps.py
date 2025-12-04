from behave import given, when, then
from patterns import SimpleDrinkFactory, Order, PercentageDiscount, FixedDiscount
import math

@given('пустой заказ с процентной скидкой {percent:d}')
def step_given_order_with_percentage_discount(context, percent):
    context.factory = SimpleDrinkFactory()
    context.order = Order(discount_strategy=PercentageDiscount(percent))

@when('я добавляю в заказ "{drink_type}"')
def step_when_add_drink(context, drink_type):
    drink = context.factory.create_drink(drink_type)
    context.order.add_drink(drink)

@then('итоговая сумма должна быть {expected:f}')
def step_then_total_should_be(context, expected):
    total = context.order.total()
    assert math.isclose(total, expected, rel_tol=0.001) 

@given('пустой заказ с фиксированной скидкой {value:f}')
def step_given_order_with_fixed_discount(context, value):
    context.factory = SimpleDrinkFactory()
    context.order = Order(discount_strategy=FixedDiscount(value))
