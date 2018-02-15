import numpy as np
import pandas as pd
from pandas import Series, DataFrame

'''
Data alignment means adding/combining two series together, two dataframes together, or a series with a dataframe
'''


# Adding/combining series
ser1 = Series([0,1,2], index=['A','B','C'])
print ser1
ser2 = Series([3,4,5,6], index=['A','B','C','D'])
print ser2
# When we add 2 series, they sum according to the index labels. If there index label is missing from one of the series, returns NaN
print ser1+ser2


# Adding/combining dataframes
dframe1 = DataFrame(np.arange(4).reshape(2,2),columns=list('AB'),index=['NYC','LA'])
print dframe1
dframe2 = DataFrame(np.arange(9).reshape(3,3),columns=list('ADC'),index=['NYC','LA','DC'])
print dframe2
print dframe1 + dframe2  # Only 2 cells are successfully added because those were the only entries where the rows and columns from the two dataframes matched up


# Adding using .add with fill_value=0 will add even if one dataframe doesn't have those labels, instead of returning NaN
# This is important for adding different sized dataframes, but don't want to lose all your data to Null/NaN values
print dframe1.add(dframe2,fill_value=0)

# Adding series to dataframe
ser3 = dframe2.ix[0]
print ser3
print dframe2-ser3