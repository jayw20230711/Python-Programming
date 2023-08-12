"""
SciPy Sparse Data

What is Sparse Data
Sparse data is data that has mostly unused elements (elements that don't carry any information ).

It can be an array like this one:

[1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]

Sparse Data: is a data set where most of the item values are zero.

Dense Array: is the opposite of a sparse array: most of the values are not zero.

In scientific computing, when we are dealing with partial derivatives in linear algebra we will come across sparse data.

How to Work With Sparse Data
SciPy has a module, scipy.sparse that provides functions to deal with sparse data.

There are primarily two types of sparse matrices that we use:
CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products

We will use the CSR matrix in this tutorial.

CSR Matrix
We can create CSR matrix by passing an arrray into function
scipy.sparse.csr_matrix().

"""
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print('\nprint csr_matrix :')
print(csr_matrix(arr))

"""
OUTPUT :
(0, 5)	1
(0, 6)	1
(0, 8)	2
  
From the result we can see that there are 3 items with value.
The 1. item is in row 0 position 5 and has the value 1.
The 2. item is in row 0 position 6 and has the value 1.
The 3. item is in row 0 position 8 and has the value 2.

Sparse Matrix Methods
Viewing stored data (not the zero items) with the data property:

Sparse Matrix Methods
Viewing stored data (not the zero items) with the data property:

"""

arr2 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print('\nViewing stored data (not the zero items) : ')
print(csr_matrix(arr2).data)   # [1 1 2]

"""
Counting nonzeros with the count_nonzero() method:
"""
print('\nCounting non zero items :')
print(csr_matrix(arr2).count_nonzero())  # 3

"""
Removing zero-entries from the matrix with the eliminate_zeros() method:
"""
arr3 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr3)
mat.eliminate_zeros()

print('\nRemoving zero-entries from the matrix : ')
print(mat)

"""
Eliminating duplicate entries with the sum_duplicates() method:
"""
arr4 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat1 = csr_matrix(arr4)
mat1.sum_duplicates()

print('\nEliminating duplicate entries by adding them : ')
print(mat1)

"""
Converting from csr to csc with the tocsc() method:
"""
arr5 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

newarr = csr_matrix(arr5).tocsc()

print('\nConverting from csr to csc : ')
print(newarr)

"""
Note: Apart from the mentioned sparse specific operations, sparse matrices support all of the operations that normal 
matrices support e.g. reshaping, summing, arithemetic, broadcasting etc.
"""
