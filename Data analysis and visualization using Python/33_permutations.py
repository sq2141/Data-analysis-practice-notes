import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Create a permutation of dataframe
dframe = DataFrame(np.arange(16).reshape(4,4))
print dframe
blender = np.random.permutation(4)  #blender creates a random permutation of 0 1 2 3
print blender
print dframe.take(blender)  # From the dataframe, take index (rows) in the order that is in blender

# Permutation with replacement
box = np.array([1,2,3])
shaker = np.random.randint(0,len(box),size=10)  # randint picks from 0 to len(box) with replacement 10 times
print shaker
hand_grab = box.take(shaker)  # take box values in the order of shaker