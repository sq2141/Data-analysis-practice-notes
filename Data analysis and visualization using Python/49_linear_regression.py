import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# Get data
from sklearn.datasets import load_boston
boston = load_boston()
print boston.DESCR # DESCR is specific to this toy training set

# Histogram of the label (or target, the value you want your model to predict)
plt.hist(boston.target,bins=50)  # .target is specific to this toy training dataset
plt.xlabel('Prices in thousands')
plt.ylabel('Number of houses')

# Visualize one variable (potential predictor) and the label with a scatterplot
plt.figure()
plt.scatter(boston.data[:,5],boston.target)
plt.xlabel('Number of rooms')
plt.ylabel('Prices in thousands')

# Import data into a pandas dataframe using the training dataset's specific methods
boston_df = DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df['Price'] = boston.target
print boston_df.head()

# Using seaborn's linearplot (lmplot) to automatically get a scatterplot and a fit
sns.lmplot('RM','Price',data=boston_df)

# Univariate linear regression 'manually' using numpy
# Constructing X and Y arrays
X = boston_df['RM'] # but this doesnt work because...
print X.head()
print X.shape
X = np.vstack(boston_df.RM) # although X was already an n-by-1 column, numpy needs it in a specific n-by-1 column format, which is what vstack doess
print X[0:5]
print X.shape

# Add a second column of all 1's to X (the constant term)
X = np.array([[value,1] for value in X])
print X[0:5]

Y = boston_df['Price']

# Get 1st order and constant weights as m and b
m,b = np.linalg.lstsq(X,Y)[0]

# Plot
plt.figure()
plt.plot(boston_df.RM,boston_df.Price,'o')  # Plot the datapoints

x = boston_df.RM
plt.plot(x,m*x+b,'r',label='Best Fit Line')

# Get the total error
result = np.linalg.lstsq(X,Y)
error_total = result[1]  # sum of squared error
rmse = np.sqrt(error_total/len(X))  # root mean square error, which is approximately the standard deviation
print rmse  # therefore, the price of the house won't wary more than two times the rmse 95% of the time

# Multivariate regression using scikit learn
import sklearn
from sklearn.linear_model import LinearRegression

# Set up data columns
lreg = LinearRegression()  # set up a linear regression object
X_multi = boston_df.drop('Price',axis=1)
Y_target = boston_df.Price

# Regression
lreg.fit(X_multi,Y_target)

# See coefficients (after putting them into a dataframe)
coeff_df = DataFrame(boston_df.columns)
coeff_df.columns = ['Features']

coeff_df['Coefficient Estimate'] = Series(lreg.coef_)

print coeff_df
print ('The number of coefficients used was %d ' %len(lreg.coef_))
print ('The estimated intercept coefficient is %.2f ' %lreg.intercept_)

# Using training and validation
X_train,X_test,Y_train,Y_test = sklearn.cross_validation.train_test_split(X_multi,boston_df.Price)
print X_train.shape, X_test.shape, Y_train.shape, Y_test.shape  # 75/25 Train/Test split

# Train
lreg = LinearRegression()
lreg.fit(X_train,Y_train)

# Validate that the error is not that different between predicted tested and predicted trained
pred_train = lreg.predict(X_train)
pred_test = lreg.predict(X_test)

print ('Fit a model X_train, and calculate the MSE with Y_train: %.2f' %np.mean((Y_train-pred_train)**2))
print ('Fit a model X_train, and calculate the MSE with X_test and Y_test: %.2f' %np.mean((Y_test-pred_test)**2))

# Residual plot
plt.figure()
train = plt.scatter(pred_train,(pred_train - Y_train),c='b',alpha=0.5)
test = plt.scatter(pred_test,(pred_test - Y_test),c='r',alpha=0.5)
plt.hlines(y=0,xmin=-20,xmax=50)

plt.show()