"""
NumPy Trigonometric Functions

Trigonometric Functions
NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos
and tan values.

"""
import numpy as np

x = np.sin(np.pi/2)

print('\nFind Sin() of pi/2 :')
print(x)

"""
Find sine values for all of the values in arr:
"""
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print('\nFind sine values for [np.pi/2, np.pi/3, np.pi/4, np.pi/5]  :')
print(x)    # [1.         0.8660254  0.70710678 0.58778525]

"""
Convert Degrees Into Radians

By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and 
vice versa as well in NumPy.

Note: radians values are pi/180 * degree_values.
"""
arr2 = np.array([90, 180, 270, 360])

y = np.deg2rad(arr2)

print('\nConvert all of the values [90, 180, 270, 360] to Radians :')
print(y)    # [1.57079633 3.14159265 4.71238898 6.28318531]

"""
Radians to Degrees
"""
arr3 = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x1 = np.rad2deg(arr3)

print('\nConvert all of the values in [np.pi/2, np.pi, 1.5*np.pi, 2*np.pi] to Degrees  :')
print(x1)   # [ 90. 180. 270. 360.]

"""
Finding Angles

Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).

NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan 
values given.
"""
x2 = np.arcsin(1.0)

print('\nFind the angle of 1.0  :')
print(x2)   # 1.5707963267948966

"""
Angles of Each Value in Arrays
"""
arr4 = np.array([1, -1, 0.1])

x3 = np.arcsin(arr4)

print('\nFind the angle for all of the sine values in [1, -1, 0.1]  :')
print(x3)   # [ 1.57079633 -1.57079633  0.10016742]


"""
Hypotenuse

Finding hypotenuse using pythagoras theorem in NumPy.

NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenuse based on 
pythagoras theorem.
"""
base = 3
perp = 4

x4 = np.hypot(base, perp)

print('\nFind the hypotenuse for 4 base and 3 perpendicular :')
print(x4)   # 5.0
