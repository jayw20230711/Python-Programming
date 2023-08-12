"""
Python math.ceil() Method

Definition and Usage
The math.ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result.

Tip: To round a number DOWN to the nearest integer, look at the math.floor() method.

Syntax
math.ceil(x)

Parameter	    Description
x	            Required. Specifies the number to round up

Technical Details
Return Value:	    An int value, representing the rounded number.
Change Log:	        Python 3+ : Returns an int value
                    Python 2.x :        Returns a float value.

"""
import math

print(math.ceil(1.4))
print(math.ceil(5.3))
print(math.ceil(-5.3))
print(math.ceil(22.6))
print(math.ceil(10.0))
