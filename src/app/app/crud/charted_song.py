import datetime
from typing import Dict

from sqlalchemy.orm import Session

from app.crud.base import BaseCRUD
from app.models.chart import Chart
from app.models.charted_song import ChartedSong
from app.schemas.charted_song import CreateChartedSongSchema, UpdateChartedSongSchema


class ChartedSongCRUD(BaseCRUD[ChartedSong, CreateChartedSongSchema, UpdateChartedSongSchema]):  # type: ignore
    def get_places_on_dates(
        self, session: Session, start_date: datetime.date, end_date: datetime.date, user_id: int, song_id: int
    ) -> Dict[Chart, int]:

        chart_songs = (
            session.query(ChartedSong)
            .join(Chart)
            .filter(
                ChartedSong.song_id == song_id,
                Chart.user_id == user_id,
                Chart.date >= start_date,
                Chart.date <= end_date,
            )
        )

        result = {chart_song.chart: chart_song.place for chart_song in chart_songs}

        return result
