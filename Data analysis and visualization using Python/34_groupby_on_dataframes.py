import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Group by values in one column
dframe = DataFrame({'k1':['X','X','Y','Y','Z'],
                    'k2':['alpha','beta','alpha','beta','alpha'],
                    'dataset1':np.random.randn(5),
                    'dataset2':np.random.randn(5)})
print dframe

group1 = dframe['dataset1'].groupby(dframe['k1'])
print group1
group1.mean()

# Group by lists
cities = np.array(['NY','LA','LA','NY','NY'])
month = np.array(['JAN','FEB','JAN','FEB','JAN'])
print dframe['dataset1'].groupby([cities,month]).mean()

# Group by values in multiple columns
print dframe.groupby(['k1','k2']).mean()

# Group by to get size
print dframe.groupby(['k1']).size()  # Get number values in each group

# Group by and loop
for name,group in dframe.groupby('k1'):
    print "This is the %s group" %name
    print group
    print '\n'

for (k1,k2), group in dframe.groupby(['k1','k2']):
    print "Key1 = %s, Key2 = %s" % (k1,k2)
    print group
    print '\n'

# Create a dictionary of the data
group_dict = dict(list(dframe.groupby('k1')))
print group_dict['X']

group_dict_axis1 = dict(list(dframe.groupby(dframe.dtypes,axis=1)))  # separate data by the data type
print group_dict_axis1


# Groupby columns
dataset2_group = dframe.groupby(['k1','k2'])[['dataset2']]
print dataset2_group.mean()