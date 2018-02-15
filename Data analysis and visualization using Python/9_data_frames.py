import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import webbrowser

'''
Dataframes can be thought of as spreadsheets
'''

# open browser to NFL record page
website='https://en.wikipedia.org/wiki/NFL_win%E2%80%93loss_records'
# webbrowser.open(website)

# I manually copied data from the webpage to clipboard. can now read from what I have copied on my clipboard
# nfl_frame = pd.read_clipboard()
nfl_frame = pd.read_excel('nfl.xlsx')  # or i can save it to an excel and read the excel file
print nfl_frame
print nfl_frame.head(3)  # To see the first X rows
print nfl_frame.tail(2)  # To see the last X rows
print nfl_frame.ix[3:4]  # Grab an index of rows

# Get column names
print nfl_frame.columns

# Get a column's row data
print nfl_frame.Team

# If a column name has more than one word in it (i.e. has a space), use square bracket like this
print nfl_frame['First Season']

# Grab a subset of columns
nfl_subset = DataFrame(nfl_frame,columns=['Team','First Season','Total Games'])
print nfl_subset

# Assign values to entire columns
nfl_frame['Stadium'] = "Levi's Stadium"
print nfl_frame

# Assign values to individual rows of a column
nfl_frame['Stadium'] = np.arange(5)
print nfl_frame

# Add a series to dataframe
stadiums = Series(["Ken's Stadium", "AT&T Stadium"], index = [4,0])
print stadiums
nfl_frame['Stadium'] = stadiums
print nfl_frame

# Deleting columns
del nfl_frame["Stadium"]

# Constructing dataframes by passing in dictionary
city_data ={'City':['SF','LA','NYC'], 'Population':[8.3, 3.8, 8.4]}
print city_data
city_frame = DataFrame(city_data)
print city_frame