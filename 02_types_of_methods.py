# Types of Methods in Python

class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print("Instance method:", self.name)

    @classmethod
    def class_method(cls):
        print("Class method:", cls.college)

    @staticmethod
    def static_method():
        print("Static method: Welcome to Python")

s = Student("Aryan")
s.instance_method()
Student.class_method()
Student.static_method()
