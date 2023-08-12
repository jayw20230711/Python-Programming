"""
SciPy Getting Started

Installation of SciPy
If you have Python and PIP already installed on a system, then installation of SciPy is very easy.

Install it using this command:

# C:/Users/Your Name>pip install scipy

If this command fails, then use a Python distribution that already has SciPy installed like, Anaconda, Spyder etc.

Import SciPy
Once SciPy is installed, import the SciPy module(s) you want to use in your applications by adding the from scipy
import module statement:
"""
from scipy import constants
import scipy

print('How many cubic meters are in one liter :')
print(constants.liter)

# constants: SciPy offers a set of mathematical constants, one of them is liter which returns 1 liter as cubic meters.
# You will learn more about constants in the next chapter.

"""
Checking SciPy Version
The version string is stored under the __version__ attribute.
"""
print('\nChecking SciPy Version :')
print(scipy.__version__)
