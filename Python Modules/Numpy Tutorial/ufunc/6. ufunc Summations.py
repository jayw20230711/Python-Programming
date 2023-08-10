"""
NumPy Summations

Summations
What is the difference between summation and addition?

Addition is done between two arguments whereas summation happens over n elements.

"""
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr1 = np.add(arr1, arr2)

print('Add values in [1, 2, 3] and [1, 2, 3] :')
print(newarr1)       # [2 4 6]

"""
Sum the values in arr1 and the values
"""
arr3 = np.array([1, 2, 3])
arr4 = np.array([1, 2, 3])

newarr2 = np.sum([arr1, arr2])

print('\nSum the values in [1, 2, 3] and [1, 2, 3]')
print(newarr2)    # 12

"""
Summation Over an Axis

If you specify axis=1, NumPy will sum the numbers in each array.
"""
arr5 = np.array([1, 2, 3])
arr6 = np.array([1, 2, 3])

newarr3 = np.sum([arr5, arr6], axis=1)

print('\nSum values in arrays over 1st axis :')
print(newarr3)  # [6 6]

"""
Cumulative Sum

Cumulative sum means partially adding the elements in array.

E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

Perform partial sum with the cumsum() function.
"""
arr7 = np.array([1, 2, 3])

newarr4 = np.cumsum(arr7)

print('\nPerform partial sum with the cumsum() function :')
print(newarr4)      # [1 3 6]
