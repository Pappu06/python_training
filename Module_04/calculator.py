# A fully functional Calculator. Using pakackge and modules

from calulator import math


print("====Welcome to the Calculator====")

num1 = float(input("Enter the first number: ")) # taking input from the user for the first number
num2 = float(input("Enter the second number: ")) # taking input from the user for the second number

# Displaying the menu of operations
print("Select operation:")
print("1. Add") 
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ") # taking input from the user for the operation choice


# Performing the selected operation based on user input
if choice == '1':
    print(f"{num1} + {num2} = {math.add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {math.subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {math.multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {math.divide(num1, num2)}")
else:
    print("Invalid input. Please enter a valid choice.")


