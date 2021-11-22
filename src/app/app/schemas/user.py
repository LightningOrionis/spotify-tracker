from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str
    hashed_password: str


class CreateUserSchema(BaseUser):
    id: int


class UpdateUserSchema(BaseUser):
    pass
