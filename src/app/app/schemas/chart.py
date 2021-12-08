import datetime
from datetime import date
from typing import List

from pydantic import BaseModel

from app.schemas.charted_song import ChartedSong


class BaseChart(BaseModel):
    name: str
    user_id: int

    class Config:
        arbitrary_types_allowed = True


class CreateChartSchema(BaseChart):
    date: str


class UpdateChartSchema(BaseChart):
    pass


class Chart(BaseChart):
    chart_songs: List[ChartedSong]
    date: datetime.date

    class Config:
        orm_mode = True
