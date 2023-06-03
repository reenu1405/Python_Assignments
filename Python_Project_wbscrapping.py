# Extracting Stock Data Using a Web Scraping

"""
Extracting data using Beautiful soup

Downloading the Webpage Using Requests Library
Parsing Webpage HTML Using BeautifulSoup
Extracting Data and Building DataFrame
Extracting data using pandas
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
"""
Using Webscraping to Extract Stock Data Example
We will extract Netflix stock data 
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html.

In this example, 
we are using yahoo finance website and looking to extract Netflix data.
"""
"""
On the following webpage we have a table with columns name (Date, Open, High, Low, close, adj close volume) out of which we must extract following columns
Date
Open
High
Low
Close
Volume
"""

"""
***Steps to be followed for extracting data***
- Send an HTTP request to the webpage using the requests library.
- Parse the HTML content of the webpage using BeautifulSoup.
- Identify the HTML tags that contain the data you want to extract.
- Use BeautifulSoup methods to extract the data from the HTML tags.
- Print the extracted data
"""

# Step-1 Send an HTTP Request to the webpage using requests library

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

"""
The requests.get() method takes a URL as its first argument, 
which specifies the location of the resource to be retrieved. 
In this case, the value of the url variable is passed as 
the argument to the requests.get() method,
as we've stored a webpage URL in a url variable.

we have used .text method for extracting the HTML content as a string 
in order to make it readable.
"""

data = requests.get(url).text
# print(data)

# Step 2: Parse the HTML content

soup = BeautifulSoup(data, 'html5lib')

# Step 3: Identify the HTML tags
"""
As stated above webpage consist of table so, 
we will be scrapping the content of the HTML webpage and 
convert the table into a dataframe.

We will creates an empty DataFrame using the pd.
DataFrame() function with the following columns.
"Date"
"Open"
"High"
"Low"
"Close"
"Volume"
"""

netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close","Adj Close", "Volume"])

"""
Step-4 Use Beautiful soup method for extracting data
We will use find() and find_all() methods of the BeautifulSoup object to 
locate the table body and table row respectively in the HTML.

The find() method will return particular tag content.
The find_all() method returns a list of all matching tags in the HTML.
"""
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

# Finally we append the data of each row to the table
    netflix_data.loc[len(netflix_data)] = {"Date": date, "Open": Open, "High": high, "Low": low, "Close": close, "Adj Close": adj_close, "Volume": volume}

# Step 5: print out the DataFrame using head() or tail() function
print(netflix_data.head())

# Extracting data using pandas library
# use the pandas read_html function from pandas library and use the URL for extracting data.

read_html_pandas_data = pd.read_html(url)
# or
# we can convert the BeautifulSoup object to a string
read_html_pandas_data1 = pd.read_html(str(soup))

netflix_dataframe = read_html_pandas_data[0]
print(netflix_dataframe.head())
