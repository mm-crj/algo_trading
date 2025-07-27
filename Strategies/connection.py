import importlib
from configparser import ConfigParser

import pandas as pd
import psycopg2


def read_data():
    '''Read data from the PostgresSQL database'''
    parser = ConfigParser()
    parser.read("config.ini")

    params = {
        "dbname": parser["database"]["dbname"],
        "user": parser["database"]["user"],
        "password": parser["database"]["password"],
        "host": parser["database"]["host"],
        "port": parser["database"]["port"],
    }

    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    cur.execute("SELECT * FROM historical_data;")

    results = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()
    return pd.DataFrame(results,columns=colnames)
