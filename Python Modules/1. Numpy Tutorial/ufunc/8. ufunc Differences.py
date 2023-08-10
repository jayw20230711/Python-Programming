"""
NumPy Differences

Differences
A discrete difference means subtracting two successive elements.
E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]

To find the discrete difference, use the diff() function.

"""
import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print('\nCompute discrete difference of the elements in [10, 15, 25, 5] :')
print(newarr)   # [  5  10 -20]  because 15-10=5, 25-15=10, and 5-25=-20

"""
We can perform this operation repeatedly by giving parameter n.

E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then, since n=2, 
we will do it once more, with the new result: [1-1, 1-1] = [0, 0]
"""
arr2 = np.array([10, 15, 25, 5])

newarr2 = np.diff(arr, n=2)

print('\nCompute discrete difference of the following array twice :')
print(newarr2)  # : 15-10=5, 25-15=10, and 5-25=-20 AND 10-5=5 and -20-10=-30
