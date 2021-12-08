from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Author(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)

    # songs = relationship("SongAuthorAssociation", back_populates="author")
    songs = relationship("Song", back_populates="author")
