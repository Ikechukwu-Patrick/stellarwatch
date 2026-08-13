from datetime import datetime

from pydantic import BaseModel


class StellarHealthRead(BaseModel):
    id: int
    status: str
    latest_ledger: int | None
    oldest_ledger: int | None
    ledger_retention_window: int | None
    response_time_ms: float
    checked_at: datetime
