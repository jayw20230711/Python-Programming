"""
Filtering Arrays
Getting some elements out of an existing array and creating a new array out of them is called filtering.

In NumPy, you filter an array using a boolean index list.

A boolean index list is a list of booleans corresponding to indexes in the array.

If the value at an index is True that element is contained in the filtered array, if the value at that index
is False that element is excluded from the filtered array.

"""
import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]
newarr = arr[x]
print(newarr)           # [41 43]

"""
Creating the Filter Array
In the example above we hard-coded the True and False values, but the common use is to create a 
filter array based on conditions.
"""
# Create a filter array that will return only values higher than 42:
arr2 = np.array([41, 42, 43, 44])

# # Create an empty list
filter_arr = []

# go through each element in
for element in arr2:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr2 = arr2[filter_arr]

print(arr2, 'Print values greater than 42')
print('Index :', filter_arr)
print(newarr2)

"""
Create a filter array that will return only even elements from the original array:
"""
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

fil_arr = []
for element in arr3:
    if element % 2  == 0:
        fil_arr.append(True)
    else:
        fil_arr.append(False)
newarr3 = arr3[fil_arr]

print('Array :', arr3)
print('Index for even numbers : ', fil_arr)
print(newarr3)

"""
Creating Filter Directly From Array
The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.

We can directly substitute the array instead of the iterable variable in our condition and it will work 
just as we expect it to.
"""
fl_arr = arr > 42
newarr4 = arr[fl_arr]

print(newarr4)
