from pydantic import BaseModel
from uuid import UUID

class AdvertiserCreate(BaseModel):
    name: str

class AdvertiserResponse(BaseModel):
    id: UUID
    name: str

    class Config:
        from_attributes = True