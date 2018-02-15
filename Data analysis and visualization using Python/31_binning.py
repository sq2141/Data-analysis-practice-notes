import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# Use Cut function from Panda to bin items
years = [1990,1991,1992,2008,2012,2015,1987,1969,2013,2008,1999]
decade_bins = [1960,1970,1980,1990,2000,2010,2020]
decade_cat = pd.cut(years,decade_bins)  # cut years into decade_bins
print decade_cat
print decade_cat.categories
print pd.value_counts(decade_cat)

# Cut into X number of bins instead of predetermined bin intervals
cut_2 = pd.cut(years,2,precision=1)  # cut into 2 bins with 1 year precision
print pd.value_counts(cut_2)
