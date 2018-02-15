import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Rename index with map (mapping is like transforming)
dframe = DataFrame(np.arange(12).reshape(3,4),
                   index=['NY','LA','SF'],
                   columns=['A','B','C','D'])
print dframe
print dframe.index.map(str.lower)
dframe.index = dframe.index.map(str.lower)
print dframe

# Another way to rename
print dframe.rename(index=str.title,columns=str.lower)  #str.title capitalizes the first letter

# Rename using dictionary
print dframe.rename(index={'ny':'New York'}, columns={'A':'ALPHA'})