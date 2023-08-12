"""
Python math.prod() Method

Definition and Usage
The math.prod() method returns the product of the elements from the given iterable.

Syntax
math.prod(iterable, start)

Parameter	    Description
iterable	    Required. Specifies the elements of the iterable whose product is computed by the function
start	        Optional. Specifies the starting value of the product. Default value is 1

"""
import math

sequence = (2, 2, 2)

# Return the product of the elements
print(math.prod(sequence))
