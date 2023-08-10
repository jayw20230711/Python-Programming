"""
NumPy Hyperbolic Functions

NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh,
cosh and tanh values..
"""
import numpy as np

x = np.sinh(np.pi/2)

print('\nFind sinh() value of PI/2 :')
print(x)    # 2.3012989023072947

"""
Find cosh values for all of the values in arr:
"""
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x1 = np.cosh(arr)

print('\nFind cosh values for [np.pi/2, np.pi/3, np.pi/4, np.pi/5]  :')
print(x1)   # [2.50917848 1.60028686 1.32460909 1.20397209]

"""
Finding Angles

Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).

Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and 
tanh values given.
"""
x2 = np.arcsinh(1.0)

print('\nFind the angle of 1.0  :')
print(x2)    # 0.881373587019543

"""
Angles of Each Value in Arrays
"""
arr2 = np.array([0.1, 0.2, 0.5])

x3 = np.arctanh(arr2)

print('\nFind the angle for all of the tanh() values [0.1, 0.2, 0.5] :')
print(x3)   # [0.10033535 0.20273255 0.54930614]
