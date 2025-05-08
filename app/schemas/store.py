from pydantic import BaseModel
from typing import Optional

class StoreSchema(BaseModel):
    id: int
    zone_id: int
    name: Optional[str]
    tax_id: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True

class StoreCreateSchema(BaseModel):
    zone_id: int
    name: Optional[str]
    tax_id: Optional[str]
    description: Optional[str]

class StoreUpdateSchema(BaseModel):
    zone_id: Optional[int] = None
    name: Optional[str] = None
    tax_id: Optional[str] = None
    description: Optional[str] = None