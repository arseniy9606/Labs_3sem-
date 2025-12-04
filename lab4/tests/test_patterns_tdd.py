import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


import pytest
from unittest.mock import Mock

from patterns import SimpleDrinkFactory, Milk, Sugar, Order, PercentageDiscount, FixedDiscount
from payment import pay_for_order


def test_factory_creates_espresso():
    factory = SimpleDrinkFactory()
    drink = factory.create_drink("espresso")

    assert drink.description() == "Эспрессо"
    assert drink.cost() == 2.0


def test_decorator_adds_milk_and_sugar():
    factory = SimpleDrinkFactory()
    drink = factory.create_drink("latte")
    drink = Milk(Sugar(drink))

    assert "Латте" in drink.description()
    assert "молоко" in drink.description()
    assert "сахар" in drink.description()
    assert drink.cost() == pytest.approx(4.2)


def test_order_with_percentage_discount():
    factory = SimpleDrinkFactory()
    order = Order(discount_strategy=PercentageDiscount(10))  # 10%

    order.add_drink(factory.create_drink("espresso"))  # 2.0
    order.add_drink(factory.create_drink("latte"))     # 3.5

    assert order.total() == pytest.approx(4.95)


def test_order_with_fixed_discount():
    factory = SimpleDrinkFactory()
    order = Order(discount_strategy=FixedDiscount(2.0))

    order.add_drink(factory.create_drink("espresso"))  # 2.0
    order.add_drink(factory.create_drink("latte"))     # 3.5

    assert order.total() == pytest.approx(3.5)


def test_pay_for_order_uses_notifier_mock():
    factory = SimpleDrinkFactory()
    order = Order()
    order.add_drink(factory.create_drink("espresso"))

    notifier_mock = Mock()
    order_id = "ORDER-123"

    amount = pay_for_order(order, notifier_mock, order_id)

    notifier_mock.send_payment_success.assert_called_once_with(order_id, amount)
    assert amount == pytest.approx(2.0)
