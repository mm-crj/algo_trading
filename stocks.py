""" A script to import data from Nasdaq and predict the buy sell times by choosing exponential averages. """

# import googlefinance as gf
# import nasdaqdatalink as nl
import yfinance as yf
import pandas as pd
import numpy as np
from math import floor
# from termcolor import colored as cl
import matplotlib.pyplot as plt

# Date time modules
from datetime import date
from dateutil.relativedelta import relativedelta

# python calculate 6 months ago from today
months_6 = date.today() + relativedelta(months=-6)

# Importing the yfinance package

# Set the start and end date
start_date = months_6
end_date = date.today()

# Set the ticker
ticker = 'GOOGL'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print the last 5 rows
# print(data.tail())

def get_macd(price, slow, fast, smooth):
    exp1 = price.ewm(span = fast, adjust = False).mean()
    exp2 = price.ewm(span = slow, adjust = False).mean()
    macd = pd.DataFrame(exp1 - exp2).rename(columns = {'Close':'macd'})
    signal = pd.DataFrame(macd.ewm(span = smooth, adjust = False).mean()).rename(columns = {'macd':'signal'})
    hist = pd.DataFrame(macd['macd'] - signal['signal']).rename(columns = {0:'hist'})
    frames =  [macd, signal, hist]
    df = pd.concat(frames, join = 'inner', axis = 1)
    return df
googl_macd = get_macd(data['Close'], 26, 12, 9)
# print(googl_macd.tail())
# print(googl_macd)

#############################################
# Plotting the data
############################################
def plot_macd(prices, macd, signal, hist):
    ax1 = plt.subplot2grid((8,1), (0,0), rowspan = 5, colspan = 1)
    ax2 = plt.subplot2grid((8,1), (5,0), rowspan = 3, colspan = 1)

    ax1.plot(prices)
    ax2.plot(macd, color = 'grey', linewidth = 1.5, label = 'MACD')
    ax2.plot(signal, color = 'skyblue', linewidth = 1.5, label = 'SIGNAL')

    for i in range(len(prices)):
        if str(hist[i])[0] == '-':
            ax2.bar(prices.index[i], hist[i], color = '#ef5350')
        else:
            ax2.bar(prices.index[i], hist[i], color = '#26a69a')

    plt.legend(loc = 'lower right')

plot_macd(googl['Close'], googl_macd['macd'], googl_macd['signal'], googl_macd['hist'])
