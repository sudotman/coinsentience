from datetime import date, datetime
import requests

r = requests.get("https://api.binance.com/api/v3/time")
r = r.json()


serverTime = r['serverTime']

print(serverTime)

currentTime = datetime.fromtimestamp(int(serverTime)/1000)

print(currentTime)

def returnTime():
    r = requests.get("https://api.binance.com/api/v3/time")
    r = r.json()
    serverTime = r['serverTime']
    currentTime = (str) (datetime.fromtimestamp(int(serverTime)/1000))
    return currentTime

#d2 = today.strftime("%B %d, %Y")
