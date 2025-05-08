from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Zone(Base):
    __tablename__ = "zone"

    id = Column(Integer, primary_key=True, index=True)
    mall_id = Column(Integer, ForeignKey("mall.id"), nullable=False)
    name = Column(String(250), nullable=False)