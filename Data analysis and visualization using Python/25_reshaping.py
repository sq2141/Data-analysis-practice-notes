import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# Use stack to pivot columns into rows, so everything is in one column running down
dframe1 = DataFrame(np.arange(8).reshape(2,4),
                    index=pd.Index(['LA','SF'],name='city'),
                    columns=pd.Index(['A','B','C','D'],name='letter'))  # passing the index as pd.Index allows me to name the index
print dframe1
dframe_st = dframe1.stack()
print dframe_st

# Unstack
dframe_unst = dframe_st.unstack('city')  # unstacking by city puts cities as columns, effectively transposing the original dataframe
print dframe_unst

# How stack and unstack handles null values
ser1 = Series([0,1,2],index=['Q','X','Y'])
ser2 = Series([4,5,6],index=['X','Y','Z'])
print ser1
print ser2
dframe = pd.concat([ser1,ser2],keys=['Alpha','Beta'])
print dframe
print dframe.unstack()  # Get NaN values when we stack
print dframe.unstack().stack()  # Stacking them again gets rid of NaN values. Can use dropna=False argument to keep NaNs
