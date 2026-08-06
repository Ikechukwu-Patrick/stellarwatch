import time

import httpx

from app.models.health_check import HealthCheck
from app.models.service import Service
from app.repositories.alert_repository import get_latest_alert_for_service
from app.services.alert_service import create_alert
from app.services.health_check_service import save_health_check


def check_service(service: Service) -> HealthCheck:
    start = time.perf_counter()

    try:
        response = httpx.request(
            method=service.method,
            url=service.url,
            timeout=10,
        )

        elapsed = (time.perf_counter() - start) * 1000

        health_check = HealthCheck(
            service_id=service.id,
            status_code=response.status_code,
            response_time_ms=round(elapsed, 2),
            is_healthy=response.status_code < 400,
        )

    except httpx.HTTPError:
        elapsed = (time.perf_counter() - start) * 1000

        health_check = HealthCheck(
            service_id=service.id,
            status_code=None,
            response_time_ms=round(elapsed, 2),
            is_healthy=False,
        )

    saved_health_check = save_health_check(health_check)

    latest_alert = get_latest_alert_for_service(service.id)

    if not saved_health_check.is_healthy:
        create_alert(
            service_id=service.id,
            alert_type="DOWN",
            title=f"{service.name} is DOWN",
            message=f"{service.name} is unreachable or returned an error.",
            severity="critical",
        )

    elif latest_alert is not None and latest_alert.alert_type == "DOWN":
        create_alert(
            service_id=service.id,
            alert_type="RECOVERED",
            title=f"{service.name} RECOVERED",
            message=f"{service.name} is healthy again.",
            severity="info",
        )

    return saved_health_check
