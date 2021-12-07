from pydantic import BaseModel

from app.schemas.song import Song


class BaseChartedSong(BaseModel):
    place: int


class CreateChartedSongSchema(BaseChartedSong):
    chart_id: int
    song_id: int


class UpdateChartedSongSchema(CreateChartedSongSchema):
    pass


class ChartedSong(BaseChartedSong):
    song: Song

    class Config:
        orm_mode = True
