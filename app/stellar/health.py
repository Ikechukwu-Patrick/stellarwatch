import time

from app.stellar.client import get_stellar_rpc_server


def check_stellar_rpc() -> dict:
    server = get_stellar_rpc_server()

    started_at = time.perf_counter()

    try:
        response = server.get_health()
        response_time_ms = (time.perf_counter() - started_at) * 1000

        return {
            "status": response.status,
            "latest_ledger": response.latest_ledger,
            "oldest_ledger": response.oldest_ledger,
            "ledger_retention_window": response.ledger_retention_window,
            "response_time_ms": round(response_time_ms, 2),
        }

    except Exception as exc:
        response_time_ms = (time.perf_counter() - started_at) * 1000

        return {
            "status": "down",
            "latest_ledger": None,
            "oldest_ledger": None,
            "ledger_retention_window": None,
            "response_time_ms": round(response_time_ms, 2),
            "error": str(exc),
        }
