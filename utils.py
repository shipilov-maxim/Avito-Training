from pymongo import MongoClient

from config.settings import MONGO_HOST, MONGO_PORT, MONGO_USERNAME, MONGO_PASSWORD, MONGO_DB


def get_db_handle():

    client = MongoClient(host=MONGO_HOST,
                         port=int(MONGO_PORT),
                         username=MONGO_USERNAME,
                         password=MONGO_PASSWORD
                         )
    db_handle = client.MONGO_DB.to_do_item
    return db_handle
