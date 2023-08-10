"""
Pandas DataFrames

What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

"""
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print('\nCreate a simple Pandas DataFrame :')
print(df)

"""
Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)
"""
print('\nReturn row 0 : ')
print(df.loc[0])

print('\nReturn row 0 and 1 :')
print(df.loc[[0, 1]])

# Note: When using [], the result is a Pandas DataFrame.

"""
Named Indexes
With the index argument, you can name your own indexes.
"""
df2 = pd.DataFrame(data, index=["day1", "day2", "day3"])

print('\nAdd a list of names to give each row a name :')
print(df2)

"""
Locate Named Indexes
Use the named index in the loc attribute to return the specified row(s).
"""
print('\nReturn "day2" :')
print(df2.loc["day2"])

"""
Load Files Into a DataFrame
If your data sets are stored in a file, Pandas can load them into a DataFrame.
"""

df3 = pd.read_csv('data.csv')

print('\nLoad a comma separated file (CSV file) into a DataFrame :')
print(df3)
