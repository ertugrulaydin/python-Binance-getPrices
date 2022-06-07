import json
import requests
  
# Defining Binance API URL
key = "https://api.binance.com/api/v3/ticker/price?symbol="
  
# Making list for multiple crypto's
currencies = ["USDTTRY","BTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT","AVAXUSDT","APEUSDT","MATICUSDT","NEARUSDT","LTCUSDT","ICPUSDT","MINAUSDT","DOTUSDT","FTTUSDT","AXSUSDT","SHIBUSDT","SXPUSDT","SRMUSDT","RAYUSDT","CLVUSDT","ALGOUSDT","CAKEUSDT","KSMUSDT"]
j = 0
  
# running loop to print all crypto prices
print("BINANCE")
for i in range(len(currencies)):
    
    # completing API for request
    url = key+currencies[i]  
    data = requests.get(url)
    data = data.json()
    print("{} : {}".format(data['symbol'],data['price']))
    
