"""
Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they
are actually the same object, with the same memory location:

Operator	Description	                                            Example
is 	        Returns True if both variables are the same object	    x is y
is not	    Returns True if both variables are not the same object	x is not y

"""

a = 20
b = 20

print('id(a) :', id(a))
print('id(b) :', id(b))

if (a is b):      # Returns True if both variables are the same object
    print(str(a) + " and "+str(b) + " have the same identity" )
else:
    print(str(a) + " and "+str(b) + " do not have the same identity")

if(id(a) == id(b)):     # Returns the id of an object
    print(str(a) + " and " + str(b) + " have the same identity")
else:
    print(str(a) + " and "+str(b) + " do not have the same identity")

c = 40
d = c - b
print("ID of the object a is : ", id(a))
print("ID of the object b is : ", id(b))
print("ID of the object d is : ", id(d))

b = 30
if (a is not b):
    print(str(a) + " and " + str(b) + " do not have have the same identity")
else:
    print(str(a) + " and "+str(b) + " have the same identity")

print("ID of the object b is : ", id(b))
