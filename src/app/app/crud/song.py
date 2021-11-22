from app.models.song import Song
from app.schemas.song import CreateSongSchema, UpdateSongSchema

from .base import BaseCRUD


class SongCRUD(BaseCRUD[Song, CreateSongSchema, UpdateSongSchema]):  # type: ignore
    pass
