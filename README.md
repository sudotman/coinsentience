# Prerequisites
pip install csv
pip install wheel
pip install TA_Lib-0.4.21-cp39-cp39-win_amd64.whl 

pip install -r requirements.txt

.venv\Scripts\activate

# Using Flask and Jinja for stuff. Jinja is basically html with extra programming stuff like looping

## In jinja/flask
the variables are basically defined as {{ these_brackets}}

And then, we can pass them as paramaters to whatever file we will call through our render template.

So essentially, the jinja/flask/render_templates basically treat html files as callback functions, and well yeah you pass parameters.

# WSS / Websocket Streams:

Base endpoint: wss://stream.binance.com:9443

## View data through websockets:
wscat -c wss://stream.binance.com:9443/ws/btcusdt@trade / wss://stream.binance.com:9443/ws/btcusdt@kline_5m

### Store the data to a file: 
wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee dataset.txt


Raw streams are accessed at /ws/<streamName>
Combined streams are accessed at /stream?streams=<streamName1>/<streamName2>/<streamName3>


# Trade Streams Payload
{
  "e": "trade",     // Event type
  "E": 123456789,   // Event time
  "s": "BNBBTC",    // Symbol
  "t": 12345,       // Trade ID
  "p": "0.001",     // Price
  "q": "100",       // Quantity
  "b": 88,          // Buyer order ID
  "a": 50,          // Seller order ID
  "T": 123456785,   // Trade time
  "m": true,        // Is the buyer the market maker?
  "M": true         // Ignore
}

# Kline/Candlestick Charts:
{
  "e": "kline",     // Event type
  "E": 123456789,   // Event time
  "s": "BNBBTC",    // Symbol
  "k": {
    "t": 123400000, // Kline start time
    "T": 123460000, // Kline close time
    "s": "BNBBTC",  // Symbol
    "i": "1m",      // Interval
    "f": 100,       // First trade ID
    "L": 200,       // Last trade ID
    "o": "0.0010",  // Open price
    "c": "0.0020",  // Close price
    "h": "0.0025",  // High price
    "l": "0.0015",  // Low price
    "v": "1000",    // Base asset volume
    "n": 100,       // Number of trades
    "x": false,     // Is this kline closed?
    "q": "1.0000",  // Quote asset volume
    "V": "500",     // Taker buy base asset volume
    "Q": "0.500",   // Taker buy quote asset volume
    "B": "123456"   // Ignore
  }
}

# KLINE AGGREGATE FORMAT
[
  [
    1499040000000,      // Open time
    "0.01634790",       // Open
    "0.80000000",       // High
    "0.01575800",       // Low
    "0.01577100",       // Close
    "148976.11427815",  // Volume
    1499644799999,      // Close time
    "2434.19055334",    // Quote asset volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base asset volume
    "28.46694368",      // Taker buy quote asset volume
    "17928899.62484339" // Ignore.
  ]
]

