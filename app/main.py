import asyncio

from fastapi import FastAPI
from sqlmodel import SQLModel

from app.api.service_router import router as service_router
from app.core.config import settings
from app.db.database import engine
from app.models.health_check import HealthCheck
from app.models.service import Service
from app.workers.monitor_worker import monitor_services
from app.api.health_check_router import router as health_check_router

from app.api.health_check_router import router as health_check_router

from app.api.health_check_router import (
    router as health_check_router,
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)


@app.on_event("startup")
async def on_startup():
    SQLModel.metadata.create_all(engine)

    # Start the background monitoring worker
    asyncio.create_task(monitor_services())


app.include_router(service_router)

app.include_router(health_check_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
    }


@app.get("/health")
def health():
    return {"status": "healthy"}