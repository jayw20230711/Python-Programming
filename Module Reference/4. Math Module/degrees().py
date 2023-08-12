"""
Python math.degrees() Method

Definition and Usage
The mmath.degrees() method converts an angle from radians to degrees.

Tip: PI (3.14..) radians are equal to 180 degrees, which means that 1 radian is equal to 57.2957795 degrees.

Tip: See also math.radians() to convert a degree value into radians.

Syntax
math.degrees(x)

Parameter	Description
x	        Required. A radian value to convert into degrees. If the parameter is not a number, it returns a TypeError

Technical Details
Return Value:	    A float value, representing the value in degrees
Python Version:	    2.3

"""
import math

# Convert from radians to degrees:
print(math.degrees(8.90))
print(math.degrees(-20))
print(math.degrees(1))
print(math.degrees(90))
