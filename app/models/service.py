from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.db.base import BaseModel

if TYPE_CHECKING:
    from app.models.alert import Alert
    from app.models.health_check import HealthCheck


class Service(BaseModel, table=True):
    __tablename__ = "services"

    id: int | None = Field(default=None, primary_key=True)

    name: str
    url: str
    method: str = "GET"

    is_active: bool = True

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    health_checks: list["HealthCheck"] = Relationship(
        back_populates="service",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )

    alerts: list["Alert"] = Relationship(
        back_populates="service",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )
