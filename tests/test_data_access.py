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
from sqlalchemy.ext.declarative import declarative_base

# from cy_data_access import cy_data_access


def test_save_candle_to_db():
    Base = declarative_base()
