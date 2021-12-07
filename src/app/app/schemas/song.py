from typing import List

from pydantic import BaseModel

from app.schemas.author import BaseAuthor


class BaseSong(BaseModel):
    name: str


class CreateSongSchema(BaseSong):
    id: int
    authors: List[BaseAuthor]


class UpdateSongSchema(BaseSong):
    pass


class Song(CreateSongSchema):
    pass
