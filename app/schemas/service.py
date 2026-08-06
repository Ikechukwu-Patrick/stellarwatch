from pydantic import BaseModel, HttpUrl


class ServiceCreate(BaseModel):
    name: str
    url: HttpUrl
    method: str = "GET"


class ServiceUpdate(BaseModel):
    name: str | None = None
    url: HttpUrl | None = None
    method: str | None = None
    is_active: bool | None = None


class ServiceRead(BaseModel):
    id: int
    name: str
    url: HttpUrl
    method: str
    is_active: bool

    class Config:
        from_attributes = True
