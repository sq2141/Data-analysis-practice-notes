import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Adding columns to dataframes using mapping
dframe = DataFrame({'city':['Alma','Brian Head','Fox Park'],
                    'altitude':[3158, 3000,2762]})
print dframe

state_map = {'Alma':'Colorado','Brian Head':'Utah', 'Fox Park':'Wyoming'}
dframe['state'] = dframe['city'].map(state_map)
print dframe
