"""
Pandas Series

What is a Series?
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.


"""
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print('Create a simple Pandas Series from a list :')
print(myvar)

"""
Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second 
value has index 1 etc.

This label can be used to access a specified value.
"""

print('\nReturn the first value of the Series :')
print(myvar[0])

"""
Create Labels
With the index argument, you can name your own labels.
"""
b = [2, 7, 5]

var2 = pd.Series(b, index=["x", "y", "z"])

print('\nCreate Labels :')
print(var2)

"""
When you have created labels, you can access an item by referring to the label.
"""
print('\nAccess items using the labels :')
print(var2["y"])

"""
Key/Value Objects as Series
You can also use a key/value object, like a dictionary, when creating a Series.
"""
calories = {"day1": 420, "day2": 380, "day3": 390}

var3 = pd.Series(calories)

print('\nCreate a simple Pandas Series from a dictionary :')
"""
Note: The keys of the dictionary become the labels.
"""
print(var3)

"""
To select only some of the items in the dictionary, use the index argument and specify only the items you want to 
include in the Series.
"""
calories2 = {"day1": 420, "day2": 380, "day3": 390}

var4 = pd.Series(calories2, index=["day1", "day2"])

print('\nCreate a Series using only data from "day1" and "day2" :')
print(var4)

"""
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
"""
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

var5 = pd.DataFrame(data)

print('\nCreate a DataFrame from two Series :\n')
print(var5)
