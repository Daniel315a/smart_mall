from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from app.database import Base

class Gender(Base):
    __tablename__="gender"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(10),nullable=True)