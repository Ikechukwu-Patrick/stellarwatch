from sqlmodel import Session, select

from app.db.database import engine
from app.models.stellar_health import StellarHealth


def create_stellar_health(
    health: StellarHealth,
) -> StellarHealth:
    with Session(engine) as session:
        session.add(health)
        session.commit()
        session.refresh(health)
        return health


def get_stellar_health_history(
    limit: int = 50,
) -> list[StellarHealth]:
    with Session(engine) as session:
        statement = (
            select(StellarHealth).order_by(StellarHealth.checked_at.desc()).limit(limit)
        )
        return list(session.exec(statement).all())
