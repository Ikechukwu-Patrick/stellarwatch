from sqlmodel import Session

from app.db.database import engine
from app.models.health_check import HealthCheck


def create_health_check(health_check: HealthCheck) -> HealthCheck:
    with Session(engine) as session:
        session.add(health_check)
        session.commit()
        session.refresh(health_check)
        return health_check