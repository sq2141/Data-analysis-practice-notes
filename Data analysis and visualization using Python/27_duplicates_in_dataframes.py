import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# Find duplicates
dframe = DataFrame({'key1':['A']*2 + ['B']*3,
                    'key2': [2,2,2,3,3] })
print dframe
print dframe.duplicated()

# Drop duplicates
print dframe.drop_duplicates()

# Drop duplicates specifically in one column
print dframe.drop_duplicates(['key1'])