"""
Python Comparison Operators
Comparison operators are used to compare two values:

Operator	Name	                    Example
==	        Equal	                    x == y
!=	        Not equal	                x != y
>	        Greater than	            x > y
<	        Less than	                x < y
>=	        Greater than or equal to	x >= y
<=	        Less than or equal to	    x <= y

"""

a = 21
b = 10
c = 0

if (a == b):
    print("a is eqal to b")
else:
    print("a is not equal to b")

if ( a != b):
    print("a is not equal to b")
else:
    print("a is equal to b")

if ( a < b ):
    print("a is less than b")
else:
    print("a is greater than b")

if (a > b):
    print("a is greater than b")
else:
    print("a is less than b")

if (a >= b):
    print("a is greater than or equal to b")
else:
    print("a is less than or equal to b")

if ( a <= b):
    print("a is less than or equal to b")
else:
    print(str(a) + " is greater than or equal to " + str(b))
