import time

import httpx

from app.models.health_check import HealthCheck
from app.models.service import Service
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

    except Exception:
        elapsed = (time.perf_counter() - start) * 1000

        health_check = HealthCheck(
            service_id=service.id,
            status_code=None,
            response_time_ms=round(elapsed, 2),
            is_healthy=False,
        )

    return save_health_check(health_check)