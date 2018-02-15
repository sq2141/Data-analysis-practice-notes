# Standard imports
import numpy as np
import pandas as pd
from numpy.random import randn

# Stats imports
from scipy import stats

# Plotting imports
import matplotlib as mlp
import matplotlib.pyplot as plt
import seaborn as sns

# Load one of seaborn's practice dataset
flight_dframe = sns.load_dataset('flights')
print flight_dframe.head()

# Pivot this dataframe (kind of like going from long table to wide table so it's easier to manage)
flight_dframe = flight_dframe.pivot('month','year','passengers')  # rows = month, column = year, cells fileld with passengers
print flight_dframe

# Create a heatmap
sns.heatmap(flight_dframe,center=flight_dframe.loc['January',1955])  # center specifies which location's value should map to the neutral color of the heatmap

# Put heatmap on a subplot
f,(ax1,ax2) = plt.subplots(2,1)
yearly_flights = flight_dframe.sum()
years = pd.Series(yearly_flights.index.values)  # To get things in the right format
years = pd.DataFrame(years)
flights = pd.Series(yearly_flights.values)
flights = pd.DataFrame(flights)
year_dframe = pd.concat((years,flights),axis=1)
year_dframe.columns = ['Year','Flights']
print year_dframe

sns.barplot(x='Year',y='Flights',data=year_dframe,ax=ax1)
sns.heatmap(flight_dframe,cmap='Blues',ax=ax2,cbar_kws={'orientation':'horizontal'})
plt.yticks(rotation=0)

# Clustered heatmaps put similar rows next to each other
sns.clustermap(flight_dframe)
sns.clustermap(flight_dframe,col_cluster=False)  # only cluster rows

# Standardize
sns.clustermap(flight_dframe,standard_scale=1)  # standardize by the columns/year
sns.clustermap(flight_dframe,standard_scale=0)  # standardize by the rows/month
sns.clustermap(flight_dframe,z_score=1)  # standardize by z-score

plt.show()