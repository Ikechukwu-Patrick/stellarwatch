from fastapi import FastAPI
from sqlmodel import SQLModel

from app.api.service_router import router as service_router
from app.core.config import settings
from app.db.database import engine
from app.models.service import Service

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


app.include_router(service_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


from app.models.health_check import HealthCheck    