"""
Simple Arithmetic

You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of
the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic
conditionally.

Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.

All of the discussed arithmetic functions take a where parameter in which we can specify that condition.
"""
import numpy as np

"""
Addition
The add() function sums the content of two arrays, and return the results in a new array
"""

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr1 = np.add(arr1, arr2)

# The example above will return [30 32 34 36 38 40] which is the sums of 10+20, 11+21, 12+22 etc.
#
print("Add the arrays : [10, 11, 12, 13, 14, 15],[20, 21, 22, 23, 24, 25] ")
print(newarr1)  # [30 32 34 36 38 40]

"""
Subtraction
The subtract() function subtracts the values from one array with the values from another array, and return the 
results in a new array.
"""
arr3 = np.array([10, 20, 30, 40, 50, 60])
arr4 = np.array([20, 21, 22, 23, 24, 25])

newarr2 = np.subtract(arr3,arr4)
print("\nSubtract the arrays : [10, 11, 12, 13, 14, 15],[20, 21, 22, 23, 24, 25] ")
print(newarr2)    # [-10  -1   8  17  26  35]

"""
Multiplication
The multiply() function multiplies the values from one array with the values from another array, and return the 
results in a new array.
"""
arr5 = np.array([10, 20, 30, 40, 50, 60])
arr6 = np.array([20, 21, 22, 23, 24, 25])

newarr3 = np.multiply(arr5, arr6)

print('\nMultiply arrays : [10, 11, 12, 13, 14, 15],[20, 21, 22, 23, 24, 25] ')
print(newarr3)  # [ 200  420  660  920 1200 1500]

"""
Division
The divide() function divides the values from one array with the values from another array, and return the 
results in a new array.
"""
arr7 = np.array([10, 20, 30, 40, 50, 60])
arr8 = np.array([3, 5, 10, 8, 2, 33])

newarr4 = np.divide(arr7, arr8)

print('\nDivide the values in [10, 20, 30, 40, 50, 60] with the values in [3, 5, 10, 8, 2, 33]:')
print(newarr4)  # [ 3.33333333  4.          3.          5.         25.          1.81818182]

"""
Power
The power() function rises the values from the first array to the power of the values of the second array, and return 
the results in a new array.
"""

arr9 = np.array([10, 20, 30, 40, 50, 60])
arr10 = np.array([3, 5, 6, 8, 2, 33])

newarr5 = np.power(arr9, arr10)

print('\nRaise the values in [10, 20, 30, 40, 50, 60] to the power of values in [3, 5, 6, 8, 2, 33]:')
print(newarr5)   # [         1000       3200000     729000000 6553600000000          2500             0]

"""
Remainder
Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to 
the values in the second array, and return the results in a new array.
"""

arr11 = np.array([10, 20, 30, 40, 50, 60])
arr12 = np.array([3, 7, 9, 8, 2, 33])

newarr6 = np.mod(arr11, arr12)

print('\nReturn the remainders of values [10, 20, 30, 40, 50, 60] corresponding to [3, 7, 9, 8, 2, 33]):')
print(newarr6)  # [ 1  6  3  0  0 27]

"""
You get the same result when using the remainder() function:
"""

arr13 = np.array([10, 20, 30, 40, 50, 60])
arr14 = np.array([3, 7, 9, 8, 2, 33])

newarr7 = np.remainder(arr13, arr14)

print('\nusing the remainder() function:')
print(newarr7)

"""
Quotient and Mod
The divmod() function return both the quotient and the the mod. The return value is two arrays, the first array 
contains the quotient and second array contains the mod.

"""

arr15 = np.array([10, 20, 30, 40, 50, 60])
arr16 = np.array([3, 7, 9, 8, 2, 33])

newarr8 = np.divmod(arr15, arr16)

print('\nReturn the quotient and mod:')
print(newarr8)   # (array([ 3,  2,  3,  5, 25,  1]), array([ 1,  6,  3,  0,  0, 27]))

"""
Absolute Values
Both the absolute() and the abs() functions do the same absolute operation element-wise but we should use absolute() 
to avoid confusion with python's inbuilt math.abs()
"""

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print('\nReturn the quotient and mod:')
print(newarr)   # [1 2 1 2 3 4]
