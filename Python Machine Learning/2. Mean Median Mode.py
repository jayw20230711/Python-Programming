"""
MACHINE LEARNING - Mean Median Mode

What can we learn from looking at a group of numbers?

In MACHINE LEARNING (and in mathematics) there are often three values that interests us:

Mean - The average value
Median - The mid point value
Mode - The most common value

Example: We have registered the speed of 13 cars:
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

What is the average, the middle, or the most common speed value?

Mean
The mean value is the average value.

To calculate the mean, find the sum of all values, and divide the sum by the number of values:
(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77

"""
import numpy as np
from scipy import stats             # for later examples

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = np.mean(speed)
print('Mean value of array : ', speed)
print('Mean = ', x)     # 89.76923076923077

"""
Median
The median value is the value in the middle, after you have sorted all the values:
77, 78, 85, 86, 86, 86, -87-, 87, 88, 94, 99, 103, 111

It is important that the numbers are sorted before you can find the median.
"""
x = np.median(speed)
print('Median = ', x)           # 87.0

"""
If there are two numbers in the middle, divide the sum of those numbers by two.
77, 78, 85, 86, 86, --86, 87--, 87, 94, 98, 99, 103

(86 + 87) / 2 = 86.5
"""
speed = [99, 86, 87, 88, 86, 103, 87, 94, 78, 77, 85, 86]

x = np.median(speed)
print('\nMedian value of array : ', speed)
print('Median = ', x)           # 86.5

"""
Mode
The Mode value is the value that appears the most number of times:
99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86        = 86

The SciPy module has a method for this. Use the SciPy mode() method to find the number that appears the most:

from scipy import stats
"""
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = stats.mode(speed)
print('\nMode value of the array : ', speed)
print('Mode = ', x)             # ModeResult(mode=array([86]), count=array([3]))
