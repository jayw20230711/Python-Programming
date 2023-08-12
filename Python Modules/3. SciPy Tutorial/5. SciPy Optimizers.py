"""
SciPy Optimizers

Optimizers in SciPy
Optimizers are a set of procedures defined in SciPy that either find the minimum value of a function, or the root
of an equation.

Optimizing Functions
Essentially, all of the algorithms in Machine Learning are nothing more than a complex equation that needs to be
minimized with the help of given data.

Roots of an Equation
NumPy is capable of finding roots for polynomials and linear equations, but it can not find roots for non linear
equations, like this one:

x + cos(x)

For that you can use SciPy's optimze.root function.

This function takes two required arguments:
- fun - a function representing an equation.
- x0 - an initial guess for the root.

The function returns an object with information regarding the solution.

The actual solution is given under attribute x of the returned object:
"""
from scipy.optimize import root
from math import cos
from scipy.optimize import minimize

def eqn(x):
    return x + cos(x)

my_root = root(eqn, 0)

print('\nPrint the root value  X :')
print(my_root.x)        # [-0.73908513]
# Note: The returned object has much more information about the solution.

# Print all information about the solution (not just x which is the root)
print('\nPrint all information about the solution (not just x which is the root) :')
print(my_root)
"""
OUTPUT:
 fjac: array([[-1.]])
     fun: array([0.])
 message: 'The solution converged.'
    nfev: 9
     qtf: array([-2.66786593e-13])
       r: array([-1.67361202])
  status: 1
 success: True
       x: array([-0.73908513])
"""

##

"""
Minimizing a Function
A function, in this context, represents a curve, curves have high points and low points.

High points are called maxima.

Low points are called minima.

The highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima.

The lowest point in whole curve is called global minima, whereas the rest of them are called local minima.

Finding Minima
We can use scipy.optimize.minimize() function to minimize the function.

The minimize() function takes the following arguments:
- fun - a function representing an equation.
- x0 - an initial guess for the root.
- method - name of the method to use. Legal values:
    'CG'
    'BFGS'
    'Newton-CG'
    'L-BFGS-B'
    'TNC'
    'COBYLA'
    'SLSQP'

- callback - function called after each iteration of optimization.
- options - a dictionary defining extra params:
  {
     "disp": boolean - print detailed description
     "gtol": number - the tolerance of the error
  }

"""
def eqn(x):
    return x**2 + x + 2

my_min = minimize(eqn, 0, method='BFGS')

print('\nMinimize function : ')
print(my_min)
