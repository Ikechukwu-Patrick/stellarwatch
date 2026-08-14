from datetime import datetime, timezone

from sqlmodel import Field

from app.db.base import BaseModel


class StellarHealth(BaseModel, table=True):
    __tablename__ = "stellar_health"

    id: int | None = Field(default=None, primary_key=True)

    status: str
    latest_ledger: int | None = None
    oldest_ledger: int | None = None
    ledger_retention_window: int | None = None
    response_time_ms: float
    checked_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
