"""
Create a NumPy ndarray Object
NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.

"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(type(arr))                    # <class 'numpy.ndarray'>

"""
To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, 
and it will be converted into an ndarray:
"""
arr2 = np.array((1, 2, 3, 4, 5))
print('\narr2 :')
print(arr2)
print(type(arr2))                   # <class 'numpy.ndarray'>

"""
Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).

nested array: are arrays that have arrays as their elements.
"""

"""
0-D Arrays
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
"""
arr3 = np.array(42)
print('\narr3 0-D : ')
print(arr3)
print(type(arr3))                   # <class 'numpy.ndarray'>

"""
1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.
"""
arr4 = np.array([1, 2, 3, 4, 5])
print('\narr4 1-D :')
print(arr4)

"""
2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.

NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
"""
arr5 = np.array([[1, 2, 3], [4, 5, 6]])
print('\n arr5 2-D : ')
print(arr5)
print(arr5.shape)

"""
3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.

Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
"""
arr6 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print('\n arr6 3-D : ')
print(arr6)

"""
Check Number of Dimensions?
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
"""
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print('\n', a, 'is a ', a.ndim, 'Dimension array.')
print(b, ' is a ', b.ndim, 'Dimension array.')
print(c, ' is a ', c.ndim, 'Dimension array.')
print(d, ' is a ', d.ndim, 'Dimension array.')
print('\nShape of ', a, 'is ', a.shape)
print('\nShape of ', b, 'is ', b.shape)
print('\nShape of ', c, 'is ', c.shape)
print('\nShape of ', d, 'is ', d.shape)


"""
Higher Dimensional Arrays
An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument.
"""
arr7 = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr7)
print('number of dimensions : ', arr7.ndim)
print(arr7.shape)
