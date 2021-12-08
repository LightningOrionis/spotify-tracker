from pydantic import BaseModel


class BaseAuthor(BaseModel):
    name: str


class CreateAuthorSchema(BaseAuthor):
    id: int


class UpdateAuthorSchema(BaseAuthor):
    pass


class Author(BaseAuthor):
    id: int

    class Config:
        orm_mode = True


class NestedAuthorToAdd(BaseModel):
    id: int

    class Config:
        orm_mode = True
