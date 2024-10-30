import logging

from pymongo import MongoClient
from pymongo.collection import Collection
from pydantic import BaseSettings

LOGGER = logging.getLogger()


class Settings(BaseSettings):
    mongo_connection_string_param_name: str


class MongoHandler:
    def __init__(self):
        self.settings = Settings()
        self.client = MongoClient(self.settings.mongo_connection_string_param_name)

    def collection(self, db_name: str, collection_name: str) -> Collection:
        return self.client[db_name][collection_name]


MONGO_HANDLER = MongoHandler()
