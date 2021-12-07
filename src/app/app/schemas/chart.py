from datetime import date
from typing import List

from pydantic import BaseModel

from app.models.charted_song import ChartedSong


class BaseChart(BaseModel):
    date: date
    name: str
    user_id: int


class CreateChartSchema(BaseChart):
    pass


class UpdateChartSchema(BaseChart):
    pass


class Chart(BaseChart):
    charted_songs: List[ChartedSong]

    class Config:
        arbitrary_types_allowed = True
