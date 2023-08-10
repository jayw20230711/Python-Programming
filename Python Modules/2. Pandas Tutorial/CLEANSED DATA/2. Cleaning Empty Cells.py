"""
Pandas - Cleaning Empty Cells

Empty Cells
Empty cells can potentially give you a wrong result when you analyze data.

Remove Rows
One way to deal with empty cells is to remove rows that contain empty cells.

This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
"""
import pandas as pd

df = pd.read_csv('data.csv')
new_df = df.dropna()

print(new_df.to_string())

"""
Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

If you want to change the original DataFrame, use the inplace = True argument:
"""
df2 = pd.read_csv('data.csv')

df2.dropna(inplace=True)

print(df2.to_string())

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL
# values from the original DataFrame.

"""
Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value:
"""
df3 = pd.read_csv('data.csv')

print('\nReplace null values with 130 :')
df3.fillna(130, inplace=True)
print(df3.to_string())

"""
Replace Only For Specified Columns
The example above replaces all empty cells in the whole Data Frame.

To only replace empty values for one column, specify the column name for the DataFrame:
"""
df4 = pd.read_csv('data.csv')

print('\nReplace NULL values in the "Calories" columns with the number 130 :')
df4["Calories"].fillna(130, inplace=True)
print(df4.to_string())

"""
Replace Using Mean, Median, or Mode
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
"""
df5 = pd.read_csv('data.csv')

X = df5["Calories"].mean()

df5["Calories"].fillna(X, inplace=True)

print('\nReplace Using Mean : ', X)
print(df5.to_string())

# Mean = the average value (the sum of all values divided by number of values).

"""
Calculate the MEDIAN, and replace any empty values with it:
"""
df6 = pd.read_csv('data.csv')
Y = df6["Calories"].median()

df6["Calories"].fillna(Y, inplace=True)

print('\nReplace Using Median : ', Y)
print(df6.to_string())

# Median = the value in the middle, after you have sorted all values ascending.

"""
Calculate the MODE, and replace any empty values with it:
"""
df7 = pd.read_csv('data.csv')
z = df7["Calories"].mode()[0]

df7["Calories"].fillna(z, inplace=True)
print('\nReplace using Mode :', z)
print(df7.to_string())
