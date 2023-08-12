"""
Python math.atan() Method

Definition and Usage
The math.atan() method returns the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians.

Arc tangent is also defined as an inverse tangent function of x, where x is the value of the arc tangent is to be
calculated.

Syntax
math.atan(x)

Parameter	    Description
x	            Required. A positive or negative number. If x is not a number, it returns error a TypeError

Technical Details
Return Value:	    A float value, from -PI/2 to PI/2, representing the arc tangent of a number
Python Version:	    1.6.1

"""
import math

# Return the arc tangent of different numbers
print(math.atan(0.39))
print(math.atan(67))
print(math.atan(-21))
