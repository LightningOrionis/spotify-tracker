from datetime import date

from app.database.base import Base
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Chart(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False, default=date.today())
    name = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    chart_songs = relationship("ChartedSong", back_populates="chart")
    user = relationship("User", back_populates="user")
