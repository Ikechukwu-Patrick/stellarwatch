from app.models.health_check import HealthCheck
from app.repositories import health_check_repository


def save_health_check(health_check: HealthCheck) -> HealthCheck:
    return health_check_repository.create_health_check(health_check)