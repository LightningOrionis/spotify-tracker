from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str
    hashed_password: str
    spotify_access_token: Optional[str]
    spotify_refresh_token: Optional[str]


class CreateUserSchema(BaseUser):
    id: int


class UpdateUserSchema(BaseUser):
    pass
