from fastapi import APIRouter

from app.repositories import alert_repository
from app.schemas.alert import AlertRead

router = APIRouter(
    prefix="/api/v1/alerts",
    tags=["Alerts"],
)


@router.get("", response_model=list[AlertRead])
def get_alerts():
    return alert_repository.get_all_alerts()
