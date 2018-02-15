import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Replacing values in series
ser1 = Series([1,2,3,4,1,2,3,4])
print ser1
print ser1.replace(1,np.nan)  # select the value you want to replace and then the new value to be replaced with

# Multiple replaces at once
print ser1.replace([1,4],[100,400])

