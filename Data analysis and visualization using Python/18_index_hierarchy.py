import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

# Multiple index levels (like having multiple dimensions)
ser = Series(randn(6),index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])
print ser
print ser[1]  # calling upper index level
print ser[:,'a']  # calling lower index levels

# Convert multiple index series to dataframe
dframe = ser.unstack()
print dframe

# Dataframes with multiple level indexes (like higher level column and row labels)
dframe2 = DataFrame(np.arange(16).reshape(4,4),index=[['a','a','b','b'],[1,2,1,2]],columns=[['NYC','NYC',"LA",'SF'],['cold','hot','hot','cold']])
print dframe2

# Giving index names
dframe2.index.names = ['IND1','IND2']
dframe2.columns.names = ['CITIES','TEMP']
print dframe2

# Swap index levels
dframe3 = dframe2.swaplevel('CITIES','TEMP',axis=1)
print dframe3

# Sort index
print dframe2.sortlevel(1)  # sort by lower level index

# Perform operations on specific level
print dframe2.sum(level='TEMP',axis=1)  # add on temp level, ignoring/lumping cities
