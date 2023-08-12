"""
Python Random shuffle() Method

Definition and Usage
The shuffle() method takes a sequence, like a list, and reorganize the order of the items.

Note: This method changes the original list, it does not return a new list.

Syntax
random.shuffle(sequence, function)

Parameter	Description
sequence	Required. A sequence.
function	Optional. The name of a function that returns a number between 0.0 and 1.0.
            If not specified, the function random() will be used

"""
import random

mylist = ["apple", "banana", "cherry"]

random.shuffle(mylist)

print(mylist)

def myfunction():
    return 0.1

mylist2 = ["apple", "banana", "cherry"]
random.shuffle(mylist2, myfunction)

print(mylist2)


