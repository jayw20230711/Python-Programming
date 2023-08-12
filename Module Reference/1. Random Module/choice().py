"""
Python Random choice() Method

Definition and Usage
The choice() method returns a randomly selected element from the specified sequence.

The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

Syntax
random.choice(sequence)

Parameter	Description
sequence	Required. A sequence like a list, a tuple, a range of numbers etc.

"""
import random

# Return a random element from a list:
mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))

x = "WELCOME"

print(random.choice(x))
