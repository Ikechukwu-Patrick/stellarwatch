from app.models.alert import Alert
from app.repositories import alert_repository


def create_alert(
    service_id: int,
    alert_type: str,
    title: str,
    message: str,
    severity: str = "critical",
) -> Alert | None:

    latest_alert = alert_repository.get_latest_alert_for_service(service_id)

    # Prevent duplicate DOWN alerts
    if latest_alert and latest_alert.alert_type == "DOWN" and alert_type == "DOWN":
        print(f"Alert already exists for service {service_id}. Skipping...")
        return None

    # Prevent duplicate RECOVERED alerts
    if (
        latest_alert
        and latest_alert.alert_type == "RECOVERED"
        and alert_type == "RECOVERED"
    ):
        return None

    alert = Alert(
        service_id=service_id,
        alert_type=alert_type,
        title=title,
        message=message,
        severity=severity,
    )

    return alert_repository.create_alert(alert)
