import datetime

from sqlalchemy.orm import Session

from app.crud.base import BaseCRUD
from app.models.chart import Chart
from app.schemas.chart import CreateChartSchema, UpdateChartSchema


class ChartCRUD(BaseCRUD[Chart, CreateChartSchema, UpdateChartSchema]):  # type: ignore
    def get_user_charts_in_day(self, session: Session, date: datetime.date, user_id: int):
        objects = session.query(Chart).filter(Chart.user_id == user_id, Chart.date == date).all()
        return objects
