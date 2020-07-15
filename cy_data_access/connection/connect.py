import os
from pymodm.connection import connect

# ==== Configuration ====

DB_CONFIG = 'cfg'

CN_SEQUENCE = 'sequence'
CN_CCXT_CONFIG = 'cxt'

# ==== Market ====

DB_MARKET = 'market'

# ==== Backtest ====

DB_BACKTEST = 'backtest'


def connect_db(user, password, host='127.0.0.1:27017', db_name=None):
    # 连接到数据库
    uri = "mongodb://{}:{}@{}/{}?authSource=admin".format(user, password, host, db_name)
    connect(uri, db_name)


def connect_db_env(host='127.0.0.1:27017', db_name=None):
    connect_db(os.environ['DB_MNR_USER'], os.environ['DB_MNR_PWD'], host, db_name)
