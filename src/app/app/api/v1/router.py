from fastapi import APIRouter

from app.api.v1.endpoints import chart, user

router = APIRouter()
router.include_router(chart.router, prefix="/charts")
router.include_router(user.router, prefix="/users")
