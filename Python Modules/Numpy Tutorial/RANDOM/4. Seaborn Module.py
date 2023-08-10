"""
Seaborn Module

Visualize Distributions With Seaborn
Seaborn is a library that uses PYTHON Matplotlib underneath to plot graphs. It will be used to visualize random
distributions.

Distplots
Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the
distribution of points in the array.

Import PYTHON Matplotlib
Import the pyplot object of the PYTHON Matplotlib module in your code using the
following statement: import matplotlib.pyplot as plt

Import Seaborn
Import the Seaborn module in your code using the following statement: import seaborn as sns
"""
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

"""
Plotting a Distplot Without the Histogram
"""
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

"""
Note: We will be using: sns.distplot(arr, hist=False) to visualize random distributions in this tutorial.
"""