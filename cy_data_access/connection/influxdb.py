from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS


def influx_client_query_data_frame(host='http://localhost:8086', query=''):
    """ 查询数据 """
    client = InfluxDBClient(url=host, token="", org="", debug=False)
    result = client.query_api().query_data_frame(org="", query=query)
    client.__del__()
    return result


def influx_client_write_data_frame(host='http://localhost:8086', df=None, df_time_index_name='', database='', measurement_name='', tag_columns=[]):
    """ 保存数据 """
    client = InfluxDBClient(url=host, token="", org="", debug=False)
    write_client = client.write_api(write_options=WriteOptions(batch_size=500,
                                                               flush_interval=10_000,
                                                               jitter_interval=2_000,
                                                               retry_interval=5_000,
                                                               max_retries=5,
                                                               max_retry_delay=30_000,
                                                               exponential_base=2))
    df.set_index(df_time_index_name, inplace=True)
    write_client.write(database, record=df, data_frame_measurement_name=measurement_name, data_frame_tag_columns=tag_columns)
    write_client.__del__()


def influx_client_delete_data(host='http://localhost:8086', measurement='', start_date_str="1970-01-01T00:00:00Z", stop_date_str="2100-02-01T00:00:00Z"):
    """删除数据"""
    client = InfluxDBClient(url="http://localhost:8086", token="")
    delete_api = client.delete_api()
    try:
        delete_api.delete(start_date_str, stop_date_str, f'_measurement={measurement}', bucket='my-bucket', org='my-org')
    finally:
        client.__del__()
