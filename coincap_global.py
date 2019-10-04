from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
parameters = {
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '0b5a9b5a-042a-4973-8116-c2fc6979c93c',
}
 
session = Session()
session.headers.update(headers)


""" global_url = 'https://api.coinmarketcap.com/v2/global/'
request = requests.get(global_url)
results = request.json()
 """

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#print(json.dumps(results, sort_keys=True, indent=4))

#active_currencies = results['data']['active_cryptocurrencies']
#print(active_currencies)