import numpy as np
import pandas as pd
from numpy.random import randn
import random

pd.set_option('display.max_rows', None)
#pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

salesHourly = pd.read_excel('saleshourly.xlsx')
salesHourly = salesHourly[['M01AB', 'Year', 'Month', 'Weekday Name']]

salesHourly_2014 = salesHourly[salesHourly['Year'] == 2014].sample(frac=1).head(5)
salesHourly_2015 = salesHourly[salesHourly['Year'] == 2015].sample(frac=1).head(5)
salesHourly_2016 = salesHourly[salesHourly['Year'] == 2016].sample(frac=1).head(5)
salesHourly_2017 = salesHourly[salesHourly['Year'] == 2017].sample(frac=1).head(5)
salesHourly_2018 = salesHourly[salesHourly['Year'] == 2018].sample(frac=1).head(5)
salesHourly_2019 = salesHourly[salesHourly['Year'] == 2019].sample(frac=1).head(5)

salesHourly = pd.concat([salesHourly_2014, salesHourly_2015, salesHourly_2016, salesHourly_2017, salesHourly_2018, salesHourly_2019])
# print(salesHourly)


# create a new column
# salesHourly['M01A(B + E)'] = salesHourly['M01AB'] + salesHourly['M01AE']
# salesHourly['New'] = None

# drop a column
# salesHourly.drop('New', axis=1, inplace=True)

# get a row(s)
# print(salesHourly.loc[4]) # string can also be passed if indexes are string
# print(salesHourly.iloc[4])
# print(salesHourly.iloc[4:10])

# applying conditions
# print(salesHourly['M01AE'].head(100) > 0)
# print(salesHourly[salesHourly['M01AE'] > 0].head(50))
# print(salesHourly[salesHourly['Year'] == 2014])
# print(salesHourly[salesHourly['Year'] == 2015][['R03', 'R06']])
# print(salesHourly[(salesHourly['Year'] == 2016) & (salesHourly['Month'] == 1)])

# print(salesHourly.head(10))

# salesHourly.dropna(inplace=True) # default drops row
# salesHourly.fillna(value='MISSING', inplace=True)
# salesHourly.fillna(value=salesHourly['Year'].mean(), inplace=True)

# reset index
# salesHourly.reset_index()

# set index
# salesHourly.set_index(a_list_of_index, inplace = True)

# groupByYear = salesHourly.groupby('Year')
# print(groupByYear.sum()['R03'])
# print(groupByYear.sum())
# print(groupByYear.describe())

# dataOne = salesHourly[(salesHourly['Year'] == 2015) & (salesHourly['M01AB'] > 0)].head(10)
# dataTwo = salesHourly[(salesHourly['Year'] == 2016) & (salesHourly['M01AE'] > 0)].head(10)

# print(dataOne)
# print('=====================')
# print(dataTwo)
# print('=====================')
# print(pd.concat([dataOne, dataTwo], axis=0))
# print('=====================')
# print(pd.concat([dataOne, dataTwo], axis=1))


# dataFirst = salesHourly[(salesHourly['Year'] == 2015) & (salesHourly['M01AB'] > 0)].head(3)
# dataSecond = salesHourly[(salesHourly['Year'] == 2015) & (salesHourly['M01AE'] > 0)].head(3)
#
# dataFirst.set_index(['Year'], inplace=True)
# dataSecond.set_index(['Year'], inplace=True)
#
# print(dataFirst)
# print(dataSecond)

# df = pd.merge(dataFirst, dataSecond, how='inner', on=['Year', 'Weekday Name'])
# print(df)
# print(len(df))

# print(dataFirst.join(dataSecond, how='inner', lsuffix='Year'))

# operations
# print(salesHourly['Weekday Name'].unique())
# print(salesHourly['Weekday Name'].nunique())
# print(salesHourly['Weekday Name'].value_counts())
# print(salesHourly['M01AB'].sum())
# print(salesHourly['M01AB'].mean())

# def times2(x):
#     return x*2
# print(salesHourly['M01AB'].apply(times2))

# print(salesHourly.sort_values(by='Month'))


# multi level index
# outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
# inside = [1, 2, 3, 1, 2, 3]
# hier_index = list(zip(outside, inside))
# hier_index = pd.MultiIndex.from_tuples(hier_index)

# data = pd.DataFrame(randn(6,2), index=hier_index, columns=['A', 'B'])

# print(data.loc['G1'])
# print(data.loc['G1'].loc[1])
# print(data.loc['G1'].loc[3]['B'])

# def add(x):
#     return x + random.randint(0,10)
#
# salesHourly['M01AB2'] = salesHourly['M01AB'].apply(add)
# salesHourly['N02BA2'] = salesHourly['N02BA'].apply(add)
# salesHourly['R032'] = salesHourly['R03'].apply(add)
#
# salesHourly.drop(['M01AB', 'N02BA', 'R03'], axis=1, inplace=True)
#
# cols = ['M01AB2', 'N02BA2', 'R032', 'Weekday Name', 'Month', 'Year']
# salesHourly = salesHourly[cols]
# salesHourly.to_excel('sales.xlsx', index=False)