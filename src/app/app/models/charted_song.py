from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database.base import Base


class ChartedSong(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    place = Column(Integer, nullable=False)

    song_id = Column(Integer, ForeignKey("song.id"), nullable=False)
    chart_id = Column(Integer, ForeignKey("chart.id"), nullable=False)

    song = relationship("Song", back_populates="chart_songs")
    chart = relationship("Chart", back_populates="chart_songs")
