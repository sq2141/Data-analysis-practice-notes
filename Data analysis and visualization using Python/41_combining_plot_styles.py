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

dataset = randn(100)

# Distplot allows combining of plots
sns.distplot(dataset,bins=25)  # by default, it combines a KDE with a histogram

# Different type sof plots can be turned on and off as distplot arguments
plt.figure()
sns.distplot(dataset,bins=25,rug=True,hist=False)

# Control properties of specific plots within distplot
plt.figure()
sns.distplot(dataset,bins=25,
             kde_kws={'color':'indianred','label':'KDE plot'},
             hist_kws={'color':'blue','label':'Histogram','alpha':0.3})

# PS. Seaborn can take inputs in the form of Pandas types (series, dataframes)

plt.show()
