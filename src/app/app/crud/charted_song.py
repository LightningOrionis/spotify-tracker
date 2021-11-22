import datetime
from typing import Dict

from sqlalchemy.orm import Session

from app.models.chart import Chart
from app.models.charted_song import ChartedSong
from app.schemas.charted_song import CreateChartedSongSchema, UpdateChartedSongSchema

from .base import BaseCRUD


class ChartedSongCRUD(BaseCRUD[ChartedSong, CreateChartedSongSchema, UpdateChartedSongSchema]):  # type: ignore
    def get_places_on_dates(
        self, session: Session, start_date: datetime.date, end_date: datetime.date, user_id: int, song_id: int
    ) -> Dict[Chart, int]:
        result = {}

        charts = (
            session.query(Chart).filter(Chart.date > start_date, Chart.date < end_date, Chart.user_id == user_id).all()
        )

        for chart in charts:
            for chart_song in chart.chart_songs:
                if chart_song.song_id == song_id:
                    result[chart] = chart_song.place
                    break

        return result
