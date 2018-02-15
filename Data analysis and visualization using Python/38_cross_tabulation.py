import pandas as pd
from StringIO import StringIO

# Cross Tabulation is a special case of pivot tables. It is just a frequency table

# Creating some data (don't need to know)
data = """\
Sample Animal Intelligence
1 Dog Smart
2 Dog Smart
3 Cat Dumb
4 Cat Dumb
5 Dog Dumb
6 Cat Smart"""

dframe = pd.read_table(StringIO(data),sep='\s+')
print dframe

print pd.crosstab(dframe.Animal,dframe.Intelligence,margins=True)