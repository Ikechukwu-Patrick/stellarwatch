from unittest.mock import patch

from app.services.stellar_monitoring_service import monitor_stellar_network


def test_monitor_stellar_network():
    expected = {
        "status": "healthy",
        "latest_ledger": 4104824,
        "oldest_ledger": 3983706,
        "ledger_retention_window": 120960,
        "response_time_ms": 100.0,
    }

    with patch(
        "app.services.stellar_monitoring_service.check_stellar_rpc",
        return_value=expected,
    ):
        result = monitor_stellar_network()

    assert result.status == "healthy"
    assert result.latest_ledger == 4104824
    assert result.oldest_ledger == 3983706
    assert result.ledger_retention_window == 120960
    assert result.response_time_ms == 100.0
