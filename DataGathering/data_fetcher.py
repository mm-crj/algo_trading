import pandas as pd
import psycopg2
import yfinance as yf
from psycopg2 import sql


class DataFetcher:
    def __init__(self, db_config):
        self.connection = psycopg2.connect(**db_config)

    def fetch_historical_data(self, symbol, start_date, end_date):
        data = yf.download(symbol, start=start_date, end=end_date)
        data.reset_index(inplace=True)

        self.store_data(symbol, data)
    #
    def store_data(self, symbol, data):
        with self.connection.cursor() as cursor:
            insert_querry =  sql.SQL( "INSERT INTO historical_data (symbol, date, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s)")
            records_to_insert = [
                        (symbol,
                        row['Date'].iloc[0],
                        row[('Open', symbol)],
                        row[('High', symbol)],
                        row[('Low', symbol)],
                        row[('Close', symbol)],
                        row[('Volume', symbol)])
                for index, row in data.iterrows()
                ]
            cursor.executemany(insert_querry, records_to_insert)
            self.connection.commit()
    def close_connection(self):
        self.connection.close()
