# While Loop in Python
i = 0
while i < 5: # Condition for the loop to run
    print("hello")
    i += 1 # Increment i to avoid infinite loop

# break statement to exit the loop
i = 0
while i < 5:
    if i == 3:
        break # Exit the loop when i is 3
    print(i)
    i += 1

# continue statement to skip the current iteration
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue # Skip the rest of the loop when i is 3
    print(i)

# pass statement to do nothing
i = 0
while i < 5:
    i += 1
    if i == 3:
        pass # Do nothing when i is 3
    print(i)

    
