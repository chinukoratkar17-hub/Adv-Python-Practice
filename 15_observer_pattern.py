# Observer Design Pattern

class Observer:
    def update(self, message):
        print("Notification:", message)

class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

subject = Subject()
subject.add_observer(Observer())
subject.notify("New notice available")
