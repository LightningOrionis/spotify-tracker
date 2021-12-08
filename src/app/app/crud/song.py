from sqlalchemy.orm import Session

from app.crud.base import BaseCRUD
from app.crud.author import AuthorCRUD
from app.models.song import Song
from app.models.author import Author
from app.schemas.song import CreateSongSchema, UpdateSongSchema


class SongCRUD(BaseCRUD[Song, CreateSongSchema, UpdateSongSchema]):  # type: ignore
    def create(self, session: Session, obj_to_add: CreateSongSchema) -> Song:
        crud = AuthorCRUD(Author)
        author = crud.get(session, id=obj_to_add.author_id)
        model = Song(
            id=obj_to_add.id,
            name=obj_to_add.name,
            author=author
        )

        session.add(model)
        session.commit()
        session.refresh(model)

        return model
