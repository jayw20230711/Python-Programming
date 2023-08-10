"""
NumPy Logs

NumPy provides functions to perform log at the base 2, e and 10.

We will also explore how we can take log for any base by creating a custom ufunc.

All of the log functions will place -inf or inf in the elements if the log can not be computed.
"""
from math import log            # for log base e
import numpy as np

"""
Log at Base 2
Use the log2() function to perform log at the base 2.
"""
arr1 = np.arange(1, 10)
# Note: The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included)

print('\nArray values:')
print(arr1)

print('\nFind log at base 2 of elements in the array')
print(np.log2(arr1))    # [0.  1.   1.5849625  2.    2.32192809 2.5849625  2.80735492    3.   3.169925  ]

"""
Log at Base 10
Use the log10() function to perform log at the base 10.
"""
arr2 = np.arange(1, 10)
print('\nArray values:')
print(arr2)

print('\nFind log at base 10 of elements in the array')
print(np.log10(arr2))   # [0.  0.30103  0.47712125 0.60205999 0.69897  0.77815125  0.84509804 0.90308999 0.95424251]

"""
Natural Log, or Log at Base e
Use the log() function to perform log at the base e.
"""
arr3 = np.arange(1, 10)

print('\nFind log at base e of elements in the array')
print(np.log(arr3))     # [0. 0.69314718 1.09861229 1.38629436 1.60943791 1.79175947 1.94591015 2.07944154 2.19722458]

"""
Log at Any Base
NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt
function math.log() with two input parameters and one output parameter:
"""
nplog = np.frompyfunc(log, 2, 1)

print('\nusing any base:')
print(nplog(100, 15))
