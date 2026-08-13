import asyncio
from unittest.mock import patch

from app.models.stellar_health import StellarHealth
from app.workers.monitor_worker import run_monitoring_cycle


def test_stellar_monitoring_is_called():
    expected = StellarHealth(
        status="healthy",
        latest_ledger=4105000,
        oldest_ledger=3984000,
        ledger_retention_window=120960,
        response_time_ms=150.0,
    )

    with patch(
        "app.workers.monitor_worker.monitor_stellar_network",
        return_value=expected,
    ) as mock_monitor:
        asyncio.run(run_monitoring_cycle())

    mock_monitor.assert_called_once()
