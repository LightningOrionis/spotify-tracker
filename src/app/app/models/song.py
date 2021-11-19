from app.database.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Song(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)

    authors = relationship("Association", back_populates="song")
    chart_songs = relationship("ChartSong", back_populates="song")
