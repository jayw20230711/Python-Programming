# import numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))            # <class 'numpy.ndarray'>

arr2 = [1, 2, 3, 4, 5]
print(arr2)
print(type(arr2))           # <class 'list'>
"""
Checking NumPy Version
The version string is stored under __version__ attribute.
"""
print(np.__version__)