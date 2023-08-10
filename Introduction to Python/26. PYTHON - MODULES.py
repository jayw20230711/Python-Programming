"""
Python Modules

Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

Create a Module
To create a module just save the code you want in a file with the file extension .py

Save this code in a file named MYMODULE.py

def greeting(name):
  print("Hello, " + name)

To use a module use the import statement.

Note: When using a function from a module, use the syntax: module_name.function_name.

You can create an alias when you import a module, by using the as keyword:

import MYMODULE as mx
a = mx.person1["age"]
print(a)

"""

import platform
import MYMODULE

from MYMODULE import person1        # Import From Module

MYMODULE.greeting("Subash")

"""
Variables in Module
The module can contain functions, as already described, but also variables of all 
types (arrays, dictionaries, objects etc):
"""
a = MYMODULE.person1["age"]
print(a)

print(MYMODULE.person1)

"""
Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.
"""
x = platform.system()
print(x)

"""
Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

Note: The dir() function can be used on all modules, also the ones you create yourself.
"""

y = dir(platform)
print(y)

z = dir(MYMODULE)
print(z)

"""
Import From Module
You can choose to import only parts from a module, by using the from keyword.

from MYMODULE import person1

Note: When importing using the from keyword, do not use the module name when referring to elements 
in the module. Example: person1["age"], not mymodule.person1["age"]
"""
print(person1["age"])
