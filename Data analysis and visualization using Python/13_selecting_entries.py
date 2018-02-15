import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser1 = Series(np.arange(3),index=['a','b','c'])
ser1 = 2*ser1
print ser1

# Grab value by index
print ser1['b']
print ser1[2]
print ser1[0:3]
print ser1[['c','a']]

# Grab values by logic
print ser1[ser1>1]

# We can also set values by logic
ser1[ser1>3]=10
print ser1

# Selecting data in a DataFrame
dframe = DataFrame(np.arange(25).reshape(5,5),index=['NYC','LA','CHI','SF','DC'], columns=['a','b','c','d','e'])
print dframe

# Selecting by column
print dframe['b']
print dframe[['b','c','e']]
print dframe[dframe['c']>8]  # grab all entries where the entry in the c column is greater than 8

# Get a boolean dataframe
print dframe > 10

# Can also use ix to label index (get row data)
print dframe.ix['LA']
print dframe.ix[2]