from app.stellar.client import get_stellar_rpc_server


def get_latest_ledger() -> int:
    server = get_stellar_rpc_server()
    response = server.get_health()

    return response.latest_ledger
