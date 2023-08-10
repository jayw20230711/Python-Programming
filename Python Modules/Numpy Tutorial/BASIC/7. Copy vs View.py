"""
NumPy Array Copy vs View

The Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array,
and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made
to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes
made to the original array will affect the view.

COPY:
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
arr[0] = 42

print(arr)          # [42  2  3  4  5]
print(x)            # [1 2 3 4 5]   :The copy SHOULD NOT be affected by the changes made to the original array.

"""
VIEW:
Make a view, change the original array, and display both arrays:
"""
arr2 = np.array([1, 2, 3, 4, 5])

x = arr2.view()
arr2[0] = 55

print(arr2)         # [55  2  3  4  5]
print(x)            # [55  2  3  4  5] :The view SHOULD be affected by the changes made to the original array.

"""
Make Changes in the VIEW:

Make a view, change the view, and display both arrays:
"""
arr3 = np.array([1, 2, 3, 4, 5])

x = arr3.view()
x[0] = 31

print(arr3)         # [31  2  3  4  5]   : The original array SHOULD be affected by the changes made to the view.
print(x)            # [31  2  3  4  5]

"""
Check if Array Owns its Data
As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

Every NumPy array has the attribute base that returns None if the array owns the data.

Otherwise, the base  attribute refers to the original object.

"""

arr4 = np.array([1, 2, 3, 4, 5])

x = arr4.copy()
y = arr4.view()

print(x.base)       # None                  : The copy returns None.
print(y.base)       # [1 2 3 4 5]           : The view returns the original array.

