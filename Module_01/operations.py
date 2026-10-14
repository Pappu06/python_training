# Operations in python
# arithmetic operations
print("Arithmetic Operations:")


x = 10
y = 5
print(x + y)  # addition
print(x - y)  # subtraction
print(x * y)  # multiplication
print(x / y)  # division
print(x % y)  # modulus
print(x ** y) # exponentiation

# comparison operations
print("Comparison Operations:")


x = 10  
y = 5
print(x > y)  # greater than
print(x < y)  # less than   
print(x == y) # equal to
print(x != y) # not equal to

# logical operations
print("Logical Operations:")    


x = True
y = False
print(x and y) # logical AND
print(x or y)  # logical OR
print(not x)   # logical NOT

# assignment operations
print("Assignment Operations:")


x = 10
x += 5  # equivalent to x = x + 5
print(x)  # prints 15

x = 10  
x -= 5  # equivalent to x = x - 5
print(x)  # prints 5

x = 10
x *= 5  # equivalent to x = x * 5
print(x)  # prints 50

x = 10
x /= 5  # equivalent to x = x / 5
print(x)  # prints 2.0


# logical operations with multiple conditions
print("Logical Operations with Multiple Conditions:")

x = 10
y = 5
print(x > 5 and y < 10)  # True
print(x > 5 or y > 10)   # True
print(not (x > 5 and y < 10)) # False


#membership operations
print("Membership Operations:")

x = [1, 2, 3, 4, 5]
print(3 in x)  # True
print(6 not in x)  # True   


# identify operators in python
print("Identity Operations:")


x = 10
y = 10
print(x is y)  # True, because both x and y point to the same object in memory
print(x is not y)  # False, because x and y point to the same object in memory

