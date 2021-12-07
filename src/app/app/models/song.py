from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base_class import Base
from app.models.author_song_association import SongAuthorAssociation  # noqa


class Song(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    authors = relationship("SongAuthorAssociation", back_populates="song")
    chart_songs = relationship("ChartedSong", back_populates="song")
