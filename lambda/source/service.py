from pymongo.collection import Collection
from typing import List

from source.config import MONGO_HANDLER
from source.model import User, Challenge, UserChallenges

import random

DATABASE_NAME = "platzi_daily"


class DataCollection:
    collection: Collection

    COLLECTION_NAME = ""

    def __init__(self):
        self.collection = MONGO_HANDLER.collection(DATABASE_NAME, self.COLLECTION_NAME)


class UserData(DataCollection):
    COLLECTION_NAME = "users"

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


class ChallengeData(DataCollection):
    COLLECTION_NAME = "challenges"

    def get_challenges(self) -> List[Challenge]:
        challenges = []
        response = self.collection.find({}, {"id": 1, "name": 1, "description": 1})

        for doc in response:
            challenges.append(Challenge.parse_obj(doc))

        return challenges

    def get_challenge_by_id(self, id: str) -> Challenge:
        response = self.collection.find_one({"id": id})

        return Challenge.parse_obj(response)

    def insert_challenge(self, challenge: Challenge) -> str:
        response = self.collection.insert_one(challenge.dict(exclude_none=True))
        return response.inserted_id

    def insert_challenge_bulk(self, challenges: List[Challenge]):
        response = self.collection.insert_many(
            [challenge.dict(exclude_none=True) for challenge in challenges]
        )
        return response


class UserChallenge(DataCollection):
    COLLECTION_NAME = "user_challenges"

    def get_challenges(self, username: str) -> List[UserChallenges]:
        challenges = []
        response = self.collection.find(
            {"username": username}, {"id": 1, "challenge_ids": 1}
        )

        for doc in response:
            challenges.append(UserChallenges.parse_obj(doc))

        return challenges

    def get_random_challenge(self, username: str) -> Challenge:
        response = self.collection.find_one(
            {"username": username}, {"id": 1, "challenge_ids": 1}
        )

        challenges_ids = UserChallenges.parse_obj(response).challenge_ids
        random_id = random.choice(challenges_ids)

        return ChallengeData().get_challenge_by_id(random_id)

    def insert_user_challenges(self, user_challenge: UserChallenges) -> str:
        response = self.collection.insert_one(user_challenge.dict(exclude_none=True))
        return response.inserted_id

    def insert_user_challenges_bulk(self, user_challenges: List[UserChallenges]):
        response = self.collection.insert_many(
            [challenge.dict(exclude_none=True) for challenge in user_challenges]
        )
        return response
