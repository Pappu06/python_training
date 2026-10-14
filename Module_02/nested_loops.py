# Nested Loops in Python
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

# Nested loops can also be used to create patterns
# Example: Print a square pattern
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()  # Move to the next line after each row

# Example: Print a triangle pattern
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()  # Move to the next line after each row

# Example: Print a reverse triangle pattern
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line after each row