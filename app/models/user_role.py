from sqlalchemy import Column, Integer, String
from app.database import Base

class UserRole(Base):
    __tablename__ = "user_role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
