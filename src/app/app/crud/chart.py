from app.models.chart import Chart
from app.schemas.chart import CreateChartSchema, UpdateChartSchema

from .base import BaseCRUD


class ChartCRUD(BaseCRUD[Chart, CreateChartSchema, UpdateChartSchema]):  # type: ignore
    pass
