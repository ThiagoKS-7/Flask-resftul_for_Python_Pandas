from pymongo import MongoClient


def set_database():
    client = client = MongoClient("172.16.57.2",27017)
    db = client.PythonPandas
    collection = db.Users
    return client, db, collection