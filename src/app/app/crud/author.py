from sqlalchemy.orm import Session

from app.models.author import Author
from app.schemas.author import CreateAuthorSchema, UpdateAuthorSchema

from .base import BaseCRUD


class AuthorCRUD(BaseCRUD[Author, CreateAuthorSchema, UpdateAuthorSchema]):  # type: ignore
    def get_by_name(self, session: Session, name: str):
        obj = session.query(Author).filter(Author.name == name).first()
        return obj
