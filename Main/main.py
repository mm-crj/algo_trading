# from config import config
from configparser import ConfigParser
import psycopg2
import importlib
from DataGathering.data_fetcher import DataFetcher
import DataGathering.data_fetcher
importlib.reload(DataGathering.data_fetcher)


def main():
    """connecting to PostgreSQL database server"""
    # conn = None
    # params = None
    # try:
    #     params = config()
    #     print('connecting to the PostgreSQL server')
    #     conn = psycopg2.connect(**params)
    #     cur = conn.cursor()
    #     print('PostgreSQL database version:')
    #     cur.execute('SELECT version()')
    #     db_version = cur.getchone()
    #     print(db_version)
    #     cur.close()
    # except (Exception, psycopg2.DatabaseError) as error:
    #     print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('Database connection closed.')
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


