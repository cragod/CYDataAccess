from ..connection.define import *
from pymodm import fields, MongoModel


class Sequence(MongoModel):
    """保存各个库的 _id 字段最大值"""
    name = fields.CharField()
    max_id = fields.IntegerField()

    @classmethod
    def fetch_next_id(cls, name):
        assert name is not None and len(name) > 0
        # Find and Increase
        for seq in Sequence.objects.raw({'name': name}):
            seq.max_id += 1
            seq.save()
            return seq.max_id
        # Not found
        Sequence(name=name, max_id=0).save()
        return 0

    class Meta:
        collection_name = CN_SEQUENCE
        connection_alias = DB_CONFIG


class CCXTConfiguration(MongoModel):
    """CCXT 配置"""
    identifier = fields.IntegerField(primary_key=True)
    app_key = fields.CharField(min_length=3)
    app_secret = fields.CharField(min_length=3)
    app_pw = fields.CharField(min_length=3)
    e_type = fields.IntegerField(mongo_name='type')

    class Meta:
        collection_name = CN_CCXT_CONFIG
        connection_alias = DB_CONFIG