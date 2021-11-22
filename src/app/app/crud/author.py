from app.models.author import Author
from app.schemas.author import CreateAuthorSchema, UpdateAuthorSchema

from .base import BaseCRUD


class AuthorCRUD(BaseCRUD[Author, CreateAuthorSchema, UpdateAuthorSchema]):  # type: ignore
    pass
