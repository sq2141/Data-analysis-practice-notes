'''
Logistic regression

- Logistic regression means regressing onto categorical variables (i.e. classifying a data set)
- This tutorial practices binary classification (e.g. spam or not spam)

'''

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import math

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

import statsmodels.api as sm

# Import data using statsmodels practice dataset
df = sm.datasets.fair.load_pandas().data

# Create a new column for labeling case as having had an affair or not
def affair_check(x):
    if x != 0:
        return 1
    else:
        return 0

df['Had_Affair'] = df['affairs'].apply(affair_check)
print df.head()

# Groupby
print df.groupby('Had_Affair').mean()  # Remember for groupby objects, you have to also call an aggregate function (like sum, mean)

# Visualize
'''
sns.factorplot(x='age',data=df.sort_values(by='age'),hue='Had_Affair',kind='count',palette='coolwarm')
sns.factorplot(x='yrs_married',data=df.sort_values(by='yrs_married'),hue='Had_Affair',kind='count',palette='coolwarm')
sns.factorplot(x='children',data=df.sort_values(by='children'),hue='Had_Affair',kind='count',palette='coolwarm')
sns.factorplot(x='educ',data=df.sort_values(by='educ'),hue='Had_Affair',kind='count',palette='coolwarm')
'''

# Convert categorical variables into dummy variables
occ_dummies = pd.get_dummies(df['occupation'])
hus_occ_dummies = pd.get_dummies(df['occupation_husb'])
print occ_dummies.head()

occ_dummies.columns = ['occ1','occ2','occ3','occ4','occ5','occ6']
hus_occ_dummies.columns = ['hocc1','hocc2','hocc3','hocc4','hocc5','hocc6']

# Set up X and Y dataframes for logistic regression
X = df.drop(['occupation','occupation_husb','Had_Affair'],axis=1)
dummies = pd.concat([occ_dummies,hus_occ_dummies],axis=1)
X = pd.concat([X,dummies],axis=1)

'''
Multicollinearity consideration
- dummy variables are highly correlated
- one fix: drop for example occ1 and hocc1 (sacrifice one data point) to avoid collinearity
'''

X = X.drop(['occ1','hocc1','affairs'],axis=1)
print X.head()

Y = df.Had_Affair
Y = np.ravel(Y)  # flatten Y into proper format

# Model
log_model = LogisticRegression()
log_model.fit(X,Y)

print Y.mean()  # Proportion of women who have affairs: 32%
print log_model.score(X,Y)  # Accuracy rate of model: 72%
# Check the null error rate. If our model simply guessed 'no affair' we would have 68% accuracy.
# So while we are doing better than the null rate, we are not doing much better

# Check coefficients of model to see what variables are strong predictors
coeff_df = DataFrame(zip(X.columns,np.transpose(log_model.coef_)))
print coeff_df  # Positive coefficient means increase likelihood of having an affair

# Testing and training data set
X_train, X_test, Y_train, Y_test = train_test_split(X,Y)
log_model2 = LogisticRegression()
log_model2.fit(X_train,Y_train)

class_predict = log_model2.predict(X_test)
print metrics.accuracy_score(Y_test,class_predict)




plt.show()