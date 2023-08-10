"""
Python Dictionaries

Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

"""
Dictionary Items
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

"""
Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Duplicates Not Allowed
Dictionaries cannot have two items with the same key:
Duplicate values will overwrite existing values:
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

"""
Dictionary Length
To determine how many items a dictionary has, use the len() function:
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisdict))

"""
Dictionary Items - Data Types
The values in dictionary items can be of any data type:
"""
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict)

"""
type()
From Python's perspective, dictionaries are defined as objects with the data type 'dict':

<class 'dict'>
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))

"""
Python - Access Dictionary Items

Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:

"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

"""
There is also a method called get() that will give you the same result:
"""
x = thisdict.get("brand")
print(x)

"""
Get Keys
The keys() method will return a list of all the keys in the dictionary.
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.keys()
print(x)

"""
The list of the keys is a view of the dictionary, meaning that any changes done to the 
dictionary will be reflected in the keys list.
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change

"""
Get Values
The values() method will return a list of all the values in the dictionary.
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.values()
print(x)
# print(thisdict.values())

"""
The list of the values is a view of the dictionary, meaning that any changes done to the 
dictionary will be reflected in the values list.
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

"""
Add a new item to the original dictionary, and see that the values list gets updated as well:
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change

"""
Get Items
The items() method will return each item in a dictionary, as tuples in a list.
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict.items()
print(x)

"""
The returned list is a view of the items of the dictionary, meaning that any changes done to 
the dictionary will be reflected in the items list.
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

"""
Add a new item to the original dictionary, and see that the items list gets updated as well:
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change

"""
Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

"""
Python - Change Dictionary Items

Change Values
You can change the value of a specific item by referring to its key name:
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 2018}

print(thisdict)

"""
Update Dictionary
The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

""""
Python - Add Dictionary Items

Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}

print(thisdict)

"""
Update Dictionary
The update() method will update the dictionary with the items from a given argument. If the item does not exist, 
the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs.
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

"""
Python - Remove Dictionary Items

Removing Items
There are several methods to remove items from a dictionary:
he pop() method removes the item with the specified key name:
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

"""
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

"""
The del keyword removes the item with the specified key name:
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
del thisdict["model"]
print(thisdict)

"""
The del keyword can also delete the dictionary completely:
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
# print(thisdict)  # this will cause an error because "thisdict" no longer exists.

"""
The clear() method empties the dictionary:
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

"""
Python - Loop Dictionaries

Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, 
but there are methods to return the values as well.

Print all key names in the dictionary, one by one:
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)

"""
Print all values in the dictionary, one by one:
"""
for x in thisdict:
    print(thisdict[x])

"""
You can also use the values() method to return values of a dictionary:
"""
for x in thisdict.values():
    print(x)

print(thisdict.values())

"""
You can use the keys() method to return the keys of a dictionary:
"""
for x in thisdict.keys():
    print(x)

print(thisdict.keys())

"""
Loop through both keys and values, by using the items() method:
"""
for x, y in thisdict.items():
    print(x, y)

"""
Python - Copy Dictionaries

Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to 
dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

"""
Another way to make a copy is to use the built-in function dict().
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

"""
Python - Nested Dictionaries

Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
"""
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily)

"""
Or, if you want to add three dictionaries into a new dictionary:

Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
"""
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily)
