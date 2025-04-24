from pydantic import BaseModel
from typing import Optional

class MallSchema(BaseModel):
    id: int
    city_id: int
    name: Optional[str]
    tax_id: Optional[str]
    location: Optional[str]

    class Config:
        orm_mode = True

class MallCreateSchema(BaseModel):
    city_id: int
    name: Optional[str]
    tax_id: Optional[str]
    location: Optional[str]

class MallUpdateSchema(BaseModel):
    city_id: Optional[int] = None
    name: Optional[str] = None
    tax_id: Optional[str] = None
    location: Optional[str] = None