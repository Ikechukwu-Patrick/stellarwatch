from app.services.health_check_service import (
    get_health_checks,
    get_service_history,
)


class HealthCheckQueryService:
    def get_all(self):
        return get_health_checks()

    def get_history(self, service_id: int):
        return get_service_history(service_id)