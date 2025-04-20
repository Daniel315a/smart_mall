from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    mall_id = Column(Integer, nullable=True)
    store_id = Column(Integer, nullable=True)
    name = Column(String(45), nullable=True)
    role_id = Column(Integer, ForeignKey("user_role.id"), nullable=False)
    created_at = Column(DateTime)