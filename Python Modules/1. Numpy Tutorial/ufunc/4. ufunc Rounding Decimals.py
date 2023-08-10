"""
Rounding Decimals

Rounding Decimals
There are primarily five ways of rounding off decimals in NumPy:

truncation
fix
rounding
floor
ceil

"""
import numpy as np

"""
Truncation
Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
"""
arr1 = np.trunc([-3.1666, 3.6667])

print('\nRemove the decimals with trunc() function :')
print(arr1)     # [-3.  3.]

"""
Same example, using fix():
"""
arr2 = np.fix([-3.1666, 3.6667])

print('\nRemove the decimals using fix() :')
print(arr2)     # [-3.  3.]

"""
Rounding
The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

E.g. round off to 1 decimal point, 3.16666 is 3.2
"""
arr3 = np.around(3.1666, 2)

print('\nRound off 3.1666 to 2 decimal places:')
print(arr3)     # 3.17

arr31 = np.around(3.1666)
print('\nRound off 3.1666 when decimal input omitted:')
print(arr31)

"""
Floor
The floor() function rounds off decimal to nearest lower integer.

E.g. floor of 3.166 is 3.
"""
arr4 = np.floor([-3.1666, 3.6667])

print('\nFloor the elements of array [-3.1666, 3.6667]:')
print(arr4)         # [-4.  3.]

"""
Ceil
The ceil() function rounds off decimal to nearest upper integer.

E.g. ceil of 3.166 is 4.
"""
arr5 = np.ceil([-3.1666, 3.6667])

print('\nCeil the elements [-3.1666, 3.6667]:')
print(arr5)         # [-3.  4.]
