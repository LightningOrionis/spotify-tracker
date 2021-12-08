import datetime
from typing import List, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.charted_song import ChartedSong as CSSchema, CreateChartedSongSchema
from app.models.charted_song import ChartedSong
from app.crud.charted_song import ChartedSongCRUD
from app.models.chart import Chart
from app.crud.chart import ChartCRUD
from app.models.song import Song
from app.schemas.chart import Chart as ChartSchema
from app.schemas.song import Song as SongSchema
from app.api import deps


router = APIRouter()
crud = ChartedSongCRUD(ChartedSong)


@router.post("/", response_model=CSSchema)
async def create_song(song: CreateChartedSongSchema, session: Session = Depends(deps.get_db_session)):
    return crud.create(session, song)


@router.get("/", response_model=List[CSSchema])
async def get_all(session: Session = Depends(deps.get_db_session)):
    return crud.get_all(session)


@router.delete("/{id}")
async def remove(id: int, session: Session = Depends(deps.get_db_session)):
    return crud.delete(session, id)


@router.get("/get_difference/{start_date}/{end_date}", response_model=List[Dict[str, Dict[datetime.date, int]]])
def get_difference(
        start_date: str, end_date: str, session: Session=Depends(deps.get_db_session), user=Depends(deps.get_current_user)
):
    start_date_dt = datetime.datetime.strptime(start_date, "%d-%m-%Y").date()
    end_date_dt = datetime.datetime.strptime(end_date, "%d-%m-%Y").date()
    charts = session.query(Chart).filter(
        Chart.date >= start_date_dt,
        Chart.date <= end_date_dt
    ).all()
    song_ids = {cs.song.id for chart in charts for cs in chart.chart_songs}
    result = []
    for song_id in song_ids:
        song = session.query(Song).get(song_id)
        dates_and_places = crud.get_places_on_dates(session, start_date_dt, end_date_dt, user.id, song_id)
        places = [v for k, v in dates_and_places.items()]
        # return places
        if len(set(places)):
            result.append({song.name: dates_and_places})
    return result