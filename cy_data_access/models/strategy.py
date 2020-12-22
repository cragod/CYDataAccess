from ..connection.connect import *
from pymodm import fields, MongoModel


class StrategryCfg(MongoModel):
    identifier = fields.IntegerField(primary_key=True)
    coin_pair = fields.CharField()
    leverage = fields.FloatField()
    strategy_name = fields.CharField()
    parameters = fields.DictField()
    time_interval = fields.CharField()

    class Meta:
        connection_alias = DB_STRATEGY
        collection_name = CN_STRATEGY_CFG
