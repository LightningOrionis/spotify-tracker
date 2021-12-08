from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database.base_class import Base
from app.models.author import Author  # noqa


# class SongAuthorAssociation(Base):
#     song_id = Column(Integer, ForeignKey("song.id"), primary_key=True)
#     author_id = Column(Integer, ForeignKey("author.id"), primary_key=True)
#
#     song = relationship("Song", back_populates="authors")
#     author = relationship("Author", back_populates="songs")
