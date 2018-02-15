import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

donor_df = pd.read_csv('Election_Donor_Data.csv')
print donor_df.head()
print donor_df.info()

# Distribution of donation amounts
sns.distplot(donor_df['contb_receipt_amt'])
print donor_df['contb_receipt_amt'].value_counts()

don_mean = donor_df['contb_receipt_amt'].mean()
don_std = donor_df['contb_receipt_amt'].std()

# Printing strings with number placeholders
print ('The average donation was $%.2f, with standard deivation of $%.2f' %(don_mean,don_std))

# Make a copy of a column with only donation amounts
top_donor = donor_df['contb_receipt_amt'].copy()  # call copy so that the series can be sorted in the next step
top_donor.sort()

# Drop negative values from the series as those represent refunds
top_donor = top_donor[top_donor>0]
print top_donor
print top_donor.value_counts()

# Make a series of small common donations
plt.figure()
com_don = top_donor[top_donor < 2500]
com_don.hist(bins=100)

# Assign a party to each candidate using a map
print donor_df['cand_nm'].value_counts()

party_map = {'Obama, Barack':'Democrat',
             'Paul, Ron':'Republican',
             'Romney, Mitt':'Republican',
             'Gingrich, Newt':'Republican',
             'Santorum, Rick':'Republican',
             'Cain, Herman':'Republican',
             'Perry, Rick':'Republican',
             'Bachmann, Michelle':'Republican',
             "Roemer, Charles E. 'Buddy' III":'Republican',
             'Pawlenty, Timothy':'Republican',
             'Huntsman, Jon':'Republican',
             'Johnson, Gary Earl':'Republican',
             'McCotter, Thaddeus G':'Republican'}

donor_df['Party'] = donor_df.cand_nm.map(party_map)
print donor_df['Party'].value_counts()

# Get rid of negative contributions
donor_df = donor_df[donor_df['contb_receipt_amt']>0]

# Groupby candidate then count number of donation receipts
donor_df_grouped = donor_df.groupby('cand_nm')
print donor_df_grouped.contb_receipt_amt.count()  # count number of occurances

# Print out results using a for loop
cand_amt = donor_df_grouped.contb_receipt_amt.sum()  # count sum/total

i = 0
for cand_don in cand_amt:
    print ('The candidate %s raised %.0f dollars' %(cand_amt.index[i],cand_don))
    i = i + 1

plt.figure()
cand_amt.plot(kind='bar',color='royalblue')

# Gropuby party
donor_df_grouped2 = donor_df.groupby('Party')
plt.figure()
donor_df_grouped2.contb_receipt_amt.sum().plot(kind='bar',color='royalblue')


# Use pivot table to organize the values in the cells, the row label, the column label, and how value in the cell is calculated
occupation_df = donor_df.pivot_table('contb_receipt_amt',  # what value to use in the cell
                                     index='contbr_occupation',  # what to group the rows
                                     columns='Party',  # how to group the columns
                                     aggfunc='sum')  # how value in the cell is calculated

print occupation_df.head()
print occupation_df.shape

# since above dataset is too large (45k professions), set a cutoff
occupation_df = occupation_df[occupation_df.sum(1)>1000000]
print occupation_df.shape

occupation_df.plot(kind='barh',cmap='seismic') # horizontal barplot

# Drop certain cases
occupation_df.drop(['INFORMATION REQUESTED PER BEST EFFORTS','INFORMATION REQUESTED'],axis=0,inplace=True)

# Combine certain cases
occupation_df.loc['CEO'] = occupation_df.loc['CEO'] + occupation_df.loc['C.E.O.']  #
occupation_df.drop('C.E.O.', inplace=True)
print occupation_df.head()

occupation_df.sort_index(ascending=0).plot(kind='barh',cmap='seismic') # horizontal barplot

plt.show()