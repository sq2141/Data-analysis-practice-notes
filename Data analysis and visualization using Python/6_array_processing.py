import numpy as np
import matplotlib.pyplot as plt


# Create meshgrid
points = np.arange(-5, 5, 0.01)
dx, dy = np.meshgrid(points, points)
z = (np.sin(dx) + np.sin(dy))

# Plotting using matplotlib.pyplot
plt.imshow(z)
plt.title('Plot for sin(x)+sin(y)')
plt.colorbar()
plt.draw()

# numpy where, long way of doing things
A = np.array([1, 2, 3, 4])
B = np.array([100, 200, 300, 400])
condition = np.array([True,True,False,False])  # create a boolean array
answer = [(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)]
print answer

answer2 = np.where(condition,A,B)  # numpy where is a short way of doing the above
print answer2

# conditional re-assignment using numpy where
from numpy.random import randn
arr = randn(5,5)
answer3 = np.where(arr<0,0,arr) # if arr values less than 0, change to 0, else keep current arr value
print answer3

# get stats of arrays
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print arr
print arr.sum()
print arr.sum(0)  # sum along the columns
print arr.mean()
print arr.std()
print arr.var()

# test conditions in boolean arrays
bool_arr = np.array([True,False,True])
print bool_arr.any()  # returns a boolean (true or false) if ANY value in the array was true
print bool_arr.all()  # returns a boolean (true or false) if ALL values in the array was true

# sort arrays
arr = randn(5)
print arr
arr.sort()
print arr

# get array with unique values (i.e. gets rid of duplicates)
countries = np.array(['France','Germany','China','USA','Russia','USA'])
print np.unique(countries)

# if elements in one array appear in a second array (like python keyword in, but can query multiple elements(arrays))
print np.in1d(['France','USA','Australia'],countries)

