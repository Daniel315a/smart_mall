from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from app.database import Base

class Client(Base):
    __tablename__="client"
    id=Column(Integer,primary_key=True,index=True)
    gender_id=Column(Integer,ForeignKey("gender.id"),nullable=False) 
    dni=Column(Integer,nullable=False)
    first_name=Column(String(250),nullable=False)
    last_name=Column(String(250),nullable=True)
    email=Column(String(250),nullable=True)
    birthday=Column(DateTime,nullable=True)
