from app.repositories.health_check_repository import (
    get_latest_health_checks,
    get_total_health_checks,
)
from app.repositories.service_repository import ServiceRepository
from app.schemas.dashboard import DashboardSummary
from sqlmodel import Session


class DashboardService:
    def __init__(self, session: Session):
        self.repository = ServiceRepository(session)

    def get_dashboard_summary(self) -> DashboardSummary:
        services = self.repository.get_all()

        total_services = len(services)

        latest_checks = get_latest_health_checks()

        healthy_services = sum(
            1 for check in latest_checks if check.is_healthy
        )

        unhealthy_services = total_services - healthy_services

        total_health_checks = get_total_health_checks()

        overall_uptime = (
            (healthy_services / total_services) * 100
            if total_services > 0
            else 0.0
        )

        return DashboardSummary(
            total_services=total_services,
            healthy_services=healthy_services,
            unhealthy_services=unhealthy_services,
            total_health_checks=total_health_checks,
            overall_uptime=round(overall_uptime, 2),
        )