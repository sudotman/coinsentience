from flask import Flask, render_template, request, flash, redirect, jsonify
import config, csv
from binance.client import Client
from binance.enums import *
from flask_cors import CORS


import helperFunctions

app = Flask(__name__)
CORS(app)


# A secret key is required to avoid cross scripting
app.secret_key = config.SECRET_KEY

client = Client(config.API_KEY, config.API_SECRET)

# Using Flask and Jinja for stuff. Jinja is basically html with extra programming stuff like looping

@app.route('/home')
def home():
    return "<b> Home Sweet Test </b>"

@app.route('/')
def index():
    title = 'CoinSentient'

    account = client.get_account()

    balances = account['balances']

    exchange_info = client.get_exchange_info()

    orders = client.futures_get_all_orders()
    #trades = client.get_recent_trades(symbol='BTCUSDT',limit=50)
    # print (orders)
    # print(exchange_info)

    symbols = exchange_info['symbols']



    return render_template('index.html', title=title, my_balances = balances, symbols = symbols, orders = orders)

@app.route('/buy', methods=['POST'])
def buy():
    print(request.form)

    try:
        order = client.create_order(symbol=request.form['symbol'], 
            side=SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = request.form['quantity'])
    except Exception as e:
        flash(e.message, "error")

    return redirect('/')

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/strategy')
def strategy():
    print(request.form)
    try:
        order = client.create_order(symbol=request.form['symbol'], 
            side=SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = request.form['quantity'])
    except Exception as e:
        flash(e.message, "error")

    return redirect('/')

@app.route('/settings')
def settings():
    return 'settings'

@app.route('/history')
def history():
   
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Aug, 2021", helperFunctions.returnTime())

    processed_candlesticks = []

    for data in candlesticks:
        # creating a dictionary to parse the data from binance in a format that lightweight charts want
        candlestick = { 
            "time": data[0] / 1000, 
            "open": data[1], 
            "high": data[2], 
            "low": data[3], 
            "close": data[4] 
        }

        processed_candlesticks.append(candlestick)
    processed_candlesticks = jsonify(processed_candlesticks)
    return processed_candlesticks

