x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type,
# and can even change type after they have been set.
x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)

# CASTING
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

print('\n print data in type:')
print(x)  # 3
print(y)  # 3
print(z)  # 3.0

"""
Get the Type
You can get the data type of a variable with the type() function.
"""
print("\nnGet the type")
x = 5
y = "John"
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>

"""
Single or Double Quotes?
String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

"""

"""
Case-Sensitive
Variable names are case-sensitive.

This will create two variables:

"""
a = 4
A = "Sally"  # A will not overwrite a

print("\n case sensitive variables:")
print(a)  # 4
print(A)  # Sally

"""
VARIABLE NAMES

Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print("\n")
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

"""
ASSIGN MULTIPLE VALUES :

[1] Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""
x, y, z = "Orange", "Banana", 4  # "Cherry"
print('\n multiple values assign in single line: ')
print(x)
print(y)
print(z)

"""
[2] One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
"""
x = y = z = "Orange"
print('\n assign multiple variables single value')
print(x)
print(y)
print(z)

"""
UNPACK A COLLECTION:
If you have a collection of values in a list, tuple etc. Python allows you to 
extract the values into variables. This is called unpacking.
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print('\n unpacking a collection:')
print(x)
print(y)
print(z)

"""
OUTPUT VARIABLES:
The Python print() function is often used to output variables.
"""
x = "\nPython is awesome"
print(x)

"""
In the print() function, you output multiple variables, separated by a comma:
"""
x = "\nPython"
y = "is"
z = "awesome"
print(x, y, z)

"""
You can also use the + operator to output multiple variables:
"""
x = "\nPython "  # NOTICE THE SPACE
y = "is "  # NOTICE THE SPACE
z = "awesome"
print(x + y + z)

"""
For numbers, the + character works as a mathematical operator:
"""
x = 5
y = 10
print('\n add x + y :')
print(x + y)

""""
In the print() function, when you try to combine a string 
and a number with the + operator, Python will give you an error:
x = 5
y = "John"
print(x + y)

The best way to output multiple variables in the print() function 
is to separate them with commas, which even support different data types:
"""
x = 5
y = "John"
print('\n', x, y)

"""
GLOBAL VARIABLES:
Variables that are created outside of a function (as in all of the examples above) 
are known as global variables.
Global variables can be used by everywhere, both inside of functions and outside.
"""
x = "awesome"


def myfunc():
    print("\nPython is " + x)


myfunc()

""""
If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. The global variable with the same name will remain 
as it was, global and with the original value.
"""
x = "awesome"


def myfunc():
    x = "fantastic"
    print("\nPython is " + x)


myfunc()

print("\nPython is " + x)
