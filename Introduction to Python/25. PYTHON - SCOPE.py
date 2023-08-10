"""
Python Scope

A variable is only available from inside the region it is created. This is called scope.
"""


def myfunc():
    x = 300
    print(x)


myfunc()

"""
Function Inside Function
As explained in the example above, the variable x is not available outside the function, but it is available for 
any function inside the function:
"""


def myfunc2():
    x = 400

    def myinnerfunc():
        print(x)

    myinnerfunc()

myfunc2()

"""
Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.
"""

x= 500

def myfunc3():
    print(x)

myfunc3()
print(x)

"""
Naming Variables
If you operate with the same variable name inside and outside of a function, Python will treat them as 
two separate variables, one available in the global scope (outside the function) and one available in the 
local scope (inside the function):

"""

x = 200

def myfunc4():
    x = 300
    print(x)
myfunc4()
print(x)


"""
Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.
"""

def myfunc5():
    global y
    y = 600

myfunc5()
print(y)

"""
Also, use the global keyword if you want to make a change to a global variable inside a function.
"""
x = 700

def myfunc6():
    global x
    x = 250

myfunc6()
print(x)
