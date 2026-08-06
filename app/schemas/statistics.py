from datetime import datetime

from pydantic import BaseModel


class ServiceStatistics(BaseModel):
    service_id: int
    total_checks: int
    successful_checks: int
    failed_checks: int
    uptime_percentage: float
    average_response_time: float
    last_checked: datetime | None
    current_status: str
