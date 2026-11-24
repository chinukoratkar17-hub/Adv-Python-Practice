# Closures in Python

def outer(message):
    def inner():
        print(message)
    return inner

greet = outer("Hello from closure")
greet()
