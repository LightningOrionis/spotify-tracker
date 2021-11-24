from app.crud.base import BaseCRUD
from app.models.song import Song
from app.schemas.song import CreateSongSchema, UpdateSongSchema


class SongCRUD(BaseCRUD[Song, CreateSongSchema, UpdateSongSchema]):  # type: ignore
    pass
