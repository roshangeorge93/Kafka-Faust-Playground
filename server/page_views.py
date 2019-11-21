import faust

app = faust.App(
    'page_views',
    broker='kafka://kafka:9092',
    store='rocksdb://',
    topic_partitions=1,
)


class PageView(faust.Record):
    id: str
    user: str


page_view_topic = app.topic('page_views', value_type=PageView)

page_views = app.Table('page_views', default=int)


@app.agent(page_view_topic)
async def count_page_views(views):
    async for view in views.group_by(PageView.id):
        page_views[view.id] += 1
        print(page_views[view.id])
        if page_views[view.id] > 3:
            print(view.user)


if __name__ == '__main__':
    app.main()
