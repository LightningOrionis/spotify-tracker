from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str
    spotify_access_token: Optional[str]
    spotify_refresh_token: Optional[str]


class CreateUserSchema(BaseUser):
    id: int
    password: str


class UpdateUserSchema(BaseUser):
    password: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True
