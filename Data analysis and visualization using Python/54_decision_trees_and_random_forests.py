import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

from sklearn.datasets import make_blobs

# Generate 500x2 matrix with 4 labels to make clusters
X,y = make_blobs(n_samples=500,centers=4,random_state=8,cluster_std=2.4)
print X
print y
plt.figure(figsize=(6,6))
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap='jet') # X is coordinates, y is color label


# Visualization function (copied from iPython notebook)
from sklearn.tree import DecisionTreeClassifier
def visualize_tree(classifier, X, y, boundaries=True,xlim=None, ylim=None):
    '''
    Visualizes a Decision Tree.
    INPUTS: Classifier Model, X, y, optional x/y limits.
    OUTPUTS: Meshgrid visualization for boundaries of the Decision Tree
    '''

    # Fit the X and y data to the tree
    classifier.fit(X, y)


    # Automatically set the x and y limits to the data (+/- 0.1)
    if xlim is None:
        xlim = (X[:, 0].min() - 0.1, X[:, 0].max() + 0.1)
    if ylim is None:
        ylim = (X[:, 1].min() - 0.1, X[:, 1].max() + 0.1)

    # Assign the variables
    x_min, x_max = xlim
    y_min, y_max = ylim


    # Create a mesh grid
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))

    # Define the Z by the predictions (this will color in the mesh grid)
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])

    # Reshape based on meshgrid
    Z = Z.reshape(xx.shape)

    # Plot the figure (use)
    plt.figure(figsize=(10,10))
    plt.pcolormesh(xx, yy, Z, alpha=0.2, cmap='jet')


    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='jet')

    #Set Limits
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    def plot_boundaries(i, xlim, ylim):
        '''
        Plots the Decision Boundaries
        '''
        if i < 0:
            return

        # Shorter variable name
        tree = classifier.tree_

        # Recursively go through nodes of tree to plot boundaries.
        if tree.feature[i] == 0:
            plt.plot([tree.threshold[i], tree.threshold[i]], ylim, '-k')
            plot_boundaries(tree.children_left[i],
                            [xlim[0], tree.threshold[i]], ylim)
            plot_boundaries(tree.children_right[i],
                            [tree.threshold[i], xlim[1]], ylim)

        elif tree.feature[i] == 1:
            plt.plot(xlim, [tree.threshold[i], tree.threshold[i]], '-k')
            plot_boundaries(tree.children_left[i], xlim,
                            [ylim[0], tree.threshold[i]])
            plot_boundaries(tree.children_right[i], xlim,
                            [tree.threshold[i], ylim[1]])

    # Random Forest vs Single Tree
    if boundaries:
        plot_boundaries(0, plt.xlim(), plt.ylim())


clf = DecisionTreeClassifier(max_depth=2,random_state=0)  # More depth fit better, but may overfit
visualize_tree(clf,X,y)


# To get past overfitting, use ensemble method (such as a random forest)

# Use scikitlearn to make a random forest
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100,random_state=0)  # n_estimators is the number of decision trees
visualize_tree(clf,X,y,boundaries=False)

'''
Random forest for regression
'''

# Generate some data for regression

x = 10 * np.random.rand(100)

def sin_model(x,sigma=0.2):
    noise = sigma * np.random.rand((len(x)))
    return np.sin(5*x) + np.sin(0.5*x) + noise

y = sin_model(x)

plt.figure()
plt.errorbar(x,y,0.1,fmt='o')

# Random Forest Regression
from sklearn.ensemble import RandomForestRegressor
xfit = np.linspace(0,10,1000)
rfr = RandomForestRegressor(100)

rfr.fit(x[:,None],y)
yfit = rfr.predict(xfit[:,None])
ytrue = sin_model(xfit,0)

plt.figure()
plt.errorbar(x,y,0.1,fmt='o')
plt.plot(xfit,yfit,'-r')
plt.plot(xfit,ytrue, '-k',alpha=0.5)


plt.show()