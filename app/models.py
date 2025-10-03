from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String, nullable=False, index=True)
    quantity = Column(Integer, nullable=False)
    status = Column(String, nullable=False, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
