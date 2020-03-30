#!/usr/bin/env python

"""Tests for `cy_data_access` package."""

from CYDataAccess import cli
import pytest

from click.testing import CliRunner
from cy_components.utils.coin_pair import CoinPair
from cy_components.defines.enums import TimeFrame
from cy_widgets.exchange.provider import CCXTProvider, ExchangeType
from cy_widgets.fetcher.exchange import ExchangeFetcher
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, DECIMAL, DateTime

# from cy_data_access import cy_data_access


def test_save_candle_to_db():
    engine = engine = create_engine("mysql+pymysql://root:lcrc881116@149.129.48.95:3306/market", echo=True)
    provider = CCXTProvider(api_key="", secret="", params={}, exg_type=ExchangeType.Bitfinex)

    fetcher = ExchangeFetcher(provider)
    df = fetcher.fetch_historical_candle_data(CoinPair('ETH', 'BTC'), TimeFrame.Minute_30, 1585131432, 500)
    print(df)
