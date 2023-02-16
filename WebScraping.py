from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

# getting contents of the webpage
html_data = requests.get('https://en.wikipedia.org/wiki/List_of_largest_banks ')


# parsing the data from the html
soup = BeautifulSoup(html_data.text, 'html.parser')


# create a blank data frame
data_frame = pd.DataFrame(columns=['Name', 'Market Cap (US$ Billion)'])


# Looping through the data in html to extract the table and appending it on the data_frame
for row in soup.find_all('tbody')[2].find_all('tr'):
    col = row.find_all('td')
    if len(col) > 0:
        name = col[1].text.strip()
        market_cap = float(col[2].string.strip())
        data_frame = data_frame.append({"Name": name, "Market cap (US$ Billion)": market_cap}, ignore_index= True)

print(data_frame.head(5))

# loading the data frame into a json file
data_to_json = data_frame.to_json('bank_market_cap.json', orient='records')

# read the python file into python object
with open('bank_market_cap.json', 'r') as file:
    data = json.load(file)

print(data)
