from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship

from app.db.base import BaseModel


class HealthCheck(BaseModel, table=True):
    __tablename__ = "health_checks"

    id: Optional[int] = Field(default=None, primary_key=True)

    service_id: int = Field(foreign_key="services.id")

    status_code: int | None = None
    response_time_ms: float | None = None
    is_healthy: bool = False

    checked_at: datetime = Field(default_factory=datetime.utcnow)

    service: "Service" = Relationship(back_populates="health_checks")