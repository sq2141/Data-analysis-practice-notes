import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# Create the dataframe
animals = DataFrame(np.arange(16).reshape(4,4),
                    columns = ['W','X','Y','Z'],
                    index = ['dog','cat','bird','mouse'])
print animals
animals.ix[1:2,['W','Y']] = np.nan
print animals

# Map columns to behaviors then groupby column names
behavior_map = {'W':'good','X':'bad','Y':'good','Z':'bad'}  # relating each column to a good or bad behavior
animal_col = animals.groupby(behavior_map,axis=1)
print animal_col.sum()  # show group sum according to the groupby

# Groupby on Series
behav_series = Series(behavior_map)
print behav_series
animal_col2 = animals.groupby(behav_series,axis=1).count() # count the instances in which animals appeared in the good and bad columns
print animal_col2

# Groupby the length of the animal's name
animal_col3 = animals.groupby(len).sum()  #sum means after grouping, what value you want to show. in this case, sum
print animal_col3

# Groupby 2 things
keys = ['A','B','A','B']
animal_col4 = animals.groupby([len,keys]).max()
print animal_col4

# Groupby with index hierarchy
hier_col = pd.MultiIndex.from_arrays([['NY','NY','NY','SF','SF'],[1,2,3,1,2]],names=['City','sub_value'])
print hier_col
dframe_hr = DataFrame(np.arange(25).reshape(5,5),columns=hier_col)
dframe_hr = dframe_hr * 100
print dframe_hr