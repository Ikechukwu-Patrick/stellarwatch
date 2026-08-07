from pydantic import BaseModel


class DashboardStats(BaseModel):
    total_services: int
    healthy_services: int
    down_services: int
    total_alerts: int
