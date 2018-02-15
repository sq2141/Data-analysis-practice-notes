import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Split, Apply, Combine means groupbying/collapsing data into groups, applying some function/manipulation, then putting the data back together

# Use same wine dataset as last exercise
dframe_wine = pd.read_csv('winequality-red.csv',sep=';')
print dframe_wine.head()

# What if we wanted to sort by highest alcohol content (continuous var) but also see the rank of the alcoholic content within quality groups

# First step sort dataframe by descending alcoholic content
dframe_wine.sort('alcohol',ascending = False,inplace=True)  # inplace means the effect takes place on the dframe_wine dataset
print dframe_wine

# Second, group by the quality range (integers), and apply the ranker function
def ranker(df):
    df['alc_content_rank'] = np.arange(len(df)) + 1
    return df

dframe_wine = dframe_wine.groupby('quality').apply(ranker)
print dframe_wine.head()

# Now if we wanted to see the highest alcoholic content wine for each quality group, call the dataframe where the alc_content_rank = 1
print dframe_wine[dframe_wine.alc_content_rank==1]

# If we wanted to see how many wines belong to each quality rating
print dframe_wine['quality'].value_counts()