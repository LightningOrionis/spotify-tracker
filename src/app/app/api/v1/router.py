from fastapi import APIRouter

from app.api.v1.endpoints import chart

router = APIRouter()
router.include_router(chart.router, prefix="/charts")
