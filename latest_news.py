import json
import time
import tushare as ts

import mongoConfig


def prepare_data():
    latest_news = ts.get_latest_news()
    if latest_news is None or latest_news.empty:
        return
    latest_news_json = latest_news.to_json(orient='records')
    collection = mongoConfig.get_collection_default("latest_news")
    current_date = time.strftime("%Y-%m-%d")
    mongoConfig.clear_collection(collection)
    print(latest_news_json)
    mongoConfig.insert_json(collection, json.loads(latest_news_json))


if __name__ == "__main__":
    prepare_data()

