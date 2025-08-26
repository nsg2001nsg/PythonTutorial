# Pandas allows us to manipulate and analyze data using data frame structures/ format

# one-dimensional (1D) NumPy array with a label and an index attached to it.
# Also, unlike NumPy arrays, they can contain non-numeric data (characters, dates, time, booleans, etc.).
# Usually we work with Series only as part of dataframes.
# pd.Series(data, dtype)

# data frame is a 2D labeled data structure kind of like an Excel table or sql table
# DF forms the basis of pandas operations
# here are various ways of creating dataframes, for instance, creating them from dictionaries, reading from .txt and .csv files, etc.

import pandas as pd

"""
values = [x for x in range(1, 11)]
# print(type(values))

s = pd.Series([x for x in range(1, 11)])  # has default indexes. Table format
print(type(s))
# print(s)

# indexes could be assigned manually
s = pd.Series([x for x in range(1, 5)], index=['a', 'b', 'c', 'd'])
print(s)

ser1 = pd.Series([x for x in range(1, 5)])
ser2 = pd.Series([x for x in range(5, 9)])
print(ser1 + ser2)  # both columns[indices] are added

"""

"""
# Creating DF using series/lists

cars_per_cap = pd.Series([809, 731, 588, 18, 200, 70, 45])
country = pd.Series(['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'])
drives_right = pd.Series([False, True, True, True, False, False, False])

df = pd.DataFrame({'Cars Per Cap': cars_per_cap, 'Country': country, 'Drives Right': drives_right})
print(df)

# pandas.DataFrame  interprets each element (of the list) passed as a row to make it column we use transpose T attribute
names = ['Nandini', 'Khushi', 'Rinchi', 'Purvi']
ages = [23, 23, 23, 25]
df = pd.DataFrame([names, ages]).T
df.columns = ['Names', 'Ages']
print(df)
"""

# Creating DF from external files.
"""
# external files may not necessarily be in the form of lists/series.
# We will have to load data store in form of csv file, text file etc.

# header="infer" → default → Pandas guesses the first row is column names.
# index_col="ID" makes that column the index
# names=[]  we can provides sustom column names
# since the fi le has no headers read_csv uses the first row as one, so we have to specify header=None

df = pd.read_csv('cars.csv', header=None)  # now each column is marked with indices instead
print(df)
print(type(df))

print(df.head())       # first 5 rows
print(df.tail())       # last 5 rows
print(df.info())       # structure
print(df.describe())   # stats summary
print(df.shape)        # (rows, cols)
print(df.columns)      # column names
print(df.index)        # row labels
"""

# Rows and Columns manipulation
"""
df = pd.read_csv('cars.csv', header=None, index_col=[0, 1])  # column 1 is assigned as index for rows and the index name is now 1
df.index.names = ['Region_code', 'Country_code']
df.columns = ['Country', 'Cars per capita', 'Drives right']  # assigning column headers in runtime after the dataset is loaded
print(df.index)  # shows row index names and is also used t assign row index names
print(df)

# creating multilevel indexing aka hierarchical index is also possible by passing to columns in the set_index
# Can also pass a list of tuples with multiple indexes as row index

# n = 6
# squares = pd.Series([x ** 2 for x in range(1, n+1)], index=[x for x in range(1, n+1)])
# print(squares)


import matplotlib.pyplot as plt

df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/A08MajL8qN4rq72EpVJbAP1Rw/marks_1.csv', sep='|',
                 header=None, index_col=0)
df.index.name = 'S.No.'
df.columns = ['Name', 'Subject', 'Maximum Marks', 'Marks Obtained', 'Percentage']
print(df)
df['Marks Obtained'].plot(kind='bar')
plt.show()
"""

# Indexing and slicing
"""
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/A08MajL8qN4rq72EpVJbAP1Rw/marks_1.csv', sep='|',
                 header=None, index_col=0)
df.index.name = 'S.No.'
df.columns = ['Name', 'Subject', 'Maximum Marks', 'Marks Obtained', 'Percentage']
print(df)

# fetching specific columns
print(df['Name'])  # single bracket returns object of type series
print(df[['Name', 'Marks Obtained']])  # double bracket returns object of type dataframe
print(df.loc[1])  # returns row at index (position based)
print(df.iloc[1]) # returns row at index (index based)
"""

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df.iloc[[x for x in range(1, df.shape[0]) if not x % 2]]  # index based
print(df_2.head(5))
df_2 = df.loc[[x for x in range(2, df.shape[0]) if not x % 2], ['wind', 'rain', 'area']]  # to extract rows of specific columns
print(df_2.head(5))  # label based indexing

# slicing can also be done in iloc
print(df.iloc[0:5, 7:])  # indexing column as well

# subsetting dataframe based on conditions
print(df[df['wind'] > 5])  # gives rows where the condition is met
print(df[0:2])  # indexing

# .isin() can be used in conditionals where we want to check a certain condition from a collection is met
# .isna() to check for null values

print(df[(df['area'] > 0) & (df['wind'] > 1) & (df['temp'] > 15)])
