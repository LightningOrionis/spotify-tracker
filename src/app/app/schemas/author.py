from pydantic import BaseModel


class BaseAuthor(BaseModel):
    name: str


class CreateAuthorSchema(BaseAuthor):
    id: int


class UpdateAuthorSchema(BaseAuthor):
    pass
