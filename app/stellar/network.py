from app.core.config import settings


def get_stellar_network() -> dict:
    return {
        "network": settings.STELLAR_NETWORK,
        "rpc_url": settings.STELLAR_RPC_URL,
    }
