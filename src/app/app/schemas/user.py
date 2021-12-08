from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str


class CreateUserSchema(BaseUser):
    id: int
    password: str
    code: str


class UpdateUserSchema(BaseUser):
    password: str


class User(BaseUser):
    id: int
    spotify_access_token: str
    spotify_refresh_token: str

    class Config:
        orm_mode = True
