from typing import List, Optional
from pydantic import BaseModel


class Path(BaseModel):
    id: str
    name: str
    thumbnail: str


class CourseResource(BaseModel):
    id: str
    archive: str


class Course(BaseModel):
    id: str
    name: str
    thumbnail: str
    school_ids: List[str]
    resource_id: str


class School(BaseModel):
    id: str
    name: str
    thumbnail: str


class StreakDay(BaseModel):
    dt: int


class DayCover(BaseModel):
    dt: int


class Stats(BaseModel):
    points: int
    streak_days: List[StreakDay]
    train_days: int
    cover_days: List[DayCover]


class User(BaseModel):
    username: Optional[str]
    name: Optional[str]
    thumbnail: Optional[str]
    stats: Optional[Stats]
    courses: Optional[List[Course]]
    paths: Optional[List[Path]]


class ChallengeResource(BaseModel):
    id: str
    archive: str


class Challenge(BaseModel):
    id: str
    name: str
    description: str
    created_at: int
    duration_sec: int
    resource_id: str
    award_points: int


class UserChallenges(BaseModel):
    id: str
    user_id: str
    challenge_ids: List[str]
