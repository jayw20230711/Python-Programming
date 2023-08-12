"""
Python math.comb() Method

Definition and Usage
The math.comb() method returns the number of ways picking k unordered outcomes from n possibilities, without
repetition, also known as combinations.

Note: The parameters passed in this method must be positive integers.

Syntax
math.comb(n, k)

Parameter	    Description
n	            Required. Positive integers of items to choose from
k	            Required. Positive integers of items to choose

Note: If the value of k is greater than the value of n it will return 0 as a result.

Note: If the parameters are negative, a ValueError occurs. If the parameters are not integers, a TypeError occurs.

Technical Details
Return Value:	        An int value, representing the total number of combinations
Python Version:	        3.8

"""
import math

# Initialize the number of items to choose from
n = 7

# Initialize the number of possibilities to choose
k = 5

# Print total number of possible combinations
print(math.comb(n, k))

# print(math.comb(4, 6))      # 0
