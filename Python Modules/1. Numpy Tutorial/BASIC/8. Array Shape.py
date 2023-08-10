"""
Shape of an Array
The shape of an array is the number of elements in each dimension.

Get the Shape of an Array
NumPy arrays have an attribute called shape that returns a tuple with each index having the number
of corresponding elements.
"""

import numpy as np

# 0-D Arrays
arrd0 = np.array(42)
print(arrd0)                # 42
print(arrd0.shape)          # ()
print(arrd0.ndim)           # 0
print(type(arrd0))          # <class 'numpy.ndarray'>

# Print the shape of a 1-D array:
arrd1 = np.array([1, 2, 3, 4])
print(arrd1)
print(arrd1.shape)          # (4,)

# Print the shape of a 2-D array:
arrd2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arrd2.shape)        # (2, 4)
print('arrd2 @ [0, 1, 1, 0]  = ', arrd2 @ [0, 1, 1, 0])         # [ 5 13]
"""
Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that 
last dimension has value 4:
"""

arr2 = np.array([1, 2, 3, 4], ndmin=5)

print(arr2)                                 # [[[[[1 2 3 4]]]]]
print('Shape of array :', arr2.shape)       # Shape of array : (1, 1, 1, 1, 4)

print(arr2[0])                      # [[[[1 2 3 4]]]]
print(arr2[0, 0])                   # [[[1 2 3 4]]]
print(arr2[0, 0, 0])                # [[1 2 3 4]]
print(arr2[0, 0, 0, 0])             # [1 2 3 4]
print(arr2[0, 0, 0, 0, 0])          # 1
print(arr2[0, 0, 0, 0, 0:])         # [1 2 3 4]

"""
What does the shape tuple represent?
Integers at every index tells about the number of elements the corresponding dimension has.

In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.
"""
