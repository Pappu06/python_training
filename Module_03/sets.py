# Sets in python
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Print the set
print(type(my_set))  # Print the type of the set

# set can contain different data types
my_set2 = {1, "hello", 3.14, True}
print(my_set2)  # Print the set with different data types

# set constructor
my_set3 = set((1, 2, 3, 4, 5))
print(my_set3)  # Print the set created using the set constructor

# set with range
my_set4 = set(range(1, 11))
print(my_set4)  # Print the set created using range

# Adding elements to a set
my_set.add(6)  # Add an element to the set
print(my_set)  # Print the updated set

# Removing elements from a set
my_set.remove(3)  # Remove an element from the set
print(my_set)  # Print the updated set after removing an element

# Discard method
my_set.discard(4)  # Discard an element from the set
print(my_set)  # Print the updated set after discarding an element

# pop method
popped_element = my_set.pop()  # Remove and return an arbitrary element from the set
print(popped_element)  # Print the popped element
print(my_set)  # Print the updated set after popping an element


# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
# Union of two sets
union_set = set_a.union(set_b)
print(union_set)  # Print the union of set_a and set_b

# Intersection of two sets
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Print the intersection of set_a and set_b

# Difference of two sets
difference_set = set_a.difference(set_b)
print(difference_set)  # Print the difference of set_a and set_b

# Symmetric difference of two sets
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Print the symmetric difference of set_a and set_b
