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

'''
Boxplots
'''
data1 = randn(100)
data2 = randn(100)
sns.boxplot(data=[data1,data2])


'''
Violin plot (combines boxplot with KDE plot)
'''

# Examples of boxplot not showing the whole picture
# Norm dist
data3 = stats.norm(0,5).rvs(100)
# Two gamma dist. concatenated together
data4 = np.concatenate([stats.gamma(5).rvs(50)-1,
                        -1*stats.gamma(5).rvs(50)])

# Box plot both data3 and data4
plt.figure()
sns.boxplot(data=[data3,data4])
# These look similar as boxplots, but violin plot reveals underlying difference

plt.figure()
sns.violinplot(data=[data3,data4])


plt.show()