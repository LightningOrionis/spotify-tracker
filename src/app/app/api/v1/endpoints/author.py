from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.author import Author as AuthorSchema
from app.models.author import Author
from app.crud.author import AuthorCRUD, CreateAuthorSchema
from app.api import deps


router = APIRouter()
crud = AuthorCRUD(Author)


@router.post("/", response_model=AuthorSchema)
async def create_author(author: CreateAuthorSchema, session: Session = Depends(deps.get_db_session)):
    return crud.create(session, author)


@router.get("/", response_model=List[AuthorSchema])
async def get_authors(session: Session = Depends(deps.get_db_session)):
    return crud.get_all(session)

