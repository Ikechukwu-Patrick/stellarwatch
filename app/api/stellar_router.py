from fastapi import APIRouter, HTTPException

from app.services.stellar_monitoring_service import (
    get_stellar_health_history,
)
from app.stellar.health import check_stellar_rpc
from app.stellar.ledger import get_latest_ledger
from app.stellar.network import get_stellar_network

router = APIRouter(
    prefix="/api/v1/stellar",
    tags=["Stellar"],
)


@router.get("/health")
def stellar_health():
    try:
        return check_stellar_rpc()
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Stellar RPC health check failed: {exc}",
        ) from exc


@router.get("/health/history")
def stellar_health_history(limit: int = 50):
    return get_stellar_health_history(limit)


@router.get("/network")
def stellar_network():
    return get_stellar_network()


@router.get("/ledger/latest")
def latest_ledger():
    try:
        return {"latest_ledger": get_latest_ledger()}
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Failed to retrieve latest Stellar ledger: {exc}",
        ) from exc
