from sqlmodel import Session, select

from app.db.database import engine
from app.models.health_check import HealthCheck


def create_health_check(health_check: HealthCheck) -> HealthCheck:
    with Session(engine) as session:
        session.add(health_check)
        session.commit()
        session.refresh(health_check)
        return health_check


def get_all_health_checks() -> list[HealthCheck]:
    with Session(engine) as session:
        statement = select(HealthCheck).order_by(HealthCheck.checked_at.desc())
        return list(session.exec(statement))


def get_service_history(service_id: int) -> list[HealthCheck]:
    with Session(engine) as session:
        statement = (
            select(HealthCheck)
            .where(HealthCheck.service_id == service_id)
            .order_by(HealthCheck.checked_at.desc())
        )
        return list(session.exec(statement))


def get_total_health_checks() -> int:
    with Session(engine) as session:
        return len(session.exec(select(HealthCheck)).all())


def get_latest_health_checks() -> list[HealthCheck]:
    with Session(engine) as session:
        services = session.exec(select(HealthCheck.service_id).distinct()).all()

        latest_checks = []

        for service_id in services:
            statement = (
                select(HealthCheck)
                .where(HealthCheck.service_id == service_id)
                .order_by(HealthCheck.checked_at.desc())
            )

            health_check = session.exec(statement).first()

            if health_check:
                latest_checks.append(health_check)

        return latest_checks