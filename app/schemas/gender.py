from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GenderSchema(BaseModel):
    id:int
    name:str

    class Config:
        orm_mode = True