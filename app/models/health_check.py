from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.db.base import BaseModel

if TYPE_CHECKING:
    from app.models.service import Service


class HealthCheck(BaseModel, table=True):
    __tablename__ = "health_checks"

    id: int | None = Field(default=None, primary_key=True)

    service_id: int = Field(foreign_key="services.id")

    status_code: int | None = None

    response_time_ms: float | None = None

    is_healthy: bool = False

    checked_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    service: "Service" = Relationship(back_populates="health_checks")
