"""
Python math.gcd() Method

Definition and Usage
The math.gcd() method returns the greatest common divisor of the two integers int1 and int2.

GCD is the largest common divisor that divides the numbers without a remainder.

GCD is also known as the highest common factor (HCF).

Tip: gcd(0,0) returns 0.

Syntax
math.gcd(int1, int2)

Parameter	    Description
int1	        Required. The first integer to find the GCD for
int2	        Required. The second integer to find the GCD for

Technical           Details
Return Value:	    An int value, representing the greatest common divisor (GCD) for two integers
Python Version:	    3.5

"""
import math

# find the  the greatest common divisor of the two integers
print(math.gcd(3, 6))
print(math.gcd(6, 12))
print(math.gcd(12, 36))
print(math.gcd(-12, -36))
print(math.gcd(5, 12))
print(math.gcd(10, 0))
print(math.gcd(0, 34))
print(math.gcd(0, 0))

