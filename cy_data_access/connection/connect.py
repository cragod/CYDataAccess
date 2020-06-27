from pymodm.connection import connect

# ==== Configuration ====

DB_CONFIG = 'cfg'

CN_SEQUENCE = 'sequence'
CN_CCXT_CONFIG = 'cxt'


def connect_db(name, password, ip, db_name):
    # 连接到数据库
    uri = "mongodb://{}:{}@{}/{}?authSource=admin".format(name, password, ip, db_name)
    connect(uri, db_name)
