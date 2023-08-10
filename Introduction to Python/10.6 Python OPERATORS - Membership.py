"""
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	                                                                        Example
in 	        Returns True if a sequence with the specified value is present in the object	    x in y
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y

"""

a = 3
b = 20

numbers = [1, 2, 3, 4, 5]

if a in numbers:
    print(str(a) + " is available in the list: ", numbers)
else:
    print(str(a) + " is not available in the list : ", numbers)

if b not in numbers:
    print(str(b) + " is not in the list: ", numbers)
else:
    print(str(b) + " is in the list : ", numbers)
