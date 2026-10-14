# Tuples in Python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Print the tuple
print(type(my_tuple))  # Print the type of the tuple

# tuple can contain different data types
students = ("rahul", "sneha", "priya", 55, 22.25, 30)
print(students)  # Print the tuple with different data types

# tuple constructor
my_tuple2 = tuple((1, 2, 3, 4, 5))
print(my_tuple2)  # Print the tuple created using the tuple constructor

# tuple with range
my_tuple3 = tuple(range(1, 11))
print(my_tuple3)  # Print the tuple created using range

# Slicing in tuples
print(my_tuple3[0:3])  # Print the first three numbers
print(my_tuple3[6:9])  # Print the following three numbers
print(my_tuple3[::-1])  # Print the last number

# Tuple methods
my_tuple4 = (1, 5, 3, 8, 6, 2, 4, 7)
print(my_tuple4)  # Print the tuple

# count method
count_of_5 = my_tuple4.count(5)  # Count the occurrences of 5 in the tuple
print(count_of_5)  # Print the count of 5 in the tuple

# index method
index_of_8 = my_tuple4.index(8)  # Find the index of 8 in the tuple
print(index_of_8)  # Print the index of 8 in the tuple

# tuple unpacking
names = ("rahul", "sneha", "priya")
name1, name2, name3 = names  # Unpack the tuple into variables
for name in names:
    print(name)  # Print each name in the tuple