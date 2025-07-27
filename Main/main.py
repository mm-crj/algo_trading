import importlib
from configparser import ConfigParser

import psycopg2

import DataGathering.data_fetcher
from DataGathering.data_fetcher import DataFetcher

importlib.reload(DataGathering.data_fetcher)


def main():
   ''''connecting to PostgreSQL database server'''
    parser = ConfigParser()
    parser.read("config.ini")

    params = {
        "dbname": parser["database"]["dbname"],
        "user": parser["database"]["user"],
        "password": parser["database"]["password"],
        "host": parser["database"]["host"],
        "port": parser["database"]["port"],
    }

    if params is not None:
        data_featcher = DataFetcher(params)
        data_featcher.fetch_historical_data("BND", "2020-01-01", "2023-12-31")
        data_featcher.close_connection()


if __name__ == "__main__":
    main()
