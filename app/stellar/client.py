from stellar_sdk import SorobanServer

from app.core.config import settings


def get_stellar_rpc_server() -> SorobanServer:
    return SorobanServer(settings.STELLAR_RPC_URL)
