import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

# Build a matrix using numpy functions
arr = np.array([[1,2,np.nan],[np.nan,3,4]])
print arr

# Create a dataframe from the matrix
dframe1 = DataFrame(arr,index=['a','b'],columns=['One','Two','Three'])
print dframe1

'''
Some functions to call on dataframes
'''

# Sum down the columns of a dataframe, ignoring NaNs
print dframe1.sum()
# Sum across the rows of a dataframe
print dframe1.sum(axis=1)

# Min/Max
print dframe1.min()
# Min/Max value's index
print dframe1.idxmin()

# Describe some summary statistics
print dframe1.describe()


# Covariance
import pandas.io.data as pdweb
import datetime
prices = pdweb.get_data_yahoo(['SPY','AAPL','BP'], start=datetime.datetime(2010,1,1),end=datetime.datetime(2015,1,1))['Adj Close'] # Get stock prices
print prices.head()
volume = pdweb.get_data_yahoo(['SPY','AAPL','BP'], start=datetime.datetime(2010,1,1),end=datetime.datetime(2015,1,1))['Volume'] # Get volume
print volume.head()
rets = prices.pct_change()  # Call pct_change to get percent change
corr = rets.corr  # Calculate correlation

# Plot
import matplotlib.pyplot as plt
import seaborn as sns
# prices.plot()
# Make correlation plot with seaborn
sns.corrplot(rets,annot=False,diag_names=False)
plt.show()

# Other calls
# ser1.unique()
# ser1.value_counts() 