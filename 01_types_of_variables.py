# Types of Variables in Python

class Student:
    college = "ABC College"       # Class variable

    def __init__(self, name, marks):
        self.name = name         # Instance variable
        self.marks = marks

    def show(self):
        age = 20                 # Local variable
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Age:", age)
        print("College:", Student.college)

s1 = Student("Aryan", 85)
s1.show()
