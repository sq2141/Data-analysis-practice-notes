import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

'''
Excel file format

In excel, change data from wide to long form by:
- Pressing alt, d, p
- Multiple consolidation ranges
- I will create the page fields
- Select data range including labels
- Right click last cell of pivot table and click Show Details

'''

# Use panda to read excel file and store in dataframe
xlsfile = pd.ExcelFile('CAMPARI_data.xlsx')
dframe = xlsfile.parse('Sheet10')
# print dframe

# Use seaborn's boxplot to plot the dataframe
sns.set_style("ticks")  # style should be set before plot
sns.set_context("talk")
sns.boxplot(x='Condition',y='Fluorescence Ratio',hue='Segment',data=dframe)
sns.despine()  # modifications on style should be set after plot)

# Using seaborn's stripplot to show the datapoints
plt.figure()
sns.stripplot(x='Condition',y='Fluorescence Ratio',hue='Segment',data=dframe,size=8,edgecolor="gray")
sns.despine()

# Both on one graph, remove legend
fig, (ax1,ax2) = plt.subplots(1,2)
sns.set_style("ticks")  # style should be set before plot
sns.set_context("talk")
sns.boxplot(ax=ax1,x='Condition',y='Fluorescence Ratio',hue='Segment',data=dframe)
sns.stripplot(ax=ax2,x='Condition',y='Fluorescence Ratio',hue='Segment',data=dframe,size=8,edgecolor="gray")
sns.despine()
ax2.legend_.remove()


plt.show()