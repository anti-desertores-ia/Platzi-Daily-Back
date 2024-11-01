from source.service import UserData, UserChallenge
from source.config import LOGGER

from pydantic import BaseSettings


class Settings(BaseSettings):
    ranking_num_people: int


SETTINGS = Settings()


def get_users(*args, **kwargs) -> dict:
    response = []

    try:
        user_data = UserData().get_users()
        response = dict(response=[user.dict(exclude_none=True) for user in user_data])
    except Exception as e:
        LOGGER.error(f"Couldnt retrieve users: {e}")

    return response


def get_ranking(*args, **kwargs):
    response = []

    try:
        user_data = UserData().get_ranking_top(num_users=SETTINGS.ranking_num_people)
        response = dict(response=[user.dict(exclude_none=True) for user in user_data])
    except Exception as e:
        LOGGER.error(f"Couldnt retrieve users: {e}")

    return response


def get_user(username: str, *args, **kwargs):
    response = None

    try:
        user_data = UserData().get_user_by_username(username=username)
        response = dict(response=user_data.dict(exclude_none=True))
    except Exception as e:
        LOGGER.error(f"Couldnt retrieve users: {e}")

    return response


def get_challenge_by_user(username: str, *args, **kwargs):
    response = None

    try:
        user_challenges = UserChallenge().get_challenges(username=username)
        response = dict(response=user_challenges.dict(exclude_none=True))
    except Exception as e:
        LOGGER.error(f"Couldnt retrieve challenges for {username}: {e}")

    return response


def get_random_challenge_by_user(username: str, *args, **kwargs):
    response = None

    try:
        user_challenges = UserChallenge().get_random_challenge(username=username)
        response = dict(response=user_challenges.dict(exclude_none=True))
    except Exception as e:
        LOGGER.error(f"Couldnt retrieve random challenge for {username}: {e}")

    return response


def empty(*args, **kwargs):
    return {}
