import numpy as np
import pandas as pd
from pandas import Series, DataFrame

'''
Pivot tables

- Pivot tables collapse repeated labels in a certain category to sum values per category

'''

# Just loading the table. Don't have to know how
import pandas.util.testing as tm; tm.N = 3
def unpivot(frame):
    N, K = frame.shape

    data = {'value':frame.values.ravel('F'),
            'variable':np.asarray(frame.columns).repeat(N),
            'date':np.tile(np.asarray(frame.index),K)}

    return DataFrame(data, columns=['date','variable','value'])
dframe = unpivot(tm.makeTimeDataFrame())
print dframe

# Create pivot table
dframe_piv = dframe.pivot('date','variable','value')  # specify what you want for the rows, the columns, and what you want the fill value to be
print dframe_piv