"""
Python math.isclose() Method

Definition and Usage
The math.isclose() method checks whether two values are close to each other, or not. Returns True if the values are
close, otherwise False.

This method uses a relative or absolute tolerance, to see if the values are close.

Tip: It uses the following formula to compare the values: abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

Syntax
math.isclose(a, b, rel_tol, abs_tol)

Parameter	        Description
a	                Required. The first value to check for closeness
b	                Required. The second value to check for closeness
rel_tol = value	    Optional. The relative tolerance. It is the maximum allowed difference between value a and b.
                    Default value is 1e-09
abs_tol = value	    Optional. The minimum absolute tolerance. It is used to compare values near 0. The value must
                    be at least 0

Technical           Details
Return Value:	    A bool value. True if the values are close, otherwise False
Python Version:	    3.5

"""
import math

# compare the closeness of two values
print(math.isclose(1.233, 1.4566))
print(math.isclose(1.233, 1.233))
print(math.isclose(1.233, 1.24))
print(math.isclose(1.233, 1.233000001))


# Use absolute tolerance:
# compare the closeness of two values
print('\n')
print(math.isclose(8.005, 8.450, abs_tol=0.4))
print(math.isclose(8.005, 8.450, abs_tol=0.5))
