"""
NumPy GCD Greatest Common Denominator

Finding GCD (Greatest Common Denominator)
The GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor) is the biggest number that is a
common factor of both of the numbers.
"""
import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print('\nFind the HCF of the 6 amd 9 :')
print(x)    # 3          : (6/3=2 and 9/3=3).

"""
Finding GCD in Arrays

To find the Highest Common Factor of all values in an array, you can use the reduce() method.

The reduce() method will use the ufunc, in this case the gcd() function, on each element, and reduce the array 
by one dimension.

"""
arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print('\nFinding GCD in [20, 8, 32, 36, 16] :')
print(x)    # 4
