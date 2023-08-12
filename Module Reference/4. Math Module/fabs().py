"""
Python math.fabs() Method

Definition and Usage
The math.fabs() method returns the absolute value of a number, as a float.

Absolute denotes a non-negative number. This removes the negative sign of the value if it has any.

Unlike Python abs(), this method always converts the value to a float value.

Syntax
math.fabs(x)

Parameter	    Description
x	            Required. A number. If we try anything else except a number, it returns a TypeError

Technical Details
Return Value:	        A float value, representing the absolute value of x
Python Version:	        2.6

"""
import math

# Print absolute values from numbers
print(math.fabs(-66.43))
print(math.fabs(-7))
