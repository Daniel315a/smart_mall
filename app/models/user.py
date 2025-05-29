from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from app.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    mall_id = Column(Integer, nullable=True)
    store_id = Column(Integer, nullable=True)
    auth0_id = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), nullable=True)
    nickname = Column(String(50), nullable=True)
    name = Column(String(100), nullable=True)
    picture = Column(Text, nullable=True)
    role_id = Column(Integer, ForeignKey("user_role.id"), nullable=False)
    created_at = Column(DateTime)
