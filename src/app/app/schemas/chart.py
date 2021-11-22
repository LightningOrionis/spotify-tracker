from datetime import date

from pydantic import BaseModel


class BaseChart(BaseModel):
    date: date
    name: str


class CreateChartSchema(BaseChart):
    user_id: int


class UpdateChartSchema(BaseChart):
    user_id: int
