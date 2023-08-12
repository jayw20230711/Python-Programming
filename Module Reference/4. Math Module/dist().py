"""
Python math.dist() Method

Definition and Usage
The math.dist() method returns the Euclidean distance between two points (p and q), where p and q are the coordinates
of that point.

Note: The two points (p and q) must be of the same dimensions.

Syntax
math.dist(p, q)

Parameter	    Description
p	            Required. Specifies point 1
q	            Required. Specifies point 2

Technical Details
Return Value:	    A float value, representing the Euclidean distance between p and q
Python Version:	    3.8

"""
import math

p = [3]
q = [1]

# Calculate Euclidean distance
print(math.dist(p, q))

p = [3, 3]
q = [6, 12]

# Calculate Euclidean distance
print(math.dist(p, q))

