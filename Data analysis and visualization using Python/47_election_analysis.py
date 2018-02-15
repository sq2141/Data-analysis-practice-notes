from __future__ import division
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

import requests
from StringIO import StringIO

sns.set_style('whitegrid')
sns.set_context('poster')

'''
Questions:
1) Who was being polled and what was their party affiliation?
2) Did the poll results favor Romney or Obama?
3) How do undecided voters affect the poll?
4) Can we account for the undecided voters?
5) How did voter sentiment change over time?
6) Can we see an effect in the polls from the debate?
'''

# Read election poll dataset into a pandas dataset
url='http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv'
source = requests.get(url).text
poll_data = StringIO(source)
poll_df = pd.read_csv(poll_data)
print poll_df.head()

# Who was being polled? (bargraph/factorplot)
sns.factorplot(x='Affiliation',kind='count',data=poll_df,order=(['Dem','None','Rep']),hue='Population',size=6,aspect=2)

# What was the mean and stdev
avg = poll_df[['Obama','Romney','Undecided']].mean()
std = poll_df[['Obama','Romney','Undecided']].std()

plt.figure()
avg.plot(kind='bar',yerr=std,legend=False,color='indianred')

# Concatenating dataframes using pd.concat
poll_avg = pd.concat([avg,std],axis=1)
poll_avg.columns = ['Average','STD']
print poll_avg.head()

# Time series
poll_df.sort_values(by='End Date').plot(x='End Date',y=['Obama','Romney','Undecided'],linestyle='',marker='o',markersize='10')

# Definte a new column to calculate the difference b/w Obama and Romney
poll_df['Difference'] = (poll_df.Obama-poll_df.Romney)/100
print poll_df.head()

# Groupby to collapse polls starting on the same date, reducing the data to the mean of the collapsed data
poll_df = poll_df.groupby(['Start Date'],as_index=False).mean()  # as_index keeps current index, instead of using start date as index
print poll_df.head()
poll_df.sort_values(by='Start Date').plot(x='Start Date',y='Difference',xlim=(329,356))

# Adding vertical lines to indicate dates on which debates happened
plt.axvline(x=329+2,color='grey')
plt.axvline(x=329+10,color='grey')
plt.axvline(x=329+21,color='grey')

plt.show()