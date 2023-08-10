"""
NumPy LCM Lowest Common Multiple

Finding LCM (Lowest Common Multiple)
The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.

"""
import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print('\nFind the LCM of the 4 and 6 :')
print(x)    # 12   : (4*3=12 and 6*2=12).


"""
Finding LCM in Arrays
To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.

The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by 
one dimension.
"""
arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print('\nFind the Lowest Common Multiple of [3, 6, 9]')
print(x)    # 18    : (3*6=18, 6*3=18 and 9*2=18)

"""
LCM of all values of an array where the array contains all integers from 1 to 10:
"""
arr2 = np.arange(1, 11)

x = np.lcm.reduce(arr2)

print('\nArray of values : ', arr2)
print('\nFind LCM of all values of an array where the array contains all integers from 1 to 10 :')
print(x)
