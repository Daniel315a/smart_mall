from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClientSchema(BaseModel):
    id:int
    gender_id:int
    dni:int
    first_name:str
    last_name:Optional[str]
    email:str
    birthday:datetime
    
    class Config:
        orm_mode = True

class ClientCreateSchema(BaseModel):
    gender_id:int
    dni:int
    first_name:str
    last_name:Optional[str]
    email:str
    birthday:datetime

class ClientUpdateSchema(BaseModel):
    gender_id:int
    dni:int
    first_name:str
    last_name:Optional[str]
    email:str
    birthday:datetime
