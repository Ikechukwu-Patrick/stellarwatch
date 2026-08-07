from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.db.base import BaseModel

if TYPE_CHECKING:
    from app.models.service import Service


class Alert(BaseModel, table=True):
    __tablename__ = "alerts"

    id: int | None = Field(default=None, primary_key=True)

    service_id: int = Field(foreign_key="services.id")

    alert_type: str

    title: str

    message: str

    severity: str = "warning"

    is_sent: bool = False

    created_at: datetime = Field(default_factory=datetime.utcnow)

    service: "Service" = Relationship(back_populates="alerts")
