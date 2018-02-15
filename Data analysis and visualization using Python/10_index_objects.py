import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# Reminder that indexes in Series can be strings
my_ser = Series([1,2,3,4], index=['A','B','C','D'])
print my_ser

my_index = my_ser.index
print my_index

# get individual index
print my_index[2]

# get a range of index
print my_index[2:]  # print index value/string of 3rd row and after

# you can't change the index value/string one at a time