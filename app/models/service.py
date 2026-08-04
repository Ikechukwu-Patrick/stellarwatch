from datetime import datetime
from typing import Optional

from sqlmodel import Field

from app.db.base import BaseModel
from sqlmodel import Field, Relationship


class Service(BaseModel, table=True):
    __tablename__ = "services"

    id: Optional[int] = Field(default=None, primary_key=True)

    name: str
    url: str
    method: str = "GET"

    is_active: bool = True

    created_at: datetime = Field(default_factory=datetime.utcnow)

    health_checks: list["HealthCheck"] = Relationship(
    back_populates="service"
)

from app.models.health_check import HealthCheck
    