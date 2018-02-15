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
Start with making a kd plot manually
'''

# Plotting a dataset as ticks
dataset = randn(25)
sns.rugplot(dataset)
# plt.ylim(0,1)

# Plotting a dataset as histogram
plt.hist(dataset,alpha=0.5)

# Manually generating gaussian fits to ticks to get kernels
plt.figure()
sns.rugplot(dataset)
x_min = dataset.min() - 2
x_max = dataset.max() + 2
x_axis = np.linspace(x_min,x_max,100)
bandwidth = ((4*dataset.std()**5)/(3*len(dataset))) ** 0.2  # equation for estimating bandwidth
kernel_list = []
for datapoint in dataset:

    # Create a kernel for each point and append it to the kernel_list
    kernel = stats.norm(datapoint,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)

    # Scale for plotting
    kernel = kernel / kernel.max()  # Normalizes everything by the max
    kernel = kernel * 0.4  # Set peak to 0.4

    plt.plot(x_axis,kernel,color='grey',alpha=0.5)

plt.ylim(0,1)
# To get the kernel density plot, sum the individual kernels
sum_kde = np.sum(kernel_list,axis=0)
fig = plt.figure()
plt.plot(x_axis,sum_kde,color='indianred')
sns.rugplot(dataset)
plt.yticks([])  # get rid of y tick marks
plt.suptitle('Sum of the basis functions')

'''
Generating kernel density estimation plots in one step using seaborn
'''
# KDE plot using seaborn
plt.figure()
sns.kdeplot(dataset)

# Changing the bandwidth from seaborn's default (trying several). If the bandwidth (width of the individual kernels) is wide, then the KDE is smoothened and less sensitive to high frequency changes
plt.figure()
for bw in np.arange(0.5,2,0.25):
    sns.kdeplot(dataset,bw=bw,lw=1.8,label=bw)

# Changing the type of kernel (trying several)
plt.figure()
kernel_options = ['biw','cos','epa','gau','tri']

for type in kernel_options:
    sns.kdeplot(dataset,kernel=type,label=type)

'''
Cumulative density function plot
'''
plt.figure()
sns.kdeplot(dataset,cumulative=True)

'''
KDE for Multi-dimensional data
'''
mean = [0,0]
cov = [[1,0],[0,100]]

plt.figure()
dataset2 = np.random.multivariate_normal(mean,cov,1000)  # Draws samples from a multivariate random distribution
dframe = pd.DataFrame(dataset2,columns=['X','Y'])
sns.kdeplot(dframe)  # Using seaborn on pandas dataframe

plt.figure()
sns.kdeplot(dframe.X,dframe.Y,shade=True,cmap='Blues')  # Can pass two vectors separately, also shade

print dframe

# Show plots
plt.show()