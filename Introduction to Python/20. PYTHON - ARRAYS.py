"""
Python Arrays

Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

Arrays
Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python
you will have to import a library, like the NumPy library.

Arrays are used to store multiple values in one single variable:
An array can hold many values under a single name, and you can access the values by referring to an index number.
"""

cars = ["Ford", "Volvo", "BMW"]
print(cars)

"""
An array can hold many values under a single name, and you can access the values by referring to an index number.

Access the Elements of an Array
You refer to an array element by referring to the index number.
"""
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

"""
Modify the value of the first array item:
"""
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)

"""
The Length of an Array
Use the len() method to return the length of an array (the number of elements in an array).

Note: The length of an array is always one more than the highest array index.
"""
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

"""
Looping Array Elements
You can use the for in loop to loop through all the elements of an array.
"""
cars = ["Ford", "Volvo", "BMW"]

for x in cars:
    print(x)

"""
Adding Array Elements
You can use the append() method to add an element to an array.
"""
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

"""
Removing Array Elements
You can use the pop() method to remove an element from the array.
"""
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)

"""
You can also use the remove() method to remove an element from the array.

Note: The list's remove() method only removes the first occurrence of the specified value.
"""
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)
