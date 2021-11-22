from pydantic import BaseModel


class BaseSong(BaseModel):
    name: str


class CreateSongSchema(BaseSong):
    id: int
    author_id: int


class UpdateSongSchema(BaseSong):
    author_id: int
