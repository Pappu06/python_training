# OOP in python 

class student: # defining a class
    name = "pappu"
    age = 23

student1 = student() # creating an object of the class student

print(student1.name)
print(student1.age)

class computer: # defining a class
    def __init__(self, cpu, ram, model): # __init__ method
        self.cpu = cpu
        self.ram = ram
        self.model = model

    def config(self):
        print("this is config: ", self.cpu, self.ram, self.model)

system_01 = computer("i5", "12GB", "Asus")              # object 1
system_02 = computer("Ryzen 5", "16GB", "Lenovo")       # object 2
system_03 = computer("i7", "12BG", "Acer")              # object 3

system_01.config()
system_02.config()
system_03.config()

