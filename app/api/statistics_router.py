from fastapi import APIRouter, HTTPException

from app.schemas.statistics import ServiceStatistics
from app.services.statistics_service import get_service_statistics

router = APIRouter(
    prefix="/api/v1/services",
    tags=["Statistics"],
)


@router.get(
    "/{service_id}/stats",
    response_model=ServiceStatistics,
)
def service_statistics(service_id: int):
    statistics = get_service_statistics(service_id)

    if statistics is None:
        raise HTTPException(
            status_code=404,
            detail="No health check history found",
        )

    return statistics