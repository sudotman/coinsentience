from flask import Flask, render_template, request, flash, redirect
import config, csv
from binance.client import Client
from binance.enums import *

app = Flask(__name__)

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
    print(exchange_info)

    symbols = exchange_info['symbols']

    return render_template('index.html', title=title, my_balances = balances, symbols = symbols)

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

@app.route('/settings')
def settings():
    return 'settings'

