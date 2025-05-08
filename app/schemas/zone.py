from pydantic import BaseModel
from typing import Optional

class ZoneSchema(BaseModel):
    id: int
    mall_id: int
    name: Optional[str]

    class Config:
        orm_mode = True

class ZoneCreateSchema(BaseModel):
    mall_id: int
    name: Optional[str]

class ZoneUpdateSchema(BaseModel):
    name: Optional[str] = None