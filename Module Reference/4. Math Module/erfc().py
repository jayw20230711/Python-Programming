"""
Python math.erfc() Method

Definition and Usage
The math.erfc() method returns the complementary error function of a number.

This method accepts a value between - inf and + inf, and returns a value between 0 and 2.

Syntax
math.erfc(x)

Parameter	    Description
x	            Required. A number to find the complementary error function of

Technical Details
Return Value:	        A float value, representing the complementary error function of a number
Python Version:	        3.2

"""
import math

# Print complementary error function for different numbers
print(math.erfc(0.67))
print(math.erfc(1.34))
print(math.erfc(-6))
