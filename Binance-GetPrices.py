import json
import requests
  

key = "https://api.binance.com/api/v3/ticker/price?symbol="
  

currencies = ["USDTTRY","BTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT","AVAXUSDT","APEUSDT","MATICUSDT","NEARUSDT","LTCUSDT","ICPUSDT","MINAUSDT","DOTUSDT","FTTUSDT","AXSUSDT","SXPUSDT","SRMUSDT","RAYUSDT","CLVUSDT","ALGOUSDT","CAKEUSDT","KSMUSDT"]
  

print("BINANCE")
for i in range(len(currencies)):
    
    
    url = key+currencies[i]  
    data = requests.get(url)
    data = data.json()
    print("{}.{} : {}".format(i+1,data['symbol'],float(data['price'])))
    
