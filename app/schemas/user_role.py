from pydantic import BaseModel

class UserRoleSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True