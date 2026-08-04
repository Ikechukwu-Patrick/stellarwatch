from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_services: int
    healthy_services: int
    unhealthy_services: int
    total_health_checks: int
    overall_uptime: float