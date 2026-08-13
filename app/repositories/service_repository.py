from sqlmodel import Session, select

from app.models.service import Service
from app.schemas.service import ServiceUpdate


class ServiceRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, service: Service) -> Service:
        self.session.add(service)
        self.session.commit()
        self.session.refresh(service)
        return service

    def get_all(self) -> list[Service]:
        statement = select(Service)
        return self.session.exec(statement).all()

    def get_by_id(self, service_id: int) -> Service | None:
        return self.session.get(Service, service_id)

    def get_by_name(self, name: str) -> Service | None:
        statement = select(Service).where(Service.name == name)
        return self.session.exec(statement).first()

    def update(self, db_service: Service, service: ServiceUpdate) -> Service:
        update_data = service.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_service, key, value)

        self.session.add(db_service)
        self.session.commit()
        self.session.refresh(db_service)
        return db_service

    def delete(self, db_service: Service):
        self.session.delete(db_service)
        self.session.commit()
