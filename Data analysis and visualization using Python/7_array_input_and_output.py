import numpy as np


# Saving numpy arrays
arr = np.arange(10)
print arr
np.save('myarray',arr)
del arr

arr = np.load('myarray.npy')
print arr


# Saving multiple arrays
arr1 = np.arange(3)
arr2 = np.arange(6)
np.savez('multiarray.npz', x=arr1, y=arr2)  # save as x and y in ziparray.npz

arrs = np.load('multiarray.npz')
print arrs['x']  # read out the x array
print arrs['y']  # read out the y array


# Saving number array as text files
arr = np.array ([[1,2,3],[4,5,6]])
np.savetxt('mytextarray.txt',arr,delimiter=',')

arr = np.loadtxt('mytextarray.txt',delimiter=',')
print arr

