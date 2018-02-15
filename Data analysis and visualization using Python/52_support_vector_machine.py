import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets

# Import iris dataset
iris = datasets.load_iris()

X = iris.data
Y = iris.target

from sklearn.svm import SVC  # support vector classification

# Train/Test Split
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y)

# Fit model
model = SVC()
model.fit(X_train, Y_train)

# Check accuracy
from sklearn import metrics
Y_pred = model.predict(X_test)
# print metrics.accuracy_score(Y_test,Y_pred)

'''
Four different SVM models
'''

from sklearn import svm
X = iris.data[:,:2]
Y = iris.target

C = 1.0

svc = svm.SVC(kernel='linear',C=C).fit(X,Y)
rbf_svc = svm.SVC(kernel='rbf',gamma=0.7,C=C).fit(X,Y)
poly_svc = svm.SVC(kernel='poly',degree=3,C=C).fit(X,Y)
lin_svc = svm.LinearSVC(C=C).fit(X,Y)

h = 0.02

x_min = X[:,0].min() - 1
x_max = X[:,0].max() + 1
y_min = X[:,1].min() - 1
y_max = X[:,1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))

titles = ['SVC with linear kernel',
          'Linear SVC (linear kernel)',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel']

plt.figure()
for i,clf in enumerate((svc,lin_svc,rbf_svc,poly_svc)):
    plt.subplot(2,2,i+1)
    plt.subplots_adjust(wspace=0.4,hspace=0.4)
    Z = clf.predict(np.c_[xx.ravel(),yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx,yy,Z,cmp=plt.cm.terrain,alpha=0.5, linewidth = 0)
    plt.scatter(X[:,0],X[:,1],c=Y,cmap=plt.cm.Dark2)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(),xx.max())
    plt.ylim(yy.min(),yy.max())
    plt.title(titles[i])



plt.show()