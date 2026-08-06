from sqlmodel import Session, select

from app.db.database import engine
from app.models.alert import Alert


def create_alert(alert: Alert) -> Alert:
    with Session(engine) as session:
        session.add(alert)
        session.commit()
        session.refresh(alert)
        return alert


def get_all_alerts() -> list[Alert]:
    with Session(engine) as session:
        statement = select(Alert).order_by(Alert.created_at.desc())
        return list(session.exec(statement))


def get_latest_alert_for_service(service_id: int) -> Alert | None:
    with Session(engine) as session:
        statement = (
            select(Alert)
            .where(Alert.service_id == service_id)
            .order_by(Alert.created_at.desc())
        )

        return session.exec(statement).first()
