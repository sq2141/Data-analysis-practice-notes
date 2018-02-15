import numpy as np

# taking the transpose of a matrix
arr = np.arange(50).reshape((10, 5))
arrT = arr.T

# taking the dot product
dotProduct = np.dot(arr.T, arr)

# creating 3-d arrays
arr3d = np.arange(50).reshape((5, 5, 2))  # 5 layers of 5x2 matrices

# transpose a 3-d matrix and swap axes

print(arr3d)
