import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from app.api import alert_router
from app.api.dashboard_router import router as dashboard_router
from app.api.health_check_router import router as health_check_router
from app.api.service_router import router as service_router
from app.api.statistics_router import router as statistics_router
from app.api.stellar_router import router as stellar_router
from app.core.config import settings
from app.db.database import engine
from app.workers.monitor_worker import monitor_services

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

# Allow the React/Vite frontend to communicate with the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    SQLModel.metadata.create_all(engine)

    # Start the background monitoring worker
    asyncio.create_task(monitor_services())


app.include_router(service_router)
app.include_router(health_check_router)
app.include_router(statistics_router)
app.include_router(dashboard_router)
app.include_router(alert_router.router)
app.include_router(stellar_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
