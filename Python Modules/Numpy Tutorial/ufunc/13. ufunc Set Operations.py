"""
NumPy Set Operations

What is a Set
A set in mathematics is a collection of unique elements.

Sets are used for operations involving frequent intersection, union and difference operations.

Create Sets in NumPy
We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember
that the set arrays should only be 1-D arrays.
"""
import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print('\nConvert following array with repeated elements [1, 1, 1, 2, 3, 4, 5, 5, 6, 7] to a set  :')
print(x)    # [1 2 3 4 5 6 7]

"""
Finding Union

To find the unique values of two arrays, use the union1d() method.
"""
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print('\nFind union of the following two set arrays [1, 2, 3, 4] and [3, 4, 5, 6]  :')
print(newarr)


"""
Finding Intersection

To find only the values that are present in both arrays, use the intersect1d() method.
"""
arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([3, 4, 5, 6])

newarr1 = np.intersect1d(arr3, arr4, assume_unique=True)

print('\nFind intersection of the following two set arrays [1, 2, 3, 4] and [3, 4, 5, 6] :')
print(newarr1)

"""
Note: the intersect1d() method takes an optional argument assume_unique, which if set to True can speed up computation.
It should always be set to True when dealing with sets.
"""

"""
Finding Difference

To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.

"""
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr2 = np.setdiff1d(set1, set2, assume_unique=True)

print('\nTo find only the values in the [1, 2, 3, 4] that is NOT present in the [3, 4, 5, 6] :')
print(newarr2)

"""
Note: the setdiff1d() method takes an optional argument assume_unique, which if set to True can speed up computation. 
It should always be set to True when dealing with sets.
"""

"""
Finding Symmetric Difference

To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
"""
set3 = np.array([1, 2, 3, 4])
set4 = np.array([3, 4, 5, 6])

newarr2 = np.setxor1d(set3, set4, assume_unique=True)

print('\nTo find only the values that are NOT present in BOTH sets [1, 2, 3, 4] and [3, 4, 5, 6] :')
print(newarr2)

"""
Note: the setxor1d() method takes an optional argument assume_unique, which if set to True can speed up computation. 
It should always be set to True when dealing with sets.
"""