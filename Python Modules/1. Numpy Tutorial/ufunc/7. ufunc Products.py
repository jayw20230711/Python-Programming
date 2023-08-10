"""
NumPy Products

To find the product of the elements in an array, use the prod() function.

"""
import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print('Find product of the elements in [1, 2, 3, 4]')
print(x)    # 1*2*3*4 = 24

"""
Find the product of the elements of two arrays:
"""
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

y = np.prod([arr1, arr2])

print('\nProduct of the elements of two arrays :')
print(y)    # 1*2*3*4*5*6*7*8 = 40320

"""
Product Over an Axis

If you specify axis=1, NumPy will return the product of each array.
"""
arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([5, 6, 7, 8])

newarr = np.prod([arr3, arr4], axis=1)

print('\nPerform product over 1st Axis :')
print(newarr)   # [  24 1680]


"""
Cumulative Product

Cumulative product means taking the product partially.
E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

Perform partial sum with the cumprod() function.
"""
arr5 = np.array([5, 6, 7, 8])

newarr1 = np.cumprod(arr5)

print('\n')
print(newarr1)     # [   5   30  210 1680]
