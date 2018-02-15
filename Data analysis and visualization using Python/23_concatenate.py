import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Concatenate in numpy
arr1 = np.arange(9).reshape(3,3)
print arr1
print np.concatenate([arr1,arr1], axis=1)

# Concatenate in pandas series
ser1 = Series([0,1,2], index=['T','U','V'])
ser2 = Series([3,4], index=['X','Y'])
print ser1
print ser2
print pd.concat([ser1,ser2])  # if axis is set to 1, creates a dataframe with 2 columns
print pd.concat([ser1,ser2],keys=['cat1','cat2'])  # concatenate with labels

# Concatenate in dataframes
dframe1 = DataFrame(np.random.randn(4,3),columns=['X','Y','Z'])
print dframe1
dframe2 = DataFrame(np.random.randn(3,3),columns=['Y','Q','X'])
print dframe2
print pd.concat([dframe1,dframe2])  # Combines according to column labels, with NaN for missing values
print pd.concat([dframe1,dframe2],ignore_index=True)  # give a continuous index instead of retaining original index