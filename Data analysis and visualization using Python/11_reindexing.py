import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

'''
Reindexing here means adding new index entries to an already existing Series or Dataframe
'''

ser1 = Series([1,2,3,4], index=['A','B','C','D'])
print ser1

# Reindexing will create a new Series, and if the old series didn't have values associated with new index names, they will be left NaN
ser2 = ser1.reindex(['A','B','C','D','E','F'])
print ser2

# Or we can reindex and fill new indexes with some value
ser3 = ser2.reindex(['A','B','C','D','E','F','G'], fill_value=0)
print ser3

# Another way to reindex and fill (forward fill, ffill)
ser4 = Series(['USA','Mexico','Canada'],index=[0,5,10])
print ser4
ser5 = ser4.reindex(range(15),method='ffill')
print ser5

# Reindex dataframes
dframe = DataFrame(randn(25).reshape((5,5)),index=['A','B','D','E','F'],columns=['col1','col2','col3','col4','col5'])
print dframe

# Reindex rows of dataframes
dframe2=dframe.reindex(['A','B','C','D','E','F'])
print dframe2

# Reindex columns of dataframes
dframe3 = dframe2.reindex(columns=['col1','col2','col3','col4','col5','col6'])
print dframe3

# Another way to reindex using .ix (which queries indexes, but creates new rows/columns if not found)
dframe4 = dframe.ix[['A','B','C','D','E','F'],['col1','col2','col3','col4','col5','col6']]
print dframe4