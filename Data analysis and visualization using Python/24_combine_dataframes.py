import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Use numpy's where command to do logic on two series
ser1 = Series([2,np.nan,4,np.nan,6,np.nan], index=['Q','R','S','T','U','V'])
print ser1
ser2 = Series(np.arange(len(ser1)),dtype=np.float64, index=['Q','R','S','T','U','V'])
print ser2
print Series(np.where(pd.isnull(ser1),ser2,ser1),index=ser1.index)  # Get value of ser1 if not null, and replace with ser2 if null

# Can do the same thing using panda's combine
print ser1.combine_first(ser2)  # Take ser1, combine with ser2, but if there is a null value, use value from ser2

# Combine DataFrames
nan=np.nan
dframe_odds = DataFrame({'X':[1.,nan,3.,nan],
                         'Y':[nan,5.,nan,7.],
                         'Z':[nan,9.,nan,11.]})
dframe_evens = DataFrame({'X':[2.,4.,nan,6.,8],
                         'Y':[nan,10.,12.,14.,16.]})
print dframe_odds
print dframe_evens
print dframe_odds.combine_first(dframe_evens)

