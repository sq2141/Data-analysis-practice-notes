import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

# Download two modules: Xlrd and openpyxL

xlsfile = pd.ExcelFile('nfl.xlsx')
dframe = xlsfile.parse('Sheet1')
print dframe

# see pandas documentation for additional arguments like get specific rows etc.