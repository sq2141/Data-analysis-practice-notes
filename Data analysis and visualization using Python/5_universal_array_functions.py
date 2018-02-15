import numpy as np

arr = np.arange(11)

# universal functions can be applied to any value in an array
arrSqrt = np.sqrt(arr)
arrExp = np.exp(arr)


# binary functions (functions that use 2 arrays)
A = np.random.randn(10)
B = np.random.randn(10)

arrSum = np.add(A, B)
arrMax = np.maximum(A, B)


print arrMax