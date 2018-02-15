from __future__ import division
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

from pandas_datareader.data import DataReader
from datetime import datetime


sns.set_style('whitegrid')

'''
Questions:

1) What was the change in price of the stock over time?
2) What was the daily return of the stock on average?
3) What was the moving average of the various stocks?
4) What was the correlation between different stocks' closing prices? their daily returns?
5) How much value do we put at risk by investing in a particular stock?
6) How can we attempt to predict future stock behavior?

'''

# Import stock data
tech_list = ['AAPL','GOOG','MSFT','AMZN']
end = datetime.now()
start = datetime(end.year-1,end.month,end.day)
for stock in tech_list:
    globals()[stock] = DataReader(stock,'yahoo',start,end)  # Now each stock name (e.g. AAPL) is an entire dataframe global variable
print AAPL.head()

# Use plot method that comes with dataframes (pandas actually) for line plots (like time series)
AAPL['Adj Close'].plot(legend=True,figsize=(10,4))
plt.figure()
AAPL['Volume'].plot(legend=True,figsize=(10,4))

# Calculate moving average
ma_range = [10,20,50]
for ma in ma_range:
    column_name = 'MA for %s days' %(str(ma))
    AAPL[column_name] = pd.rolling_mean(AAPL['Adj Close'],ma)

AAPL[['Adj Close','MA for 10 days','MA for 20 days','MA for 50 days']].plot(subplots=False,legend=True,figsize=(10,4))

# Daily returns
AAPL['Daily Return'] = AAPL['Adj Close'].pct_change()
plt.figure()
AAPL['Daily Return'].plot(legend=True)

# Histogram using seaborn's functions
plt.figure()
sns.distplot(AAPL['Daily Return'].dropna())

# Look at multiple stocks at once
closing_df = DataReader(tech_list,'yahoo',start,end)['Adj Close']
tech_rets = closing_df.pct_change()

# Use jointplot
sns.jointplot('GOOG','MSFT',tech_rets,kind='scatter')

# Comparing multiple pairs simultaneously
print tech_rets.head()
sns.pairplot(tech_rets.dropna())

# Customize pairplot using PairGrid
'''
returns_fig = sns.PairGrid(tech_rets.dropna())  # PairGrid is what pairplot is built on
returns_fig.map_upper(plt.scatter,color='purple')
returns_fig.map_lower(sns.kdeplot,cmap='cool_d')
returns_fig.map_diag(plt.hist,bins=30)
'''

# Using seaborn's corrplot to get numerical correlation
plt.figure()
sns.corrplot(tech_rets.dropna(),annot=True)

# X-Y scatter plot of mean and stdev (risk). To see how to label, see documentation on annotation
plt.figure()
rets = tech_rets.dropna()
area = np.pi*20
plt.scatter(rets.mean(),rets.std(),s = area)
plt.xlabel('Expected returns')
plt.ylabel('Risk')

# Suppress all previous figures to reduce runtime
plt.close('all')

sns.distplot(AAPL['Daily Return'].dropna(),bins=100)
print rets['AAPL'].quantile(0.05)  # With 95% confidence, what is the lowest return or greatest percent loss to suffer given the past data.
# This percent is the Value at Risk (VaR)

# Value at Risk using the Monte Carlo simulation method
days = 365
dt = 1/days
mu = rets.mean()['GOOG']
sigma = rets.std()['GOOG']

# Monte Carlo simulation
def stock_monte_carlo(start_price,days,mu,sigma):

    price = np.zeros(days)
    price[0] = start_price

    shock = np.zeros(days)
    drift = np.zeros(days)

    for x in xrange(1,days):

        shock[x] = np.random.normal(loc=mu*dt,scale=sigma*np.sqrt(dt))
        drift[x] = mu * dt
        price[x] = price[x-1] + (price[x-1] * (drift[x]+shock[x]))

    return price

start_price = 500.87

plt.figure()
for run in xrange(100):
    plt.plot(stock_monte_carlo(start_price,days,mu,sigma))

plt.xlabel('Days')
plt.ylabel('Price')
plt.title('Monte Carlo Analysis for Google')


# Run simulation and store final price
runs = 1000
simulations = np.zeros(runs)

for run in xrange(runs):
    simulations[run] = stock_monte_carlo(start_price,days,mu,sigma)[days-1]

q = np.percentile(simulations,1)
plt.figure()
plt.hist(simulations,bins=20)

# Display 1% quantile
plt.figtext(0.15,0.6,'q(0.99): $%.2f' %q)

# Plot a line at the 1% quantile result
plt.axvline(x=q, linewidth=4, color='r')











plt.show()