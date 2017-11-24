import time

import mongoConfig
import tushare
import json


def prepare_data():
    real_time_box_office = tushare.realtime_boxoffice()
    if real_time_box_office is None or real_time_box_office.empty:
        return
    record_json = real_time_box_office.to_json(orient='records')
    print(record_json)
    collection = mongoConfig.get_collection_default("realtime_boxoffice")
    current_date = time.strftime("%Y-%m-%d")
    mongoConfig.clear_collection(collection)
    # mongoConfig.remove(collection, {"time": {'$regex': current_date}})
    mongoConfig.insert_json(collection, json.loads(record_json))


if __name__ == "__main__":
    prepare_data()
