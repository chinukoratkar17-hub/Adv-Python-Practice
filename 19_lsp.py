# SOLID Principle: Liskov Substitution Principle (LSP)

class Bird:
    def eat(self):
        print("Bird is eating")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

def bird_activity(bird):
    bird.eat()

s = Sparrow()
bird_activity(s)
s.fly()
