# Inheritance -- It appends the properties of parant class and it can be multiple inherit from multilpe classes

class Animal:
    def eat(self):
        print("Animal can eat.")

class Mammal(Animal): # Mammal class inherit the peoperties of Animal class 
    def walk(self):
        print("Mammal can walk.")


class Dog(Mammal): # Multi level inheritance Dog class inherit the both properties of Animal and Mammal 
    def bark(self):
        print("Dog is barking.")


dog = Dog() # object of dog class

dog.eat() # Access Animal property from dog objectt
dog.walk()
dog.bark()