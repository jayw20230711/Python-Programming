"""
Python Random getrandbits() Method

Definition and Usage
The getrandbits() method returns an integer in the specified size (in bits).

Syntax
random.getrandbits(n)

Parameter	Description
n	        Required. A number specifying the size, in bits, of the returned integer.

"""
import random

x = random.getrandbits(8)
# x = random.getrandbits(16)

print(x)
