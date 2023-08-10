"""
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

"""
class MyClass:
    x = 5
print(MyClass)

"""
Create Object
Now we can use the class named MyClass to create objects:
"""
p1 = MyClass()
print(p1.x)

"""
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary 
to do when the object is being created:

Note: The __init__() function is called automatically every time the class is being used to create a new object.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p2 = Person("John", 37)
print(p2.name)
print(p2.age)

"""
Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p3 = Person("John", 36)
p3.myfunc()

"""
The self parameter is a reference to the current instance of the class, and is used to access
variables that belongs to the class. It does not have to be named self , you can call it whatever you like,
but it has to be the first parameter of any function in the class:
"""
class Party:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def secfunc(abc):
        print("Hello my name is " + abc.name + " and my age is " + str(abc.age))


p4 = Party("John", 36)
p4.secfunc()

"""
Modify Object Properties
You can modify properties on objects like this:
"""

p4.age = 53
p4.secfunc()

"""
Delete Object Properties
You can delete properties on objects by using the del keyword:
"""
del p4.age
try:
    # p4.secfunc()  # both methods work
    print(p4.age)
except AttributeError as error:
    print(error)

"""
Delete Objects
You can delete objects by using the del keyword:
"""
del p4
try:
    print(p4)
except NameError as error:
    print(error)

"""
The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, 
put in the pass statement to avoid getting an error.
"""
class NewClass:
    pass
