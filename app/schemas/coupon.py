from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CouponSchema(BaseModel):
    id:int
    coupon_type:int
    store_id:int
    description:Optional[str]
    initial_date:datetime
    end_date:datetime
    
    class Config:
        orm_mode = True

class CuponCreateSchema(BaseModel):
    coupon_type:int
    store_id:int
    description:Optional[str]
    initial_date:datetime
    end_date:datetime
