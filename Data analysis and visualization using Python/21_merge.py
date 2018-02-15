import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Create 2 dataframes
dframe1 = DataFrame({'key':['X','Y','Z','Z','X','X'], 'data_set_1':np.arange(6)})
print dframe1
dframe2 = DataFrame({'key':['Q','Y','Z'],'data_set_2':[1,2,3]})
print dframe2

# Merge
merged = pd.merge(dframe1,dframe2)
print merged
print pd.merge(dframe1,dframe2,on='key')  #which column to merge on
print pd.merge(dframe1,dframe2,on='key',how='left')
print pd.merge(dframe1,dframe2,on='key',how='right')
print pd.merge(dframe1,dframe2,on='key',how='outer')

# Many-to-many merge
dframe3 = DataFrame({'key':['X','X','X','Y','Z','Z'], 'data_set_3':range(6)})
print dframe3
dframe4 = DataFrame({'key':['Y','Y','X','X','Z'], 'data_set_4':range(5)})
print dframe4
print pd.merge(dframe3,dframe4)

# Multiple keys
df_left = DataFrame({'key1':['SF','SF','LA'],
                     'key2':['one','two','three'],
                     'left_data':[10,20,30]})
df_right = DataFrame({'key1':['SF','SF','LA','LA'],
                      'key2':['one','one','one','two'],
                      'right_data':[40,50,60,70]})
print df_left
print df_right
print pd.merge(df_left,df_right,on=['key1','key2'],how='outer')