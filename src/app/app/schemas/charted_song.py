from pydantic import BaseModel


class BaseChartedSong(BaseModel):
    place: int
    song_id: int
    chart_id: int


class CreateChartedSongSchema(BaseChartedSong):
    pass


class UpdateChartedSongSchema(BaseChartedSong):
    pass
