from app.models.health_check import HealthCheck
from app.repositories import health_check_repository


def save_health_check(health_check: HealthCheck) -> HealthCheck:
    return health_check_repository.create_health_check(health_check)


def get_health_checks() -> list[HealthCheck]:
    return health_check_repository.get_all_health_checks()


def get_service_history(service_id: int) -> list[HealthCheck]:
    return health_check_repository.get_service_history(service_id)