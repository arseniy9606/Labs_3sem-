class Notifier:
    def send_payment_success(self, order_id: str, amount: float) -> None:
        print(f"Заказ {order_id} оплачен на сумму {amount}")

