from app.database.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Author(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)

    songs = relationship("Association", back_populates="author")
