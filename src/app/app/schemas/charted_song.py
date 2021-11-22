from pydantic import BaseModel


class BaseChartedSong(BaseModel):
    place: int


class CreateChartedSongSchema(BaseChartedSong):
    song_id: int
    chart_id: int


class UpdateChartedSongSchema(BaseChartedSong):
    song_id: int
    chart_id: int
