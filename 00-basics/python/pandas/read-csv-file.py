
# * pip3 install pandas

import pandas as pd
from pathlib import Path

customers_csv = Path("00-basics/python/pandas/customers-100.csv")

df = pd.read_csv(customers_csv)
print(type(df))

print(df)
# * Read only top 5 records
print(df.head())

# ^ Comprise a new data frame
x = df[['Customer Id']]
print(x)

# ^ Comprise a new data frame
x = df[['Index','Customer Id', 'First Name', 'Email']]
print(x)

# ^ iloc method to represent the row and column value
print(df.iloc[0,0])

# ^ loc method to represent the row and column value
print(df.loc[0,'First Name'])

# dfNew = df
# dfNew.index = ['a','b','c','d','e']
# print(dfNew)
# print(dfNew.loc['a','First Name'])

print(df.iloc[0:2, 0:3])

# print(df.loc[0:2, 'Index':'Customer Id'])

firstName = df['First Name'].unique()
print(len(firstName))

df1 = df[df['Subscription Date'] <= '2020-12-12']
print(df1)

df1.to_csv('00-basics/python/pandas/filtered.csv')