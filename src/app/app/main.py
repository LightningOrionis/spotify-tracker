import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.router import router
from app.core.config import SETTINGS

app = FastAPI(
    title=SETTINGS.PROJECT_NAME,
    openapi_url=f"{SETTINGS.API_V1_STR}/openapi.json",
)


if SETTINGS.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in SETTINGS.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


if __name__ == "__main__":
    app.include_router(router, prefix=SETTINGS.API_V1_STR)
    uvicorn.run(app, host="0.0.0.0", port=3000)
