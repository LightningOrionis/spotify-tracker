from app.models.charted_song import ChartedSong
from app.schemas.charted_song import CreateChartedSongSchema, UpdateChartedSongSchema

from .base import BaseCRUD


class ChartedSongCRUD(BaseCRUD[ChartedSong, CreateChartedSongSchema, UpdateChartedSongSchema]):  # type: ignore
    pass
