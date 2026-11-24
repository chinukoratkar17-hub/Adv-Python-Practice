# Strategy Design Pattern

class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class Card:
    def pay(self, amount):
        print("Paid", amount, "using Card")

class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)

payment = Payment(UPI())
payment.make_payment(500)

payment = Payment(Card())
payment.make_payment(1000)
