from datetime import datetime

from pydantic import BaseModel


class AlertRead(BaseModel):
    id: int
    service_id: int
    title: str
    message: str
    severity: str
    is_sent: bool
    created_at: datetime

    model_config = {"from_attributes": True}
