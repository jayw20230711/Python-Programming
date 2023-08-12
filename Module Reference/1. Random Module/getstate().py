"""
Python Random getstate() Method

Definition and Usage
The getstate() method returns an object with the current state of the random number generator.

Use this method to capture the state, and use the setstate() method, with the captured state, to restore the state

Syntax
random.getstate()

Return the current state of the random generator:
"""
import random

x = random.getstate()

print(x)
