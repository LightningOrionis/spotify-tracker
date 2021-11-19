from app.database.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    spotify_access_token = Column(String)
    spotify_refresh_token = Column(String)

    charts = relationship("Chart", back_populates="user")
