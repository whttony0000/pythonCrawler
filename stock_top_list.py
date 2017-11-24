import json
import time
import tushare as ts

import mongoConfig


def prepare_data():
    current_date = time.strftime("%Y-%m-%d")
    top_list = ts.top_list(current_date)
    if top_list is None or top_list.empty:
        return
    record_json = top_list.to_json(orient='records')
    print(record_json)
    collection = mongoConfig.get_collection_default("stock_top_list")
    mongoConfig.clear_collection(collection)
    mongoConfig.insert_json(collection, json.loads(record_json))


if __name__ == "__main__":
    prepare_data()
