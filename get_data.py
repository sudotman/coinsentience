import config, csv
import helperFunctions

#binance imports
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

client = Client(config.API_KEY, config.API_SECRET)




### Obtain current Klines/Candles and store them/output them

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
    
# write our data to a file 
csvfile = open('Current_15minutes.csv','w',newline='')

candlestick_writer = csv.writer(csvfile, delimiter=',')

for candlestick in candles:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()


### Obtain historical Klines/Candles and store/output them

# h_candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "16 Aug, 2021", "17 Aug, 2021")
#h_candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Jan, 2021", "1 July, 2021")
h_candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2010", helperFunctions.returnTime())
h_csvfile = open('HistoricalDaily.csv','w',newline='')
h_candlestick_writer = csv.writer(h_csvfile, delimiter=',')

for candlestick in h_candles:
    candlestick[0] = candlestick[0] / 1000
    h_candlestick_writer.writerow(candlestick)

h_csvfile.close()




#######  not in use

# print each ticker individually

# prices = client.get_all_tickers()
#for price in prices:
#   print(price)
