import json

import requests
import pandas as pd

# calling the API key
url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey= *** INSERT API KEY HERE ****"

# checking the response status
url_request = requests.get(url)
urltext = url_request.text


try:
    parsed_data = json.loads(urltext)
    data = pd.DataFrame(parsed_data)  # storing the data into df
    data = data[['rates']]  # selecting only the column we want
    data.to_csv('exchange_rates_1.csv', index=True)  # storing the df into csv file
except json.JSONDecodeError as e:
    print('Error parsing JSON data', e)
