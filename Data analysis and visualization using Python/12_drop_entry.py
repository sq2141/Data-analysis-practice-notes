import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

'''
How to drop index
'''

# Drop index in Series
ser1 = Series(np.arange(3),index=['a','b','c'])
print ser1
ser1 = ser1.drop('b') # call drop and input index label
print ser1

# Drop row in DataFrame
ser2 = DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['x','y','z'])
print ser2
ser2 = ser2.drop('b') # drop a row by index
print ser2

# Drop columns in Dataframe
ser3 = ser2.drop('z', axis=1)  # axis means dimension, x axis = 0, y axis = 1 etc..
print ser3