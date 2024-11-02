from typing import List, Optional
from pydantic import BaseModel


class Path(BaseModel):
    id: Optional[str]
    name: Optional[str]
    thumbnail: Optional[str]


class CourseResource(BaseModel):
    id: Optional[str]
    archive: Optional[str]


class Course(BaseModel):
    id: Optional[str]
    name: Optional[str]
    thumbnail: Optional[str]
    school_ids: Optional[List[str]]
    resource_id: Optional[str]


class School(BaseModel):
    id: Optional[str]
    name: Optional[str]
    thumbnail: Optional[str]


class StreakDay(BaseModel):
    dt: Optional[int]


class DayCover(BaseModel):
    dt: Optional[int]


class Stats(BaseModel):
    points: Optional[int]
    streak_days: Optional[List[StreakDay]]
    train_days: Optional[int]
    cover_days: Optional[List[DayCover]]


class User(BaseModel):
    username: Optional[str]
    name: Optional[str]
    thumbnail: Optional[str]
    stats: Optional[Stats]
    courses: Optional[List[Course]]
    paths: Optional[List[Path]]


class ChallengeResource(BaseModel):
    id: Optional[str]
    archive: Optional[str]


class Challenge(BaseModel):
    id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    created_at: Optional[int]
    duration_sec: Optional[int]
    resource_id: Optional[str]
    award_points: Optional[int]


class UserChallenges(BaseModel):
    id: Optional[str]
    user_id: Optional[str]
    challenge_ids: Optional[List[str]]
