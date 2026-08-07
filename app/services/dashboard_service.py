from sqlmodel import Session, select

from app.db.database import engine
from app.models.alert import Alert
from app.models.health_check import HealthCheck
from app.models.service import Service
from app.schemas.dashboard import DashboardStats


def get_dashboard_stats() -> DashboardStats:
    with Session(engine) as session:

        services = session.exec(select(Service)).all()

        total_services = len(services)

        healthy_services = 0
        down_services = 0

        for service in services:
            latest = session.exec(
                select(HealthCheck)
                .where(HealthCheck.service_id == service.id)
                .order_by(HealthCheck.checked_at.desc())
            ).first()

            if latest:
                if latest.is_healthy:
                    healthy_services += 1
                else:
                    down_services += 1

        total_alerts = len(session.exec(select(Alert)).all())

        return DashboardStats(
            total_services=total_services,
            healthy_services=healthy_services,
            down_services=down_services,
            total_alerts=total_alerts,
        )
