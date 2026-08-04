from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.config import settings
from app.db.session import get_session
from app.schemas.dashboard import DashboardSummary
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix=f"{settings.API_V1_PREFIX}/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "",
    response_model=DashboardSummary,
)
def get_dashboard(
    session: Session = Depends(get_session),
):
    service = DashboardService(session)
    return service.get_dashboard_summary()