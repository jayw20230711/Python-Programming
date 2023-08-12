"""
SciPy Spatial Data

Working with Spatial Data
Spatial data refers to data that is represented in a geometric space.

E.g. points on a coordinate system.

We deal with spatial data problems on many tasks.

E.g. finding if a point is inside a boundary or not.

SciPy provides us with the module scipy.spatial, which has functions for working with spatial data.


Triangulation
A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of
the polygon.

A Triangulation with points means creating surface composed triangles in which all of the given points are on at least
one vertex of any triangle in the surface.

One method to generate these triangulations through points is the Delaunay() Triangulation.

"""
import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
from scipy.spatial import KDTree
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import cosine
from scipy.spatial.distance import hamming

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices

print('Create a triangulation using points : ')
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()

# Note: The simplices property creates a generalization of the triangle notation.

"""
Convex Hull
A convex hull is the smallest polygon that covers all of the given points.

Use the ConvexHull() method to create a Convex Hull.

"""

points2 = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points2)
hull_points = hull.simplices

plt.scatter(points2[:, 0], points2[:, 1])
for simplex in hull_points:
    plt.plot(points2[simplex, 0], points2[simplex, 1], 'k-')

plt.show()

"""
KDTrees

KDTrees are a data structure optimized for nearest neighbor queries.
E.g. in a set of points using KDTrees we can efficiently ask which points are nearest to a certain given point.

The KDTree() method returns a KDTree object.
The query() method returns the distance to the nearest neighbor and the location of the neighbors.

"""
points3 = [(1, -1), (2, 3), (-2, 3), (2, -3)]

kdtree = KDTree(points3)

res = kdtree.query((1, 1))

print('\nFind the nearest neighbor to point (1,1) :')
print(res)  # (2.0, 0)

"""
Distance Matrix
There are many Distance Metrics used to find various types of distances between two points in data science, Euclidean 
distsance, cosine distsance etc.

The distance between two vectors may not only be the length of straight line between them, it can also be the angle 
between them from origin, or number of unit steps required etc.

Many of the Machine Learning algorithm's performance depends greatly on distance metrices. E.g. "K Nearest Neighbors", 
or "K Means" etc.

Let us look at some of the Distance Metrices:


Euclidean Distance
Find the euclidean distance between given points.
"""
p1 = (1, 0)
p2 = (10, 2)

res2 = euclidean(p1, p2)

print('\nFind the euclidean distance between given points :')
print(res2)  # 9.219544457292887

"""
Cityblock Distance (Manhattan Distance)

Is the distance computed using 4 degrees of movement.
E.g. we can only move: up, down, right, or left, not diagonally.
"""
p3 = (1, 0)
p4 = (10, 2)

res3 = cityblock(p3, p4)

print('\nFind the cityblock distance between given points :')
print(res3)     # 11

"""
Cosine Distance

Is the value of cosine angle between the two points A and B.

"""
p5 = (1, 0)
p6 = (10, 2)

res4 = cosine(p1, p2)

print('\nFind the cosine distsance between given points :')
print(res4)  # 0.019419324309079777

"""
Hamming Distance

Is the proportion of bits where two bits are difference.
It's a way to measure distance for binary sequences.
"""
print('\nFind the hamming distance between given points : ')
p1 = (True, False, True)
p2 = (False, True, True)

res5 = hamming(p1, p2)

print(res5)   # 0.6666666666666666
