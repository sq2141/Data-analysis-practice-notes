import numpy as np
import pandas as pd
from pandas import Series, DataFrame

'''
Series is like an array but is indexed (has labels). It is like Python's dictionary; dictionaries and Pandas' series can be converted back and forth (See below)
'''

obj = Series([3,6,9,12])
print obj
print obj.values
print obj.index

# Create a series with an index that I specify
ww2_cas = Series([87, 43, 30, 21, 4], index=['USSR','Germany','China','Japan','USA'])  # casualties in hundred thousands
print ww2_cas

# We can use the index name to call the series value
print ww2_cas['USSR']

# Check which countries had casualties greater than 4
print ww2_cas[ww2_cas > 4]

# Check if index or value is in series
print 'USSR' in ww2_cas

# Convert series into dictionary, then back to series
ww2_dict = ww2_cas.to_dict()
print ww2_dict
ww2_series = Series(ww2_dict)
print ww2_series

# Make a series from dictionary, drawing cases where index name is found in countries list
countries = ['China','Germany','Japan','USA','USSR','Argentina']
obj2 = Series(ww2_dict,index=countries)
print obj2

# Checks series for NaN (Not a Number/Null values), or where there is Not NaN
print pd.isnull(obj2)
print pd.notnull(obj2)

# Adding series together
print ww2_series
print obj2
print ww2_series + obj2

# Series can have a string name property attached to it
obj2.name = 'WW2 Casualties'
print obj2

# Index can also have a string label (like labeling a column in Excel)
obj2.index.name = 'Countries'
print obj2