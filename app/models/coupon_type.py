from sqlalchemy import Column, Integer, String
from app.database import Base

class CouponType(Base):
    __tablename__ = "coupon_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)