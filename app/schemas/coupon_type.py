from pydantic import BaseModel

class CouponTypeSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True