import pandas as pd
import yfinance as yf
import psycopg2
from psycopg2 import sql

class DataFetcher:
    def __init__(self, db_config):
        self.connection = psycopg2.connect(**db_config)

    def fetch_historical_data(self, symbol, start_date, end_date):
        data = yf.download(symbol, start=start_date, end=end_date)
        data.reset_index(inplace=True)

        self.store_data(symbol, data)

    def store_data(self, symbol, data):
        with self.connection.cursor() as cursor:
            for index, row in data.iterrows():
                cursor.execute(
                    sql.SQL("INSERT INTO historical_data (symbol, date, open, high, low, close, volume) VALUE (%s, %s, %s, %s, %s, %s, %s)"),
                    (symbol, row['Date'], row['Open'], row['High'], row['Low'], row['Close'], row['Volume'])
                )
                self .connection.commit()
    def close_connection(self):
        self.connection.close()
