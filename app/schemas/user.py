from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    id: int
    mall_id: Optional[int]
    store_id: Optional[int]
    auth0_id: str
    email: Optional[str]
    nickname: Optional[str]
    name: Optional[str]
    picture: Optional[str]
    role_id: int
    created_at: Optional[datetime]

    model_config = {
        "from_attributes": True
    }

class UserCreateSchema(BaseModel):
    auth0_id: str
    email: Optional[str]
    nickname: Optional[str]
    name: Optional[str]
    picture: Optional[str]
    role_id: int

class UserWithTokenSchema(BaseModel):
    user: UserSchema
    token: str