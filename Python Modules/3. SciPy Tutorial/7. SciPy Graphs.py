"""
SciPy Graphs

Working with Graphs
Graphs are an essential data structure.

SciPy provides us with the module scipy.sparse.csgraph for working with such data structures.

Adjacency Matrix
Adjacency matrix is a nxn matrix where n is the number of elements in a graph.

And the values represents the connection between the elements.

Example:

B - 1 - A - 2 - c

For a graph like this, with elements A, B and C, the connections are:

A & B are connected with weight 1.

A & C are connected with weight 2.

C & B is not connected.

The Adjency Matrix would look like this:
      A B C
   A:[0 1 2]
   B:[1 0 0]
   C:[2 0 0]

Below follows some of the most used methods for working with adjacency matrices.

"""
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order

arr = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

newarr = csr_matrix(arr)

print('\nFind all of the connected components using connected_components() method: ')
print(connected_components(newarr))     # (1, array([0, 0, 0]))

"""
Dijkstra
Use the dijkstra method to find the shortest path in a graph from one element to another.

It takes following arguments:
1. return_predecessors: boolean (True to return whole path of traversal otherwise False).
2. indices: index of the element to return all paths from that element only.
3. limit: max weight of path.

"""

arr2 = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr2 = csr_matrix(arr2)

print('\nshortest path from element 1 to 2 dijkstra method : ')
print(dijkstra(newarr2, return_predecessors=True, indices=0))   # (array([0., 1., 2.]), array([-9999,     0,     0]))

"""
Floyd Warshall
Use the floyd_warshall() method to find shortest path between all pairs of elements.

"""

arr3 = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr3 = csr_matrix(arr3)

print('\nshortest path between all pairs of elements floyd_warshall() method  : ')

print(floyd_warshall(newarr3, return_predecessors=True))

"""
Bellman Ford
The bellman_ford() method can also find the shortest path between all pairs of elements, but this method can handle 
negative weights as well.
"""
arr4 = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr4 = csr_matrix(arr4)

print('\nFind shortest path from element 1 to 2 with given graph with a negative weight using bellman_ford() method : ')
print(bellman_ford(newarr4, return_predecessors=True, indices=0))

"""
Depth First Order

The depth_first_order() method returns a depth first traversal from a node. 
This function takes following arguments:
    1. the graph
    2. the starting element to traverse graph from
"""
arr5 = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr5 = csr_matrix(arr5)

print('\nTraverse the graph depth first for given adjacency matrix using depth_first_order() method :')
print(depth_first_order(newarr5, 1))

"""
Breadth First Order

The breadth_first_order() method returns a breadth first traversal from a node.

This function takes following arguments:
    1. the graph
    2. the starting element to traverse graph from

"""
arr6 = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr6 = csr_matrix(arr6)

print('\nTraverse the graph breadth first for given adjacency matrix using breadth_first_order() method :')
print(breadth_first_order(newarr6, 1))
