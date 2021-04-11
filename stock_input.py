# for data manipulation and analysis
import pandas as pd
# work with arrays
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

# workaround to get data from Yahoo Finance
yf.pdr_override()

stock=input("Enter a stock ticker symbol: ")
print(stock)

start_year = 2020
start_month = 10
start_day = 22

start = dt.datetime(start_year,start_month,start_day)

now = dt.datetime.now()

# generate data
# columns: Open        High         Low       Close   Adj Close    Volume
df = pdr.get_data_yahoo(stock,start,now)

ma=50

sma_string="Sma_" + str(ma)

# create a column named sma_string
# value based on the mean of last 50 values of Adj Close
df[sma_string] = df["Adj Close"].rolling(window = ma).mean()

# array starts with row with ma not equaled to NaN
df=df.iloc[ma:]

print(df)

numH = 0
numL = 0

for i in df.index:
    is_higher = (df["Adj Close"][i] > df[sma_string][i])
    higher_lower = "higher" if is_higher else "lower"
    print(f"The close is {higher_lower} than the 50-day MA")
    
    if(is_higher):
        numH += 1
    else:
        numL += 1

print(f"Number of days higher than the 50-day MA: {numH}")
print(f"Number of days lower than the 50-day MA: {numL}")
