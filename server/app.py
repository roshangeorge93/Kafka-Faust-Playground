import time
from faust import App
from datetime import datetime
from config import BROKER_URLS, ROCKS_DB_URL

app = App(
    'app_main',
    broker=BROKER_URLS,
    store=ROCKS_DB_URL,
    autodiscover=True,
    reply_create_topic=True,
)

topic = app.topic(
    'sample_topic',
    # value_type=bytes,
    value_type=str,
    partitions=1,
)


@app.agent(topic)
async def read_topic(streams):
    async for payload in streams:
        print("RECEIVED:", payload)
        print("DONE")


if __name__ == '__main__':
    app.main()
