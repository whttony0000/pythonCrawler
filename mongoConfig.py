import pymongo
from pymongo import MongoClient


# 获取client
def get_client(_uri='mongodb://userName:password@host:port/defualt_db_name'):
    return MongoClient(_uri)


# 获取db
def get_db(_client, db_name='default_db_name'):
    return _client.get_database(db_name)


# 获取collection
def get_collection(_db, collection_name):
    return _db.get_collection(collection_name)


# 清楚所有记录
def clear_collection(_collection):
    _collection.remove()


def remove(_collection, _filter):
    _collection.remove(_filter)


# 插入
def insert_json(_collection, _json):
    _collection.insert(_json)


# 计数
def count_all(_collection):
    return _collection.find().count()


# 查询第一个
def select_one(_collection, _filter):
    return _collection.find_one(_filter)


# 查询所有
def select_many_asc(_collection, _filter, sort_field):
    return _collection.find(_filter).sort(sort_field, pymongo.ASCENDING)


# 查询所有
def select_many_desc(_collection, _filter, sort_field):
    return _collection.find(_filter).sort(sort_field, pymongo.DESCENDING)


# 更新
def update(_collection, where_clause, set_clause):
    _collection.update(where_clause, {"$set": set_clause})


def get_collection_default(collection_name):
    return get_collection(get_db(get_client()), collection_name)
