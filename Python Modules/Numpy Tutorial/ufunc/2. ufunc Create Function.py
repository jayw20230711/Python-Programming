"""
Create Your Own ufunc

How To Create Your Own ufunc?
To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add
it to your NumPy ufunc library with the frompyfunc() method.

The frompyfunc() method takes the following arguments:

1. function - the name of the function.
2. inputs - the number of input arguments (arrays).
3. outputs - the number of output arrays.

"""
import numpy as np

# Create your own ufunc for addition:

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print('result: ')
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

"""
Check if a Function is a ufunc
Check the type of a function to check if it is a ufunc or not.

A ufunc should return <class 'numpy.ufunc'>.

"""
# import numpy as np

print('\ncheck function type of add:')
print(type(np.add))

"""
If it is not a ufunc, it will return another type, like this built-in NumPy function for joining two or more arrays:
"""
print('\ncheck function type of concatenate:')
print(type(np.concatenate))

"""
If the function is not recognized at all, it will return an error:
"""
# print('\nCheck the type of something that does not exist. This will produce an error:')
# print(type(np.blahblah))

"""
To test if the function is a ufunc in an if statement, use the numpy.ufunc value (or np.ufunc if you use np as 
an alias for numpy):
"""
print('\nhow to test this in if statement:')
if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

