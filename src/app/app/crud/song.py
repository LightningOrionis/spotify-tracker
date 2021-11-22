from sqlalchemy.orm import Session

from app.models.author_song_association import SongAuthorAssociation
from app.models.song import Song
from app.schemas.song import CreateSongSchema, UpdateSongSchema

from .base import BaseCRUD


class SongCRUD(BaseCRUD[Song, CreateSongSchema, UpdateSongSchema]):  # type: ignore
    def create(self, session: Session, obj_to_add: CreateSongSchema) -> Song:
        obj_data = obj_to_add.dict()

        for author in obj_to_add["authors"]:
            association_item = SongAuthorAssociation(author_id=author, song_id=obj_data["id"])
            session.add(association_item)
            session.commit()
            session.refresh(association_item)

        obj_data.pop("authors")
        song = Song(**obj_data)

        session.add(song)
        session.commit()
        session.refresh(song)

        return song
