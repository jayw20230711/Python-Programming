"""
Uniform Distribution
Used to describe probability where every event has equal chances of occurring.

E.g. Generation of random numbers.

It has three parameters:
a - lower bound - default 0 .0.
b - upper bound - default 1.0.
size - The shape of the returned array.

"""
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.uniform(size=(2, 3))
print('Create a 2x3 uniform distribution sample :')
print(x)

"""
Visualization of Uniform Distribution
"""
sns.distplot(random.uniform(size=1000), hist=False)

plt.show()



