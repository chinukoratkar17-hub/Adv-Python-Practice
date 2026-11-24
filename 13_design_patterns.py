# Introduction to Design Patterns

# A design pattern is a reusable solution to a common software problem.

class Logger:
    def log(self, message):
        print("LOG:", message)

class Application:
    def __init__(self, logger):
        self.logger = logger

    def run(self):
        self.logger.log("Application is running")

app = Application(Logger())
app.run()
