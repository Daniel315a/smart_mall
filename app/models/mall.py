from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Mall(Base):
    __tablename__ = "mall"

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey("city.id"), nullable=False)
    name = Column(String(250), nullable=False)
    tax_id = Column(String(45), nullable=False)
    location = Column(String(250), nullable=False)