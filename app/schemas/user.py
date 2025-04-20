from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    id: int
    mall_id: Optional[int]
    store_id: Optional[int]
    name: Optional[str]
    role_id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True

class UserCreateSchema(BaseModel):
    mall_id: Optional[int]
    store_id: Optional[int]
    name: Optional[str]
    role_id: int

class UserUpdateSchema(BaseModel):
    mall_id: Optional[int] = None
    store_id: Optional[int] = None
    name: Optional[str] = None
    role_id: Optional[int] = None