from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.service import ServiceCreate, ServiceRead
from app.services.service_service import ServiceService

router = APIRouter(
    prefix="/api/v1/services",
    tags=["Services"],
)


@router.post(
    "",
    response_model=ServiceRead,
    status_code=status.HTTP_201_CREATED,
)
def create_service(
    service: ServiceCreate,
    session: Session = Depends(get_session),
):
    service_service = ServiceService(session)
    return service_service.create_service(service)


@router.get(
    "",
    response_model=list[ServiceRead],
)
def get_services(
    session: Session = Depends(get_session),
):
    service_service = ServiceService(session)
    return service_service.get_services()


@router.get(
    "/{service_id}",
    response_model=ServiceRead,
)
def get_service(
    service_id: int,
    session: Session = Depends(get_session),
):
    service_service = ServiceService(session)

    service = service_service.get_service(service_id)

    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found",
        )

    return service


@router.delete(
    "/{service_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_service(
    service_id: int,
    session: Session = Depends(get_session),
):
    service_service = ServiceService(session)

    deleted = service_service.delete_service(service_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found",
        )


@router.post("/{service_id}/check")
def run_check(
    service_id: int,
    session: Session = Depends(get_session),
):
    service_service = ServiceService(session)

    result = service_service.run_health_check(service_id)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found",
        )

    return result