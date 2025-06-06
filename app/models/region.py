from sqlalchemy import Column, Integer, String
from app.database import Base

class Region(Base):
    __tablename__ = "region"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
