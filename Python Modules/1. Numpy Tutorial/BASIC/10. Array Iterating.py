"""
Array Iterating

Iterating means going through elements one by one.

As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

If we iterate on a 1-D array it will go through each element one by one.

"""
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

"""
Iterating 2-D Arrays
In a 2-D array it will go through all the rows.
"""
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr2:
    print(x)
# If we iterate on a n-D array it will go through n-1th dimension one by one.

"""
To return the actual values, the scalars, we have to iterate the arrays in each dimension.
"""

for x in arr2:
    for y in x:
        print(y)

"""
Iterating 3-D Arrays
In a 3-D array it will go through all the 2-D arrays.
"""
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr3:
    print(x)

"""
To return the actual values, the scalars, we have to iterate the arrays in each dimension.
"""
for x in arr3:
    for y in x:
        for z in y:
            print(z)

"""
Iterating Arrays Using nditer()
The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
It solves some basic issues which we face in iteration, lets go through it with examples.

Iterating on Each Scalar Element
In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult 
to write for arrays with very high dimensionality.
"""
narr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print('Using the nditer() module: ')
for x in np.nditer(narr):
    print(x)

"""
Iterating Array With Different Data Types
We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array) so it needs some 
other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we 
pass flags=['buffered'].
"""
# Iterate through the array as a string:

arr4 = np.array([1, 2, 3])

print("Iterate through the array as a string")
for x in np.nditer(arr4, flags=['buffered'], op_dtypes='S'):
    print(x)

"""
Iterating With Different Step Size
We can use filtering and followed by iteration.
"""
print("Iterate through every scalar element of the 2D array skipping 1 element: ")

arr5 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr5[:, ::2]):
    print(x)

"""
Enumerated Iteration Using ndenumerate()
Enumeration means mentioning sequence number of somethings one by one.

Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can 
be used for those usecases.

"""
# Enumerate on following 1D arrays elements:
arrd1 = np.array([1, 2, 3])

print('print index alongside the values for 1D array:')
for idx, x in np.ndenumerate(arrd1):
    print(idx, x)

# Enumerate on following 2D array's elements:
arrd2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print('print index alongside the values for 2D array:')
for idx, x in np.ndenumerate(arrd2):
    print(idx, x)
