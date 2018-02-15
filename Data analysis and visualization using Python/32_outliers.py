import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Find outliers in a dataset by using greater/lesser than logic to find values

# Generate a dataframe
np.random.seed(12345)
dframe = DataFrame(np.random.randn(1000,4))
print dframe.head()

# Describe the data
print dframe.describe()

# Get the first column
col = dframe[0]
print col.head()

# Get values greater than 3
print col[np.abs(col)>3]

# Get values greater than 3 in the whole dataframe
print dframe[(np.abs(dframe)>3).any(1)]  # if any values in a row > 3, return the row

# Set cap to +/-3
dframe[np.abs(dframe)>3] = np.sign(dframe)*3
print dframe.describe()