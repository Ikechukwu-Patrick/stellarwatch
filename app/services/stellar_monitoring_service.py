from sqlmodel import Session

from app.core.config import settings
from app.db.database import engine
from app.models.service import Service
from app.models.stellar_health import StellarHealth
from app.repositories import (
    alert_repository,
    service_repository,
    stellar_health_repository,
)
from app.services.alert_service import create_alert
from app.stellar.health import check_stellar_rpc

STELLAR_SERVICE_NAME = "Stellar RPC"


def get_or_create_stellar_service() -> Service:
    with Session(engine) as session:
        repository = service_repository.ServiceRepository(session)

        service = repository.get_by_name(STELLAR_SERVICE_NAME)

        if service:
            return service

        service = Service(
            name=STELLAR_SERVICE_NAME,
            url=settings.STELLAR_RPC_URL,
            method="GET",
            is_active=True,
        )

        return repository.create(service)


def monitor_stellar_network() -> StellarHealth:
    result = check_stellar_rpc()

    health = StellarHealth(
        status=result["status"],
        latest_ledger=result["latest_ledger"],
        oldest_ledger=result["oldest_ledger"],
        ledger_retention_window=result["ledger_retention_window"],
        response_time_ms=result["response_time_ms"],
    )

    saved_health = stellar_health_repository.create_stellar_health(health)

    stellar_service = get_or_create_stellar_service()

    latest_alert = alert_repository.get_latest_alert_for_service(stellar_service.id)

    if saved_health.status == "down":
        create_alert(
            service_id=stellar_service.id,
            alert_type="DOWN",
            title="Stellar RPC is DOWN",
            message="Stellar RPC health check failed.",
            severity="critical",
        )

    elif latest_alert and latest_alert.alert_type == "DOWN":
        create_alert(
            service_id=stellar_service.id,
            alert_type="RECOVERED",
            title="Stellar RPC RECOVERED",
            message="Stellar RPC is healthy again.",
            severity="info",
        )

    return saved_health


def get_stellar_health_history(limit: int = 50) -> list[StellarHealth]:
    return stellar_health_repository.get_stellar_health_history(limit)
