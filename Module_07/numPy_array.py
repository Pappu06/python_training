import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60]
])

print("Array: ")
print(arr)

# important NumPy array arttributes
print("important NumPy array arttributes")

print("Dimension:", arr.ndim) # shows dimension of array 
print("Size:", arr.size) # shows size of array
print("Shape:", arr.shape) # shows shape of array 
print("Data type:", arr.dtype) # shows data type of array


# Mathamatical operation in numpy array 
print(" ")
print("Mathamatical operation in numpy array")

print("add 5")
print(arr + 5)
print("sub 5")
print(arr - 5)
print("multi 5")
print(arr * 5)
print("divide 5")
print(arr / 5)
print("expo 5")
print(arr ** 5)
print("modulus 5")
print(arr % 5)


# Operation between two arrays 
print("Operation between two arrays ")

a = np.array([10,20,30,40,50])
b = np.array([70,60,90,30,80])

print(a+b)
print(a-b)
print(a*b)
print(a/b)


# creating arrays in numpy 

#np.zeros()
arr1 = np.zeros(5)
print(arr1)

#np.zeros() 2D
arr2 = np.zeros((2,3))
print(arr2)

# np.ones()
arr3 = np.ones(5)
print(arr3)

# np.arange(start, stop, step)

arr4 = np.arange(1, 11, 2)
print(arr4)

arr5 = np.arange(10)
print(arr5)

arr6 = np.arange(1, 11)
print(arr6)


# np.linspace() Creates a specified number of evenly spaced values between two endpoints.

arr7 = np.linspace(0,10,5)
print(arr7)

# np.eye() Creates a identity matrix

arr8 = np.eye(3)
print(arr8)

# np.reshape()
arr9 = np.arange(9)
print(arr9)

print(arr9.reshape(3,3))
print(arr9.reshape(3,-1))


#  Aggregation Functions

marks = np.array([70,80,90,60,100])

print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard deviation:", np.std(marks))