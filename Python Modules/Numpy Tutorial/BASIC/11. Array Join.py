"""
Joining NumPy Arrays
Joining means putting contents of two or more arrays in a single array.

In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis.
If axis is not explicitly passed, it is taken as 0.

"""
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
# arrn = np.concatenate((arr2, arr1))

print('Join two 1-D arrays using Concatenate() function on Axi= 0 :')
print(arr)
# print(arrn)

# arr = np.concatenate((arr1, arr2), axis=1)  # numpy.AxisError: axis 1 is out of bounds for array of dimension 1
# print(arr)

"""
Join two 2-D arrays along rows (axis=1):
"""
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print('\nJoin two 2-D arrays using Concatenate() function along rows (axis=0) :')
arr3 = np.concatenate((arr1, arr2))
print(arr3)

print('\nJoin two 2-D arrays using Concatenate() function along rows (axis=1)  :')
arr4 = np.concatenate((arr1, arr2), axis=1)
print(arr4)

"""
Joining Arrays Using Stack Functions
Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

We can concatenate two 1-D arrays along the second axis which would result in putting them one over 
the other, ie. stacking.

We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is 
not explicitly passed it is taken as 0.
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print('\nConcatenate using stack() function along new axis=0 :')
arr5 = np.stack((arr1, arr2), axis=0)
print(arr5)

print('\nConcatenate using stack() function along new axis=1 :')
arr6 = np.stack((arr1, arr2), axis=1)
print(arr6)

"""
Stacking Along Rows
NumPy provides a helper function: hstack() to stack along rows.
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr7 = np.hstack((arr1, arr2))
print('\nStack along rows using hstack() function : ')
print(arr7)

"""
Stacking Along Columns
NumPy provides a helper function: vstack()  to stack along columns.
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr8 = np.vstack((arr1, arr2))
print('\nStack along columns using vstack() function :')
print(arr8)

"""
Stacking Along Height (depth)
NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print('Stack along the depth/height using dstack() function : ')
arr9 = np.dstack((arr1, arr2))
print(arr9)
