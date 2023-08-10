from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""
Normal (Gaussian) Distribution

The Normal Distribution is one of the most important distributions.
It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.
It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.

Use the random.normal() method to get a Normal Data Distribution.

It has three parameters:
loc - (Mean) where the peak of the bell exists.
scale - (Standard Deviation) how flat the graph distribution should be.
size - The shape of the returned array.

"""
x = random.normal(size=(2, 3))
# print('Generate a random normal distribution of size 2x3 :')
# print(x)

# print('Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2 :')
y = random.normal(loc=1, scale=2, size=(2, 3))
# print(y)

"""
Visualization of Normal Distribution
"""
sns.distplot(random.normal(size=1000), hist=False)
plt.title("Normal Distribution with displot() :")
# plt.xlabel("")
# plt.ylabel("")
plt.show()

sns.kdeplot(random.normal(size=1000))
plt.title("Normal Distribution with kdeplot() :")
plt.show()

sns.distplot(random.normal(loc=1, scale=2, size=(2, 3)), hist=True)
plt.show()
