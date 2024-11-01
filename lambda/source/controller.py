from source.service import UserData
from source.config import LOGGER

from pydantic import BaseSettings


class Settings(BaseSettings):
    ranking_num_people: int


SETTINGS = Settings()


def get_users(*args, **kwargs) -> dict:
    user_data = []

    try:
        user_data = UserData().get_users()
    except Exception as e:
        LOGGER.error(f"Couldnt retrieve users: {e}")

    return dict(response=[user.dict(exclude_none=True) for user in user_data])


def get_ranking(*args, **kwargs):
    user_data = []

    try:
        user_data = UserData().get_ranking_top(num_users=SETTINGS.ranking_num_people)
    except Exception as e:
        LOGGER.error(f"Couldnt retrieve users: {e}")

    return dict(response=[user.dict(exclude_none=True) for user in user_data])


def get_user(username: str, *args, **kwargs):
    user_data = None

    try:
        user_data = UserData().get_user_by_username(username=username)
    except Exception as e:
        LOGGER.error(f"Couldnt retrieve users: {e}")

    return dict(response=user_data.dict(exclude_none=True))


def empty(*args, **kwargs):
    return {}
