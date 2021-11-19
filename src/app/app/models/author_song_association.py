from app.database.base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class SongAuthorAssociation(Base):
    song_id = Column(Integer, ForeignKey("song.id"), primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"), primary_key=True)

    song = relationship("Song", back_populates="association")
    author = relationship("Author", back_populates="association")
