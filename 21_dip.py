# SOLID Principle: Dependency Inversion Principle (DIP)

class MessageService:
    def send(self, message):
        raise NotImplementedError

class EmailService(MessageService):
    def send(self, message):
        print("Email sent:", message)

class Notification:
    def __init__(self, service):
        self.service = service

    def notify(self, message):
        self.service.send(message)

email = EmailService()
notification = Notification(email)
notification.notify("Welcome!")
