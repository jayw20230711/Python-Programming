"""
Python math.radians() Method

Definition and Usage
The math.radians() method converts a degree value into radians.

Tip: See also math.degrees() to convert an angle from radians to degrees.

Syntax
math.radians(x)

Parameter	    Description
x	            Required. The degree value to be converted into radians. If the parameter is not a number, it
                returns a TypeError

Technical           Details
Return Value:	    A float value, representing the radian value of an angle
Python Version:	    2.0

"""
import math

# Convert different degrees into radians
print(math.radians(180))
print(math.radians(100.03))
print(math.radians(-20))
