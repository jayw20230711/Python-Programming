"""
Python math.erf() Method

Definition and Usage
The math.erf() method returns the error function of a number.

This method accepts a value between - inf and + inf, and returns a value between - 1 to + 1.

Syntax
math.erf(x)

Parameter	    Description
x	            Required. A number to find the error function of

Technical Details
Return Value:	    A float value, representing the error function of a number
Python Version:	    3.2

"""
import math

# Print error function for different numbers
print(math.erf(0.67))
print(math.erf(1.34))
print(math.erf(-6))


# Print the error function of the same number, positive and negative
print(math.erf(1.28))
print(math.erf(-1.28))
