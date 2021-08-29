import backtrader as bt
import datetime



class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                print(
                    'Buy Executed, Price:' + (str) (order.executed.price) + ' Cost: '+ (str) (order.executed.value) + ' Comm:' + (str) (order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
               print(
                    'Sell Executed, Price:' + (str) (order.executed.price) + ' Cost: '+ (str) (order.executed.value) + ' Comm:' + (str) (order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            print('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        print('Resulting PNL, GROSS: '+ (str) (trade.pnl) + ' NET: ' + (str) (trade.pnlcomm) + '\n')
    
    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy(size=1)
        
        if self.rsi > 70 and self.position:
            self.close()

class StochasticStrategy(bt.Strategy):

    def __init__(self):
        self.stoch = bt.talib.STOCH(self.data.high, self.data.low, self.data.close,
                                   fastk_period=14, slowk_period=3, slowd_period=3)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                print(
                    'Buy Executed, Price:' + (str) (order.executed.price) + ' Cost: '+ (str) (order.executed.value) + ' Comm:' + (str) (order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
               print(
                    'Sell Executed, Price:' + (str) (order.executed.price) + ' Cost: '+ (str) (order.executed.value) + ' Comm:' + (str) (order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            print('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        print('Resulting PNL, GROSS: '+ (str) (trade.pnl) + ' NET: ' + (str) (trade.pnlcomm) + '\n')
    
    def next(self):
        if self.stoch < 20 and not self.position:
            self.buy(size=1)
        
        if self.stoch > 80 and self.position:
            self.close()

# Plays crossover of 13,21 and enters a position only when price is above 200 EMA.
class EMAStrategy(bt.Strategy):
    params = dict(fast = 13, slow = 21, long = 200)

    def __init__(self):
        self.fast_ema = bt.indicators.EMA(self.data, period=self.p.fast)
        self.slow_ema = bt.indicators.EMA(self.data, period=self.p.slow)
        self.long_ema = bt.indicators.EMA(self.data, period=self.p.long)
        self.signal = bt.indicators.CrossOver(self.fast_ema, self.slow_ema)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                print(
                    'Buy Executed, Price:' + (str) (order.executed.price) + ' Cost: '+ (str) (order.executed.value) + ' Comm:' + (str) (order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
               print(
                    'Sell Executed, Price:' + (str) (order.executed.price) + ' Cost: '+ (str) (order.executed.value) + ' Comm:' + (str) (order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            print('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        print('Resulting PNL, GROSS: '+ (str) (trade.pnl) + ' NET: ' + (str) (trade.pnlcomm) + '\n')
    
    def next(self):
        if self.data.close[0] > self.long_ema[0] and self.signal > 0.0 and not self.position:
            self.buy(size=1)
        
        elif self.data.close[0] < self.long_ema[0] and self.signal < 0.0 and self.position:
            self.close()

# Purely plays crossover of 13,21 EMAs, and disregards everything else
class EMAStrategyAggressive(bt.Strategy):
    params = dict(fast = 13, slow = 21, long = 200)

    def __init__(self):
        self.fast_ema = bt.indicators.EMA(self.data, period=self.p.fast)
        self.slow_ema = bt.indicators.EMA(self.data, period=self.p.slow)
        self.long_ema = bt.indicators.EMA(self.data, period=self.p.long)
        self.signal = bt.indicators.CrossOver(self.fast_ema, self.slow_ema)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                print(
                    'Buy Executed, Price:' + (str) (order.executed.price) + ' Cost: '+ (str) (order.executed.value) + ' Comm:' + (str) (order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
               print(
                    'Sell Executed, Price:' + (str) (order.executed.price) + ' Cost: '+ (str) (order.executed.value) + ' Comm:' + (str) (order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            print('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        print('Resulting PNL, GROSS: '+ (str) (trade.pnl) + ' NET: ' + (str) (trade.pnlcomm) + '\n')
    
    def next(self):
        if self.signal > 0.0 and not self.position:
            self.buy(size=1)
        
        elif self.signal < 0.0 and self.position:
            self.close()

# Ichimoku 
class Ichimoku(bt.Strategy):
    params = (
        ('atrperiod', 14),  # ATR Period (standard)
        ('atrdist_x', 1.5),   # ATR distance for stop price
        ('atrdist_y', 1.35),   # ATR distance for take profit price
        ('tenkan', 20),
        ('kijun', 60),
        ('senkou', 120),
        ('senkou_lead', 60),  # forward push
        ('chikou', 60),  # backwards push
    )

    def notify_order(self, order):
        if order.status == order.Completed:
            pass

        if not order.alive():
            self.order = None  # indicate no order is pending

    def __init__(self):
        self.ichi = bt.indicators.Ichimoku(self.datas[0],
                                           tenkan=self.params.tenkan,
                                           kijun=self.params.kijun,
                                           senkou=self.params.senkou,
                                           senkou_lead=self.params.senkou_lead,
                                           chikou=self.params.chikou)

        # Cross of tenkan and kijun -
        #1.0 if the 1st data crosses the 2nd data upwards - long 
        #-1.0 if the 1st data crosses the 2nd data downwards - short

        self.tkcross = bt.indicators.CrossOver(self.ichi.tenkan_sen, self.ichi.kijun_sen)

        # To set the stop price
        self.atr = bt.indicators.ATR(self.data, period=self.p.atrperiod)

      # Long Short ichimoku logic
        self.long = bt.And((self.data.close[0] > self.ichi.senkou_span_a(0)),
        (self.data.close[0] > self.ichi.senkou_span_b(0)),
        (self.tkcross == 1))
        
        self.short = bt.And((self.data.close[0] < self.ichi.senkou_span_a(0)),
        (self.data.close[0] < self.ichi.senkou_span_b(0)),
        (self.tkcross == -1))

    def start(self):
        self.order = None  # sentinel to avoid operrations on pending order

    def next(self):
        if self.order:
            return  # pending order execution

        if not self.position:  # not in the market
            if self.short:
                self.order = self.sell()
                ldist = self.atr[0] * self.p.atrdist_x
                self.lstop = self.data.close[0] + ldist
                pdist = self.atr[0] * self.p.atrdist_y
                self.take_profit = self.data.close[0] - pdist
            if self.long:
                self.order = self.buy()
                ldist = self.atr[0] * self.p.atrdist_x
                self.lstop = self.data.close[0] - ldist
                pdist = self.atr[0] * self.p.atrdist_y
                self.take_profit = self.data.close[0] + pdist

        else:  # in the market
            pclose = self.data.close[0]
            # pstop = self.pstop

            # if  ((pstop<pclose<self.take_profit)|(pstop>pclose>self.take_profit)):
                # self.close()  # Close position



class HODL(bt.Strategy):

    def start(self):
        self.val_start = self.broker.get_cash()  # keep the starting cash

    def nextstart(self):
        # Buy all the available cash
        size = int(self.broker.get_cash() / self.data)
        self.buy(size=size)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                print(
                    'Buy Executed, Price:' + (str) (order.executed.price) + ' Cost: '+ (str) (order.executed.value) + ' Comm:' + (str) (order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm

            self.bar_executed = len(self)


        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        print('Resulting PNL, GROSS: '+ (str) (trade.pnl) + ' NET: ' + (str) (trade.pnlcomm) + '\n')


cerebro = bt.Cerebro()
cerebro.broker.setcash(100000.0)

# fromdate = datetime.datetime.strptime('2020-07-01', '%Y-%m-%d')
# todate = datetime.datetime.strptime('2020-07-12', '%Y-%m-%d')

# daily / dt format 2 signifies unix timestamps
data = bt.feeds.GenericCSVData(dataname='HistoricalDaily.csv', dtformat = 2)

# 15 minutes
# data = bt.feeds.GenericCSVData(dataname='Current_15minutes.csv', dtformat = 2, compression = 15, timeframe = bt.TimeFrame.Minutes)

# A particular range
fromdate = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2021-04-12', '%Y-%m-%d')

# data = bt.feeds.GenericCSVData(dataname='Historical_30minutes.csv', dtformat = 2, compression = 15, timeframe = bt.TimeFrame.Minutes, fromdate = fromdate, todate = todate)

cerebro.adddata(data)

cerebro.addstrategy(Ichimoku)

# Broker / 0.1% ... divide by 100 to remove the %
cerebro.broker.setcommission(commission=0.001)

startingMoney = cerebro.broker.getvalue()
print('\nStarting Portfolio Value: %.2f' % startingMoney + '\n')
print('\nOrders:')

cerebro.run()

endMoney = cerebro.broker.getvalue()
print('\nFinal Portfolio Value: %.2f' % endMoney)

totalROE = ((endMoney - startingMoney) / startingMoney) * 100

print('\nTotal ROE: %.2f' % totalROE + '%')

cerebro.plot()