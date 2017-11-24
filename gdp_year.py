import json

import tushare as ts

import mongoConfig


def prepare_data():
    deposit_rate = ts.get_gdp_year()
    record_json = deposit_rate.to_json(orient='records')
    print(record_json)
    collection = mongoConfig.get_collection_default("gdp_year")
    mongoConfig.clear_collection(collection)
    mongoConfig.insert_json(collection, json.loads(record_json))


if __name__ == "__main__":
    prepare_data()
