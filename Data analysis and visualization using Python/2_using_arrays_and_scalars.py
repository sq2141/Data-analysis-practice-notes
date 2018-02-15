from __future__ import division
import numpy as np

# in python 2.7, division returns an INTEGER
a = 5/2
print(a)

# if you add a decimal point in either number, division returns a FLOAT
b = 5./2
print(b)

# if you import division from __future__, division automatically returns a FLOAT
c = 5/2
print(c)

# create a 2x4 array
arr1 = np.array([[1, 2, 3, 4], [8, 9, 10, 11]])  # square brackets around each row AND around the entire array
print(arr1)

# multiplying arrays multiply the individual cells
print(arr1*arr1)

# subtracting arrays
print(arr1-arr1)

# scalar operations with arrays
print(1/arr1)

# exponential operations
print(arr1**3)