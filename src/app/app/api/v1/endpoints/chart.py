import datetime
from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api import deps
from app.crud.chart import ChartCRUD
from app.models.chart import Chart
from app.models.user import User
from app.schemas.chart import CreateChartSchema, Chart as ChartSchema

router = APIRouter()
STR_CONVERT_PATTERN = "%d-%m-%Y"
DATE_REGEX_PATTERN = r"[\d]{1,2}-[\d]{1,2}-[\d]{4}"


@router.get("/per_days", response_model=List[ChartSchema])
async def get_all_charts_per_days(
    session=Depends(deps.get_db_session),
    date_start: str = Query(
        (datetime.date.today() - datetime.timedelta(days=7)).strftime(STR_CONVERT_PATTERN), regex=DATE_REGEX_PATTERN
    ),
    date_end: str = Query(datetime.date.today().strftime(STR_CONVERT_PATTERN), regex=DATE_REGEX_PATTERN),
    user: User = Depends(deps.get_current_user),
) -> dict:
    crud = ChartCRUD(Chart)
    all_charts = crud.get_charts_between_days(
        session=session,
        date_start=datetime.datetime.strptime(date_start, STR_CONVERT_PATTERN),
        date_end=datetime.datetime.strptime(date_end, STR_CONVERT_PATTERN),
        user_id=user.id,
    )
    return all_charts


@router.get("/{chart_name}", response_model=ChartSchema)
async def get_chart_by_chart_name(
    chart_name: str, session=Depends(deps.get_db_session), user=Depends(deps.get_current_user)
) -> dict:
    crud = ChartCRUD(Chart)
    chart = crud.get_chart_by_name(session=session, name=chart_name, user_id=user.id)
    return chart


@router.post('/', response_model=ChartSchema)
async def create_chart(chart: CreateChartSchema, session=Depends(deps.get_db_session)):
    crud = ChartCRUD(Chart)
    chart = crud.create(session, chart)

    return chart


@router.get("/", response_model=List[ChartSchema])
async def get_all(session=Depends(deps.get_db_session)):
    crud = ChartCRUD(Chart)
    charts = crud.get_all(session)

    return charts


@router.delete("/{id}")
async def remove(id: int, session = Depends(deps.get_db_session)):
    crud = ChartCRUD(Chart)
    return crud.delete(session, id)


@router.patch("/{id}/{user_id}", response_model=ChartSchema)
async def patch(id: int, user_id: int, session: Session = Depends(deps.get_db_session)):
    obj = session.query(Chart).get(id)
    obj.user_id = 2
    session.commit()
    return obj