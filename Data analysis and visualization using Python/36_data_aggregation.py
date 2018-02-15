import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

# Here we work with an actual dataset

# Data aggregation refers to operations that produces a scalar
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'
dframe_wine = pd.read_csv('winequality-red.csv',sep=';')  # load downloaded data sheet
print dframe_wine.head()

# Take a look at dimension of dataset
print dframe_wine.shape

# Take a look at the mean of a column
print dframe_wine['alcohol'].mean() # get the mean of just the alcohol content column

# Implement groupby on the wine dataset to see how subgroups within the dataset behave
wino = dframe_wine.groupby('quality')  # Group by the 'quality' column's value, which is an interger
print wino.describe()  # See descriptive stats on the grouped dataset

# Running a custom analysis on the dataset to get some scalar that we define
def max_to_min(arr):  # E.g. if we want to find the max - min difference within a groupby'd column
    return arr.max() - arr.min()

# To get an aggregate/scalar statistic on a dataset using a custom function:
print wino.agg(max_to_min)

# Can also pass strings
print wino.agg('mean')

# Adding a new column to the dataset, that comes from operation on existing columns
# Working off of the original dataset, see what's the relationship between alcoholic content and rating, so create a new column
dframe_wine['qual/alc ratio'] = dframe_wine['quality'] / dframe_wine['alcohol']
print dframe_wine

# Remember pivot tables is an alternative to groupby, so here we can use pivot table to group by values
print dframe_wine.pivot_table(index=['quality'])  # pivot on quality (same as group by quality)

# If we wanted to do some exploratory visualization
dframe_wine.plot(kind='scatter',x='quality',y='alcohol')

# Add plt.show() at the end to show the plot
plt.show()