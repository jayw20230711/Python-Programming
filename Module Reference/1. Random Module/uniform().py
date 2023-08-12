"""
Python Random uniform() Method

Definition and Usage
The uniform() method returns a random floating number between the two specified numbers (both included).

Syntax
random.uniform(a, b)

Parameter	Description
a	        Required. A number specifying the lowest possible outcome
b	        Required. A number specifying the highest possible outcome

"""
import random

# Return a random number between, and included, 20 and 60:
print(random.uniform(20, 60))
