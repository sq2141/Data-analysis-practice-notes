import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris
from sklearn import metrics

# Load data
iris = load_iris()
X = iris.data
Y = iris.target
print iris.DESCR

iris_data = DataFrame(X,columns=['Sepal Length','Sepal Width','Petal Length','Petal Width'])
iris_target = DataFrame(Y,columns=['Species'])
iris_target = iris_target.Species.map({0:'Setosa',1:'Versicolour',2:'Virginica'})
iris = pd.concat([iris_data,iris_target],axis=1)
print iris.head()

# Initial visualization
sns.pairplot(data=iris,hue='Species',size=2)
sns.factorplot(x='Petal Length',data=iris,hue='Species',kind='count')

# Train/Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.4,random_state=3)  # 40% of data for testing, use 3 for seed

# Multiclass logistic regression using one-vs-all method
# Fit
logreg = LogisticRegression()
logreg.fit(X_train,Y_train)
# Predict
Y_pred = logreg.predict(X_test)
# Check accuracy
print metrics.accuracy_score(Y_test,Y_pred)

# Multiclass logistic regression using k neighbours
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 6)

knn.fit(X_train,Y_train)

y_pred = knn.predict(X_test)
print metrics.accuracy_score(Y_test,Y_pred)

# Test a range of k's
k_range = range(1,86) # integers starting at 1 and stopping before 21

accuracy = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train,Y_train)
    Y_pred = knn.predict(X_test)
    accuracy.append(metrics.accuracy_score(Y_test,Y_pred))
    print Y_pred
    print metrics.accuracy_score(Y_test,Y_pred)

plt.figure()
plt.plot(k_range,accuracy,marker='o',markerfacecolor='r')
plt.xlabel('K value')
plt.ylabel('Accuracy')
plt.ylim(0,1)




plt.show()