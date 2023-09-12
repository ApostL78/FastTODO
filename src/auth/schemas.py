import datetime

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    username: str
    email: str
    registered_at: datetime.datetime


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str


class UserUpdate(schemas.BaseUserUpdate):
    pass
