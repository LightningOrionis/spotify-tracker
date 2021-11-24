from app.crud.base import BaseCRUD
from app.models.user import User
from app.schemas.user import CreateUserSchema, UpdateUserSchema


class UserCRUD(BaseCRUD[User, CreateUserSchema, UpdateUserSchema]):  # type: ignore
    pass
