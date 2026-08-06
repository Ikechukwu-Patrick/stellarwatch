from sqlmodel import Session

from app.models.service import Service
from app.monitoring.health_checker import check_service
from app.repositories.service_repository import ServiceRepository
from app.schemas.service import ServiceCreate


class ServiceService:
    def __init__(self, session: Session):
        self.repository = ServiceRepository(session)

    def create_service(self, service: ServiceCreate) -> Service:
        db_service = Service(
            name=service.name,
            url=str(service.url),
            method=service.method,
        )
        return self.repository.create(db_service)

    def get_services(self) -> list[Service]:
        return self.repository.get_all()

    def get_service(self, service_id: int) -> Service | None:
        return self.repository.get_by_id(service_id)

    def delete_service(self, service_id: int) -> bool:
        service = self.repository.get_by_id(service_id)

        if not service:
            return False

        self.repository.delete(service)
        return True

    def run_health_check(self, service_id: int):
        service = self.get_service(service_id)

        if service is None:
            return None

        return check_service(service)
