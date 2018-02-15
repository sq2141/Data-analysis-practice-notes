import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# Find missing values
data = Series(['one','two',np.nan,'four'])
print data
print data.isnull()  # boolean test for NaN

# Drop NaN values
print data.dropna()

# In Dataframes
dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])
print dframe

# Without further arguments, dropna drops row/columns if there is even just one NaN in it
clean_dframe = dframe.dropna()
print clean_dframe

# Can specify to drop NaN's that span entire rows
clean_dframe = dframe.dropna(how='all')
print clean_dframe

# Drop columns by specifying axis=1
clean_dframe = dframe.dropna(axis=1)
print clean_dframe

# Can threshold to keep rows/columns with at least X values
npn = np.nan
dframe2 = DataFrame ([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])
print dframe2
print dframe2.dropna(thresh=2)  # keep rows with at least 2 data points

# Fill NaN with...
print dframe2.fillna(1)

# Fill NaN with ... depending on column
print dframe2.fillna({0:0,1:1,2:2,3:3})  # Fill nth column's NaN values with NaN

