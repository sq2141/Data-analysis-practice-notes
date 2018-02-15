import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

titanic_df = pd.read_csv('train.csv')
print titanic_df.head()
print titanic_df.shape
print titanic_df.info()

'''
Some basic questions:
1) Who were the passengers on the Titanic (Ages,Gender,Class,...etc) aka. See the distribution of these variables
2) What deck were the passengers on and how does that relate to their class?
3) Where did the passengers come from?
4) Who was alone and who was with family?
5) What factors helped someone survive the sinking?
'''

# Passenger count by sex and class
sns.factorplot(x='Sex',data=titanic_df.sort_values(by=['Sex','Pclass'],ascending=[0,1]),kind='count',hue='Pclass')
sns.factorplot(x='Pclass',kind='count',data=titanic_df.sort_values(by=['Sex','Pclass'],ascending=[0,1]),hue='Sex')

# Add a new column by 'applying' a custom-built function
def male_female_child(passenger):
    age,sex = passenger

    if age < 16:
        return 'child'
    else:
        return sex

titanic_df['person'] = titanic_df[['Age','Sex']].apply(male_female_child,axis=1)
print titanic_df.head(10)
sns.factorplot(x='Pclass',kind='count',data=titanic_df,hue='person')

# Use pandas to plot a histogram
plt.figure()
titanic_df['Age'].hist(bins=70)
print titanic_df['Age'].mean()

# Count within a column
print titanic_df['person'].value_counts()

# Use seaborn's FacetGrid to do multiple plots on one figure
fig = sns.FacetGrid(titanic_df,hue='Sex',aspect=4)

bins = np.linspace(0,70,70)
fig.map(sns.distplot,'Age',bins=bins)

oldest = titanic_df['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()

# Drop Null values from the Cabin column using dropna
deck = titanic_df['Cabin'].dropna()
print deck.head()
# Cabin levels are categorized A,B,C,D,E,F,G, so only need first letter
levels = []
for level in deck:
    levels.append(level[0])  # append the first letter
print levels

cabin_df = DataFrame(levels)
cabin_df.columns = ['Cabin']
sns.factorplot(x='Cabin',kind='count',data=cabin_df.sort_values(by='Cabin',ascending=1),palette='winter_d') # but produces a T cabin...

# Creating a new table dropping cases containing specific values
cabin_df = cabin_df[cabin_df.Cabin != 'T']
sns.factorplot(x='Cabin',kind='count',data=cabin_df.sort_values(by='Cabin',ascending=1),palette='winter_d') # but produces a T cabin...


# Factorplot to see how two categorical variables are related
sns.factorplot(x='Embarked',kind='count',data=titanic_df.sort_values(by='Pclass'),hue='Pclass')

# Calculate values in put in a new column (whether alone or with family) based on existing column values
def alone_or_fam(passenger):
    sib, par = passenger
    if sib==0 and par==0:
        with_fam = 'Alone'
    else:
        with_fam = 'With Family'
    return with_fam

titanic_df['alone_or_fam']=titanic_df[['SibSp','Parch']].apply(alone_or_fam,axis=1)

sns.factorplot(x='Pclass',kind='count',data=titanic_df.sort_values(by='Pclass'),hue='alone_or_fam')

# What factors help someone survive?
titanic_df['Survivor'] = titanic_df.Survived.map({0:'no',1:'yes'})
sns.factorplot(x='Pclass',y='Survived',data=titanic_df.sort_values(by='Pclass'))
sns.factorplot(x='Pclass',y='Survived',data=titanic_df.sort_values(by='Pclass'),hue='person')

plt.figure()
sns.lmplot(x='Age',y='Survived',data=titanic_df)

generations = np.linspace(0,80,8)
sns.lmplot(x='Age',y='Survived',data=titanic_df.sort_values(by='Pclass'),hue='Pclass',palette='winter',x_bins=generations)

sns.lmplot(x='Age',y='Survived',data=titanic_df.sort_values(by='Pclass'),hue='Sex',palette='winter',x_bins=generations)

# Did the deck have an effect on passenger survival rate?
def deck_check(cabin):
    cabin = cabin[0]
    return cabin

titanic_df['Deck'] = titanic_df['Cabin'].dropna().apply(deck_check)
print titanic_df.head()
Tdropped = titanic_df[titanic_df.Cabin != 'T']

sns.factorplot(x='Deck',y='Survived',data=Tdropped.sort_values(by='Deck'))

# Did have a family member increase the odds of surviving the crash?
sns.factorplot(x='alone_or_fam',y='Survived',data=titanic_df)

plt.show()