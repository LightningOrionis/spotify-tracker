from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class Author(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)

    songs = relationship("Association", back_populates="author")
