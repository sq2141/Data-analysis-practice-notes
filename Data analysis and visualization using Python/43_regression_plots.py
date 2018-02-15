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


# Scatter plot with regression line
tips = sns.load_dataset('tips')
print tips.head()
sns.lmplot('total_bill','tip',tips,order=4,  # order means nth degree polynomial fit
           scatter_kws={'marker':'o','color':'indianred'},  # input additional arguments as a dictionary and separately adjust each plot
           line_kws={'linewidth':1,'color':'blue'})

# Scatter plot alone
sns.lmplot('total_bill','tip',tips,fit_reg=False)

# Scatter plot with discrete x-values
tips['tip_percent']=100*(tips['tip']/tips['total_bill'])  # create a new column to calculate % tip
print tips.head()
sns.lmplot('size','tip_percent',tips,x_jitter=.1,hue='sex',markers=['x','o'],palette={'Male':'royalblue','Female':'indianred'})  # size of party vs. % tip given

# Ask if the day makes a difference in tips given
sns.lmplot('total_bill','tip_percent',tips,hue='day')

# Local regression (don't worry too much about this)
sns.lmplot('total_bill','tip_percent',tips,lowess=True,line_kws={'color':'black'})

# lmplot is actually using a lower level function called regplot. Take a look at regplot
plt.figure()
sns.regplot('total_bill','tip_percent',tips)

#
fig, (ax1,ax2) = plt.subplots(1,2,sharey=True)
sns.regplot('total_bill','tip_percent',tips,ax=ax1)
sns.violinplot(data=tips.sort_values(by='size'),y='tip_percent',x='size',palette='Reds_r',ax=ax2)

plt.show()