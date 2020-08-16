import click as c
from .connection.connect import *
from .models.config import *


@c.group()
@c.option('--db-user', envvar='DB_CLI_USER', required=True)
@c.option('--db-pwd', envvar='DB_CLI_PWD', required=True)
@c.option('--db-host', default='127.0.0.1:27017', required=True)
@c.pass_context
def cydb(ctx, db_user, db_pwd, db_host):
    ctx.ensure_object(dict)
    ctx.obj['db_u'] = db_user
    ctx.obj['db_p'] = db_pwd
    ctx.obj['db_h'] = db_host


@cydb.command()
@c.option('--key', type=str, prompt=True, required=True)
@c.option('--secret', type=str, prompt=True, required=True)
@c.password_option(confirmation_prompt=False, required=False)
@c.option('--type',
          type=c.Choice(['okex', 'hbp', 'binance'], case_sensitive=False), prompt=True)
@c.pass_context
def add_ccxt_config(ctx, key, secret, password, type):
    # connect db
    connect_db(ctx.obj['db_u'], ctx.obj['db_p'], ctx.obj['db_h'], DB_CONFIG)
    # save config
    e_type = 0
    if type == 'hbp':
        e_type = CCXTExchangeType.HuobiPro
    elif type == 'okex':
        e_type = CCXTExchangeType.Okex
    elif type == 'binance':
        e_type = CCXTExchangeType.Binance
    result = CCXTConfiguration(identifier=Sequence.fetch_next_id(CN_CCXT_CONFIG),
                               app_key=key,
                               app_secret=secret,
                               app_pw=password,
                               e_type=e_type).save()
    c.echo('Result: {}(id: {})'.format(result, result.identifier))
