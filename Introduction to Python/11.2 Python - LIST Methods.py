"""
List Methods
Python has a set of built-in methods that you can use on lists.

Method	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
"""

"""
sort()	        Sorts the list

Definition and Usage
The sort() method sorts the list ascending by default.

You can also make a function to decide the sorting criteria(s).

Syntax
list.sort(reverse=True|False, key=myFunc)
Parameter Values
Parameter	Description
reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
key	Optional. A function to specify the sorting criteria(s)
"""
lst = ['k', 'a', 'b', 'g', 'c', 'd', 'e', 'f', 'g', 'h']
print('lst  -->', lst)
lst.sort()
print('lst.sort()  -->', lst)
lst.sort(reverse=True)
print('lst.sort(reverse=True)  -->', lst)

# ----------
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
print('\nSort the list by the length of the values : ', cars)


# A function that returns the length of the value:
def myFunc(e):
    return len(e)


cars.sort(key=myFunc)
print(cars)


# --------------
# A function that returns the length of the value:
# ----------------
def myFunc(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
print('\nSort the list by the length of the values and reversed : ', cars)
cars.sort(reverse=True, key=myFunc)
print('sorted list :', cars)


# -------------
# A function that returns the 'year' value:
def myFunc(e):
    return e['year']


cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

print('\nSort a list of dictionaries based on the "year" value of the dictionaries : ', cars)
cars.sort(key=myFunc)
print('Sorted list : ', cars)
