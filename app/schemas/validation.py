from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ValidationSchema(BaseModel):
    id: int 
    client_id: int
    coupon_id:int
    date:datetime
    hour:datetime
    
    class Config:
        orm_mode = True

class ValidationCreateSchema(BaseModel):
    client_id: int
    coupon_id:int
    date:datetime
    hour:datetime