from datetime import datetime

from sqlmodel import SQLModel


class HealthCheckRead(SQLModel):
    id: int
    service_id: int
    status_code: int | None
    response_time_ms: float
    is_healthy: bool
    checked_at: datetime
