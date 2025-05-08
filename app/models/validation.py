from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,Time
from app.database import Base


class Validation(Base):
    __tablename__="validation"
    id=Column(Integer,primary_key=True,index=True)
    client_id=Column(Integer,ForeignKey("client.id"),nullable=False)
    coupon_id=Column(Integer,ForeignKey("coupon.id"),nullable=False)
    date=Column(DateTime,nullable=False)
    hour=Column(Time,nullable=False)