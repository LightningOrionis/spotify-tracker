from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.song import Song as SongSchema, CreateSongSchema
from app.models.song import Song
from app.crud.song import SongCRUD
from app.api import deps


router = APIRouter()
crud = SongCRUD(Song)


@router.post("/", response_model=SongSchema)
async def create_song(song: CreateSongSchema, session: Session = Depends(deps.get_db_session)):
    return crud.create(session, song)


@router.get("/", response_model=List[SongSchema])
async def get_all(session: Session = Depends(deps.get_db_session)):
    return crud.get_all(session)
