"""
Python math.atanh() Method

Definition and Usage
The math.atanh() method returns the inverse hyperbolic tangent of a number.

Note: The parameter passed in math.atanh() must lie between -0.99 to 0.99.

Syntax
math.atanh(x)

Parameter	    Description
x	            Required. A positive or negative number between -0.99 and 0.99. If x is not a number, it returns
                a TypeError


Technical Details
Return Value:	    A float value, representing the inverse hyperbolic tangent of a number
Python Version:	    2.6

"""
import math

# print the hyperbolic arctangent of different numbers
print(math.atanh(0.59))
print(math.atanh(-0.12))
