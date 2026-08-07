from app.repositories.health_check_repository import get_service_history
from app.schemas.statistics import ServiceStatistics


def get_service_statistics(service_id: int) -> ServiceStatistics | None:
    history = get_service_history(service_id)

    if not history:
        return None

    total_checks = len(history)

    successful_checks = sum(1 for check in history if check.is_healthy)

    failed_checks = total_checks - successful_checks

    uptime_percentage = round(
        (successful_checks / total_checks) * 100,
        2,
    )

    average_response_time = round(
        sum(check.response_time_ms or 0 for check in history) / total_checks,
        2,
    )

    last_checked = history[0].checked_at

    current_status = "healthy" if history[0].is_healthy else "unhealthy"

    return ServiceStatistics(
        service_id=service_id,
        total_checks=total_checks,
        successful_checks=successful_checks,
        failed_checks=failed_checks,
        uptime_percentage=uptime_percentage,
        average_response_time=average_response_time,
        last_checked=last_checked,
        current_status=current_status,
    )
