from typing import Optional

from sqlalchemy.orm import Session

from app.core import security
from app.crud.base import BaseCRUD
from app.models.user import User
from app.schemas.user import CreateUserSchema, UpdateUserSchema


class UserCRUD(BaseCRUD[User, CreateUserSchema, UpdateUserSchema]):  # type: ignore
    def create(self, session: Session, obj_to_add: CreateUserSchema) -> User:
        db_obj = User(
            id=obj_to_add.id,
            email=obj_to_add.email,
            hashed_password=security.get_password_hash(obj_to_add.password),
            spotify_access_token=obj_to_add.spotify_access_token,
            spotify_refresh_token=obj_to_add.spotify_refresh_token,
        )

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)

        return db_obj

    def get_by_email(self, session: Session, email: str) -> Optional[User]:
        return session.query(User).filter(User.email == email).first()

    def authenticate(self, session: Session, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(session, email)

        if not user:
            return None
        if not security.verify_password(password, user.hashed_password):
            return None

        return user
