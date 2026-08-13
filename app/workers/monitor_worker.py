import asyncio

import httpx
from sqlmodel import Session, select

from app.core.config import settings
from app.db.database import engine
from app.models.service import Service
from app.monitoring.health_checker import check_service
from app.services.stellar_monitoring_service import monitor_stellar_network


async def run_monitoring_cycle():
    print("Running background health checks...")

    with Session(engine) as session:
        services = session.exec(select(Service).where(Service.is_active)).all()

        for service in services:
            try:
                check_service(service)
                print(f"Checked: {service.name}")

            except httpx.HTTPError as exc:
                print(f"Failed to check {service.name}: {exc}")

    try:
        stellar_health = monitor_stellar_network()
        print(
            "Stellar RPC:"
            f" {stellar_health.status}"
            f" (ledger={stellar_health.latest_ledger})"
        )
    except Exception as exc:
        print(f"Failed to monitor Stellar RPC: {exc}")


async def monitor_services():
    while True:
        await run_monitoring_cycle()
        await asyncio.sleep(settings.MONITOR_INTERVAL)
