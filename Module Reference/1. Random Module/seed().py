"""
Python Random seed() Method

Definition and Usage
The seed() method is used to initialize the random number generator.
The random number generator needs a number to start with (a seed value), to be able to generate a random number.

By default the random number generator uses the current system time.

Use the seed() method to customize the start number of the random number generator.

Note: If you use the same seed value twice you will get the same random number twice. See example below

Syntax
random.seed(a, version)

Parameter	Description
a	        Optional. The seed value needed to generate a random number.
            If it is an integer it is used directly, if not it has to be converted into an integer.
            Default value is None, and if None, the generator uses the current system time.
version	    An integer specifying how to convert the a parameter into a integer.
            Default value is 2


Set the seed value to 10 and see what happens:
"""
import random

random.seed(10)
# random.seed(1)

print(random.random())

# #the generator creates a random number based on the seed value, so if the seed value is 10, you will always
# get 0.5714025946899135 as the first random number.
