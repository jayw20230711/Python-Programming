"""
Python Random randrange() Method

Definition and Usage
The randrange() method returns a randomly selected element from the specified range.

Syntax
random.randrange(start, stop, step)

Parameter	Description
start	    Optional. An integer specifying at which position to start.
            Default 0
stop	    Required. An integer specifying at which position to end.
step	    Optional. An integer specifying the incrementation.
            Default 1

"""
import random

# returns a number between 3 (included) and 9 (not included)
print(random.randrange(3, 9))
