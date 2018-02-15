import numpy as np

arr = np.arange(0, 11)

# access array index with square brackets
print(arr)
print(arr[8])

# accessing a range in an array with [x: y], starting at x and stopping BEFORE y
print(arr[1:5])

# assigning values to cells in an array
arr[0:5] = 100
print(arr)

# taking a slice of an array
arr = np.arange(0, 11)
print(arr)
slice_of_arr = arr[0:6]
print(slice_of_arr)

# setting all values in slice of array to 99
slice_of_arr[:] = 99
print(slice_of_arr)
print(arr)  # notice that the original array was changed when we changed the slice. This is because when we take an array slice, numpy doesn't create a new copy of it

# to create a copy of an array, we have to state that explicitly
arr_copy = arr.copy()
arr_copy[0: 3] = 100
print(arr)
print(arr_copy)

# indexing in a 2-D array.
# Creating 2-d arrays: put values in square brackets that are separated by comma. Everything inside a pair of braces
arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))
print(arr_2d)

# get a specific row from a 2-d matrix
print(arr_2d[1])  # this prints the 2nd row, because row indices start at zero

# get a specific cell from a 2-d matrix
print(arr_2d[1, 2])

# 2-d array slicing
print(arr_2d[:2, 1:])

# fancy indexing
arr2d = np.zeros((10, 10))
print(arr2d)
arrLen = arr2d.shape[1]
print(arrLen)

for i in range(arrLen):
    arr2d[i] = i
print(arr2d)

# get entire rows with by adding another square bracket around row numbers
print(arr2d[[2, 4, 5]])
