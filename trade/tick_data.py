import json
import requests

########## GEMINI行情接口 ##########
## https://api.gemini.com/v1/pubticker/:symbol
gemini_ticker = 'https://api.gemini.com/v1/pubticker/{}'
symbol = 'btcusd'
btc_data = requests.get(gemini_ticker.format(symbol)).json()
print(json.dumps(btc_data, indent=4))
