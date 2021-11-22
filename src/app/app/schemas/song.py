from pydantic import BaseModel


class BaseSong(BaseModel):
    name: str


class CreateSongSchema(BaseSong):
    id: int
    authors: list


class UpdateSongSchema(BaseSong):
    pass
