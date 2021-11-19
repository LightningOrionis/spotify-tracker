from datetime import date

from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Chart(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False, default=date.today())
    name = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    chart_songs = relationship("ChartedSong", back_populates="chart")
    user = relationship("User", back_populates="user")
