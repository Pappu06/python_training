# Lists in python

students = ["rahul", "sachin", "rohit", "virat", "dhoni"]
print(students)  # Print the list of students

my_list = [1, 2, 3, 4, 5]
print(my_list)  # Print the list of numbers

# list constructor
my_list2 = list((1, 2, 3, 4, 5))
print(my_list2)  # Print the list created using the list constructor

# list with range
my_list3 = list(range(1, 11))   
print(my_list3)  # Print the list created using range

# Slicing in lists
print(my_list3[0:3])  # Print the first three numbers
print(my_list3[6:9])  # Print the following three numbers
print(my_list3[::-1])   # Print the last number

# List methods
my_list4 = [1, 5, 3, 8, 6, 2, 4, 7]
print(my_list4)  # Print the list

# Append method
my_list4.append(6) 
print(my_list4)  # Print the list after appending 6

# Insert method
my_list4.insert(0, 0)
print(my_list4)  # Print the list after inserting 0 at index 0

# extend method
my_list4.extend([10, 11, 12])
print(my_list4)  # Print the list after extending with [10, 11, 12]

# remove method
my_list4.remove(3)  
print(my_list4)  # Print the list after removing 3

# pop method
my_list4.pop()
print(my_list4)  # Print the list after popping the last element

# delete method
del my_list4[0]  # Delete the first element
print(my_list4)  # Print the list after deleting the first element

# sort method
my_list4.sort()
print(my_list4)  # Print the list after sorting

# sorted method
my_list5 = [5, 2, 9, 1, 5, 6]
sorted_list = sorted(my_list5) # Sort the list using the sorted() method
print(my_list5)  # Print the original list
print(sorted_list)  # Print the sorted list 

# reverse method
my_list4.reverse()
print(my_list4)  # Print the list after reversing

# count method
count_of_6 = my_list4.count(6)  # Count the occurrences of 6 in the list
print(count_of_6)  # Print the count of 6 in the list

# index method
index_of_6 = my_list4.index(6)  # Get the index of the first occurrence of 6 in the list
print(index_of_6)  # Print the index of 6 in the list



# Iterating through a list

# Using a for loop to iterate through the list of students
for student in students:
    print(student)  # Print each student in the list

# Using a while loop to iterate through the list of numbers
i = 0
while i < len(my_list):
    print(my_list[i])  # Print each number in the list
    i += 1  # Increment the index

# using index to iterate through the list of students
for i in range(len(students)):
    print(students[i])  # Print each student in the list using index


# using enumerate to iterate through the list of students
for index, student in enumerate(students):
    print(f"Index: {index}, Student: {student}")  # Print the index and student in the list 

