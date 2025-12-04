from patterns import Order
from notific import Notifier


def pay_for_order(order: Order, notifier: Notifier, order_id: str) -> float:
    amount = order.total()
    notifier.send_payment_success(order_id, amount)
    return amount
