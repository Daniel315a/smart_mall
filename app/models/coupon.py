from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from app.database import Base

class Coupon(Base): 
    __tablename__="coupon"
    id=Column(Integer, primary_key=True, index=True)
    coupon_type=Column(Integer,nullable=False)
    store_id=Column(Integer, ForeignKey("store.id"),nullable=False)
    description=Column(String(250),nullable=True)
    initial_date=Column(DateTime, nullable=False)
    end_date=Column(DateTime, nullable=False)
