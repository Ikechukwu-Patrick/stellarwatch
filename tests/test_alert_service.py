import uuid

from app.services.alert_service import create_alert


def test_create_down_alert():
    service_id = uuid.uuid4().int % 1_000_000_000

    alert = create_alert(
        service_id=service_id,
        alert_type="DOWN",
        title="Test Service is DOWN",
        message="Test Service is unreachable.",
        severity="critical",
    )

    assert alert is not None
    assert alert.service_id == service_id
    assert alert.alert_type == "DOWN"
    assert alert.severity == "critical"


def test_prevent_duplicate_down_alert():
    service_id = uuid.uuid4().int % 1_000_000_000

    first_alert = create_alert(
        service_id=service_id,
        alert_type="DOWN",
        title="Duplicate Test Service is DOWN",
        message="Test Service is unreachable.",
        severity="critical",
    )

    second_alert = create_alert(
        service_id=service_id,
        alert_type="DOWN",
        title="Duplicate Test Service is DOWN",
        message="Test Service is unreachable.",
        severity="critical",
    )

    assert first_alert is not None
    assert second_alert is None


def test_create_recovered_alert():
    service_id = uuid.uuid4().int % 1_000_000_000

    down_alert = create_alert(
        service_id=service_id,
        alert_type="DOWN",
        title="Test Service is DOWN",
        message="Test Service is unreachable.",
        severity="critical",
    )

    recovered_alert = create_alert(
        service_id=service_id,
        alert_type="RECOVERED",
        title="Test Service RECOVERED",
        message="Test Service is healthy again.",
        severity="info",
    )

    assert down_alert is not None
    assert recovered_alert is not None
    assert recovered_alert.alert_type == "RECOVERED"
