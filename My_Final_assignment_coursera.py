import pip

import yfinance as yf
import wget

# yfinance:it allows us to extract data for stocks returning data in a pandas dataframe.
import numpy as np
import pandas as pd
import json

apple = yf.Ticker("AAPL")


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json'
filename = wget.download(url)


with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable   
    # print("Type:", type(apple_info))


# Using the attribute info:extracting information about the stock as a Python dictionary.

# print(apple_info)

# We can get the 'country' using the key country
# apple_info['country']
print(apple_info['country'])

# sing the period parameter we can set how far back from the present to get data.
# The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.

apple_share_price_data = apple.history(period="max")
'''
The format that the data is returned in is a Pandas DataFrame. 
With the Date as the index the share Open, High, Low, Close, Volume, and Stock Splits are given for each day.
'''
apple_share_price_data.head()
# print(apple_share_price_data.head())

'''
We can reset the index of the DataFrame with the reset_index function. 
We also set the inplace parameter to True so the change 
takes place to the DataFrame itself.
'''
apple_share_price_data.reset_index(inplace=True)

import matplotlib
# We can plot the Open price against the Date:
apple_share_price_data.plot(x="Date", y="Open")
# print(apple_share_price_data.plot(x="Date", y="Open"))

# Extracting Dividends
# print(apple.dividends)

# We can plot the dividends overtime:

# print(apple.dividends.plot())

# Another
'''
Now using the Ticker module create an object for AMD (Advanced Micro Devices) 
with the ticker symbol is AMD called; 
name the object amd.
'''
amd = yf.Ticker("AMD")

url1 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json'
filename1 = wget.download(url1)


with open('amd.json') as json_file:
    amd_info = json.load(json_file)
print(amd_info)

'''
Question 1 Use the key 'country' to find the country the stock belongs to.
'''
print(amd_info['country'])

'''
Question 2 Use the key 'sector' to find the sector the stock belongs to.
'''
print(amd_info['sector'])

'''
Question 3 Obtain stock data for AMD using the history function, set the period to max. 
Find the Volume traded on the first day (first row)
'''
amd_stock_data = apple.history(period="max")
print(amd_stock_data.head(1))
