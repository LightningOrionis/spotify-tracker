from fastapi import APIRouter

from app.api.v1.endpoints import chart, user, author, song, charted_song

router = APIRouter()
router.include_router(chart.router, prefix="/charts")
router.include_router(user.router, prefix="/users")
router.include_router(author.router, prefix="/authors")
router.include_router(song.router, prefix="/songs")
router.include_router(charted_song.router, prefix="/csongs")

