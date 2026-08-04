from typing import Optional

from pydantic import BaseModel, HttpUrl


class ServiceCreate(BaseModel):
    name: str
    url: HttpUrl
    method: str = "GET"


class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[HttpUrl] = None
    method: Optional[str] = None
    is_active: Optional[bool] = None


class ServiceRead(BaseModel):
    id: int
    name: str
    url: HttpUrl
    method: str
    is_active: bool

    class Config:
        from_attributes = True