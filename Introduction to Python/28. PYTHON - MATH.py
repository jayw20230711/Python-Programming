"""
Python Math

Python has a set of built-in math functions, including an extensive math module, that allows you
to perform mathematical tasks on numbers.

Built-in Math Functions
The min() and max() functions can be used to find the lowest or highest value in an iterable:

"""
import math               # for examples given under the math module

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


"""
The abs() function returns the absolute (positive) value of the specified number:
"""
x = abs(-7.25)
print(x)

"""
The pow(x, y) function returns the value of x to the power of y (xy).
"""
x = pow(2, 8)
print(x)

"""
The 4. Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module:

import math

When you have imported the math module, you can start using methods and constants of the module.
"""
x = math.sqrt(64)
print(x)

"""
The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a 
number downwards to its nearest integer, and returns the result:
"""

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)
print(y)

"""
The math.pi constant, returns the value of PI (3.14...):
"""
x = math.pi

print(x)
