from sqlalchemy import Column, Integer, DECIMAL, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def get_candle_class_with_name(name):
    """表名由外部传入"""

    class ExchangeCandle(Base):
        """OHLCV"""
        __tablename__ = name
        candle_begin_time = Column(DateTime, primary_key=True)
        open = Column(DECIMAL)
        high = Column(DECIMAL)
        low = Column(DECIMAL)
        close = Column(DECIMAL)
        volume = Column(DECIMAL)
        signal = Column(Integer)
    return ExchangeCandle
