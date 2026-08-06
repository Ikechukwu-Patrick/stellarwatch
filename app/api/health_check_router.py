from fastapi import APIRouter

from app.schemas.health_check import HealthCheckRead
from app.services.health_check_query_service import (
    HealthCheckQueryService,
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Health Checks"],
)

service = HealthCheckQueryService()


@router.get(
    "/health-checks",
    response_model=list[HealthCheckRead],
)
def get_health_checks():
    return service.get_all()


@router.get(
    "/services/{service_id}/history",
    response_model=list[HealthCheckRead],
)
def get_service_history(service_id: int):
    return service.get_history(service_id)
