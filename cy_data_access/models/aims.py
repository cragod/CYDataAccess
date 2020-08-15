from ..connection.connect import *
from pymodm import fields, MongoModel


class AIMSPosition(MongoModel):
    """AIMS 策略仓位"""
    # 交易所
    exchange_name = fields.CharField(min_length=3)
    # 币对
    coin_pair = fields.CharField(min_length=3)
    # 当前基础币总花费
    cost = fields.FloatField()
    # 持有目标币数量
    hold = fields.FloatField()

    class Meta:
        collection_name = CN_AIMS_POS
        connection_alias = DB_POSITION
