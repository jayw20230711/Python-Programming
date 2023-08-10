"""
Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	                                                Example
and 	    Returns True if both statements are true	                x < 5 and  x < 10
or	        Returns True if one of the statements is true	            x < 5 or x < 4
not	        Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

"""

a = 10
b = 20
c = 0

print('a and b : ', a and b)
print('a or b : ', a or b)
print('not(a and b ): ', not(a and b))
print("\n")

# with bool() function
print("a =", a)
print("b =", b)
print("a and b -> ", bool(a and b))
print("not (a and b) ->", bool(not(a and b)))
print("a or b ->", bool(a or b))

print("\n")
if (a and b):        # AND Returns True if both statements are true
    print("a and b are true")
else:
    print("either a not true or b is not true")

if (a or b):            # OR Returns True if one of the statements is true
    print("either a is true or b is true or both are true")
else:
    print("neither a is true nor b is true")

a = 0
print("\na =", a)
print("b =", b)
print("a and b  ->",bool(a and b))
print("a or b ->",bool(a or b))
print("not (a and b) ->", bool(not(a and b)))
print("\n")

if (a and b):        # AND Returns True if both statements are true
    print("a and b are true")
else:
    print("either a not true or b is not true or both not true")

if (a or b):            # OR Returns True if one of the statements is true
    print("either a is true or b is true or both are true")
else:
    print("neither a is true nor b is true")

print("\ncheck NOT condition")
if not(a and b):  #Reverse the result, returns False if the result is true
    print(bool(not(a and b)))
else:
    print(bool(a and b))

