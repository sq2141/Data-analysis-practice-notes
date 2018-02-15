import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn


# Reading .csv file
dframe = pd.read_csv('read_write_data.csv')  # The first row read as the column names
print dframe
dframe = pd.read_csv('read_write_data.csv', header=None)  # Read without header, so all values are data values
print dframe

# Readtable method (A more generic version of read csv), can read any delimiter
dframe = pd.read_table('read_write_data.csv',sep=',',header=None)
print dframe

# Read only specific rows
print pd.read_csv('read_write_data.csv', header=None, nrows=2)  # read the first 2 rows


# Writing
dframe.to_csv('mytextdata.csv')

# Writing with other delimiters
import sys  # sees output directly instead of saving, for practice
dframe.to_csv(sys.stdout,sep='_')

# Writing a subset of columns
dframe.to_csv(sys.stdout,columns=[0,1,2])


# Plus python has built-in csv readers