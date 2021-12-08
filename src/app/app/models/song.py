from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base_class import Base
# from app.models.author_song_association import SongAuthorAssociation  # noqa


class Song(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)

    # authors = relationship("SongAuthorAssociation", back_populates="song")
    author = relationship("Author", back_populates="songs")
    chart_songs = relationship("ChartedSong", back_populates="song")
