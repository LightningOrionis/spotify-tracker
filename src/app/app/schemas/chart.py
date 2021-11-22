from datetime import date

from pydantic import BaseModel


class BaseChart(BaseModel):
    date: date
    name: str
    user_id: int


class CreateChartSchema(BaseChart):
    pass


class UpdateChartSchema(BaseChart):
    pass
