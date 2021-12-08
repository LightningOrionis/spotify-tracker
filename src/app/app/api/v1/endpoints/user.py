from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps
from app.core import security
from app.core.config import SETTINGS
from app.crud.user import UserCRUD
from app.models.user import User
from app.schemas.token import Token
from app.schemas.user import CreateUserSchema
from app.schemas.user import User as UserSchema

router = APIRouter()
crud = UserCRUD(User)


@router.post("/login", response_model=Token)
def login_user(session: Session = Depends(deps.get_db_session), form: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = crud.authenticate(session, form.username, form.password)

    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized. Invalid credentials")

    access_token_expires = timedelta(minutes=SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        "access_token": security.create_access_token(user.id, expires_delta=access_token_expires),
        "token_type": "bearer",
    }


@router.post("/register", response_model=UserSchema)
def register(user_in: CreateUserSchema, session: Session = Depends(deps.get_db_session)):
    user = crud.get_by_email(session, user_in.email)

    if user:
        raise HTTPException(status_code=400, detail="User with such email already exists")
    try:
        user = crud.create(session, user_in)
    except KeyError:
        raise HTTPException(status_code=401, detail="Bad spotify user code")

    return user
