from pydantic import BaseModel

class CitySchema(BaseModel):
    id: int
    region_id: int
    name: str

    class Config:
        orm_mode = True