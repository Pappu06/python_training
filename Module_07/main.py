# installation of NumPy ~~ pip insatll numpy  or ~~ python -m pip install numpy

# Import numpy 
import numpy as np

#  print(np.__version__) # verify installation of numpy 

# array in mumpy 
numbers = np.array([10,20,30,40,50])

print(numbers)
print(type(numbers))

# 2D array in numpy
matrix = np.array([
    [1,2,3],
    [4,5,6,],
    [7,8,9]])

print(matrix)

#3D array in numpy
cube = np.array([
    [
        [1,2,],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print(cube)