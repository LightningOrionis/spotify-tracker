from sqlalchemy.orm import Session

from app.crud.base import BaseCRUD
from app.models.author import Author
from app.schemas.author import CreateAuthorSchema, UpdateAuthorSchema


class AuthorCRUD(BaseCRUD[Author, CreateAuthorSchema, UpdateAuthorSchema]):  # type: ignore
    def get_by_name(self, session: Session, name: str):
        obj = session.query(Author).filter(Author.name == name).first()
        return obj

    def create(self, session: Session, author: CreateAuthorSchema):
        model = Author(
            id=author.id,
            name=author.name
        )

        session.add(model)
        session.commit()
        session.refresh(model)

        return model