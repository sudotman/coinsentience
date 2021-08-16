import numpy
import talib
from numpy import genfromtxt


# convert our data into a numpy array
my_data = genfromtxt('Current_15minutes.csv', delimiter=',')


# get the fourth column i.e. the close from our previously generated array
close = my_data[:,4]

print(close)


# sma = talib.SMA(close,timeperiod=13)

# print(sma)

rsi = talib.RSI(close,timeperiod=14)

print(rsi)