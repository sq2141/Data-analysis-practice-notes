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

# Create a random normal distribution dataset and histogram plot it
dataset1 = randn(100)
plt.hist(dataset1)

# Create and plot another dataset
dataset2 = randn(80)
plt.figure()
plt.hist(dataset2,color='indianred')

# Plot both datasets on one figure
fig = plt.figure()
plt.hist(dataset1,normed=True,color='indianred',alpha=0.5,bins=20)  #alpha is transparency.
plt.hist(dataset2,normed=True,alpha=0.5,bins=20)  # normed normalizes so the frequency of each dataset adds up to 1

# Using seaborn to make a joint plot
data1 = randn(1000)
data2 = randn(1000)
sns.jointplot(data1,data2)

# Show all figures
plt.show()