from sqlalchemy import Integer, ForeignKey, Table, Column
from sqlalchemy.orm import relationship

from app.database.base import Base


class SongAuthorAssociation(Base):
    song_id = Column(Integer, ForeignKey("song.id"), primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"), primary_key=True)

    song = relationship("Song", back_populates="association")
    author = relationship("Author", back_populates="association")
