# Method Resolution Order (MRO) in python

class ParentA:
    def show(self):
        print("Parent A")


class ParentB:
    def show(self):
        print("Parent B")


class Child(ParentA, ParentB):
    pass


obj = Child()
obj.show()


# The __init__() Constructor in Inheritance


# class Parent:
#     def __init__(self):
#         print("Parent constructor executed.")


# class Child(Parent):
#     pass


# obj = Child()

class Parent:
    def __init__(self):
        print("Parent constructor executed.")


class Child(Parent):
    def __init__(self):
        print("Child constructor executed.")


obj = Child()



# super() in Python

class Employee:
    def __init__(self, name):
        self.name = name
        print("Employee initialized.")


class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
        print("Developer initialized.")


dev = Developer("Pappu", "Python")

print(dev.name)
print(dev.language)

# Demo with super()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course


student = Student("Pappu", 22, "B.Tech CSE")

print(student.name)
print(student.age)
print(student.course)