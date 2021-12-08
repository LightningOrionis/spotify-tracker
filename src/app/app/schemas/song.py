from typing import List

from pydantic import BaseModel

from app.schemas.author import NestedAuthorToAdd


class BaseSong(BaseModel):
    name: str


class CreateSongSchema(BaseSong):
    id: int
    author_id: int


class UpdateSongSchema(BaseSong):
    pass


class Song(CreateSongSchema):
    class Config:
        orm_mode = True
