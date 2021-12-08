import datetime

from sqlalchemy.orm import Session

from app.crud.base import BaseCRUD
from app.models.chart import Chart
from app.schemas.chart import CreateChartSchema, UpdateChartSchema


class ChartCRUD(BaseCRUD[Chart, CreateChartSchema, UpdateChartSchema]):  # type: ignore
    def create(self, session: Session, obj_to_add: CreateChartSchema) -> Chart:
        chart = Chart(
            date=datetime.datetime.strptime(obj_to_add.date, "%d-%m-%Y"),
            name=obj_to_add.name,
            user_id=obj_to_add.user_id
        )

        session.add(chart)
        session.commit()
        session.refresh(chart)

        return chart

    def get_user_charts_in_day(self, session: Session, date: datetime.date, user_id: int):
        objects = session.query(Chart).filter(Chart.user_id == user_id, Chart.date == date).all()
        return objects

    def get_charts_between_days(
        self, session: Session, date_start: datetime.date, date_end: datetime.date, user_id: int
    ):
        objects = (
            session.query(Chart)
            .filter(
                Chart.user_id == user_id,
                Chart.date >= date_start,
                Chart.date <= date_end,
            )
            .all()
        )
        return objects

    def get_chart_by_name(self, session: Session, name: str, user_id: int):
        objects = session.query(Chart).filter(Chart.user_id == user_id, Chart.name == name).all()
        return objects
