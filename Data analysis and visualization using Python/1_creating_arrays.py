'''
Creating arrays
'''

import numpy as np


# create space
def s():
    print


# create two lists
list1 = [1, 2, 3]
list2 = [11, 22, 33]

# create a list of lists
lists = [list1, list2]

# create an array from list of lists
my_array = np.array(lists)

# print out array and properties
print(my_array)
print(my_array.shape)
print(my_array.dtype)

# create an array of zeros
my_zero_array = np.zeros([2, 4])
print(my_zero_array)

# create and empty array
empt_arr = np.empty([3, 3])
print(empt_arr)

# create an identity matrix
my_i_matrix = np.eye(5)
print(my_i_matrix)

# create an array filled with a range of numbers
arr2 = np.arange(5, 50, 2)
print(arr2)
