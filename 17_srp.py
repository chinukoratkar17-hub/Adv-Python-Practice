# SOLID Principle: Single Responsibility Principle (SRP)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

class StudentReport:
    def display(self, student):
        print("Student:", student.name)
        print("Marks:", student.marks)

s = Student("Aryan", 85)
report = StudentReport()
report.display(s)
