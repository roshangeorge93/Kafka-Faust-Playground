import os


PARTITIONS = int(os.environ.get('PARTITIONS', 2))
BROKER_URL_STRING = os.environ.get('BROKER_URL', 'kafka:9094')
BROKER_URLS = ['kafka://{}'.format(broker_url_str) for broker_url_str in BROKER_URL_STRING.split(',')]
APP_NAME = os.environ.get('APP_NAME', 'rtr_app')
ROCKS_DB_URL = 'rocksdb://'
