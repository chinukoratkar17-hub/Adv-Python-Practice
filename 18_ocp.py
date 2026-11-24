# SOLID Principle: Open/Closed Principle (OCP)

class Discount:
    def calculate(self, amount):
        return amount

class FestivalDiscount(Discount):
    def calculate(self, amount):
        return amount * 0.80

class RegularDiscount(Discount):
    def calculate(self, amount):
        return amount * 0.90

def final_price(amount, discount):
    return discount.calculate(amount)

print("Festival price:", final_price(1000, FestivalDiscount()))
print("Regular price:", final_price(1000, RegularDiscount()))
