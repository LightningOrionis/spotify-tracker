from typing import AsyncGenerator

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError

from app.core.config import SETTINGS
from app.core.security import ALGORITHM
from app.crud.user import UserCRUD
from app.database.session import Session
from app.models.user import User
from app.schemas.token import TokenPayload

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{SETTINGS.API_V1_STR}/login/access-token")


async def get_db_session() -> AsyncGenerator:
    try:
        db = Session()
        yield db
    finally:
        db.close()


async def get_current_user(session: Session = Depends(get_db_session), token: str = Depends(reusable_oauth2)):
    try:
        payload = jwt.decode(jwt=token, key=SETTINGS.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    crud = UserCRUD(User)
    user = crud.get(session, id=token_data.sub)

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    return user
