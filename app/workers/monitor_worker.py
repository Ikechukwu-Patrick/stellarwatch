import asyncio

from sqlmodel import Session, select

from app.core.config import settings
from app.db.database import engine
from app.models.service import Service
from app.monitoring.health_checker import check_service


async def monitor_services():
    while True:
        print("Running background health checks...")

        with Session(engine) as session:
            services = session.exec(
                select(Service).where(Service.is_active == True)
            ).all()

            for service in services:
                try:
                    check_service(service)
                    print(f"Checked: {service.name}")
                except Exception as e:
                    print(f"Failed to check {service.name}: {e}")

        await asyncio.sleep(settings.MONITOR_INTERVAL)