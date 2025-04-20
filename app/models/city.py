from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("region.id"), nullable=False)
    name = Column(String(250), nullable=False)