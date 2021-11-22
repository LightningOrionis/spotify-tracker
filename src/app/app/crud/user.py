from app.models.user import User
from app.schemas.user import CreateUserSchema, UpdateUserSchema

from .base import BaseCRUD


class UserCRUD(BaseCRUD[User, CreateUserSchema, UpdateUserSchema]):  # type: ignore
    pass
