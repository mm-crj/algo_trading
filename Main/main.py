from DataGathering.data_fetcher import DataFetcher


def main():
    '''Database config'''
    db_config = {
        'dbname' : 'trading_data',
        'user': 'postgres',
        'password': 'tudiwr22',
            'host': 'localhost',
            'port': '5432'
    }

    data_featcher = DataFetcher(db_config)
    data_featcher.fetch_historical_data("BND", "2020-01-01", "2023-12-31")
    data_featcher.close_connection()

if __name__ == "__main__":
    main()
