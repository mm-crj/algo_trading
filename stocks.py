""" A script to import data from Nasdaq and predict the buy sell times by choosing   """
"""      exponential averages. """
import googlefinance as gf
import nasdaqdatalink as nl
import yfinance as yf
import numpy as np

# Importing the yfinance package

# Set the start and end date
start_date = '2020-01-01'
end_date = '2022-01-01'

# Set the ticker
ticker = 'GOOGL'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print the last 5 rows
print(data.tail())
