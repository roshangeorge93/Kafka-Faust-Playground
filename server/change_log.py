import faust


app = faust.App(
    'change-log',
    broker='kafka://kafka:9094',
    store='rocksdb://',
    version=1,
    topic_partitions=8,
)

words_change_log_topic = app.topic('word-counts-word_counts-changelog', value_type=bytes)


@app.agent(words_change_log_topic)
async def read_topic(streams):
    async for k, v in streams.items():
        print("RECEIVED:", k, v)
        print("DONE")


if __name__ == '__main__':
    app.main()
