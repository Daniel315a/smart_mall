from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base

class Store(Base):
    __tablename__ = "store"

    id = Column(Integer, primary_key=True, index=True)
    zone_id = Column(Integer, ForeignKey("zone.id"), nullable=False)
    name = Column(String(250), nullable=False)
    tax_id = Column(String(45), nullable=False)
    description = Column(Text)