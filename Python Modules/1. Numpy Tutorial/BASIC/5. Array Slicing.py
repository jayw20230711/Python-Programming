"""
Slicing arrays
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1

"""
# Slice elements from index 1 to index 5 from the following array:
import numpy as np

t = (1, 2, 3)
print(t)
print(type(t))

l = [1, 2, 3]
print(l)
print(type(l))

# Note: The result includes the start index, but excludes the end index.
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])     # [2 3 4 5]
print(type(arr))

# Slice elements from index 4 to the end of the array:
print(arr[4:])      # [5 6 7]

# Slice elements from the beginning to index 4 (not included):
print(arr[:4])      # [1 2 3 4]

"""
Negative Slicing
Use the minus operator to refer to an index from the end:
"""
# Slice from the index 3 from the end to index 1 from the end:
print(arr[-3:-1])  # Note: The result includes the start index, but excludes the end index.
# [5 6]

"""
STEP
Use the step value to determine the step of the slicing:
"""
# Return every other element from index 1 to index 5:
print(arr[1:5:2])  # [2 4]

# Return every other element from the entire array:
print(arr[::2])  # [1 3 5 7]

# to print the whole array using slicing
print(arr[:])  # [1 2 3 4 5 6 7]
print(arr[0:])  # [1 2 3 4 5 6 7]
print(arr[::])  # [1 2 3 4 5 6 7]
print(arr[::1])  # [1 2 3 4 5 6 7]

# to print the whole array in reverse order using slicing
print(arr[::-1])  # [7 6 5 4 3 2 1]
print(arr[-1::-1])  # [7 6 5 4 3 2 1]
print(arr[-1])      # 7                    - scaler
print(arr.ndim)     # 1
print(arr.shape)    # (7,
print(type(arr[-1]))                       # <class 'numpy.int32'>
print(arr[-1:])     # [7]                  - 1D array
print(arr.ndim)     # 1
print(type(arr[-1:]))                      # <class 'numpy.ndarray'>

"""
Slicing 2-D Arrays

From the second element, slice elements from index 1 to index 4 (not included):
"""
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2[1, 1:4])  # [7 8 9]

# From both elements, return index 2:
print(arr2[0:2, 2])     # [3 8]

print(arr2[0:1, 2])     # [3]

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr2[0:2, 1:4])
# [[2 3 4]
#   [7 8 9]]

