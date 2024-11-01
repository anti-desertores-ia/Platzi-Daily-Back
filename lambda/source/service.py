from pymongo.collection import Collection
from typing import List

from source.config import MONGO_HANDLER
from source.model import User


class UserData:
    collection: Collection

    DATABASE_NAME = "platzi_daily"
    USER_COLLECTION_NAME = "users"

    def __init__(self):
        self.collection = MONGO_HANDLER.collection(
            self.DATABASE_NAME, self.USER_COLLECTION_NAME
        )

    def get_users(self) -> List[User]:
        users = []
        response = self.collection.find({}, {"username": 1, "name": 1, "thumbnail": 1})

        for doc in response:
            users.append(User.parse_obj(doc))

        return users

    def get_user_by_username(self, username: str) -> User:
        response = self.collection.find_one({"username": username})

        return User.parse_obj(response)

    def get_ranking_top(self, num_users: int) -> List[User]:
        users = []
        response = (
            self.collection.find(
                {}, {"username": 1, "stats.points": 1, "name": 1, "thumbnail": 1}
            )
            .sort("stats.points", -1)
            .limit(num_users)
        )

        for doc in response:
            users.append(User.parse_obj(doc))

        return users

    def insert_user(self, user: User) -> str:
        response = self.collection.insert_one(user.dict(exclude_none=True))
        return response.inserted_id

    def insert_user_bulk(self, users: List[User]):
        response = self.collection.insert_many(
            [user.dict(exclude_none=True) for user in users]
        )
        return response
