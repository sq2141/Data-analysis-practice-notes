import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

# Sort by index
ser1 = Series(range(3),index=['C','A','B'])
print ser1
print ser1.sort_index()

# Sort by value
print ser1.order()

# Rank
ser2 = Series(randn(10))
print ser2
print ser2.rank()  # Get the rank without actually sorting
print ser2.order()  # Sort

